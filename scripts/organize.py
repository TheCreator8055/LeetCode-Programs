import os
import shutil

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

files = [f for f in os.listdir(".") if os.path.isfile(f)]

for file in files:

    lower = file.lower()

    moved = False

    for key in topics:
        if key in lower:
            folder = topics[key]
            os.makedirs(folder, exist_ok=True)

            shutil.move(file, f"{folder}/{file}")
            moved = True
            break

    if not moved:
        os.makedirs("16-misc", exist_ok=True)
        shutil.move(file, f"16-misc/{file}")
