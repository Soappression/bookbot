import sys
from stats import word_count, character_count, sorter

def main():
    
    if len(sys.argv) != 2: # says if length of sys.argv is not 2 throw this error
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) # This exits the program with a non-zero status and throws an error
    
    file_content = get_book_text(sys.argv[1]) # sets the filepath parameter to sys.argv[1] which is just index 1 in sys.argv (index 0 is main.py)
    
    words = word_count(file_content)
    characters = character_count(file_content)
    sorted_instances = sorter(characters)
    num_words = len(words)
    print(f"Found {num_words} total words")
    
    for item in sorted_instances[0:2]: # loops over first 2 items in sorted_instances
        print(f"{item['char']}: {item['num']}") # prints key 'char' and value 'num'


def get_book_text(filepath):

    with open(filepath) as f: # with will stop when finished
        file_content = f.read() # sets everything inside to a string
    return file_content

main()