def getcoords(matrix, char):
    for i in range(len(matrix)):
        if char in matrix[i]:
            return (i, matrix[i].index(char))

def keygen(key):
    matrix = [['']*5 for _ in range(5)]
    
    string = 'abcdefghiklmnopqrstuvwxyz'
    k = 0
    l = 0
    for i in range(5):
        for j in range(5):
            if k < len(key):
                matrix[i][j] = key[k]
                k += 1
            else:
                while string[l] in key:
                    l += 1
                matrix[i][j] = string[l]
                l += 1
                
    print("The matrix is:")
    for row in matrix:
        print(row)
        
    return matrix            

def encrypt(text, matrix):
     
    text = text.replace(" ", "").lower()
    
    # x filler
    new_text = ""
    prev_char = ''
    for char in text:
        if char == prev_char:
            new_text += 'x' + char
        else:
            new_text += char
        prev_char = char
    
   #odd length characters
    if len(new_text) % 2 == 1:
        new_text += 'x'
    
    
    pairs = [new_text[i:i+2] for i in range(0, len(new_text), 2)]
    
    encrypted_text = ""
    for pair in pairs:
        x1, y1 = getcoords(matrix, pair[0])
        x2, y2 = getcoords(matrix, pair[1])
        if x1 == x2:
            encrypted_text += matrix[x1][(y1 + 1) % 5] + matrix[x2][(y2 + 1) % 5]
        elif y1 == y2:
            encrypted_text += matrix[(x1 + 1) % 5][y1] + matrix[(x2 + 1) % 5][y2]
        else:
            encrypted_text += matrix[x1][y2] + matrix[x2][y1]
    
    return encrypted_text


key_matrix = keygen('keyword')
encrypted = encrypt('hello', key_matrix)
print("Encrypted : ", encrypted)
