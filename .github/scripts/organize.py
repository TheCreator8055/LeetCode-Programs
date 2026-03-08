import os
import shutil
import json

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

IGNORE = {
    ".git",
    ".github",
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

items = os.listdir(".")

for item in items:

    if item in IGNORE:
        continue

    if item in topics_folders:
        continue

    if item.startswith("."):
        continue

    if not os.path.isdir(item):
        continue

    lower = item.lower()
    moved = False

    for key in topics:

        if key in lower:

            folder = topics[key]
            os.makedirs(folder, exist_ok=True)

            dest = os.path.join(folder, item)

            if not os.path.exists(dest):
                shutil.move(item, dest)

            moved = True
            break

    if not moved:

        os.makedirs("16-misc", exist_ok=True)

        dest = os.path.join("16-misc", item)

        if not os.path.exists(dest):
            shutil.move(item, dest)

    metadata[item] = {
        "name": item
    }

with open(metadata_file, "w", encoding="utf-8") as f:
    json.dump(metadata, f, indent=2)
