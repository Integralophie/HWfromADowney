def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

word = input('which word do you want to test? \n')

def is_palindrome(word):
    if len(word) == 1:
        print('yes')
        return

    elif first(word) != last(word):
        print('no its not')
        return

    else:
        is_palindrome(middle(word))

is_palindrome(word)


#is_palindrome('asdfda')
