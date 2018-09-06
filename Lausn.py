#Exercise no. 44 in chapter 4 in the textbook.
#You should output the result in a table, formatted in the following manner:
#The first line contains the word "Upper case", right justified, 15 spaces wide, followed by the count of upper case characters, right justified, 5 spaces wide.
#The second line contains the word "Lower case", right justified, 15 spaces wide, followed by the count of lower case characters, right justified, 5 spaces wide.
#The third line contains the word "Digits", right justified, 15 spaces wide, followed by the count of digits, right justified, 5 spaces wide.
#The fourth line contains the word "Punctuation", right justified, 15 spaces wide, followed by the count of punctuation characters, right justified, 5 spaces wide.
#The input prompt should be: "Enter a sentence. "
#Example input/output:
import string

sentence = input("Enter a sentence: ")

U = 0 
L = 0
D = 0 
P = 0

lengd = len(sentence)

for i in range(lengd):
    if sentence[i].isupper():
        U += 1
    if sentence[i].islower():
        L += 1
    if sentence[i].isnumeric():
        D += 1
    if sentence[i].isspace():
    #if i in sentence.punctuation:
        P += 1

R = lengd - U - L - D - P    
upper = "Upper case"
lower = "Lower case"
digits = "Digits"
punct = "Punctuations"

import math
print("{:>15}{:>5}".format(upper,U))
print("{:>15}{:>5}".format(lower,L))
print("{:>15}{:>5}".format(digits,D))
print("{:>15}{:>5}".format(punct,R))

