def decrypter(encrypted_pass):
    xlat = list("dsfd;kfoA,.iyewrkldJKDHSUBsgvca69834ncxv9873254k;fg87")
    encrypted_pass = list(encrypted_pass)
    clear_pw = [-1] * (len(encrypted_pass)//2 - 1)

    val = 0

    if(len(encrypted_pass)%2 != 0):
        print("ERROR : incorrect encrypted password format due to odd lenght")
        return -1


    seed = (int(encrypted_pass[0])) * 10 + int(encrypted_pass[1])

    if(seed > 15 or not(encrypted_pass[0].isnumeric()) or not(encrypted_pass[0].isnumeric()) ):
        print("ERROR : incorrect encrypted password format due to the first two characters being wrong")
        return -1


    for i in range(2,len(encrypted_pass)+1,1):

        if(i != 2 and i%2 == 0):
            clear_pw[i//2 - 2] = chr( val ^ ord(xlat[seed]) )
            seed += 1
            val = 0

        if(i != len(encrypted_pass)):
            val *=  16

            if encrypted_pass[i].isnumeric() : 
                val += int(encrypted_pass[i])
            else:
                encrypted_pass[i] = encrypted_pass[i].upper()
                c = encrypted_pass[i]
                if ord(c) >= ord('A') and ord(c) <= ord('F') :
                    val += int(c, 16)
    
    clear_pw = ''.join(map(str, clear_pw))
    return clear_pw


#This is the cisco type 7 encription of the string "password"
password = "021605481811003348"
password = decrypter(password)
print(password)
