#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./input/Names/invited_names.txt") as name:
    names = name.readlines()
    name_list = []
    for name in names:
        n=name.strip("\n")
        name_list.append(n)
    with open("./input/letters/starting_letter.docx") as letter:
        letter_content = letter.read()
        for i in range(len(name_list)):
            with open(f"./output/{name_list[i]}_letter.docx",mode="w") as write_letter:
                new_letter = letter_content.replace("[name]",name_list[i])
                write_letter.write(new_letter)

