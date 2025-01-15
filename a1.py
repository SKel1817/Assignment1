# Python Code _ Assignment 1
# By: Valerie Nielson
# Description: Simple program that takes a user input and puts it in a list and gives it back

# main program loop
if __name__ == "__main__":
    while True:
        user_input = input("Please enter a word enter n if you want to stop: ")
        # Check if the user wants to stop
        if user_input == 'n':
            break
        # Create a list
        word_list = []
        # Add the user input to the list
        word_list.append(user_input)
        # Print the list
        print(word_list)