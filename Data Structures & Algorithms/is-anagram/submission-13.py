from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_bag = Counter();
        t_bag = Counter();
        s_set = set();
        t_set = set();
        
        for char in s:
            s_bag.update(char);
            s_set.add(char);
        for char in t: 
            t_bag.update(char);
            t_set.add(char);

        # the set lengths and sets need to be equal 
        if ((len(s_set) != len(t_set)) or (s_set != t_set)):
            return False;
            
        # now we will loop through every letter in one of the sets
        # check bags at that char 
        # if any of them arent equal we return false 
        for char in s_set:
            if (s_bag[char] != t_bag[char]): return False;

        return True;

        