'''Contestant Number - 8258'''
# REVERSE CYPHER
#put words in a file and put the file name where words is
with open('plainText.txt', 'r') as file:
   for line in file:
      for word in line.split():
         start_word = word
# lines 2-5 search through the file and pick out the word
# These 2 lines reverse each character
reversed_word = ''
i = len(start_word) - 1

# Then the rest of this puts each character back together and prints it out to the console and stores it in reversed file
while i >= 0:
   reversed_word = reversed_word + start_word[i]
   i = i - 1
print('Reversed:\n',reversed_word)

# writes the reversed word to a file
f = open("reversedFile.txt", "w")
f.write(reversed_word)
f.close()

#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
# MAIN CEASER CYPHER - Decryption
def encryption(text, shift_num):
  encrypt_word = ""
  for charac in text:
    # cypher through characters and shift the letter
    if charac.isalpha():
      Alph = ord(charac) + shift_num
      if Alph > ord('z'):
        Alph -= 26
      finLet = chr(Alph)
      encrypt_word += finLet
  return encrypt_word

# put the number you want to shift in the varaible shifted and it will print it out and write it ot the file encrypted word.txt
shifted = 1
print('Encryption:\n',encryption(reversed_word, shifted))
f = open("encryptedText.txt", "w")
f.write(encryption(reversed_word, shifted))
f.close()
# to decrypt just copy and past the encrypted word in to plainText.txt and change the shifted variable to the negative number value respectivly
