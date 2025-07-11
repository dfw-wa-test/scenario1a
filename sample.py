#!/usr/bin/env python3

import os
import sys
import subprocess
import pickle
import random
import requests

# 1. Hard-coded secret (BAD PRACTICE)
API_TOKEN = "ghp_FAKE1234567890SECRET_newchange"
# new file change

# 2. Insecure random token (predictable)
def generate_token():
    chars = "abcdef123456"
    return "".join(random.choice(chars) for _ in range(20))

# 3. Unsafe eval on external input
def dynamic_compute(expr):
    # WARNING: Using eval on untrusted input is dangerous
    return eval(expr)

# 4. Shell command injection risk
def list_repo_files(path):
    # WARNING: shell=True can lead to injection
    cmd = f"ls {path}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout

# 5. Insecure HTTP request (SSL verification disabled)
def fetch_data(url):
    response = requests.get(url, headers={"Authorization": f"token {API_TOKEN}"}, verify=False)
    return response.text

# 6. Unsafe pickle deserialization
def load_payload(file_path):
    with open(file_path, "rb") as f:
        # WARNING: pickle.load can execute arbitrary code
        return pickle.load(f)

def main():
    print("Generated insecure token:", generate_token())

    if len(sys.argv) > 1:
        expr = sys.argv[1]
        print("Eval result:", dynamic_compute(expr))

    print("Repository files:\n", list_repo_files("."))

    # Replace with a test URL to exercise SSL bypass
    try:
        data = fetch_data("https://example.com/api/data")
        print("Fetched data:", data[:100])
    except requests.exceptions.SSLError as e:
        print("SSL verification error (expected):", e)

    # Test unsafe deserialization; ensure you've created a malicious pickle for testing
    if os.path.exists("payload.pkl"):
        payload = load_payload("payload.pkl")
        print("Untrusted payload loaded:", payload)

if __name__ == "__main__":
    main()