import my_mod #this module is where we'll perform all our data handling
    
# PART ONE - main menu and user interaction 

# main
print("\nHellloooo, Metalheads!!!")
print("Let's learn a little bit about your favorite Metal artists. \nPick an option below. (Enter Quit to leave)\n")

# We'll want our program to be able to run until the user tell us they want to quit,
# so you'll need to alter this structure as necessary
# Our main loop will present the user with a menu of options, display a table to them based on
# their choices, and present the main menu to them again to let them keep exploring or allow them to quit
print()
print("A: Bands per country")
print("B: Bands formed in year")
print("C: Bands with keyword")
print("D: Longest rocking bands\n")

# get user's choice 
user_choice = input()

# make sure we give the user the opportunity to quit the program

# If the user selects A, call the appropriate functions from your data module to print out a table,
# with countries in the first column and the number of bands formed in that country in the second column
if user_choice == "A":
    print() # you can remove this as necessary
    # use the get_bands_per_country() function to get a nested list of countries and the number of bands formed in that country
    # print the results in a formatted table with print_table()
    # allow the user to select from the main menu options when finished

# If the user selects B, ask them to enter a year
elif user_choice == "B":
    print("Want to see how Metal a given year was? \nEnter a year and check out which bands formed that year: ")
    # Use get_bands_formed_in_year() to get a nested list of all bands formed that year and their country of origin
    # Print the results with your print_table() function
    # allow the user to select from the main menu options when finished

# If the user enters C, we'll let them enter a keyword and print out a table showing them the bands
# who play that musical style
elif user_choice == "C":
    print("Looking for a specific flavor of Metal? Enter a keyword: ")
    # Ask the user to enter a keyword. We'll find all the bands whose styles contain this keyword.
    # Normalize the input to ensure the keyword is not case-sensitive
    # Use get_bands_with_style() to get a nested list of all bands whose styles contain this keyword.
    # Print the results with your print_table() function
    # allow the user to select from the main menu options when finished
    
# If the user enters D, ask them how many bands they want to see. Then we'll show them a table
# of bands and the number of years they've been active
elif user_choice == "D":
    print("How many bands do you want to see? ")
    # Get a number from the user. This will determine the number of bands we display
    # Use get_longest_lived_bands() and print_table to show them a table of bands
    # and the number of years they've been active
    # allow the user to select from the main menu options when finished

# What do we do if the user enters an invalid option?
# We'll want to give them another chance to choose a valid option
    
    
