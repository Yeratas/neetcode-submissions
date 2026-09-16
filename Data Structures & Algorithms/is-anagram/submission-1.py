class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict_s = {}
        my_dict_t = {}

        if len(s)!=len(t):
            return False

        for i in range(len(s)):
            if s[i] not in my_dict_s:
                my_dict_s[s[i]] = 1
            else:
                my_dict_s[s[i]]+=1

        for i in range(len(t)):
            if t[i] not in my_dict_t:
                my_dict_t[t[i]] = 1
            else:
                my_dict_t[t[i]]+=1
        
        return my_dict_s == my_dict_t