
# Two pointer method
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean_str = [i.lower() for i in s if i.isalnum()]
        len_clean_str = len(clean_str)

        index = 0
        while index+1 <= len_clean_str//2:
            
            if clean_str[index] != clean_str[-index-1]:
                return False
            index+=1

        else:
            return True


# more efficient method
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean_str = [i.lower() for i in s if i.isalnum()]
        
        return clean_str == clean_str[::-1]