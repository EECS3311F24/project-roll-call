from . import user
from app.services.user_service import get_name
from app.services.auth_service.token import get_user_id
from flask import session, request, jsonify

@user.route("/name", methods=['GET'])
def name():
    try:
        google_id = get_user_id(session)
        name = get_name(google_id) 
        return jsonify(name), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
