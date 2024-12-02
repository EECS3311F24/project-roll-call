from app.services.auth_service.token import get_user_id
from app.services.user_settings import get_user_settings, update_user_nonevent_setting, update_user_event_setting
from flask import session, request, jsonify
from . import setting

@setting.route("/get_settings", methods=['GET'])
def get_settings():
    try:
        google_id = get_user_id(session)
        settings = get_user_settings(google_id) 
        return jsonify(settings), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@setting.route("/update_nonevent_setting", methods=['POST'])
def update_nonevent_setting():
    try:
        google_id = get_user_id(session)
        setting_key = request.json.get("setting_key")
        new_value = request.json.get("new_value")

        if "new_value" not in request.json:
            return jsonify({"error": "new_value required"}), 400
        if not google_id:
            return jsonify({"error": "google_id required"}), 400
        if not setting_key:
            return jsonify({"error": "setting_key required"}), 400
        

        return update_user_nonevent_setting(google_id, setting_key, new_value)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@setting.route("/update_event_setting", methods=['POST'])
def update_event_setting():
    try:
        google_id = get_user_id(session)
        setting_key = request.json.get("setting_key")
        field_key = request.json.get("field_key")
        new_value = request.json.get("new_value")

        if not google_id:
            return jsonify({"error": "google_id required"}), 400
        if not setting_key:
            return jsonify({"error": "setting_key required"}), 400
        if not new_value:
            return jsonify({"error": "new_value required"}), 400

        return update_user_event_setting(google_id, setting_key, field_key, new_value)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

