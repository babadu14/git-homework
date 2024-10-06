def word(text):
    if not isinstance(text,str):
        return False
    text = list(text)
    text.sort()
    l,r = 0, 1
    while len(text) > r:
        if text[l] == text[r]:
            return False
        l +=1
        r += 1
    return True
    
print(word('telfoni'))


def reverse_string(string):
    if not isinstance(string, str):
        return False
    str1 = ''
    index = len(string)
    while index > 0:
        str1 += string[index - 1]
        index -=1 
    return str1
print(reverse_string('hello'))


def string_to_dictioanry(strg):
    if not isinstance(strg, str):
        return False
    dic = {}
    for letter in strg:
        if letter in dic:
            dic[letter] += 1
        else:
            dic[letter] = 1
    return dic
    
print(string_to_dictioanry('hello'))