# 1
x = [ [5,2,3], [10,8,9] ]
x[1][0] = 15
print(x)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z)

'''
Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ]. (Done)
Change the last_name of the first student from 'Jordan' to 'Bryant' (Done)
In the sports_directory, change 'Messi' to 'Andres' (Done)
Change the value 20 in z to 30 (Done)
(#1 DONE)
'''

# 2
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterate_dictionary(list_of_dictionaries):
    for i in range(len(students)):
        dict = students[i]
        for key, value in dict.items():
            print(key, ' - ', value)

iterate_dictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines; (DONE)
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
# (#2 DONE, not with bonus though)



# 3
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:
# Michael
# John
# Mark
# KB
# And iterateDictionary2('last_name', students) should output:
# Jordan
# Rosales
# Guillen
# Tonel

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterate_dictionary2(key_name, some_list):
    for dictionary in some_list:
        if key_name in dictionary:
            print(dictionary[key_name])
    print()

iterate_dictionary2('first_name', students)
iterate_dictionary2('last_name', students)
# (#3 DONE)


# 4
#Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(some_dict):
    for key, value in some_dict.items():
        print(f'{len(value)} {key.upper()}')
        for item in value:
            print(item)
        print()


print_info(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
# (#4 DONE)