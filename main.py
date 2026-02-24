import os
import requests
import json
import hmac
import hashlib

HASH_SECRET_KEY = os.environ["hash_secret_key"]
JSON_PAYLOAD = {"timestamp": "ISO8601","name": "Aletta Klopper","email": "klopperaletta@gmail.com","resume_link": "https://www.linkedin.com/in/aletta-klopper-18bbba42/","action_run_link": "some action link"}
POST_URL = "https://b12.io/apply/submission"

def main():
    headers = {
        "Content-Type": "application/json",
        "X-Signature-256": "sfdsdf"
    }
    message = json.dumps(JSON_PAYLOAD)

    #submission_request = requests.post(url=POST_URL, headers=headers, data=JSON_PAYLOAD)

    signature = hmac.new(
        HASH_SECRET_KEY.encode("utf-8"),
        msg=message.encode("utf-8"),
        digestmod=hashlib.sha256
    ).hexdigest()

    print(f"SIGNATURE: {signature}")
    

if __name__ == '__main__':
    main()