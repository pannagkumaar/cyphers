def keygen(key, word):
    key = key * ((len(word)//len(key)))
    key += key[0:(len(word)-len(key))]
    return key


def matrix_gen():
    matrix = [['']*26 for _ in range(26)]
    string = 'abcdefghijklmnopqrstuvwxyz'

    for i in range(26):
        for j in range(26):
            matrix[i][j] = string[(i + j) % 26]

    return matrix


def encrypt(keyword, word, matrix):
    encrypt = ''
    for i in range(len(word)):
        x1, y1 = (ord(word[i])-97), (ord(keyword[i])-97)
        encrypt += matrix[x1][y1]
    print(" The encrypted text is ", encrypt)
    return encrypt


def decrypt(keyword, encrypted, matrix):
    decrypted = ''
   
    for i in range(len(keyword)):
        y1 = ord(keyword[i]) - 97
        for j in range(26):
            if matrix[j][y1] == encrypted[i]:
                x1 = j
                break
        
        decrypted += chr(x1 + 97)
    
    print("The decrypted text is", decrypted)

key = input("Enter the keyword")
word = input("Enter the word that will be encrypted")
modified_keyword = keygen(key, word)
decrypt(modified_keyword,encrypt(word.lower(), modified_keyword.lower(), matrix_gen()), matrix_gen())

