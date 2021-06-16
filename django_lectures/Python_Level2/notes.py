# SCOPE

# Python Scope follows LEGB rules"
# Local, Enlcosing Function Locals, Global, and Built-In

# Local - Names assigned in any way within a function, and not declared global in that function
# EFL (Enclosing Function Locals) - Name in the local scope of any and all enclosing functions from inner to outer
# GLobal - Names assigned at the top-level of a module file, or declared global in a def within the file
# Built-In - Names preassingned in the built-in names module: open, range, SyntaxError, built in methods


#########################################
# In the following example, the first `print(x)` is x printing out the globally known variable because `my_func()` has not yet been declared
# When `my_func()` is called on the following line, and x is now reassigned to 50 within the scope of the function (this is only done within the scope of the function, the global variable if called later will return 25)

x = 25

def my_func():
  x = 50
  return x

print(x)
print(my_func())
