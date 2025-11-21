from stats import get_num_words
from stats import get_num_eachCharacter
from stats import sorted_list


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
    text = get_book_text("books/frankenstein.txt")
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt")
    print("----------- Word Count ----------")
    print(get_num_words(text))
    print("--------- Character Count -------")
    print_report(text)
    print("============= END ===============")


main()