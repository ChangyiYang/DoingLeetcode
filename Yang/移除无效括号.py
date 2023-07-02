# https://leetcode.cn/problems/minimum-remove-to-make-valid-parentheses/



class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        q = []

        del_list = []


        for i in range(len(s)):
            if s[i] == '(':
                q.append(i)

            if s[i] == ')':
                if q != []:
                    q.pop()
                else:
                    del_list.append(i)

        result  = ""

        for i in range(len(s)):
            if i in q or i in del_list:
                continue

            result += s[i]


        return result


        