import os
import json
import urllib.parse

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

metadata_file = "problems.json"

if os.path.exists(metadata_file):
    with open(metadata_file, "r", encoding="utf-8") as f:
        metadata = json.load(f)
else:
    metadata = {}

rows = ""
problem_rows = ""
total = 0

# Lists to collect chart datasets parameters safely
chart_labels = []
chart_data = []

# Modern flat UI color accents for chart slices
chart_colors = [
    '#ff6384', '#36a2eb', '#ffce56', '#4bc0c0', '#9966ff', 
    '#ff9f40', '#607d8b', '#8bc34a', '#e91e63', '#9c27b0', 
    '#00bcd4', '#ff5722', '#795548', '#009688', '#3f51b5', '#4caf50'
]

for topic in topics:
    if os.path.exists(topic):
        files = [
            f for f in os.listdir(topic)
            if os.path.isdir(os.path.join(topic, f))
        ]

        count = len(files)
        total += count

        rows += f"| {topic} | {count} |\n"
        
        # Capture categories containing active solutions
        if count > 0:
            # FIXED: Corrected missing replace execution parameters
            clean_label = topic.split("-", 1)[1].replace("-", " ").title()
            chart_labels.append(clean_label)
            chart_data.append(count)

        for file in files:
            # FIXED: Extracted specific item element using index bounds
            number = file.split("-")[0]
            name = file.replace(".py","").replace(".cpp","").replace(".java","")
            title = name.split("-",1)[1].replace("-", " ").title()
            url_name = title.lower().replace(" ", "-")
            link = f"https://leetcode.com{url_name}/"
            problem_rows += f"| {number} | [{title}]({link}) | {topic} |\n"

# Construct valid Chart.js object dictionary configuration configuration schema
# Construct valid Chart.js object dictionary configuration schema with enhanced data labels
chart_config = {
    "type": "doughnut",
    "data": {
        "labels": chart_labels,
        "datasets": [{
            "data": chart_data,
            "backgroundColor": chart_colors[:len(chart_data)]
        }]
    },
    "options": {
        "plugins": {
            "legend": {
                "position": "top",
                "labels": {
                    "fontSize": 13,
                    "fontStyle": "bold"
                }
            },
            # FIX: Force text inside chart slices to be crisp, bold white
            "datalabels": {
                "color": "#ffffff",
                "font": {
                    "weight": "bold",
                    "size": 14
                },
                "formatter": "function(value) { return value; }"  # Ensures raw counts show up perfectly
            }
        }
    }
}


# Safely stringify layouts config parameters and completely URL encode it
chart_json_string = json.dumps(chart_config)
encoded_param = urllib.parse.quote(chart_json_string)
markdown_chart_tag = f"![LeetCode Progress Chart](https://quickchart.io/chart?c={encoded_param})"

readme = f"""# 🚀 LeetCode Problem Archive

Automatically synced solutions from LeetCode.

## 📊 Statistics

**Total Problems Solved: {total}**

{markdown_chart_tag}

| Topic | Problems |
|------|------|
{rows}

---

## 📚 Problems

| # | Problem | Topic |
|---|---|---|
{problem_rows}

---

## 📂 Repository Structure

Problems are organized by **DSA topics**.

---

## ⚙️ Automation

This repository automatically:

• syncs solved problems from LeetCode  
• organizes them by topic  
• updates README statistics  

using GitHub Actions.
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)
