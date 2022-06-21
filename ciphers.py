# ----------------------Index Sub Cipher----------------------
from pickletools import stringnl


def encryptIndexSubstitutionCipher(text):
    strin = []
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
    pass

def decryptMorseCode(text):
    pass

# ----------------------Affine Cipher----------------------
def encryptAffineCipher(text, a, b):
    pass

def decryptAffineCipher(text, a, b):
    pass

# ----------------------Caesar Cipher----------------------
def encryptCaesarCipher(text, key1, key2):
    pass

def decryptCaesarCipher(text, key1, key2):
    pass


# ----------------------Transposition Cipher----------------------
def encryptTranspositionCipher(text, key):
    pass

def decryptTranspositionCipher(text, key):
    pass