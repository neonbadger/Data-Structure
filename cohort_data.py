def unique_houses(filename):
    """TODO: Create a set of student houses.

    Iterates over the cohort_data.txt file to look for all of the included house names
    and creates a set called 'houses' that holds those names.

        ex. houses = set([ "Hufflepuff",
                    "Slytherin",
                    "Ravenclaw",
                    "Gryffindor",
                    "Dumbledore's Army",
                    "Order of the Phoenix"
            ])

    """

    data_file = open(filename)

    all_houses = []

    for line in data_file:
        line = line.rstrip()
        personal_info = line.split('|')
        if personal_info[2]:
            all_houses.append(personal_info[2])

    houses = set(all_houses)

    data_file.close()

    # Code goes here

    return houses


def sort_by_cohort(filename):
    """TODO: Sort students by cohort.

    Iterates over the data to create a list for each cohort, ordering students
    alphabetically by first name, and have a list for tas separately. Returns list of lists.

        ex. winter_15 = ["alice tsao", "amanda gilmore", "anne vetto", "..." ]
        ex. all_students = [winter_15, spring_15, summer_15, tas]

    """

    all_students = []
    winter_15 = []
    spring_15 = []
    summer_15 = []
    tas = []

    # Code goes here

    data_file = open(filename)

    for line in data_file:
        line = line.rstrip()
        personal_info = line.split('|')
        name = " ".join(personal_info[:2])

        if personal_info[4] == "Winter 2015":
            winter_15.append(name)
        elif personal_info[4] == "Spring 2015":
            spring_15.append(name)
        elif personal_info[4] == "Summer 2015":
            summer_15.append(name)
        elif personal_info[4] == "TA":
            tas.append(name)

    winter_15.sort()
    spring_15.sort()
    summer_15.sort()
    tas.sort()

    all_students = [winter_15, spring_15, summer_15, tas]

    print "winter 15 cohort", winter_15
    print "sprint 15 cohort", spring_15
    print "summer 15 cohort", summer_15
    print "TAs", tas

    data_file.close()

    return all_students


def students_by_house(filename):
    """TODO: Sort students by house.

    Iterate over the data to create a list for each house, and sort students
    into their appropriate houses by last name. Sort TAs into a list called "tas"
    and instructors in to a list called "instructors".
    Return all lists in one list of lists.
        ex. hufflepuff = ["Gaikwad", "Le", "..." ]
        ex. tas = ["Bryant", "Lefevre", "..."]
        ex. all_students = [ hufflepuff,
                        gryffindor,
                        ravenclaw,
                        slytherin,
                        dumbledores_army,
                        order_of_the_phoenix,
                        tas,
                        instructors
            ]
    """

    all_students = []
    gryffindor = []
    hufflepuff = []
    slytherin = []
    dumbledores_army = []
    order_of_the_phoenix = []
    ravenclaw = []
    tas = []
    instructors = []

    
    # Code goes here
    data_file = open(filename)
    for line in data_file:
        line = line.rstrip()
        personal_info = line.split('|')
        if personal_info[2] == 'Gryffindor':
            gryffindor.append(personal_info[1])

        elif personal_info[2] == 'Hufflepuff':
            hufflepuff.append(personal_info[1])

        elif personal_info[2] == 'Slytherin':
            slytherin.append(personal_info[1])

        elif personal_info[2] == 'Ravenclaw':
            ravenclaw.append(personal_info[1])

        elif personal_info[2] == "Dumbledore's Army":
            dumbledores_army.append(personal_info[1])

        elif personal_info[2] == 'Order of the Phoenix':
            order_of_the_phoenix.append(personal_info[1])

        elif personal_info[4] == 'TA':
            tas.append(personal_info[1])

        elif personal_info[4] == 'I':
            instructors.append(personal_info[1])

    gryffindor.sort()
    slytherin.sort()
    order_of_the_phoenix.sort()
    hufflepuff.sort()
    ravenclaw.sort()
    dumbledores_army.sort()
    tas.sort()
    instructors.sort()

    all_students = [hufflepuff,
                    gryffindor,
                    ravenclaw,
                    slytherin,
                    dumbledores_army,
                    order_of_the_phoenix,
                    tas,
                    instructors]

    print "Hufflepuff", hufflepuff
    print "Gryffindor", gryffindor
    print "Ravenclaw", ravenclaw
    print "Slytherin", slytherin
    print "Dumbledore's Army", dumbledores_army
    print "Order of the Phoenix", order_of_the_phoenix
    print "TAs", tas
    print "Instructors", instructors


    data_file.close()

    return all_students


def all_students_tuple_list(filename):
    """TODO: Create a list of tuples of student data.

    Iterates over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)
        ex. all_people = [
                ("Alice Tsao", "Slytherin", "Kristen", "Winter 2015"),
                ("Amanda Gilmore", "Hufflepuff", "Meggie", "Winter 2015"),
                # ...
            ]
    """

    student_list = []

    data_file = open(filename)

    for line in data_file:
        line = line.rstrip()
        personal_info = line.split("|")

        if personal_info[2]:
            name = " ".join(personal_info[:2])
            house = personal_info[2]
            advisor = personal_info[3]
            cohort = personal_info[4]

            individual_tuple = (name, house, advisor, cohort)
            student_list.append(individual_tuple)

    # Code goes here

    student_list.sort()

    return student_list


def find_cohort_by_student_name(student_list):
    """TODO: Given full name, return student's cohort.

    Use the above list of tuples generated by the preceding function to make a small
    function that, given a first and last name, returns that student's cohort, or returns
    'Student not found.' when appropriate. """

    # Code goes here

    return "Student not found."


##########################################################################################
# Further Study Questions


def find_name_duplicates(filename):
    """TODO: Using set operations, make a set of student first names that have duplicates.

    Iterates over the data to find any first names that exist across multiple cohorts.
    Uses set operations (set math) to create a set of these names.
    NOTE: Do not include staff -- or do, if you want a greater challenge.

       ex. duplicate_names = set(["Sarah"])

    """

    duplicate_names = set()

    # Code goes here

    return duplicate_names


def find_house_members_by_student_name(student_list):
    """TODO: Create a function that prompts the user for a name via the command line
    and returns everyone in their house that's in their cohort.

    Use the list of tuples generated by all_students_tuple_list to make a small function that,
    when given a student's first and last name, returns students that are in both that
    student's cohort and that student's house."""

    # Code goes here

    return


#########################################################################################

# Here is some useful code to run these functions!

# print unique_houses("cohort_data.txt")
# print sort_by_cohort("cohort_data.txt")
# print students_by_house("cohort_data.txt")
# all_students_data = all_students_tuple_list("cohort_data.txt")
# print all_students_data
# find_cohort_by_student_name(all_students_data)
# print find_name_duplicates("cohort_data.txt")
# find_house_members_by_student_name(all_students_data)
