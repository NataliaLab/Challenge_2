# 4. Write a function that counts the number of vowels in a given word.
# Example 1:
# input: banana
# output: 3
# Example 2:
# input: vowels
# output: 2


x = input('? ')
def my_function():
    word = x.lower()
    letters_list = []
    letters_list.extend(word)  # list of letters in the word
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    new_list = []
    for number in range(len(letters_list)): # 6 iterations for banana
        if letters_list[number] in vowels_list:
            new_list.append(letters_list[number])
        else:
            continue
    print(len(new_list))

my_function()