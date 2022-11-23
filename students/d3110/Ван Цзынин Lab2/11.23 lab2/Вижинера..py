a = input().split()
Plaintext = a[1]
plalen = len(a[1])
key = a[0]#密钥
keylen = len(a[0])
passward = ''
if plalen <= keylen:
    for i in range(plalen):
        k = 0
        if key[i].islower():
            k = ord(key[i]) - ord('a')
        else:
            k = ord(key[i]) - ord('A')
        temp = ord(Plaintext[i])+k
        if Plaintext[i].islower():
             if temp > ord('z'):
                 passward += chr(temp - ord('z') + ord('a') - 1)
             else:
                 passward += chr(temp)
        else:
            if temp > ord('Z'):
                passward += chr(temp - ord('Z') + ord('A') - 1)
            else:
                passward += chr(temp)
else:
    key1 = str(key * (plalen // keylen) + key[:plalen - len(key * (plalen // keylen))])
    for i in range(plalen):
        k = 0
        if key1[i].islower():
            k = ord(key1[i]) - ord('a')
        else:
            k = ord(key1[i]) - ord('A')
        temp = ord(Plaintext[i]) + k
        if Plaintext[i].islower():
            if temp > ord('z'):
                passward += chr(temp - ord('z') + ord('a') - 1)
            else:
                passward += chr(temp)
        else:
            if temp > ord('Z'):
                    passward += chr(temp - ord('Z') + ord('A') - 1)
            else:
                passward += chr(temp)
print(passward)
