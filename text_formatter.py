import textwrap

def make_output_string(translated_words):
    input_string = ""
    output_string = ''

    for word in translated_words:
        input_string += word + " "

    lines = textwrap.wrap(input_string)

    for line in lines:
        output_string += f'{line}\n'

    output_string = output_string.strip()

    return output_string
