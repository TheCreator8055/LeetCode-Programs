class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> res;
        int i = 0;
        while (i < words.size()) {
            int j = i + 1, lineLen = words[i].length();
            while (j < words.size() && lineLen + 1 + words[j].length() <= maxWidth) {
                lineLen += 1 + words[j].length();
                j++;
            }
            
            string line = words[i];
            int numWords = j - i;
            // Case 1: Last line or only one word in line (Left Justify)
            if (j == words.size() || numWords == 1) {
                for (int k = i + 1; k < j; k++) line += " " + words[k];
                line += string(maxWidth - line.length(), ' ');
            } else { 
                // Case 2: Middle line with multiple words (Fully Justify)
                int totalSpaces = maxWidth - (lineLen - (numWords - 1));
                int spaceBetween = totalSpaces / (numWords - 1);
                int extraSpaces = totalSpaces % (numWords - 1);
                for (int k = i + 1; k < j; k++) {
                    int s = spaceBetween + (extraSpaces-- > 0 ? 1 : 0);
                    line += string(s, ' ') + words[k];
                }
            }
            res.push_back(line);
            i = j;
        }
        return res;
    }
};

