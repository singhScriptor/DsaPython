def miniColor(s,k):
    if(k>len(s)):return
    mini=float('inf')
    for i in range(len(s)-k+1):
        count=0
        for j in range(i,i+k):
            if(s[j]=='W'):
                count+=1
        mini=min(mini,count)
    return mini
s="BWBBW"
k=3 
print(miniColor(s,k)) 


# Task details

# Problem Statement:

# You are given a string s consisting of 'B' (black) and 'W' (white) characters. Your task is to find the minimum number of recolor operations required to obtain a substring of length k consisting of k consecutive 'B' characters. A recolor operation involves changing a 'W' character to 'B'

# Constraints:

# 1 <= |s| <= 10^5
# 1 <= k <= |s|
# Input Format:

# A string s consisting of 'B' and 'W' characters.
# An integer k representing the length of the desired substring consisting of consecutive 'B' characters.
# Output Format:

# Output an integer representing the minimum number of recolor operations required to obtain a substring of length k consisting of k consecutive 'B' characters.

# Examples:

# Input:

# s = "BWBBW"

# k = 3

# Output : 1

# Explanation: In the given string, the substring "BBB" consisting of 3 consecutive 'B' characters can be obtained by recoloring the 'W' character at index 2.


