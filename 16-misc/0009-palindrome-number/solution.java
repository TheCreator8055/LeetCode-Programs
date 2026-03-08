class Solution {
    public boolean isPalindrome(int x) {
        // Edge cases: negative numbers or numbers ending in 0 (except 0)
        if (x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }

        int revertedNumber = 0;
        while (x > revertedNumber) {
            revertedNumber = revertedNumber * 10 + x % 10;
            x /= 10;
        }

        // For odd lengths, we get rid of the middle digit by /10
        return x == revertedNumber || x == revertedNumber / 10;
    }
}

