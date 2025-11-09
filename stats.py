def sort_on(item):
    return item['count']

def count_words(book_content):
    word_list = book_content.split()
    return len(word_list)


def number_of_letters(book_content):
    count_dict = {}
    for character in book_content:
        try: 
            count_dict[character.lower()] += 1
        except KeyError:
            count_dict[character.lower()] = 1
    return count_dict


def sort_letter_counts(letter_counts):
    letter_list = []
    for letter in letter_counts:
        # print(letter)
        if letter.isalpha():
            letter_list.append({"char": letter, "count": letter_counts[letter]})
    # print(letter_list)
    letter_list.sort(reverse=True, key=sort_on)
    return letter_list