def word_count(file_content):
    
    words = file_content.split()
    

    return words

def character_count(file_content):
    char_count = {}
    file_content = file_content.lower()
    
    for character in file_content:
        if character in char_count:
            char_count[character] += 1
        else:
            char_count[character] = 1

    return char_count