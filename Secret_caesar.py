# some of this code was taken from https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/
#most recent change made on 12/12/22
# this function will decrypt the message
def decrypt(text,s):
    result = ""
    #calculate the shift used to decrypt the message by subtracting the origional shift from 26
    decryptShift = 26 - s
    # traverse text
    for i in range(len(text)):
        char = text[i]

        # decrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + decryptShift-65) % 26 + 65)

        # decrypt lowercase characters
        else:
            result += chr((ord(char) + decryptShift - 97) % 26 + 97)

    return result
#call the function for the different encrypted strings
#simply coppy the following line of code once for every string to descrypt. then, replace the hashtags in the quotes with the string to decrypt, and replace
#the lone hashtag with the shift used to encrypt the message. do not add any extra spaces or commas. 
print(decrypt("#######", #))
