from stats import count_words, number_of_letters


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    file = "books/frankenstein.txt"
    book_content = get_book_text(file)
    # print(book_content)
    num_words = count_words(book_content)
    print(f"Found {num_words} total words")
    letter_counts = number_of_letters(book_content)
    print(letter_counts)
    

    
main()