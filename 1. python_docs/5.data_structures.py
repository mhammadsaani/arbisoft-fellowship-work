### Lists

_list = [10, 13, 9, 4, 1]

## index method

# print(_list.index(4, 2, 5)) # value, starting search and ending search index



## Lists as Stack

class Stack:
    
    
    def  __init__(self) -> None:
        self.list = []
    
    def push(self, value):
        self.list.append(value)
    
    def pop(self):
        self.list.pop()
    
    def display(self):
        print(self.list)
    
stack_obj = Stack()

# stack_obj.push(10)
# stack_obj.push(20)
# stack_obj.push(30)

# stack_obj.display()

# stack_obj.pop()

# stack_obj.display()


## Lists as Queues

class Queue:
    
    
    def __init__(self) -> None:
        self.list = []
    
    def push(self, value):
        self.list.append(value)
        
    def pop(self):
        self.list.pop(0)
        
    def display(self):
        print(self.list)
        

# queue = Queue()

# queue.push(10)
# queue.push(20)
# queue.push(30)

# queue.display()

# queue.pop()

# queue.display()


### List Comprehensions (general syntax -> expression for item in collection if statement)

## without if
# squares = [x * x for x in range(10)]
# print(squares)

## with if

# squares = [x * x for x in range(10) if x % 2 == 0]
# print(squares)

## using lambda functions
# sqaures = list(map(lambda x: x * x, [1, 2, 3]))
# print(squares)

## nested for 
# coordinates = [(x, y, z) for x in range(2) for y in range(2) for z in range(2)]
# print(coordinates)


vec = [-4, -2, 0, 2, 4]

## doubled values 
doubled_values = [x * 2 for x in vec]
# print(doubled_values)

## only positive numbers
positive_only = [x for x in vec if x > 0]
# print(positive_only)

## apply a function to all elements
function_applied = [float(x) for x in vec]
# print(function_applied)

## call a method on every element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# print([x.strip() for x in freshfruit])

## creating a list containing tuples in form of x and x**x
list_of_tuples = [(x, x ** 2) for x in range(10)]
# print(list_of_tuples)

from math import pi 

## printing pi upto 5 decimal points
# print([round(pi, x) for x in range(1, 6)])

## Transposing a matrix

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

transposed_matrix = []
for col in range(len(matrix[1])):
   transposed_row = []
   for value in range(len(matrix)):
       transposed_row.append(matrix[value][col])

   transposed_matrix.append(transposed_row)

# print(matrix, "\n", transposed_matrix)

## using list comprehension

transoped_matrix = [[matrix[value][col] for value in range(len(matrix))] for col in range(len(matrix[1]))]
# print(matrix, "\n", transposed_matrix)

## using zip 
# print(list(zip(*matrix)))

# print(*matrix)

# print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))

### Tuples

a = () # empty tuples
singleton_tuple = (10)
# print(singleton_tuple, type(singleton_tuple)) 
## so to initialize a singleton tuple we use
singleton_tuple = 10, 
# print(singleton_tuple, type(singleton_tuple)) 


### removing duplicates

_list = [1, 2, 3, 4, 5, 5]
unique_list = list(set(_list))
# print(unique_list)

