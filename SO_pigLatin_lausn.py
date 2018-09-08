word = input("Enter a word: ")

decimal = 0
lengd = len(word)
#strengur = []
n = ""
m = ""
old = ""

vowel = ["a","e","i","o","u"]

while ord(word[0]) != 46:        
    for i in range(lengd):
        if word [0] in vowel:
            n = (word[i:]+"yay")
            break
        else:
            for x in range(lengd):  # þetta getur tekið öll orð
                if word[x] in vowel:
                    m = (word[x:]+word[:x]+"ay")
                    while decimal <= 0:
                        n = m
                        decimal = decimal + 1
            if n == old:
                n = (word + "ay")
    
    print(n)  
    decimal = 0
    old_word = word
    word = input("Enter a word: ")
    old = n
    if old_word == word:
        old = 0
    lengd = len(word)    


