# ----------------------Index Sub Cipher----------------------



def encryptIndexSubstitutionCipher(text):
    rettext = ""
    for letter in text:
        rettext += ("0"+str(ord(letter)-96)) if ord(letter) < 106 else (str(ord(letter)-96))
        rettext += " "

    return rettext


def decryptIndexSubstitutionCipher(text):
    rettext = ""
    lst = []
    for index in range(0,len(text)):
        if index % 3 == 1:
            lst.append(text[index-1:index+1])
            rettext += chr(int(text[index-1:index+1])+96)

    return rettext

# ----------------------Morse Code----------------------
morseCode = {
    'a': '._',
    'b': '_...',
    'c': '_._.',
    'd': '_..',
    'e': '.',
    'f': '.._.',
    'g': '__.',
    'h': '....',
    'i': '..',
    'j': '.___',
    'k': '_._',
    'l': '._..',
    'm': '__',
    'n': '_.',
    'o': '___',
    'p': '.__.',
    'q': '__._',
    'r': '._.',
    's': '...',
    't': '_',
    'u': '.._',
    'v': '..._',
    'w': '.__',
    'x': '_.._',
    'y': '_.__',
    'z': '__..'
}

def encryptMorseCode(text):
    rettext = ""
    for letter in text:
        rettext += morseCode[letter]
        rettext += " "
    return rettext


def decryptMorseCode(text):
    code = morseCode.items()
    temporary = ""
    rettext = ""

    for letter in text:
        if letter != " ":
            temporary += letter
        else:
            for member in code:
                if member[1] == temporary:
                    rettext += member[0]
                    temporary = ""         
           
    return rettext

# ----------------------Affine Cipher----------------------
def encryptAffineCipher(text, a, b):
    rettext = ""

    for letter in text:
        #using x for more clarity with the formula
        #e(x) = (a*x + b) % 26 
        x = ord(letter)-97
        rettext += chr((a*x + b) % 26 + 97)
    return rettext


def decryptAffineCipher(text, a, b):
    rettext = ""
    
    for letter in text:
        #d(x) = (pow(a,-1,26) * (x - b)) % 26
        x = ord(letter) - 97
        rettext += chr((pow(a, -1, 26) * (x-b)) % 26 + 97)
    return rettext


# ----------------------Caesar Cipher----------------------
def encryptCaesarCipher(text, key1, key2):
    masterKey = key1 # A made up name for clarity
    rettext = ""

    for index in range(0, len(text)):
        if index % 2 == 1:
            masterKey = key2
        else:
            masterKey = key1
        numvalue = ord(text[index])
        if numvalue < 58 and numvalue > 47:
            if numvalue + masterKey % 10 > 58:
               numvalue -= 10
            rettext += chr(numvalue + masterKey % 10)
        elif numvalue > 65 and numvalue < 90:
            if numvalue + masterKey % 26 > 90:
               numvalue -= 26
            rettext += chr(numvalue + masterKey % 26)
        elif numvalue > 96 and numvalue < 122:
            if numvalue + masterKey % 26 > 122:
               numvalue -= 26
            rettext += chr(numvalue + masterKey % 26)
        else:
            rettext += chr(numvalue)
    return rettext

def decryptCaesarCipher(text, key1, key2):
    masterKey = key1
    rettext = ""

    for index in range(0, len(text)):
        if index % 2 == 1:
            masterKey = key2
        else:
            masterKey = key1
        numvalue = ord(text[index])
        if numvalue < 58 and numvalue > 47:
            if numvalue + masterKey % 10 < 47:
               numvalue += 10
            rettext += chr(numvalue - masterKey % 10)
        elif numvalue > 65 and numvalue < 90:
            if numvalue + masterKey % 26 < 65:
               numvalue += 26
            rettext += chr(numvalue - masterKey % 26)
        elif numvalue > 96 and numvalue < 122:
            if numvalue + masterKey % 26 < 96:
               numvalue += 26
            rettext += chr(numvalue - masterKey % 26)
        else:
            rettext += chr(numvalue)
    return rettext



# ----------------------Transposition Cipher----------------------
def encryptTranspositionCipher(text, key):
    lst = []
    temp = ""
    rettext = ""
    for index in range(0, len(text)):
        if (index + 1) % key == 0 :   
            temp += text[index]
            lst.append(temp)
            temp = ""
        else:
            temp += text[index]
            if index == len(text)-1:
                lst.append(temp)
               
    temp = ""

    for index in range(0, key):
       for part in lst:
        if len(part) == key:
            temp += part[index]
        elif index < len(part):
            temp += part[index]
        rettext += temp
        temp = ""
    return rettext
               


def decryptTranspositionCipher(text, key):
    rettext = ""
    doubleArray = [[]]
    num = len(text)//key
    counter = len(text) - num * key

    for char in text:
        print(char)
        doubleArray.insert(text.index(char) % key, char)

    for vector in doubleArray:
        for element in vector:
            rettext += element

    return rettext
    

