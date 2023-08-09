### statement vs expression

## expression is piece of code that evaluate to / produces a value
## statement is the whole line of code/instruction itself.

statement = 2 + 3 * 9 # right part is expression, whole isntruction is statement

## a way to check is to put in print()

import sys
# print(sys.builtin_module_names) # to check build in modules
# print(sys.path)


### Compiled Python files

# to speed up things, python stores the cached version of modules in __pycache__ directory with the name
# module_name.version.pyc


# print(sys.ps1) # will work on interactive mode
# print(sys.ps2)

## dir identifies what names are present in module name space

# print(dir(list()))


from testing_packages.test import test



test()
# fibo.fib(10)
# test.test()

# temp.temp()


# if __all__ in __init__.py has a function with the name 
# of some module, then that module will not be imported



