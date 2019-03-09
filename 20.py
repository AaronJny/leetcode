class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a_list = []
        left = ['(', '[', '{']
        right = [')', ']', '}']
        for i in s:
            if len(a_list) == 0:
                if i in right:
                    return False
                else:
                    a_list.append(i)
            else:
                if i in left:
                    a_list.append(i)
                else:
                    if len(a_list) == 0:
                        return False
                    if i == ')' and a_list[-1] == '(':
                        a_list.pop(-1)
                    elif i == ']' and a_list[-1] == '[':
                        a_list.pop(-1)
                    elif i == '}' and a_list[-1] == '{':
                        a_list.pop(-1)
                    else:
                        return False
        if len(a_list) != 0:
            return False
        else:
            return True
