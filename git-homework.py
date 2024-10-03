def word(text):
    if not isinstance(text,str):
        return False
    text = list(text)
    text.sort()
    for i in range(len(text)):
        for j in range(i+1, len(text)):
            if text[i] == text[j]:
                return False
    return True
    
print(word('hello'))


