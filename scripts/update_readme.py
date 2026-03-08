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
        files = [
            f for f in os.listdir(topic)
            if os.path.isfile(os.path.join(topic, f))
        ]

        count = len(files)
        total += count

        rows += f"| {topic} | {count} |\n"


readme = f"""# 🚀 LeetCode Problem Archive

Automatically synced solutions from LeetCode.

## 📊 Statistics

**Total Problems Solved: {total}**

| Topic | Problems |
|------|------|
{rows}

---

## 📂 Repository Structure

Problems are organized by **Data Structures and Algorithms topics**.

Example structure:

01-arrays  
02-two-pointers  
03-sliding-window  
04-stack  
05-binary-search  
06-linked-list  
07-trees  
08-heap  
09-graphs  
10-dynamic-programming  

---

## 📄 File Naming Convention

Each solution follows this format:

problem-number-problem-name.extension

Example:

0001-two-sum.py  
0704-binary-search.cpp  

---

## ⚙️ Automation

This repository automatically:

• syncs solved problems from LeetCode  
• organizes them by DSA topic  
• updates the README statistics dashboard  

using GitHub Actions.
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)
