def alphabetical_sort(words):
    sorted_words = []
    while words:
        smallest = words[0]
        for word in words:
            if word < smallest:
                smallest = word
        sorted_words.append(smallest)
        words.remove(smallest)
    return sorted_words

words_list = ["ufone", "zong", "jazz"]
print(alphabetical_sort(words_list))  
