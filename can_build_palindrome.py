# Given a set S of letters (a-z), say if a palindrome can be built.
# Sample:
# {aabb} = true
# {abc}  = false
# {aac}  = true
# {abab} = true
# {bcbcba} = false

def can_build_palindrome(s):
    m = {}
    odd = False

    for c in s:
        if m.get(c):
            m[c] += 1
        else:
            m[c] = 1

    for c in m.keys():
        if m[c] % 2 != 0:
            if odd:
                return False
            odd = True

    return True

s = input()
print(can_build_palindrome(s))