import string
remove_punct = str.maketrans("","",string.punctuation)

def analyze(input):
    input = input.strip()
    vowels = ["a","e","i","o","u"]
    text_map = []

    for word in input.split():
        word_map = {
            "lowercase": word.translate(remove_punct).lower(), 
            "length_no_punct": len(word.translate(remove_punct)),
            "uppercase": 0,
            "first_vowel_index": 0,
            "character_map": []
            }
        character_map = []

        ## This retains the capitalization data
        if word[0].isupper():
            word_map["uppercase"] = 1
        
        for i, char in enumerate(word):
            if char in vowels:
                word_map["first_vowel_index"] = i
                break

        for i, char in enumerate(word):
            char_info = {
                "index": i,
                "character": char,
                "punctuation": 0
            }

            if char in string.punctuation:
                char_info["punctuation"] = 1

            character_map.append(char_info)
        
        ## Then we add the mapping of all the characters to the entry for the word, then add the word to the text.
        word_map["character_map"] = character_map
        text_map.append(word_map)
    return text_map