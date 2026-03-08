import os
import requests
import json

session_cookie = os.environ.get("LEETCODE_SESSION")

if not session_cookie:
    print("LEETCODE_SESSION not found")
    exit(1)

headers = {
    "Content-Type": "application/json",
    "Cookie": f"LEETCODE_SESSION={session_cookie}"
}

query = """
{
  matchedUser(username: "Shivanantham_M") {
    submitStats {
      acSubmissionNum {
        difficulty
        count
      }
    }
  }
}
"""

response = requests.post(
    "https://leetcode.com/graphql",
    json={"query": query},
    headers=headers
)

data = response.json()

print(json.dumps(data, indent=2))
