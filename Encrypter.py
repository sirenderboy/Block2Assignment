import argparse
def encrypt(stringtoencrypt, cipher):
    returnstring = ""
    for char in stringtoencrypt:
        charint = ord(char)
        charint = ((charint - ord('a') + cipher) %26 + ord('a'))
        returnstring += chr(charint)

    return returnstring

def decrypt(stringtoencrypt, cipher):
    returnstring = ""
    for char in stringtoencrypt:
        charint = ord(char)
        #Compared ChatGPT alphabet bounding to my original alphabet bounding method.
        #Was using ord('0') and not ord('a')
        charint = ((charint - ord('a') - cipher) %26 + ord('a'))
        returnstring += chr(charint)
    return returnstring

parser = argparse.ArgumentParser(prog='Encrypter', description='This program encrypts a string and returns it to the cmd line')
parser.add_argument("targetString", help="The string to encrypt/decrypt")
parser.add_argument("cipher", help="The amount of letters to shift", type=int)
parser.add_argument("isDecrypting", help="1 means we're decrypting, 0 means we're encrypting", type=int, choices=[0,1])
args = parser.parse_args()
print(args.isDecrypting)
if args.isDecrypting == 1:
        print(decrypt(args.targetString, args.cipher))
else:
        print(encrypt(args.targetString, args.cipher))
