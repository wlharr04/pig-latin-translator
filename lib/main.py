from lib import input_analysis
from lib import translator
from lib import text_formatter
from lib import file_handler

def main():
    while True:
        input_string = input("Enter phrase to translate into Pig Latin or q to quit:\n")
        if input_string == "q":
            print("Oodbyegay orfay ownay!")
            break
        text_map = input_analysis.analyze(input_string)
        translated_words = translator.translate(text_map)
        output_string = text_formatter.make_output_string(translated_words)
        print("\nIn Pig Latin:", output_string, sep = "\n", end = "\n\n")
        file_handler.save_file(output_string)