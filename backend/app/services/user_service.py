from mongoengine import DoesNotExist
from ..models import User, Creds

def create_user(profile):
    """
    Creates or fetches a user in the database based on their Google profile.
    
    :param profile: A dictionary containing the user's Google profile information.
    :return: The User object.
    """
    try:
        # Check if the user already exists
        user = User.objects.get(google_id=profile["google_id"])
        print("User already in database")
    except DoesNotExist:
        # Create a new user without credentials
        user = User(
            google_id=profile["google_id"],
            email=profile["email"],
            f_name=profile["f_name"],
            l_name=profile["l_name"],
            pfp=profile["pfp"],
            settings={},  # Initialize with default settings
        )

        # Save the new user to the database
        user.save()
        print(f"Created new user with email: {profile['email']}")

    return user

def get_name(google_id):
    user = User.objects.get(google_id=google_id)
    return user.f_name

def get_email(google_id):
    user = User.objects.get(google_id=google_id)
    return user.email


def get_user(google_id):
    """
    Fetches a user in the database based on their Google ID.
    """
    try:
        return User.objects.get(google_id=google_id)
    except DoesNotExist:
        return None

def user_in_db(google_id):
    """
    Checks if a user exists in the database based on their Google ID.
    """
    return User.objects(google_id=google_id).count() > 0

def store_creds(user, creds_dict):
    """
    Store or update the credentials for a user.

    :param user: The User object to update.
    :param creds_dict: A dictionary containing credentials to store.
    """
    try:
        # Create or update the Creds object
        user.creds = Creds(
            token=creds_dict["token"],
            refresh_token=creds_dict["refresh_token"],
            id_token=creds_dict["id_token"],
            token_uri=creds_dict["token_uri"],
            client_id=creds_dict["client_id"],
            client_secret=creds_dict["client_secret"],
            scopes=creds_dict["scopes"],
        )
        
        # Save changes to the database
        user.save()
        print(f"Credentials successfully stored for user {user.google_id}.")
    
    except KeyError as e:
        print(f"Missing required field in creds_dict: {e}")









    