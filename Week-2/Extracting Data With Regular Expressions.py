'''
In this assignment you will read through and parse a file
with text and numbers. You will extract all the numbers
in the file and compute the sum of the numbers.
'''
import re

try:
    fileHandle = open('./regex_sum_706599.txt')
except:
    print("Error when opening file")

text = fileHandle.read()
listNumbers = re.findall('[0-9]+', text)

sum = 0
for strNumber in listNumbers:
    sum = sum + int(strNumber)

print(sum)
