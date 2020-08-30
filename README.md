# The objective of this assignment is to cover the below topics
* Floats : Coercing to Integer
* Floats : Rounding
* Decimals
* Decimals : Constructors and Contexts
* Decimals : Math Operations
* Decimals : Performance Considerations
* Complex Numbers
* Booleans
* Booleans : Precedence and Short-Circuiting

# The below functions are implemented

    '__and__',
    '__or__',
    '__repr__',
    '__str__',
    '__add__',
    '__eq__',
    '__float__',
    '__ge__',
    '__gt__',
    '__invertsign__',
    '__le__',
    '__lt__',
    '__mul__',
    '__sqrt__',
    '__bool__'


#   '__and__'
Returns True if both statements are true
#  '__or__'
Returns True if one of the statements is true
#  '__repr__'
Python __repr__() function returns the object representation. It could be any valid python expression such as tuple, dictionary, string etc. This method is called when repr() function is invoked on the object, in that case, __repr__() function must return a String otherwise error will be thrown.
#  '__str__'
The __str__ method is useful for a string representation of the object, either when someone codes in str(your_object) , or even when someone might do print(your_object) . The __str__ method is one that should be the most human-readable possible, yet also descriptive of that exact object
#  '__add__'
the __add__ method is a magic method which gets called when we add two numbers using the + operator
#  '__eq__'
Equality in Python is more complicated than most people realize but at its core you have to implement a __eq__(self, other) method. It should return either a boolean value if your class knows how to compare itself to other or NotImplemented if it doesn't.
#  '__float__'
To get called by built-int float() method to convert a type to float.
#  '__ge__'
To get called on comparison using >= operator.
#  '__gt__'
To get called on comparison using > operator.
#  '__invertsign__'
To invert the sign of given input. If positive number is given then the function will return the negative sign of the number given else vice-versa
#  '__le__'
To get called on comparison using <= operator.
#  '__lt__'
To get called on comparison using < operator.
#  '__mul__'
To get called on multiplication operation using * operator.
#  '__sqrt__'
sqrt() function is an inbuilt function in Python programming language that returns the square root of any number.
#  '__bool__'
True means "yes" and false means "no." In Python we rarely need to use the "bool" built-in. Often expressions can just be used directly as bool expressions.