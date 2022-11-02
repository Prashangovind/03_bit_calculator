# Functions goes here 

# Put series of symbols at start and end of (for emphasis)
def statement_generator(text, decoration):

    # Make string with five characters 
    ends = decoration * 5

    # add decoration to start and end of statement 
    statement = "{}  {}  {}". format (ends, text, ends)

    print()
    print(statement)
    print()

    return ""


def user_choice(): 

    # Lists of vaild reponses
    text_ok = ["text", "t", "txt"]
    integer_ok = ["integer", "int", "#", "number"]
    image_ok = ["image", "img", "pix", "picture", "pic", "p"]

    vaild = False
    while not vaild:

        # ask user for choice and change response to lowercase
        response = input("File type (intger / text / image): "). lower()

        # Checks for vaild response and returns text, integer or image

        if response in text_ok:
            return "text"

        elif response in integer_ok:
            return "integer"

        elif response in image_ok:
            return "image"

        elif response == "i":  
            want_integer = input(" Press <enter> for an integer or any key for an image: n ") 
            if want_integer == "": 
                return "integer"
            else:
                return "image"

        else:
            #if response is not valid, output an error 
            print("Please choose a valid file type!")
            print()


#Main routain goes here

# Heading
statement_generator("Bits calaculator goes for integers, text & images", "-")

# Dissplay instructions if user has not  used the program before 

# loop allow mulitpule calculations per session 
keep_going = ""
while keep_going == "":

    # Ask the user for file type  
    data_type = user_choice()
    print("you chose", data_type)

#for integers, ask for integer 
# (must be an integer more than / epual to 0)

# for image, ask for width and height 
