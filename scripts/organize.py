import os
import shutil
import json
import re

topics = {
    "array": "01-arrays",
    "two": "02-two-pointers",
    "window": "03-sliding-window",
    "stack": "04-stack",
    "search": "05-binary-search",
    "list": "06-linked-list",
    "tree": "07-trees",
    "heap": "08-heap",
    "graph": "09-graphs",
    "dp": "10-dynamic-programming",
    "dynamic": "10-dynamic-programming",
    "backtrack": "11-backtracking",
    "greedy": "12-greedy",
    "math": "13-math",
    "bit": "14-bit-manipulation",
    "string": "15-strings"
}

IGNORE_FILES = {
    "organize.py",
    "update_readme.py",
    "fetch_leetcode.py",
    "README.md",
    "problems.json"
}

topics_folders = set(topics.values())
topics_folders.add("16-misc")

metadata_file = "problems.json"

if os.path.exists(metadata_file):
    with open(metadata_file, "r", encoding="utf-8") as f:
        metadata = json.load(f)
else:
    metadata = {}

files = [f for f in os.listdir(".") if os.path.isfile(f)]

for file in files:

    if file in IGNORE_FILES:
        continue

    if file.startswith("."):
        continue

    lower = file.lower()
    moved = False

    problem_match = re.match(r"(\d+)[-_](.*)\.", file)

    if problem_match:
        number = problem_match.group(1)
        name = problem_match.group(2).replace("-", " ").replace("_", " ").title()

        metadata[number] = {
            "name": name,
            "file": file
        }

    for key in topics:
        if key in lower:

            folder = topics[key]

            os.makedirs(folder, exist_ok=True)

            if not os.path.exists(os.path.join(folder, file)):
                shutil.move(file, os.path.join(folder, file))

            moved = True
            break

    if not moved:

        os.makedirs("16-misc", exist_ok=True)

        if not os.path.exists(os.path.join("16-misc", file)):
            shutil.move(file, os.path.join("16-misc", file))

with open(metadata_file, "w", encoding="utf-8") as f:
    json.dump(metadata, f, indent=2)
