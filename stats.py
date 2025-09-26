def get_word_count(words):
	list_word_count = words.split()
	word_count = len(list_word_count)
	return word_count

def count_letters (words):
    letters = {}
    list_words = words.split()
    for i in list_words:
        characters = list(i)
        for i in characters:
            lowercase_i = i.lower()
            if lowercase_i in letters:
                letters[lowercase_i] += 1
            else:
                letters[lowercase_i] = 1
    return letters

def sort_on(items):
    return items["num"]

def sort_dict(unsorted_dict):
    alpha_characters = []
    final_dict = {}
    for character,count in unsorted_dict.items():
        if character.isalpha():
            alpha_characters.append({"char":character,"num":count})
    alpha_characters.sort(reverse=True,key=sort_on)
    for element in alpha_characters:
        final_dict[element["char"]] = element["num"] 
    return final_dict
