class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        return_list = []
        d = set()
        for i,word in enumerate(words):
            for y,word2 in enumerate(words):
                if i == y:
                    continue
                if word not in d and word in word2:
                    return_list.append(word)
                    d.add(word)
                    break
        return return_list 