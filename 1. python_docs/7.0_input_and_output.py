### string formatting using f

name = "Hammad"
department = "CS"
role = "Fellow"

# print(f'I am {name:4} from {department} and my role is {role:4}')
# print(f'I am {name} from {department} and my role is {role}. I have {2023-2022} years of experience')

## '!a'
alphabet = "Héllo, wørld!"
# print(ascii(alphabet))
# print(f'testing for asci value {alphabet}')




## using format method

# print("I am {name}".format(name="Hammad"))


## dictionary and format method

info = {
        'name': 'Hammad',
       'department':'computer science',
       "cgpa": 3
       }

# print("My name is {0[name]:s} and I am from {0[department]:s} department with cgpa more than {0[cgpa]:d}".format(info))


## reading a file 
# with open('1. python_docs/temp.txt', 'r') as file:
#         contents = file.read()
#         print(contents)
        
        
## writing a file
# with open('1. python_docs/temp2.txt', 'w') as file:
#         contents = "a quick brown fox"
#         file.write(contents) 


## appending
# with open('1. python_docs/temp2.txt', 'a') as file:
#         file.write(' appending contents')


import json 

## data serialization
_list = [1, 2, 3]

# _list = str(_list)
# print(_list, type(_list))

# serialized_data = json.dumps(_list)
# print(serialized_data, type(serialized_data))

# with open('1. python_docs/temp.txt', 'w') as file:
#         json.dump(_list, file)

# with open('1. python_docs/temp.txt', 'r') as file:
#         print(json.load(file))
