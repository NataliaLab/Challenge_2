# 6. Modify the function created in task 5, but now as input use a csv file with words in it (ie. inputs.csv)
# Expected result: the function should create a txt file with dictionary which contains the input word as key, dictionary with vowels, and the number of the vowels as value.
# It should look like this: {'banana' : {'a': 3}}
# Example:
# input: file inputs.csv and the content of it:
# banana,vowels
# output: file results.txt and the content of it:
# {'banana' : {'a': 3}}, {'vowels' : {'o': 1, 'e': 1}}

x = open('C:\\Users\\baham\\Python-tests\\W2_6_input_file.txt', 'r')

def my_function():
    w = x.read().split(',')
    big_dict = {}
    for number in range(len(w)):  # iterating through the input file - 2 items
        word = w[number]
        word = word.lower()
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
            big_dict[word] = new_dict
#    print(big_dict)
    with open('C:\\Users\\baham\\Python-tests\\W2_6_output_file.txt', 'w') as f:
        f.write(str(big_dict))

my_function()

# x = input('? ')
# def my_function():
#     word = x.lower()
#     letters_list = []
#     letters_list.extend(word)  # list of letters in the word
#     vowels_list = ['a', 'e', 'i', 'o', 'u']
#     new_dict = {}
#     for number in range(len(letters_list)): # 6 iterations for banana
#         if letters_list[number] in vowels_list:
#             if letters_list[number] in new_dict:
#                 new_dict[letters_list[number]] = new_dict.get(letters_list[number])+1
#             else:
#                 new_dict[letters_list[number]] = 1
#         else:
#             continue
#     print(new_dict.items())
#
# my_function()