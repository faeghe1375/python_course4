from string import ascii_letters
def encrypt(string,key):
    alpha= ascii_letters
    result = ""
    for ch in string:
        if ch not in alpha:
            result =+ ch
        else:
            new_key= (alpha.index(ch) + key) % len(alpha)
            result += alpha[new_key]
    return result 
print(encrypt('faeghe',4))

