
# checks input is a number more than a given value
def num_check(question, low):   
    valid = False
    while not valid:

        error = "Please enter an integer that is more than (or equal to) {}" .format(low)
     
        try:

            # ask user to enter a number
            response = int(input(question))

            # checks that number is more than zero
            if response >= low:
                return response

            # outputs error if inputs is invalid
            else:
                print(error)
                print()

        except ValueError:    
            print(error)


# find # bit for 24 bit colour 
def image_bits():

    # get width and height...
    image_width = num_check("Image width? ", 1)
    image_height = num_check("Image height? ", 1)

    # calculate # of pixels
    num_pixels = image_width * image_height

    # calculate # bits (24 x num pixels)
    num_bits = num_pixels

    # output answer with working
    print()
    print("# of pixels = {} x {} = {}".format(image_height
                                              image_width, num_pixel))
    print("# bits = {} x 24 = {}".format(num_pixels, num_bits))
    print()

    return ""

# main routine goes here 
image_bits()
