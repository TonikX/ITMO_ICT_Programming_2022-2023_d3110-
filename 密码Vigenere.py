def VigenereEncrypto(message, key):
    msLen = len(message)
    keyLen = len(key)
    message = message.upper()
    key = key.upper()
    raw = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"# 明文空间
    # 定义加密后的字符串
    ciphertext = ""
    # 开始加密
    for i in range(0, msLen):
        # 轮询key的字符
        j = i % keyLen
        # 判断字符是否为英文字符，不是则直接向后面追加且继续
        if message[i] not in raw:
            ciphertext += message[i]
            continue
        encodechr = chr((ord(message[i]) - ord("A") + ord(key[j]) - ord("A")) % 26 + ord("A"))
        # 追加字符
        ciphertext += encodechr
    return ciphertext



def VigenereDecrypto(ciphertext, key):
    msLen = len(ciphertext)
    keyLen = len(key)
    key = key.upper()
    raw = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"# 密文空间
    plaintext = ""
    for i in range(0, msLen):# 开始解密
        # 轮询key的字符
        j = i % keyLen
        # 判断字符是否为英文字符，不是则直接向后面追加且继续
        if ciphertext[i] not in raw:
            plaintext += ciphertext[i]
            continue
        decodechr = chr((ord(ciphertext[i]) - ord("A") - ord(key[j]) - ord("A")) % 26 + ord("A"))
        # 追加字符
        plaintext += decodechr
    # 返回加密后的字符串
    return plaintext

text = VigenereEncrypto("PYTHON", "A")
print(text)
text = VigenereEncrypto("python", "a")
print(text)
text = VigenereEncrypto("ATTACKATDAWN", "LEMON")
print(text)

text = VigenereDecrypto("PYTHON", "A")
print(text)
text = VigenereDecrypto("python", "a")
print(text)
text = VigenereDecrypto("LXFOPVEFRNHR", "LEMON")
print(text)