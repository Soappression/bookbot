import sys
from stats import word_count, character_count, sorter

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_content = get_book_text(sys.argv[1])
    
    words = word_count(file_content)
    characters = character_count(file_content)
    sorted_instances = sorter(characters)
    num_words = len(words)
    print(f"Found {num_words} total words")
    
    for item in sorted_instances[0:2]:
        print(f"{item['char']}: {item['num']}")


def get_book_text(filepath):

    with open(filepath) as f:
        file_content = f.read()
    return file_content

main()