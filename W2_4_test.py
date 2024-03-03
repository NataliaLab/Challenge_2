# To test:
# 4. Write a function that counts the number of vowels in a given word.
# Example 1:
# input: banana
# output: 3
# Example 2:
# input: vowels
# output: 2



def my_function(x):
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
    return len(new_list)

def test_answer1():
    assert my_function('banana') == 3

def test_answer2():
    assert my_function('vowels') == 2