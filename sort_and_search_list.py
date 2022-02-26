"""
Assignment: Sort And Search List Assignment
Program: sort_and_search_list.py
Author: Colby Boell
Last date modified: 02/25/2022

The purpose of this program is to take a list and sort it in order and then allow user input to
search for a certain number (float number) in the list to see which index position it is in if it
is in the list at all
--FROM PREVIOUS ASSIGNMENT TO GET THE REVIEW ON THAT PART-- (EXTRA CREDIT)
The purpose of this program is to prompt the user for input that (if a number or a float) will be added
to a list and printed out. If the user inputs a string or letter it will not be added to the list. This is done
by using functions and try statements.
"""


def make_list(num):
    # list variable
    a_list = []
    # for loop to add to list based on number passed through
    for i in range(num):
        # calls input function
        new_entry = get_input()
        # try statement for input validation
        try:
            a_list.append(float(new_entry))
        except ValueError:
            # if not valid invalid message lets user know it won't be added to the list
            print('Invalid entry, entry not added to the list')
    # returns the list
    return a_list


# input function called in make_list function to validate and add to list
def get_input():
    # prompts user input and prints out the input they put in
    user_input = input("Enter a number: ")
    print(f'you entered {user_input}')
    return user_input


# function to sort list
def sort_list(the_list):
    # calls sort list
    the_list.sort()
# we do not need a return statement because we are directly changing the original list
# with sorting


def search_list(the_list):
    search_for = float(input('Input number you would like to search for '))
    return the_list.index(search_for)
# have a return statement because we are returning a number for the index spot (new number) the
# searched number is in as the result not the list itself


# main that calls make_list function
if __name__ == '__main__':
    # variable that calls make_list function, then is passed through sort list function, then prints results
    new_list = make_list(5)
    # prints list before sort
    print(f'list before sort\n{new_list}')
    sort_list(new_list)
    # prints after sort
    print(f'After sort\n{new_list}')

    # variable to call search list function prints either index position of number or not found
    try:
        print(f'Number was found in index position (after sort) {search_list(new_list)} of the list')
    except ValueError:
        print('The number you are looking for was not found in the list (default for strings)')

"""
TESTS:
1.)
Enter a number: 12
you entered 12
Enter a number: 3.3
you entered 3.3
Enter a number: 6.6
you entered 6.6
Enter a number: 4.5
you entered 4.5
Enter a number: 12
you entered 12
list before sort
[12.0, 3.3, 6.6, 4.5, 12.0]
After sort
[3.3, 4.5, 6.6, 12.0, 12.0]
Input number you would like to search for 6.6
Number was found in index position (after sort) 2 of the list
2.)
Enter a number: t
you entered t
Invalid entry, entry not added to the list
Enter a number: 5.5
you entered 5.5
Enter a number: 4.5
you entered 4.5
Enter a number: 33
you entered 33
Enter a number: 2.22
you entered 2.22
list before sort
[5.5, 4.5, 33.0, 2.22]
After sort
[2.22, 4.5, 5.5, 33.0]
Input number you would like to search for 7.77
The number you are looking for was not found in the list (default for strings)
3.)
Enter a number: 12.2
you entered 12.2
Enter a number: 4.78
you entered 4.78
Enter a number: 13
you entered 13
Enter a number: 3.56
you entered 3.56
Enter a number: 11.67
you entered 11.67
list before sort
[12.2, 4.78, 13.0, 3.56, 11.67]
After sort
[3.56, 4.78, 11.67, 12.2, 13.0]
Input number you would like to search for five
The number you are looking for was not found in the list (default for strings)

"""
