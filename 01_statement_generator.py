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

#Main routine goes here
statement_generator("look - starts", "*")

