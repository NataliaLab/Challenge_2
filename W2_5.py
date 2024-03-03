# 5. Rewrite the function from task 4 and now it should return a dictionary with the vowel as key and the number of the vowel in a word as value.
# Example 1:
# input: banana
# output: {'a': 3}
# Example 2:
# input: vowels
# output: {'o': 1, 'e': 1}

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
    new_dict = {}
    for number in range(len(letters_list)): # 6 iterations for banana
        if letters_list[number] in vowels_list:
            if letters_list[number] in new_dict:
                new_dict[letters_list[number]] = new_dict.get(letters_list[number])+1
            else:
                new_dict[letters_list[number]] = 1
        else:
            continue
    print(new_dict)

my_function()

