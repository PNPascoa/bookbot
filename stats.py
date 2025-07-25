def count(string):
    words = string.split()
    count = 0
    for word in words:
        count +=1
    return count

def occurrence(string):
    char_occur = {}
    words_case_lowered = string.lower()
    for word in words_case_lowered:
        if word in char_occur:
            char_occur[word] +=1
        else:
            char_occur[word] = 1
    return char_occur



def sort_on(items):
    return items["num"]

def sorted_dict_to_list_of_dict(dictionary):
    occur_char = []
    for key in dictionary:
        if key.isalpha():
            num = dictionary[key]
            entry = {"char" : f"{key}", "num" : num}
            occur_char.append(entry)
    
    occur_char.sort(reverse = True , key = sort_on)
    return occur_char

