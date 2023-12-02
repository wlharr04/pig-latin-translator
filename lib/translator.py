
def translate(text_map):
    translated_words = []

    for word_mapping in text_map:
        original_word = word_mapping["lowercase"]
        original_word_length = word_mapping["length_no_punct"]
        capitalized = word_mapping["uppercase"]
        first_vowel_index = word_mapping["first_vowel_index"]
        character_map = word_mapping["character_map"]
        translated_word_length = 0
        # Move the characters around:
        if original_word_length > 1 and first_vowel_index != 0:
            translated_word = original_word[first_vowel_index:] + original_word[:first_vowel_index]
        else:
            translated_word = original_word
        #Add "-ay" to the end:
        if original_word != "A" and original_word != "a":
            if translated_word[-1] != "a":
                translated_word += "a"
            translated_word += "y"

        translated_word_length = len(translated_word)
        # Add capitalization back in:
        if capitalized:
            translated_word = translated_word.capitalize()
        #Add punctuation back in:
        for char_info in character_map:
            char_index = char_info["index"]
            char = char_info["character"]
            punctuation = char_info["punctuation"]
            if punctuation:
                if original_word_length != char_index:
                    char_index = char_index - first_vowel_index
                    translated_word = translated_word[:char_index] + char + translated_word[char_index:]
                elif original_word_length == char_index and translated_word_length > 1:
                    translated_word += char  
                else:
                    char_index = char_index
                    translated_word = translated_word[:char_index] + char + translated_word[char_index:]
                
        translated_words.append(translated_word)
    return translated_words