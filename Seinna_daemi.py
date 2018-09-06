word = input("Enter a word: ")

lengd = len(word)
strengur = []

vowel = ["a","e","i","o","u"]

for i in range(lengd):
    if word[i] in vowel:
        print(word[i:]+word[:i]+"ay")
        break
    
        
