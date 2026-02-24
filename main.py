import os
import requests
import json

HASH_SECRET_KEY = os.environ["hash_secret_key"]
print(f"Hash Key: {HASH_SECRET_KEY}")