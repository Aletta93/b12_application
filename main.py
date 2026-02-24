import os
import requests
import json
import hmac
import hashlib

HASH_SECRET_KEY = os.environ["hash_secret_key"]
#JSON_PAYLOAD = {"timestamp": "ISO8601","name": "Aletta Klopper","email": "klopperaletta@gmail.com","resume_link": "https://www.linkedin.com/in/aletta-klopper-18bbba42/","action_run_link": "some action link"}
JSON_PAYLOAD = {"action_run_link":"https://link-to-github-or-another-forge.example.com/your/repository/actions/runs/run_id","email":"you@example.com","name":"Your name","repository_link":"https://link-to-github-or-other-forge.example.com/your/repository","resume_link":"https://pdf-or-html-or-linkedin.example.com","timestamp":"2026-01-06T16:59:37.571Z"}
POST_URL = "https://b12.io/apply/submission"

def main():
    headers = {
        "Content-Type": "application/json",
        "X-Signature-256": "sfdsdf"
    }
    message = json.dumps(JSON_PAYLOAD)

    #submission_request = requests.post(url=POST_URL, headers=headers, data=JSON_PAYLOAD)

    signature = hmac.new(
        HASH_SECRET_KEY,
        msg=message.encode("utf-8"),
        digestmod=hashlib.sha256
    ).hexdigest()

    print(f"SIGNATURE: {signature}")
    

if __name__ == '__main__':
    main()