from stats import word_count, character_count

def get_book_text(filepath):

    with open(filepath) as f:
        file_content = f.read()

    return file_content

def main():
    
    filepath = "books/frankenstein.txt"
    file_content = get_book_text(filepath)
    
    words = word_count(file_content)
    characters = character_count(file_content)
    num_words = len(words)
    print(f"{num_words} words found in the document")
    print(characters)


main()