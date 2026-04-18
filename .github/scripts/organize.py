import os
import shutil
import json
import re
import urllib.request

# ─────────────────────────────────────────────
# Topic keyword map  (keyword → folder)
# ─────────────────────────────────────────────
topics = {
    # Arrays
    "array": "01-arrays",
    "remove": "01-arrays",
    "rotate": "01-arrays",
    "matrix": "01-arrays",
    "spiral": "01-arrays",
    "duplicate": "01-arrays",
    "majority": "01-arrays",
    "missing": "01-arrays",
    "container": "01-arrays",
    "trap": "01-arrays",
    "product": "01-arrays",
    "merge": "01-arrays",
    "image": "01-arrays",
    "maximal": "01-arrays",

    # Two Pointers
    "3sum": "02-two-pointers",
    "4sum": "02-two-pointers",
    "closest": "02-two-pointers",
    "palindrome": "02-two-pointers",
    "reverse": "02-two-pointers",
    "swap": "02-two-pointers",

    # Sliding Window
    "window": "03-sliding-window",
    "zigzag": "03-sliding-window",
    "substring": "03-sliding-window",
    "subarray": "03-sliding-window",

    # Stack
    "stack": "04-stack",
    "parentheses": "04-stack",
    "bracket": "04-stack",
    "calculator": "04-stack",
    "histogram": "04-stack",
    "simplify": "04-stack",

    # Binary Search
    "search": "05-binary-search",
    "binary": "05-binary-search",
    "kth": "05-binary-search",
    "peak": "05-binary-search",
    "median": "05-binary-search",

    # Linked List
    "linked": "06-linked-list",
    "nodes-in": "06-linked-list",
    "cycle": "06-linked-list",
    "lru": "06-linked-list",

    # Trees
    "tree": "07-trees",
    "bst": "07-trees",
    "inorder": "07-trees",
    "preorder": "07-trees",
    "postorder": "07-trees",
    "diameter": "07-trees",
    "ancestor": "07-trees",
    "depth": "07-trees",
    "height": "07-trees",
    "symmetric": "07-trees",

    # Heap
    "heap": "08-heap",
    "priority": "08-heap",
    "frequent": "08-heap",

    # Graphs
    "graph": "09-graphs",
    "sudoku": "09-graphs",
    "dfs": "09-graphs",
    "bfs": "09-graphs",
    "island": "09-graphs",
    "course": "09-graphs",
    "clone": "09-graphs",
    "pacific": "09-graphs",
    "network": "09-graphs",
    "rotten": "09-graphs",

    # Dynamic Programming
    "dp": "10-dynamic-programming",
    "dynamic": "10-dynamic-programming",
    "fibonacci": "10-dynamic-programming",
    "climbing": "10-dynamic-programming",
    "coin": "10-dynamic-programming",
    "knapsack": "10-dynamic-programming",
    "subsequence": "10-dynamic-programming",
    "edit-distance": "10-dynamic-programming",
    "triangle": "10-dynamic-programming",
    "house": "10-dynamic-programming",
    "decode": "10-dynamic-programming",
    "partition": "10-dynamic-programming",
    "dungeon": "10-dynamic-programming",
    "unique-path": "10-dynamic-programming",
    "wildcard": "10-dynamic-programming",
    "regular-expression": "10-dynamic-programming",

    # Backtracking
    "n-queens": "11-backtracking",
    "combination": "11-backtracking",
    "permutation": "11-backtracking",
    "permutations": "11-backtracking",
    "subset": "11-backtracking",
    "letter-combination": "11-backtracking",
    "generate-parentheses": "11-backtracking",
    "gray-code": "11-backtracking",
    "word-search": "11-backtracking",
    "restore-ip": "11-backtracking",

    # Greedy
    "greedy": "12-greedy",
    "gas": "12-greedy",
    "candy": "12-greedy",
    "jump-game": "12-greedy",
    "text-justification": "12-greedy",

    # Math
    "integer-to": "13-math",
    "to-integer": "13-math",
    "roman": "13-math",
    "powx": "13-math",
    "sqrt": "13-math",
    "divide": "13-math",
    "multiply": "13-math",
    "prime": "13-math",
    "add-binary": "13-math",
    "count-and-say": "13-math",
    "missing-positive": "13-math",

    # Bit Manipulation
    "bit": "14-bit-manipulation",
    "xor": "14-bit-manipulation",
    "hamming": "14-bit-manipulation",
    "single-number": "14-bit-manipulation",

    # Strings
    "string": "15-strings",
    "anagram": "15-strings",
    "common-prefix": "15-strings",
    "strstr": "15-strings",
    "atoi": "15-strings",
    "compress": "15-strings",
    "isomorphic": "15-strings",
    "last-word": "15-strings",
    "valid-anagram": "15-strings",
    "count-and": "15-strings",

    # Hash Table
    "hash": "17-hash-table",
    "two-sum": "17-hash-table",
    "contains": "17-hash-table",

    # Prefix Sum
    "prefix-sum": "18-prefix-sum",
    "range-sum": "18-prefix-sum",

    # Intervals
    "interval": "19-intervals",
    "meeting": "19-intervals",
    "non-overlapping": "19-intervals",

    # Sorting
    "sort": "20-sorting",
    "next-permutation": "20-sorting",

    # Union Find
    "union": "21-union-find",
    "connected": "21-union-find",
    "redundant": "21-union-find",
    "accounts": "21-union-find",

    # Trie
    "trie": "22-trie",

    # Queue
    "queue": "23-queue",
    "deque": "23-queue",
}

FOLDER_LABELS = {
    "01-arrays": "Arrays",
    "02-two-pointers": "Two Pointers",
    "03-sliding-window": "Sliding Window",
    "04-stack": "Stack",
    "05-binary-search": "Binary Search",
    "06-linked-list": "Linked List",
    "07-trees": "Trees",
    "08-heap": "Heap / Priority Queue",
    "09-graphs": "Graphs",
    "10-dynamic-programming": "Dynamic Programming",
    "11-backtracking": "Backtracking",
    "12-greedy": "Greedy",
    "13-math": "Math",
    "14-bit-manipulation": "Bit Manipulation",
    "15-strings": "Strings",
    "16-misc": "Miscellaneous",
    "17-hash-table": "Hash Table",
    "18-prefix-sum": "Prefix Sum",
    "19-intervals": "Intervals",
    "20-sorting": "Sorting",
    "21-union-find": "Union Find",
    "22-trie": "Trie",
    "23-queue": "Queue",
}

IGNORE = {
    ".git", ".github",
    "organize.py", "update_readme.py", "fetch_leetcode.py",
    "README.md", "problems.json",
}

topics_folders = set(topics.values())
topics_folders.add("16-misc")


def normalize(name: str) -> str:
    """Strip leading problem number: '0042-trapping-rain-water' → 'trapping-rain-water'"""
    return re.sub(r"^\d+-", "", name.lower())


def keyword_classify(name: str):
    clean = normalize(name)
    for key, folder in topics.items():
        if key in clean:
            return folder
    return None


def classify_with_claude(problem_name: str) -> str:
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        print(f"  [AI] No ANTHROPIC_API_KEY — skipping '{problem_name}'")
        return "16-misc"

    folder_list = "\n".join(f"  {k}: {v}" for k, v in FOLDER_LABELS.items())
    clean_name = normalize(problem_name).replace("-", " ")
    prompt = (
        f"You are a DSA expert. Classify this LeetCode problem into exactly one category.\n"
        f"Return ONLY the category key, nothing else.\n\n"
        f"Problem: {clean_name}\n\n"
        f"Categories:\n{folder_list}\n\n"
        f"Reply with only the key (e.g. '07-trees')."
    )

    payload = json.dumps({
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 20,
        "messages": [{"role": "user", "content": prompt}]
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=payload,
        headers={
            "Content-Type": "application/json",
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            answer = data["content"][0]["text"].strip().lower()
            if answer in topics_folders:
                print(f"  [AI] '{problem_name}' → {answer}")
                return answer
            print(f"  [AI] Unexpected answer '{answer}' for '{problem_name}' → 16-misc")
            return "16-misc"
    except Exception as e:
        print(f"  [AI] Error for '{problem_name}': {e} → 16-misc")
        return "16-misc"


def move_to(item_path: str, item_name: str, target_folder: str):
    os.makedirs(target_folder, exist_ok=True)
    dest = os.path.join(target_folder, item_name)
    if not os.path.exists(dest):
        shutil.move(item_path, dest)
    print(f"  Moved '{item_name}' → {target_folder}/")


def process_item(item_name: str, item_path: str, metadata: dict):
    folder = keyword_classify(item_name)
    if folder is None:
        print(f"No keyword match for '{item_name}' — asking Claude AI...")
        folder = classify_with_claude(item_name)
    if folder != "16-misc":
        move_to(item_path, item_name, folder)
    metadata[item_name] = {"name": item_name, "folder": folder}


# ── Load metadata ──────────────────────────────────────────────────────────────
metadata_file = "problems.json"
metadata = {}
if os.path.exists(metadata_file):
    with open(metadata_file, "r", encoding="utf-8") as f:
        metadata = json.load(f)

# ── PASS 1: root — new problems from leetcode-sync ────────────────────────────
print("\n=== PASS 1: scanning root ===")
for item in sorted(os.listdir(".")):
    if item in IGNORE or item in topics_folders or item.startswith("."):
        continue
    if not os.path.isdir(item):
        continue
    process_item(item, item, metadata)

# ── PASS 2: rescan 16-misc — reclassify everything already stuck there ────────
misc_dir = "16-misc"
if os.path.isdir(misc_dir):
    print("\n=== PASS 2: rescanning 16-misc ===")
    for item in sorted(os.listdir(misc_dir)):
        item_path = os.path.join(misc_dir, item)
        if not os.path.isdir(item_path):
            continue
        folder = keyword_classify(item)
        if folder is None:
            print(f"No keyword match for '{item}' — asking Claude AI...")
            folder = classify_with_claude(item)
        if folder != "16-misc":
            move_to(item_path, item, folder)
        metadata[item] = {"name": item, "folder": folder}

# ── Save metadata ──────────────────────────────────────────────────────────────
with open(metadata_file, "w", encoding="utf-8") as f:
    json.dump(metadata, f, indent=2)

print("\nDone. problems.json updated.")
