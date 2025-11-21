from stats import get_num_words
from stats import sorted_list
import sys

def get_book_text(path_to_file):
    #take a txt and open it
    with open(path_to_file) as f:
        return f.read()
    
def print_report(chars):
    #print the "values" in dict of list
    sor = sorted_list(chars)
    for c in sor :
        print(f'{c["char"]}: {c["num"]}')

        
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    book_path = sys.argv[1]
    text = get_book_text(book_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(get_num_words(text))
    print("--------- Character Count -------")
    print_report(text)
    print("============= END ===============")


main()