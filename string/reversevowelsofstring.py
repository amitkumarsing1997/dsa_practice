def reverse_vowel_string(s):
    s = list(s)
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    value = []
    pos = []
    for i in range(len(s)):
        if s[i] in vowels:
            value.append(s[i])
            pos.append(i)
        value.reverse()
    for i in range(len(pos)):
        s[pos[i]] = value[i]
    return "".join(s)

s = "hello"
print(reverse_vowel_string(s))