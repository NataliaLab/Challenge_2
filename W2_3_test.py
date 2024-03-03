# To test:
# 3. Write a function to check duplicate letters in words.It must accept strings ie. a sentence.
# The function should return True if any of the words has duplicate letters else return False.
# Example 1:
# input: A cucumber is green
# output: True
# Example 2:
# input: This is it
# output: False
# Example 3:
# input: banana
# output: True



def my_function(x):
    words = x.split()   # list of words
    for number in range(len(words)): # 3 iteration, first 'cucumber'
        letters_list = []
        word = words[number]    # word to evaluate
        letters_list.extend(word)  # split the word to letters
        letters_set = set()
        letters_set.update(letters_list)
        res = 0
        if len(letters_list) > len(letters_set):
            res += 1
            break
        else:
            continue
    if res == 1:
        return 'True'
    else:
        return 'False'

def test_answer1():
    assert my_function('A cucumber is green') == 'True'

def test_answer2():
    assert my_function('This is it') == 'False'

def test_answer3():
    assert my_function('banana') == 'True'

