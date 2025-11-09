from stats import count_words, number_of_letters, sort_letter_counts


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def print_structured_count(letter_count_list):
    print("--------- Character Count -------")
    for item in letter_count_list:
        print(f"{item['char']}: {item['count']}")
    print("============= END ===============")


def main():
    file = "books/frankenstein.txt"
    book_content = get_book_text(file)
    # print(book_content)
    num_words = count_words(book_content)
    print(f"Found {num_words} total words")
    letter_counts = number_of_letters(book_content)
    processed_letter_counts = sort_letter_counts(letter_counts)
    print_structured_count(processed_letter_counts)
    

    
main()