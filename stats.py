def get_book_word_count(words):

    split_list = []

    split_list = words.split()
    if(len(split_list) <= 0):
        raise Exception("Empty String Exception")
    return split_list

def get_book_letter_count(split_words):

    letters = {}

    for word in split_words:
        for letter in word:
            low_letter = letter.lower()
            if(low_letter in letters):
                letters[low_letter] += 1
            else:
                letters[low_letter] = 1

    if(len(letters) <= 0):
        raise Exception("Failed to load letters dictionary.")

    return letters

def sort_list_counts(letters):

    sorted_letters = []  

    for letter_set in letters:
        if(letter_set.isalpha()):
            sorted_letters.append({"char" : letter_set, "count" : letters[letter_set]})

    if(len(sorted_letters) <= 0):
        raise Exception("Empty List of Dictionaries")

    def sort_on(sorted_letters):
        return sorted_letters["count"]

    sorted_letters.sort(reverse=True, key=sort_on)

    return sorted_letters
