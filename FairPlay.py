'''
Exercise # 1:
    Write a program that can encrypt and decrypt using the general Caesar cipher,
    FairPlay and Vigenère cipher.
Exercise # 2:
    Write a program that can perform a letter frequency attack on any monoalphabetic
    substitution cipher without human intervention. Your software should produce
    possible plaintexts in rough order of likelihood. It would be good if your user
i   nterface allowed the user to specify “give me the top 5 possible plaintexts.
'''
def createMatrix(key):
    
    a = 'a'
    key_count = 0
    key_len = len(key)
    #this list keeps track of the letters have already been used in the key
    alphabet = [False]*26 
    
    #iterate through the matrix key
    for i in range(0,5):
        for j in range(0,5):
            #check to see if letter has already been inserted into the matrix
            if alphabet[ord(key[key_count]) - 97] == False or alphabet[a - 97] == False: #check to see if the next letter is already in the matrix
                #fill matrix with key
                if (key_count < key_len): # potential bug --> see if index is correct
                    matrix[i][j] = key[key_count]
                    key_count += 1
                    alphabet[ord(key[key_count]) - 97] = True #mark the letter as used
                #fill matrix with alphabet
                else:
                    matrix[i][j] = a
                    a += chr(ord(a) + 1)
                    alphabet[a - 97] == True #mark the letter as used
         
    return matrix
#===================================================================================================================    

plaintext = list(input("Enter the Plaintext: "))
key = list(input("Enter the keyword: "))

matrix = createMatrix(key)

print(matrix)
