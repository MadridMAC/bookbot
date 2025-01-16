def main():
    book_path = "books/frankenstein.txt"
    word_character_report(book_path)

# Reads text from path and prints it to console
def open_book(path):
    with open(path) as f: 
        file_contents = f.read()
        return file_contents

# Count number of words from text provided
def count_words(text):
    split_text = text.split()
    return len(split_text)

# Counts the number of each character that appears in text provided
# Returns a list of dictionaries ("name", "num") that only contains characters from the alphabet
def chara_count(book):
    # All characters are set to lowercase first to prevent duplicate characters   
    flattened_text = book.lower()
    chara_dict = {}

    # For each character, create a unique entry in the dict if it does not exist
    # Else, add 1 to its value, which counts how many times it appears in the text
    for char in flattened_text:
        if char not in chara_dict:
            chara_dict[char] = 1
        else:
            chara_dict[char] += 1
    
    # Converts dict into list of dicts (dict_list)
    dict_list = []
    for item in chara_dict:
        # Check if character is part of the alphabet; if so, add to dict_list
        if item.isalpha():
            dict_list.append({"name": item, "num": chara_dict[item]})
    
    # Boot.dev provided method for sorting the dict_list
    # Source Link: https://www.boot.dev/lessons/d6536f09-dc1d-4922-a2a5-a73c536ee09d
    # This returns the value of the "num" key from a provided dict
    def sort_on(dict):
        return dict["num"]

    # Reverse and sort dict_list using sort_on, then return
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def word_character_report(path):
    # Raw text from path
    path_text = open_book(path) 
    # Total number of words
    word_count = count_words(path_text)
    # List of dicts containing alphabet characters from text and their count
    chara_dict = chara_count(path_text)

    print(f"--- Start of report for {path}---")
    print(f"There are a total of {word_count} words in the provided document")
    for i in range(0,len(chara_dict)):
        print(f"The '{chara_dict[i]["name"]}' character was found {chara_dict[i]["num"]} times")
    print(f"--- End of report---")

main()