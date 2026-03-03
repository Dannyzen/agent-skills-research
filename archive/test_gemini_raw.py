import urllib.request
import json
import os
import sys

req = urllib.request.Request(
    "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions",
    headers={
        "Authorization": "Bearer AIzaSyADsgx_zXn6Rw8BwjAyfFhDyd0jDy3pCdU",
        "Content-Type": "application/json"
    },
    data=json.dumps({
        "model": "gemini-3-flash-preview",
        "messages": [{"role": "user", "content": "hi"}],
        "stream": True
    }).encode("utf-8"),
    method="POST"
)
try:
    with urllib.request.urlopen(req) as response:
        print("Status:", response.status)
        for line in response:
            sys.stdout.buffer.write(line)
except Exception as e:
    print(f"Error: {e}")
    if hasattr(e, 'read'):
        print(e.read().decode('utf-8'))
