# Takes a string and returns word count
def get_num_words(book_string):
    word_list = book_string.split()
    return len(word_list)

# Takes a string and returns a dict with all alpha chars and their count.
# Converts the string to lowercase.
def get_num_chars(book_string):
    result = {}
    book_string = book_string.lower()

    for char in book_string:
        if char not in result and char.isalpha():
            result[char] = 1
        elif char.isalpha():
            result[char] += 1
    return result

# A function to help sort | list.sort(reverse=True, key=sort_on)
def sort_on(items):
    return items["num"]

# A function that takes a dict of chars and their count 
# And returns a list of dictionaries
# {"b" : 4868} ---> [ {"char" : "b", "num": 4868} ]
def get_sorted_chars(char_dict):
    # Create a list of dictionaries
    list_dict = []
    for pair in char_dict:
        num = char_dict[pair]
        list_dict.append({"char" : pair, "num" : num})
    # Sort that list and return
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict