def get_num_words(str):
    return len(str.split())


def get_num_char(str):
    char_count = {}

    for char in str:
        char_lower = char.lower()
        if char_lower in char_count:
            char_count[char_lower] += 1
        else:
            char_count[char_lower] = 1
    return char_count


def sort_on(items):
    return items["num"]


def get_sorted_dict(dict):
    result_list = []
    for key in dict:
        new_dictionary = {}
        new_dictionary["char"] = key
        new_dictionary["num"] = dict[key]
        result_list.append(new_dictionary)

    result_list.sort(reverse=True, key=sort_on)
    return result_list
