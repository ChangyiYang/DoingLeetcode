# https://leetcode.cn/problems/replace-words/?envType=study-plan-v2&id=bytedance-2023-spring-sprint

class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        
        # first, sort the dictionary
        
        dictionary = sorted(dictionary, key = lambda x: len(x))
        
        sentence = sentence.split()
        
        for i ,word in enumerate(sentence):
            for root in dictionary:
                if word.startswith(root):
                    sentence[i] = root
                    break
                
        return ' '.join(sentence)
            
        