# 2. Write a word counter: as input program accepts a txt file, then reads the content from the file
# and as output prints the number of words in that txt file.
# You need to create this txt file first and fill it with some sentences.
# Example:
# input: Alice in wonderland sleeps
# output: 4

f = open('C:\\Users\\baham\\Python-tests\\W2_2_input_file.txt', 'r')
print(len(f.read().split()))