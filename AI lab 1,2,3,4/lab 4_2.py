def remove_punctuations(string):

    punctuation_chars = "!@#$%^&*()_-+=<>?.,;:[]{}|\n\t"
    result = ""
    for char in string:
        if char not in punctuation_chars:
            result += char
    return result

user_input = "DONE."
result = remove_punctuations(user_input)
print(result)