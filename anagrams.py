
def are_anagrams(str1:str, str2: str):
    str1 = str1.lower()
    str2 = str2.lower()
    
    if(len(str1) == len(str2)):
        sorted_str1 = sorted(str1)
        sorted_str2 = sorted(str2)

        if(sorted_str1 == sorted_str2):
            return True
        else:
            return False
    
    return False
