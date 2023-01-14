def encryption():
    str_raw = input("please input word:")
    k = int(input("Please enter displacement value:"))
    str_change = str_raw.lower()
    str_list = list(str_change)
    str_list_encry = str_list
    i = 0
    while i < len(str_list):
        if ord(str_list[i]) < 123-k:
            str_list_encry[i] = chr(ord(str_list[i]) + k)
        else:
             str_list_encry[i] = chr(ord(str_list[i]) + k - 26)
             i = i+1
    print ("The encrypted result is:"+"".join(str_list_encry))
def decryption():
    str_raw = input("Please enter the ciphertext:")
    k = int(input("Please enter displacement value:"))
    str_change = str_raw.lower()
    str_list = list(str_change)
    str_list_decry = str_list
    i = 0
    while i < len(str_list):
        if ord(str_list[i]) >= 97+k: str_list_decry[i] = chr(ord(str_list[i]) - k)
        else: str_list_decry[i] = chr(ord(str_list[i]) + 26 - k)
        i = i+1
    print ("The encrypted result is:"+"".join(str_list_decry))
while True:
    print (u"1. encryption")
    print(u"2. decrypt")
    choice = input("please select:")
    if choice == "1": encryption()
    elif choice == "2": decryption()
    else: print (u"wrong input!")