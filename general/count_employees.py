"""
simple recursive example with counting employees under given employee

assumption:
- user has only one manager
- there are no cycles 
"""
# employees data
employees = {'Betty': 'Sam', 'Bob': 'Sally', 'Dilbert': 'Nathan',
             'Jospeh': 'Sally', 'Nathan': 'Veronica', 'Sally': 'Veronica', 
             'Veronica':'', 'Susan': 'Bob', 'Sam': 'Joseph'}


def count_employees_under(employee):
    # chek for the right input:
    if employee is None or len(employee) < 1:
        raise KeyError('please enter employee name')

    # check if employee exists:
    if not employees.has_key(employee):
        raise KeyError('given employee does not work here')

    count = 0
    for person in employees:
        if employees[person] == employee:
            count += 1
            # recursively call counting employees under person
            count += count_employees_under(person)

    return count 


# test cases
# 1. wrong input:
try:
    print count_employees_under(None)
except KeyError as e:
    print e

# 2. employee who doesn't work here
try:
    print count_employees_under('Melita')
except KeyError as e:
    print e
# 3. no employees under 
print count_employees_under('Betty')

# 4. one employee under
print count_employees_under('Sam')

# 5. general case
print count_employees_under('Sally')

# 6. all employees under
print count_employees_under('Veronica')
