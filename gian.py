# Given a set S of letters (a-z), say if a palindrome can be built.
# Sample:
# {aabb} = true
# {abc}  = false
# {aac}  = true

def can_build_palindrome(s):
    odd = False
    count = 1

    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            count += 1
        else:
            if count % 2 != 0:
                if odd:
                    return False
                else:
                    odd = True

            count = 1

    if odd and count % 2 != 0:
        return False

    return True

s = "abbcc"
print(can_build_palindrome(s))