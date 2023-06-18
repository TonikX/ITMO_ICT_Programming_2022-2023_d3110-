def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext=""
    for word in plaintext:#用word进行遍历
        if word.isupper():#isupper函数判断word是否为大写字母
            #ord函数找到word对应的Unicode码
            #公式C=(P+3) mod 26
            ciphertext += chr((ord(word) - 65 + shift) % 26 + 65)
        elif word.islower():
            ciphertext += chr((ord(word) - 97 + shift) % 26 + 97)
        else:
            ciphertext = ciphertext + word
    return ciphertext
a=encrypt_caesar("PYTHON")
print(a)
a=encrypt_caesar("python")
print(a)
a=encrypt_caesar("Python3.6")
print(a)

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    plaintext=""
    for word in ciphertext:
        if word.isupper():
            #公式P=(C-3) mod 26
            plaintext += chr((ord(word) - 65 - shift) % 26 + 65)
        elif word.islower():
            plaintext += chr((ord(word) - 97 - shift) % 26 + 97)
        else:
            plaintext = plaintext + word
    return plaintext
a=decrypt_caesar("SBWKRQ")
print(a)
a=decrypt_caesar("sbwkrq")
print(a)
a=decrypt_caesar("Sbwkrq3.6")
print(a)
