# checks user choice is ' integer', 'text' or ' image' 
def user_choice(): 

    valid = Flase
    while not valid:

        response = "File type (intger / text / image): ". lower()

        if response == "text" or response == "t":
            return response

        else:
          print("Please choose a valid file type!")
          print()


#Main routine goes here 
data_type = user_choice()                