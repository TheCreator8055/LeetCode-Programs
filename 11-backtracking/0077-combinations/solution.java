class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> res = new ArrayList<>();
        backtrack(1, n, k, new ArrayList<>(), res);
        return res;
    }
    private void backtrack(int start, int n, int k, List<Integer> current, List<List<Integer>> res) {
        if (current.size() == k) {
            res.add(new ArrayList<>(current));
            return;
        }
        for (int i = start; i <= n; i++) {
            current.add(i);
            backtrack(i + 1, n, k, current, res);
            current.remove(current.size() - 1);
        }
    }
}

