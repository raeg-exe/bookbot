def count_words(result):
    word_count = 0
    word_list = result.split()

    for i in word_list:
        word_count += 1
    return word_count

def char_count(result):
    characters = {}
    string = result.lower()

    for char in string:
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    return characters

def sort_on(d):
    return d["num"]

def sort_dict(char_count):
    char_list = [{"char": char, "num": count} for char, count in char_count.items()]
    char_list.sort(reverse=True, key=sort_on)
    return char_list
