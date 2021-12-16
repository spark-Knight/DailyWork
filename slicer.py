def EmailSlicer():
    ## here we store user Email id with the help of input()
    ##Here we are using Strip function. strip() function will 
    #remove any additional & unwanted spacing on both sides
    #of strings. So that we can make sure that we have only
    #the email in the input and not any unwanted spaces.
    Email = input("Enter Your Email: ").strip()

    #Here we are slicing the user input to obtain the username and domain
    username = Email[:Email.index('@')]
    domain = Email[Email.index('@') + 1:]

    print(f"Your username is {username} & domain is {domain}")


EmailSlicer()








