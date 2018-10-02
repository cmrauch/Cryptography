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
def init_matrix():
  n = 5
  m = 5
  a = ['a'] * n
  for i in range(n):
    a[i] = ['a'] * m
  return a

def createMatrix(key):
    
    a = 97
    key_count = 0
    key_len = len(key)
    matrix = init_matrix()
    #this list keeps track of the letters have already been used in the key
    alphabet = [False]*26 
    
    #iterate through the matrix key
    for i in range(0,5):
        for j in range(0,5):
          
          #check for duplicates
          
                   
          if key_count < key_len:
          #add key
            if not alphabet[ord(key[key_count]) - 97]:
              matrix[i][j] = key[key_count]
              alphabet[ord(key[key_count]) - 97] = True
            key_count = key_count + 1       
          #add alphabet
          elif a < 123:
            if not alphabet[a - 97]:
              matrix[i][j] = chr(a)
              print('or here')
              alphabet[(a - 97)] = True
            a = a + 1#increment a
          
          
    return matrix
  
plaintext = list(input("Enter the Plaintext: "))
key = list(input("Enter the keyword: "))

matrix = createMatrix(key)

print(matrix)
#===================================================================================================================    

plaintext = list(input("Enter the Plaintext: "))
key = list(input("Enter the keyword: "))

matrix = createMatrix(key)

print(matrix)
