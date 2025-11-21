def get_num_words(text):
#count number of words in the text
    words = text.split()
    counter = 0
    for word in words:
        counter += 1
    return f"Found {counter} total words"

def get_num_eachCharacter(text):
#count each character how many time found in text
    words = text.lower()
    chars = {}
    
    for c in words:
        if c.isalpha() :
            if c not in chars:
                chars[c] = 0
            chars[c] += 1
    return chars

def sort_on(items):
    #healper meathod
    return items["num"]


def sorted_list(text):
    #sort the chars by there by num
    sorted_text = get_num_eachCharacter(text)
    l = []
    for key,values in sorted_text.items() :
        d = {"char" : key , "num" : values}
        l.append(d)
    l.sort(reverse=True , key=sort_on)
    return l
    
        