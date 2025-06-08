def word_count(file_content):
    
    words = file_content.split()
    

    return words

def character_count(file_content):
    char_count = {}
    file_content = file_content.lower()
    
    for character in file_content:
        if character.isalpha():
            if character in char_count:
                char_count[character] += 1
            else:
                char_count[character] = 1

    return char_count

def sort_on(dict):
    return dict["num"]

def sorter(char_count):
    instances = []
    for char in char_count:
        num = char_count[char]
        instances.append({"char": char, "num": num})
    


    instances.sort(reverse=True, key=sort_on)
    return instances