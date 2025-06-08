def word_count(file_content):
    
    words = file_content.split() # splits the text into a list of words () empty () means it splits text based on whitespace
    

    return words

def character_count(file_content):
    char_count = {}
    file_content = file_content.lower() # makes all file_content lowercase
    
    for character in file_content:
        if character.isalpha(): # if character is letter...
            if character in char_count: # if character is in dictionary...
                char_count[character] += 1 # add 1
            else: # otherwise
                char_count[character] = 1 # set character as key with value 1 / loop restarts after this, character has now been added to dictionary

    return char_count

def sort_on(dict): # creates key sort_on
    return dict["num"] # returns the value "num" from a dictionary

def sorter(char_count):
    instances = [] # empty list
    for char in char_count:
        num = char_count[char] # iterating over char_cound {}
        instances.append({"char": char, "num": num}) # adding dictionary with key "char" and vlaue "num" to instances list
    


    instances.sort(reverse=True, key=sort_on) # sort list in decending order with the key sort_on
    return instances