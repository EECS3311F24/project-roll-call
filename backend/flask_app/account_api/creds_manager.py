import json
from google.oauth2.credentials import Credentials

class CredentialsManager:
    @staticmethod
    def load_creds(file_path="credentials.json", default_scopes=None):
        """Load credentials from a JSON file."""
        try:
            with open(file_path, 'r') as cred_file:
                creds_dict = json.load(cred_file)

                # Handle missing scopes
                scopes = creds_dict.get("scopes", default_scopes)
                if not scopes:
                    raise ValueError("No scopes defined in credentials and no default scopes provided.")

                return Credentials(
                    token=creds_dict["token"],
                    refresh_token=creds_dict.get("refresh_token"),
                    token_uri=creds_dict["token_uri"],
                    client_id=creds_dict["client_id"],
                    client_secret=creds_dict["client_secret"],
                    scopes=scopes
                )
        except FileNotFoundError:
            print(f"Credentials file not found at {file_path}. Please authenticate.")
            return None
        except json.JSONDecodeError as e:
            print(f"Error decoding credentials file: {e}")
            return None
        except ValueError as ve:
            print(f"Error: {ve}")
            return None
