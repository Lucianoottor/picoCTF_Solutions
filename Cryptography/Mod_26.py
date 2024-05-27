enc_flag = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ}"
flag = ""
for i in enc_flag:
    character = i
    if(character.isalpha() == True):
        if(character.isupper()):
            flag += chr((ord(character) + 13-65) % 26 + 65)
        elif(character.islower()):
            flag += chr((ord(character) + 13-97) % 26 + 97)
    else:
        flag += character
print(flag)
        
