from app.db import get_db  # MongoDB connection


def create_user(profile):
    """
    Creates or fetches a user in the database based on their Google profile.
    """
    db = get_db()
    users = db["users"]  # Use the "users" collection

    # Check if the user already exists
    user = users.find_one({"email": profile.get("google_id")})

    if not user:
        # Create a new user
        new_user = {
            "google_id" : profile["google_id"],
            "email": profile["email"],           
            "f_name": profile["f_name"],         
            "l_name": profile["l_name"],            
            "pfp": profile["pfp"],                 
            "settings": {},                              
        }
        user_id = users.insert_one(new_user).inserted_id
        new_user["_id"] = str(user_id)
        return new_user
    else:
        print("User already in database")
        user["google_id"] = str(user["google_id"])
        return user

def get_user(google_id):
    """
    Fetches a user in the database based on their Google profile.
    """
    db = get_db()
    users = db["users"]  # Use the "users" collection

    # Check if the user already exists
    return users.find_one({"google_id": google_id})

    