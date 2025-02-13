#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
INPUT_PATH = "Input/Letters"
OUTPUT_PATH = "Output/ReadyToSend/"

def read_template_letter(invited_name=""):
    text = ""
    with open(f"{INPUT_PATH}/starting_letter.txt") as file:
        lines = file.readlines()
        for line in lines:
            text += line.replace("[name]", invited_name.strip())

    return text

def generate_invited_name(invited_name="", text=""):
    with open(f"{OUTPUT_PATH}/{invited_name}.txt", "w") as file:
        file.writelines(text)

def main():
    with open(f"Input/Names/invited_names.txt") as file:
        names = file.readlines()
        for name in names:
            print(f"----GENERATED LETTER FOR {name}")
            letter_text = read_template_letter(invited_name=name)
            generate_invited_name(invited_name=name, text=letter_text)


main()