class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        common_prefix = ""
        first_word = strs[0]
        #helps us pick the character we're looking at
        for char_idx in range(len(first_word)): 
            #helps us pick the word we are looking at
            for word_idx in range(1, len(strs)): 
                if len(strs[word_idx]) <= char_idx:
                    return common_prefix
                #if chars don't match return the common prefix
                if strs[word_idx][char_idx] != first_word[char_idx]:
                    return common_prefix
            common_prefix += first_word[char_idx]
        return common_prefix

def main():
    strs = ["flower", "flow", "flight"]
    sol = Solution()
    print(sol.longestCommonPrefix(strs))

if __name__ == '__main__':
    main()