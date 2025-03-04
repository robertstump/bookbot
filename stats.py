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
