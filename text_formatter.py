def make_output_string(translated_words):
    output_string = ""

    for word in translated_words:
        output_string += word + " "

    output_string = output_string.strip()

    return output_string