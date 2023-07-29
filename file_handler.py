def save_file(contents):
    response = input("Save text to file? (Y/n) ")

    if response.lower() == "y" or response.lower() == "yes" or response == "":
        filename = input("Save as: ")
        try:
            if filename[-4:] != ".txt":
                filename += ".txt"
        except:
            filename += ".txt"

        i = 1
        while True:
            try: 
                with open(filename, "w") as file:
                    file.write(contents)
                    print("File saved successfully.")
                    break
            except:
                print("\033[1mERROR:\033[0m Unable to save file.")
            
            if i == 3:
                print("\033[1mABORTING:\033[0m No more attempts will be made.")
                break

            i += 1
            
