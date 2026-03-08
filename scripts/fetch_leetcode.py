import os
import requests

SESSION = os.getenv("LEETCODE_SESSION")

if not SESSION:
    raise Exception("Missing LEETCODE_SESSION secret")

headers = {
    "cookie": f"LEETCODE_SESSION={SESSION}",
    "user-agent": "Mozilla/5.0"
}

url = "https://leetcode.com/api/submissions/?offset=0&limit=1000"

res = requests.get(url, headers=headers)
data = res.json()

submissions = data["submissions_dump"]

EXTENSIONS = {
    "python": ".py",
    "python3": ".py",
    "cpp": ".cpp",
    "c": ".c",
    "java": ".java",
    "javascript": ".js"
}

saved = 0

for sub in submissions:

    if sub["status_display"] != "Accepted":
        continue

    title = sub["title_slug"]
    lang = sub["lang"].lower()

    if lang not in EXTENSIONS:
        continue

    ext = EXTENSIONS[lang]
    filename = f"{sub['question_id']}-{title}{ext}"

    if os.path.exists(filename):
        continue

    code_url = f"https://leetcode.com/submissions/detail/{sub['id']}/"

    page = requests.get(code_url, headers=headers)

    if page.status_code != 200:
        continue

    # crude extraction of code
    text = page.text
    start = text.find("submissionCode:")
    if start == -1:
        continue

    code_start = text.find('"', start) + 1
    code_end = text.find('"', code_start)

    code = text[code_start:code_end].encode().decode("unicode_escape")

    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)

    saved += 1
    print("Saved:", filename)

print("New files downloaded:", saved)
