from app import create_app
import os
# from app.services.report_service.scheduler import schedule_jobs

app = create_app()

if __name__ == "__main__":
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
    
    # schedule_jobs(app)
    app.run(host="localhost", port=5000, debug=True)
    