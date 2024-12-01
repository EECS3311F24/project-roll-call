from mongoengine import DoesNotExist
from ..models import User

def get_user_settings(google_id):
    try:
        user = User.objects.get(google_id=google_id)
        return user.settings
    except DoesNotExist:
        print("User doesn't exist.")
        return None
    
def update_user_nonevent_setting(google_id, setting_key, new_value):
    try:
        user = User.objects.get(google_id=google_id)

        if setting_key in user.settings:
            user.settings[setting_key] = new_value
        else:
            return {"error": f"Setting {setting_key} not found in settings"}, 404

        user.save()
        return {"message": f"{setting_key} updated successfully"}, 200
    except DoesNotExist:
        return {"error": "User not found"}, 404
    except Exception as e:
        return {"error": str(e)}, 500
    
def update_user_event_setting(google_id, setting_key, field_key, new_value):
    try:
        user = User.objects.get(google_id=google_id)

        if setting_key in user.settings and field_key in user.settings[setting_key]:
            user.settings[setting_key][field_key] = new_value
        else:
            return {"error": f"Setting {field_key} in setting {setting_key} not found in settings"}, 404

        user.save()
        return {"message": f"{field_key} updated successfully"}, 200
    except DoesNotExist:
        return {"error": "User not found"}, 404
    except Exception as e:
        return {"error": str(e)}, 500
        
