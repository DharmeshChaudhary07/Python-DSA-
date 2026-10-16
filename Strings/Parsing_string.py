# ----------------------------------------------------- String Parsing -------------------------------------------------------

# Core concept
# Parsing means reading a string from left to right and turning it into structured values: skip spaces, read a sign, 
# read digits, split on delimiters. Keep an index i and move it forward step by step, like a tiny state machine. 
# This is the string skill closest to real DE work (log lines, CSV fields, dates, version numbers).

# Quick tools: s.split() splits on any whitespace and drops empty pieces. s.split(',') keeps empty pieces. ' '.join(list) rebuilds. 
# s.strip() removes surrounding spaces.

# -------------------------------

def my_atoi(s):
    i, n = 0, len(s)
    while i < n and s[i] == ' ':              # 1) skip spaces
        i += 1
    sign = 1
    if i < n and s[i] in '+-':                # 2) read the sign
        sign = -1 if s[i] == '-' else 1
        i += 1
    result = 0
    while i < n and '0' <= s[i] <= '9':       # 3) read digits
        result = result * 10 + (ord(s[i]) - ord('0'))
        i += 1
    result *= sign
    return max(-2**31, min(2**31 - 1, result))   # 4) clamp to 32-bit range

# -------------------------------

def reverse_words(s):
    return " ".join(reversed(s.split()))      # split() handles extra spaces

def longest_common_prefix(strs):              # vertical scan: column by column
    for i in range(len(strs[0])):
        for s in strs[1:]:
            if i == len(s) or s[i] != strs[0][i]:
                return strs[0][:i]
    return strs[0]

# ----------------------------------------------------------------------------------------------------------------------------

# Time: O(n). Space: O(1) for atoi, O(n) when you build lists.

# Approach: Write the steps in plain English first (skip, sign, digits, clamp), then code one step at a time. Handle the input 
# that stops early (empty string, only spaces, no digits).

# Common mistakes: forgetting the 32-bit clamp; using s.split(' '), which leaves empty strings when there are several spaces; 
# stopping at the wrong place when a non-digit appears; s.isdigit() accepts characters like '²', so compare with '0' <= c <= '9' instead.

# Recognize the pattern: “convert a string to a number”, “split by a delimiter”, “version numbers”, “reverse words”.