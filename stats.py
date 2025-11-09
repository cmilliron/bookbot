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