import os
import requests
import re
import time

SESSION = os.getenv("LEETCODE_SESSION")

if not SESSION:
    raise Exception("Missing LEETCODE_SESSION secret")

headers = {
    "cookie": f"LEETCODE_SESSION={SESSION}",
    "user-agent": "Mozilla/5.0"
}

SUBMISSION_API = "https://leetcode.com/api/submissions/?offset=0&limit=1000"

EXTENSIONS = {
    "python": ".py",
    "python3": ".py",
    "cpp": ".cpp",
    "c": ".c",
    "java": ".java",
    "javascript": ".js"
}

def extract_code(page_text):
    """
    Extract submission code from submission page HTML.
    """
    pattern = r'submissionCode:\s*"(.+?)"'
    match = re.search(pattern, page_text, re.DOTALL)

    if not match:
        return None

    code = match.group(1)
    return code.encode().decode("unicode_escape")


print("Fetching submissions...")

res = requests.get(SUBMISSION_API, headers=headers)

if res.status_code != 200:
    raise Exception("Failed to fetch submissions")

data = res.json()
submissions = data.get("submissions_dump", [])

saved = 0
skipped = 0

for sub in submissions:

    if sub["status_display"] != "Accepted":
        continue

    title_slug = sub["title_slug"]
    question_id = str(sub["question_id"]).zfill(4)
    lang = sub["lang"].lower()

    if lang not in EXTENSIONS:
        skipped += 1
        continue

    ext = EXTENSIONS[lang]

    filename = f"{question_id}-{title_slug}{ext}"

    if os.path.exists(filename):
        continue

    submission_id = sub["id"]
    submission_url = f"https://leetcode.com/submissions/detail/{submission_id}/"

    page = requests.get(submission_url, headers=headers)

    if page.status_code != 200:
        print("Failed to open submission:", submission_id)
        continue

    code = extract_code(page.text)

    if not code:
        print("Could not extract code:", submission_id)
        continue

    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)

    saved += 1
    print("Saved:", filename)

    time.sleep(0.5)  # avoid rate limiting

print("\nSummary")
print("New files downloaded:", saved)
print("Skipped unsupported languages:", skipped)
