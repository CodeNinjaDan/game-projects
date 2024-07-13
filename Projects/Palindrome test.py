#Steps in identifying a palindrome
#Remove all the punctuation 
#Split the sentance into words 
#Create a list([]) to store  palindromic words 
#Convert the words into lowercase 
#Check if the word is a palindrome
def palindrome(sentence):
    for char in ",.?/{}!":
        sentence = sentence.replace(char, "")
    words = sentence.split
    palindromes = []
    for word in words:
        word = word.lower()
        if word == word[::-1]:
            palindromes.append(word)
    return  palindromes
sentence=input('Enter a sentence: ')
print(palindrome(sentence)) 


