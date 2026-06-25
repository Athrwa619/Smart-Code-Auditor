import os

def fetch_user_data(user_id):
    # FLAW 1: Never hardcode secret keys in your files!
    stripe_api_key = "sk_live_super_secret_key_999"
    
    # FLAW 2: Never pass user input directly to the operating system!
    command = "ping -c 4 " + user_id
    os.system(command)
    
    return "Data fetched successfully"
