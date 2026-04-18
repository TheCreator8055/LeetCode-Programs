import os
import shutil
import json
import urllib.request
import urllib.error

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
    "trap": "01-arrays",           # trapping rain water
    "product": "01-arrays",
    "merge": "01-arrays",

    # Two Pointers
    "two": "02-two-pointers",
    "threesum": "02-two-pointers",
    "palindrome": "02-two-pointers",
    "reverse": "02-two-pointers",

    # Sliding Window
    "window": "03-sliding-window",
    "zigzag": "03-sliding-window",
    "substring": "03-sliding-window",
    "subarray": "03-sliding-window",
    "maximum": "03-sliding-window",

    # Stack
    "stack": "04-stack",
    "parentheses": "04-stack",
    "bracket": "04-stack",
    "valid": "04-stack",
    "decode": "04-stack",
    "calculator": "04-stack",
    "temperature": "04-stack",
    "histogram": "04-stack",

    # Binary Search
    "search": "05-binary-search",
    "binary": "05-binary-search",
    "kth": "05-binary-search",
    "peak": "05-binary-search",
    "median": "05-binary-search",

    # Linked List
    "list": "06-linked-list",
    "linked": "06-linked-list",
    "node": "06-linked-list",
    "cycle": "06-linked-list",
    "lru": "06-linked-list",

    # Trees
    "tree": "07-trees",
    "bst": "07-trees",
    "inorder": "07-trees",
    "preorder": "07-trees",
    "postorder": "07-trees",
    "level": "07-trees",
    "diameter": "07-trees",
    "ancestor": "07-trees",
    "depth": "07-trees",
    "height": "07-trees",
    "leaf": "07-trees",
    "root": "07-trees",
    "symmetric": "07-trees",
    "path": "07-trees",

    # Heap / Priority Queue
    "heap": "08-heap",
    "priority": "08-heap",
    "frequent": "08-heap",
    "top_k": "08-heap",
    "topk": "08-heap",
    "largest": "08-heap",
    "smallest": "08-heap",
    "kth_largest": "08-heap",

    # Graphs
    "graph": "09-graphs",
    "sudoku": "09-graphs",
    "dfs": "09-graphs",
    "bfs": "09-graphs",
    "island": "09-graphs",
    "course": "09-graphs",
    "clone": "09-graphs",
    "wall": "09-graphs",
    "pacific": "09-graphs",
    "atlantic": "09-graphs",
    "flood": "09-graphs",
    "word_ladder": "09-graphs",
    "wordladder": "09-graphs",
    "network": "09-graphs",
    "rotten": "09-graphs",

    # Dynamic Programming
    "dp": "10-dynamic-programming",
    "dynamic": "10-dynamic-programming",
    "fibonacci": "10-dynamic-programming",
    "climb": "10-dynamic-programming",
    "coin": "10-dynamic-programming",
    "knapsack": "10-dynamic-programming",
    "longest": "10-dynamic-programming",
    "subsequence": "10-dynamic-programming",
    "edit": "10-dynamic-programming",
    "triangle": "10-dynamic-programming",
    "house": "10-dynamic-programming",
    "jump": "10-dynamic-programming",
    "decode": "10-dynamic-programming",
    "partition": "10-dynamic-programming",
    "paint": "10-dynamic-programming",
    "dungeon": "10-dynamic-programming",
    "unique": "10-dynamic-programming",

    # Backtracking
    "backtrack": "11-backtracking",
    "nqueens": "11-backtracking",
    "combination": "11-backtracking",
    "permutation": "11-backtracking",
    "subset": "11-backtracking",
    "letter": "11-backtracking",
    "phone": "11-backtracking",
    "generate": "11-backtracking",
    "wordSearch": "11-backtracking",
    "wordsearch": "11-backtracking",

    # Greedy
    "greedy": "12-greedy",
    "gas": "12-greedy",
    "assign": "12-greedy",
    "candy": "12-greedy",
    "task": "12-greedy",
    "schedule": "12-greedy",

    # Math
    "math": "13-math",
    "integer": "13-math",
    "number": "13-math",
    "roman": "13-math",
    "pow": "13-math",
    "sqrt": "13-math",
    "divide": "13-math",
    "multiply": "13-math",
    "plus": "13-math",
    "prime": "13-math",
    "factorial": "13-math",
    "palindrome_num": "13-math",
    "excel": "13-math",
    "happy": "13-math",
    "bulb": "13-math",
    "digit": "13-math",
    "count_primes": "13-math",
    "countprimes": "13-math",

    # Bit Manipulation
    "bit": "14-bit-manipulation",
    "xor": "14-bit-manipulation",
    "bitwise": "14-bit-manipulation",
    "hamming": "14-bit-manipulation",
    "power_of_two": "14-bit-manipulation",
    "poweroftwo": "14-bit-manipulation",
    "single_number": "14-bit-manipulation",
    "singlenumber": "14-bit-manipulation",
    "counting_bits": "14-bit-manipulation",
    "countingbits": "14-bit-manipulation",

    # Strings
    "string": "15-strings",
    "anagram": "15-strings",
    "prefix": "15-strings",
    "strstr": "15-strings",
    "atoi": "15-strings",
    "compress": "15-strings",
    "group": "15-strings",
    "isomorphic": "15-strings",
    "longest_common": "15-strings",
    "longestcommon": "15-strings",
    "word": "15-strings",
    "sentence": "15-strings",
    "title": "15-strings",
    "zigzag_conversion": "15-strings",
    "zigzagconversion": "15-strings",

    # Misc stays as fallback
    # (16-misc handled below)

    # Hash Table
    "hash": "17-hash-table",
    "hashmap": "17-hash-table",
    "map": "17-hash-table",
    "two_sum": "17-hash-table",
    "twosum": "17-hash-table",
    "contains": "17-hash-table",

    # Prefix Sum
    "prefix_sum": "18-prefix-sum",
    "prefixsum": "18-prefix-sum",
    "range_sum": "18-prefix-sum",
    "rangesum": "18-prefix-sum",
    "subarray_sum": "18-prefix-sum",
    "subarraysum": "18-prefix-sum",

    # Intervals
    "interval": "19-intervals",
    "meeting": "19-intervals",
    "insert": "19-intervals",
    "non_overlapping": "19-intervals",
    "nonoverlapping": "19-intervals",

    # Sorting
    "sort": "20-sorting",
    "quick": "20-sorting",
    "merge_sort": "20-sorting",
    "mergesort": "20-sorting",
    "bubble": "20-sorting",
    "counting_sort": "20-sorting",
    "countingsort": "20-sorting",

    # Union Find
    "union": "21-union-find",
    "disjoint": "21-union-find",
    "connected": "21-union-find",
    "component": "21-union-find",
    "redundant": "21-union-find",
    "accounts": "21-union-find",

    # Trie
    "trie": "22-trie",
    "prefix_tree": "22-trie",
    "prefixtree": "22-trie",
    "implement_trie": "22-trie",
    "implementtrie": "22-trie",

    # Queue
    "queue": "23-queue",
    "deque": "23-queue",
    "moving_average": "23-queue",
    "movingaverage": "23-queue",
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
    ".git",
    ".github",
    "organize.py",
    "update_readme.py",
    "fetch_leetcode.py",
    "README.md",
    "problems.json",
}

topics_folders = set(topics.values())
topics_folders.add("16-misc")


# ─────────────────────────────────────────────
# Claude AI classifier (called only for unmatched problems)
# ─────────────────────────────────────────────

def classify_with_claude(problem_name: str) -> str:
    """
    Ask Claude to classify a LeetCode problem name into a DSA topic folder.
    Returns a folder string like '07-trees', or '16-misc' on failure.
    """
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        print(f"  [AI] No ANTHROPIC_API_KEY found — skipping AI classification for '{problem_name}'")
        return "16-misc"

    folder_list = "\n".join(f"  {k}: {v}" for k, v in FOLDER_LABELS.items())
    prompt = (
        f"You are a DSA (Data Structures & Algorithms) expert.\n"
        f"Given the LeetCode problem folder name below, return ONLY the single best matching "
        f"category key from the list. Nothing else — just the key.\n\n"
        f"Problem folder name: {problem_name}\n\n"
        f"Available categories:\n{folder_list}\n\n"
        f"Reply with only the category key (e.g. '07-trees')."
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
            else:
                print(f"  [AI] Unexpected answer '{answer}' for '{problem_name}' — using 16-misc")
                return "16-misc"
    except Exception as e:
        print(f"  [AI] API error for '{problem_name}': {e} — using 16-misc")
        return "16-misc"


# ─────────────────────────────────────────────
# Main organiser logic
# ─────────────────────────────────────────────

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

    lower = item.lower().replace("-", "_").replace(" ", "_")

    # ── 1. Keyword match (fast, free) ──────────────────────────────
    folder = None
    for key, dest_folder in topics.items():
        if key in lower:
            folder = dest_folder
            break

    # ── 2. Claude AI fallback (only when keyword match fails) ──────
    if folder is None:
        print(f"No keyword match for '{item}' — asking Claude AI...")
        folder = classify_with_claude(item)

    # ── 3. Move ────────────────────────────────────────────────────
    os.makedirs(folder, exist_ok=True)
    dest = os.path.join(folder, item)
    if not os.path.exists(dest):
        shutil.move(item, dest)
        print(f"Moved '{item}' → {dest}")

    metadata[item] = {"name": item, "folder": folder}

with open(metadata_file, "w", encoding="utf-8") as f:
    json.dump(metadata, f, indent=2)

print("\nDone. problems.json updated.")
