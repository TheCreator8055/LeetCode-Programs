import os

topics = [
"01-arrays",
"02-two-pointers",
"03-sliding-window",
"04-stack",
"05-binary-search",
"06-linked-list",
"07-trees",
"08-heap",
"09-graphs",
"10-dynamic-programming",
"11-backtracking",
"12-greedy",
"13-math",
"14-bit-manipulation",
"15-strings",
"16-misc"
]

rows = ""
total = 0

for topic in topics:

    if os.path.exists(topic):

        files = os.listdir(topic)
        count = len(files)

        total += count

        rows += f"| {topic} | {count} |\n"

readme = f"""
# 🚀 LeetCode Problem Archive

Automatically synced solutions from LeetCode.

## 📊 Statistics

**Total Problems Solved: {total}**

| Topic | Problems |
|------|------|
{rows}

---

## 📂 Repository Structure

Problems are organized by **Data Structures & Algorithms concepts**.

Example:
