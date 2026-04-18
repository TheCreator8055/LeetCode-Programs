class Solution {
    public String simplifyPath(String path) {
        Deque<String> stack = new LinkedList<>();
        for (String dir : path.split("/")) {
            if (dir.equals("..")) stack.pollLast();
            else if (!dir.equals("") && !dir.equals(".")) stack.addLast(dir);
        }
        return "/" + String.join("/", stack);
    }
}

