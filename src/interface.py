"""This file will hold the driver code for the program."""

# Authors: Christian Lussier, Ben Watto, Mikey Spurr
# "All work is our own unless otherwise cited.""

from file_reader import *
from organizer import *
import time
#from organizer import letter_group_organizer

def main():
    """Driver program of the project."""

    # Print welcome message:
    print("*************************************************************")
    print("* Thanks for using our Registration Letter Group Organizer! *")
    print("*************************************************************")
    print()

    file_name = input("Sample input file example: ../data/input/sample_students.txt \n*** Please enter a file name to use:   ")
    print()  # blank line for spacing

    # get user's preferred genres:
    user_input_groups = input("Enter last semester's letter group order. Must contain letters A-H only!\n **Example Use: A, B, C, F, E, D, H, G\n")
    current_groups = [x.strip() for x in user_input_groups.split(', ')] # get the user's chosen preferences
    print()  # blank line for spacing
    #currentgroups = ["A", "B", "C", "F", "E", "D", "H", "G"]

    print()
    print("Previous Letter Group Order:", current_groups)
    print()
    try:
        student_list = registrationList_processor(file_name)

        # Time the algorithm:
        start_time = time.time()  # start timer
        sorted_students = letter_group_organizer(current_groups, student_list)
        stop_time = time.time()  # stop timer
        time_elapsed = stop_time - start_time  # calculate function run time
        print()
        print("** It took the algorithm this long to run:", time_elapsed)
        print()

        # file name to output to:
        chosen_file_name = input("Sample output file example: ../data/output/output.txt \n*** Please enter a file name to output sorted student info to:   ")
        print()

        output_file = open(chosen_file_name,'w') # opens previously created file, creates new file if necessary
        print()  # print blank line for spacing
        print()  # print blank line for spacing
        print("{:<30}{:<25}{:<20}{:<15}\n".format("Student Name", "Class Year", "Letter Group", "GPA")) # print output header
        output_file.write("{:<30}{:<25}{:<20}{:<15}".format("Student Name", "Class Year", "Letter Group", "GPA"))
        for ele1,ele2,ele3,ele4 in sorted_students:
            print("{:<30}{:<25}{:<20}{:<15}".format(ele1,ele2,ele3,ele4))
            output_file.write("\n{:<30}{:<25}{:<20}{:<15}".format(ele1,ele2,ele3,ele4))
        output_file.close()
    except:
        # catch any errors that may occur, likely with input file or output file
        print("\n Exiting....")

main()  # run the interface
