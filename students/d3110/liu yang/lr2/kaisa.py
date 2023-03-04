def jiami():
    str=input("请输入明文：")
    n=int(input("请输入密钥："))
    str_encrypt=""
    for letter in str:
            if letter==" ":  #遇到空格选择不加密
                letter_encrypt=" "
            else:
                letter_encrypt=chr((ord(letter)-ord("a") +n) %26 +ord("a"))
            str_encrypt += letter_encrypt
    print("密文为：",str_encrypt)
def jiemi():
    str=input("请输入密文：")
    n=int(input("请输入密钥："))
    str_decrypt=""
    for word in str:
        if word==" ":  #遇到空格选择不解密
            word_decrypt=" "
        else:
            word_decrypt=chr((ord(word)-ord("A") -n) %26 +ord("A"))
        str_decrypt = str_decrypt+word_decrypt
    print("明文为：",str_decrypt)

while 1==1:
    a=str=input("解密输入2，加密输入1， 3退出")
    if a==1:
      jiami()
    elif a==2:
        jiemi()
    elif a==3:
        break