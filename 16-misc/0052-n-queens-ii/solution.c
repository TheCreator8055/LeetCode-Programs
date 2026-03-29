int total;
void backtrack(int row, int n, int col, int d1, int d2) {
    if (row == n) { total++; return; }
    int available = ((1 << n) - 1) & ~(col | d1 | d2);
    while (available) {
        int p = available & -available;
        backtrack(row + 1, n, col | p, (d1 | p) << 1, (d2 | p) >> 1);
        available ^= p;
    }
}
int totalNQueens(int n) {
    total = 0;
    backtrack(0, n, 0, 0, 0);
    return total;
}

