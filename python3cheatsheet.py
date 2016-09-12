#Welcome to the python cheat sheet
#Single line comments start with a hashtag.

""" Multiline strings
    can be written using three "s
    and can be used as comments
"""

# 1. Primitive Datatypes and Operators

# Numbers
1 # => 1

# You can do math with numbers
1 + 1 # => 2
3 - 2 # => 1
5 * 10 # => 50

# Division returns floats by default
25 / 5 # => 5.0

# Integer division rounds down
5 // 3 # => 1
5.0 // 3.0 # => 1.0
-5 // 3 # => -2
-5.0 // 3.0 # => -2.0

# Using floats return floats
3 * 2.0 # => 6.0

# Modulo operation to find the remainder
5 % 2 # => 1

# Exponentiation (x**y, x to the yth power)
2**4 # => 16

# Enforce precendence with paretheneses
(1 + 3) * 2 # => 8

# Boolean values are primitives (Note: the capitalization)
True
False

# negate with not
not True # => False
not False # => True

# Boolean Operators
# Note "and" and "or" are case-sensitive
True and False # => False
True and True # => True
False and False # => False
True or False # => True
True or True # => True
False or False # => False

# You can use Bool operators with ints
0 and 2 # => 0
-5 or 0 # => -5
0 == False # => True
2 == True # => False
1 == True # => True

# Equality is ==
1 == 1 # => True
2 == 1 # => False

# Inequality is !=
1 != 1 # => False
1 != 2 # => True

# More comparisons
1 < 10 # => True
1 > 10 # => False
2 <= 2 # => True
2 >= 2 # => True

# Comparisons can be chained
1 < 2 < 3 # => True
2 < 3 < 2 # => False

# (is vs ==) is checks if two variables refer to the same object, but == checks
# if the objects pointed to have the same values
a = [1, 2, 3, 4] # a at a new list, [1, 2, 3, 4]
b = a # Point b at what a is pointing to
b is a # => True, a and b refer to the same object
b == a # => True, a's and b's objects are equal (they're the same object after all)
b = [1, 2, 3, 4] # => False, a and b don't refer to the same object (even though the values are the same)
b == a # => True, a's and b's objects are equal

# Strings are created with " or '
"This is a string."
'This is also a string.'

# Strings can be added too! But try not to do this.
"Hello " + "world!" # => "Hello world!"
# Strings can be added without using '+'
"Hello " "world!" # => "Hello world!"

#A string can be treated like a list of characters
"This is a string"[0] # => 'T'

# You can find the length of a string
len("This is a string") # => 16

# .format can be used to format strings, like this:
"{} can be {}".format("Strings", "interpolated") # => "Strings can be interpolated"

# You can repeat the formatting arguments to save some typing.
"{0} be nimble, {0} be quick, {0} jump over the {1}".format("Jack", "candle stick")
# => "Jack be nimble, Jack be quick, Jack jump over the candle stick"

# You can use keyboards if you don't want to count.
"{name} wants to eat {food}".format(name="Kevin", food="halal snack packs")
# "Kevin wants to eat halal snack packs"

# If your Python 3 code also needs to run on Python 2.5 and below, you can also
# still use the old style of formatting:
"%s can be %s the %s way" % ("Strings", "interpolated", "old") # => Strings can be interpolated the old way

# None is an object
None # => None

# Don't use the equality "==" symbol to compare objects to None
# Use "is" instead. This checks for equality for object identity.
"etc" is None # => False
None is None # => True

# None, 0, and empty strings/lists/dicts all evaluate to False
# All other values are True
bool(0) # => False
bool("") # => False
bool([]) # => False
bool({}) # => False

# 2. Variables and Collections
print("I'm Python. Nice to meet you!") # => I'm Python. Nice to meet you!

# By default, the print function also prints out a new line at the end.
# Use the optional argument end to change the end character.
print("Hello, World"m end="!") # => Hello World!

# Simple way to get input from console
input_string_var = input("Enter some data: ") # Returns the data as a string
# Note: In earlier versions of Python, input() method was named as raw_input()

# No need to declare variables before assigning to them
# Convention is to use lower_case_with_underscores
some_var = 5
some_var # => 5

# Accessing a previous unassigned variable is an exception.
# See Control Flow to learn more about exception handling.
some_unknown_var # => Raises a NameError

# if can be used as an expression
# Equivalent of C's '?:' ternary operator
"yahoo!" if 3 > 2 else 2 # => "yahoo!"

# Lists store sequences
li = []

# You can start with a prefilled list
other_li = [4, 5, 6]

# Add stuff to the end of a list with append
li.append(1) # li is now [1]
li.append(2) # li is now [1, 2]
li.append(3) # li is now [1, 2, 3]
li.append(4) # li is now [1, 2, 3, 4]
# Remove from the end with pop
li.pop() # => 4 and li is now [1, 2, 3]
# Let's put it back
li.append(4) # li is now [1, 2, 3, 4]

# Access a list like you would any array
li[0] # => 1
li[1] # => 2
# Look at the last element
li[-1] # => 4

# Looking out of bounds is an IndexError
li[4] # Raises an IndexError

# You can look at ranges with slice syntax.
# (It's a closed/open range for you mathy types.)
li[1:3] # => [2, 3]
# Omit the beginning
li[2:] # => [3, 4]
# Omit the end
li[:3] # => [1, 2, 3]
# Select every second entry
li[::2] # => [1, 3]
# Return a reversed copy of the list
li[::-1] # => [4, 3, 2, 1]
# Use any combination of these to make advanced slices
# li[start:end:step]

# Make a one layer deep copy using slices
li2 = li[:] # => li2 = [1, 2, 3, 4] but (li2 is li) returns false.

# Remove arbitrary elements from a list with "del"
del li[3] # li is now [1, 2, 3]

# Remove first occurrence of a value
li.remove(2) # li is now [1, 3]
li.remove(2) # Raises a ValueError as 2 is not in the list

# Insert an element at a specific index
li.insert(1, 2) # li is now [1, 2, 3] again

# Get the index of the first item fond matching the argument
li.index(2) # => 1
li.index(4) # Raises a ValueError as 4 is not in the list

# You can add lists
# Note values for li and for other_li are not modified.
li + other_li # => [1, 2, 3, 4, 5, 6]

# Cocatenate listss with "extend()"
li.extend(other_li) # Now li is [1, 2, 3, 4, 5, 6]

# Check for existence in a list with "in"
1 in li # => True

# Examine the length with "len()"
len(li) # => 6

# Tuples are like lists but are immutable.
tup = (1, 2, 3)
tup[0] # => 1
tup[0] = 3 # Raises a TypeError

# Note that a tuple of length one has to have a comma after the last element but
# tuples of other lengths, even zero do not.
type((1)) # => <class 'int'>
type((1,)) # => <class 'tuple'>
type(()) # => <class 'typle'>

# You can do most of the list operations on tuples too
len(tup) # => 3
tup + (4, 5, 6) # => (1, 2, 3, 4, 5, 6)
tup[:2] # => (1,2)
2 in tup # => True

# You can unpack tuples (or lists) into variables
a, b, c = (1, 2, 3) # a is now 1, b is now 2 and c is now 3
# You can also do extended unpacking
a, *b, c = (1, 2, 3, 4) # a is now 1, b is now [2, 3] and c is now 4
# Tuples are created by default if you leave out the parentheses
d, e, f = 4, 5, 6
# Now look how easy it is to swap two values
e, d = d, e # d is now 5 and e is now 4

# Dictionaries store mappings
empty_dict = {}
# Here is a prefilled dictionary
filled_dict = {"one": 1, "two": 2, "three": 3}

# Note keys for dictionaries have to be immutable types. This is to ensure that
# the key can be converted to a constant hash value for quick look-ups.
# Immutable types include ints, floats, strings, tuples.
invalid dict = {[1, 2, 3]: "123"} # => Raises a TypeError: unhashable type: 'list'
valid_dict = {(1, 2, 3):[1, 2, 3]} # Values can be of any type, however.

# Look up values with []
filled_dict["one"] # => 1

# Get all keys as an iterable with "keys()". We need to wrap the call in list()
# to turn it into a list. We'll talk about those later. Note - Dictionary key
# ordering is not guaranteed. Your results might not match this exactly.
list(filled_dict.keys()) # => ["three", "two", "one"]

# Get all values as an iterable with "values()". Once again we need to wrap it
# in list() to get it out of the iterable. Note - same as above regarding key ordering
list(filled_dict.values()) # => [3, 2, 1]

# Check for existence of keys in a dictionary with "in"
"one" in filled_dict # => True
1 in filled_dict # => False

# Looking up a non-existing key is a KeyError
filled_dict["four"] # => KeyError

# Use "get()" method to avoid the KeyError
filled_dict.get("one") # => 1
filled_dict.get("four") # => None

# The get method supports a default argument when the value is missing
filled_dict.get("one", 4) # => 1
filled_dict.get("four", 4) # => 4 (because it's missing)

# "setdefault()" inserts into a dictionary only if the given key isn't present
filled_dict.setdefault("five", 5) # filled_dict["five"] is set to 5
filled_dict.setdefault("five", 6) # filled_dict["five"] is still set to 5

# Adding to a dictionary
filled_dict.update({"four":4}) # => {"one": 1, "two": 2, "three": 3, "four": 4}
#filled_dict["four"] = 4 (another way to add to dict)

# Remove keys from a dictionary with del
del filled_dict["one"] # Removes the key "one" from filled dict

# From Python 3.5 you can also use the additional unpacking options
{'a': 1, **{'b': 2}} # => {'a': 1, 'b': 2}
{'a': 1, **{'a': 2}} # => {'a': 2}

# Sets store ... well sets
empty_set = set()
# Initialize a set with a bunch of values. Yeah it looks a bit like a dict. Sorry.
some_set = {1, 1, 2, 2, 3, 4} # some_set is now {1, 2, 3, 4}

# Similar to keys of a dictionary, elements of a set have to be immutable.
invalid_set = {[1], 1} # => Raises a TypeError: unhashable type: 'list'
valid_set = {(1,), 1}

# Can set new variables to a set
filled_set = some_set

# Add one more item to the set
filled_set.add(5) # filled_set is now {1, 2, 3, 4, 5}

# Do set intersection with &
other_set = {3, 4, 5, 6}
filled_set & other_set # => {3, 4, 5}

# Do set union with |
filled_set | other_set # => {1, 2, 3, 4, 5, 6}

# Do set difference with -
{1, 2, 3, 4} - {2, 3, 5} # => {1, 4}

# Do set symmetric difference with ^
{1, 2, 3, 4} ^ {2, 3, 5}

# Check if set on the left is a superset of set on the right
{1, 2} >= {1, 2, 3} # => False

# Check if set on the left is a subset of the set on the right
{1, 2} <= {1, 2, 3} # => True

# Check for existence in a set with in
2 in filled_set # => True
10 in filled_set # => False

# 3. Control Flow and Iterables

# Let's just make a variable
some_var = 5

# Here is an if statement. Identation is significant in python!
# prints "some_var is smaller than 10"

if some_var > 10:
    print("some_var is totally bigger than 10.")
elif some_var < 10:
    print("some var is smaller than 10.")
else:
    print("some_var is indeed 10.")

"""
For loops iterate over lists
prints:
    dog is a mammal
    cat is a mammal
    mouse is a mammal
"""

for animal in ["dog", "cat", "mouse"]:
    # You can use format() to interpolate formatted strings
    print("{} is a mammal".format(animal))

"""
"range(number)" returns an iterable of numbers
from zero to the given number
prints:
    0
    1
    2
    3
"""
for i in range(4):
    print(i)

"""
"range(lower,upper)" returns an iterable of numbers
from the lwoer number to the upper number
prints:
    4
    5
    6
    7
"""
for i in range(4,8):
    print(i)

"""
"range(lower, upper, step)" returns an iterable of
numbers
from the lower number to the upper number, while
incrementing
by step. If step is not indicated, the default value is 1.
prints:
    4
    6
"""
for i in range(4,8,2):
    print(i)

"""
While loops go until a condition is no longer met.
prints:
    0
    1
    2
    3
"""
x = 0
while x < 4:
    print(x)
    x += 1 # Shorthand for x = x + 1

# Handle exceptions with a try/except block
try:
    #Use "raise" to raise an error
    raise IndexError("This is an index error")
except IndexError as e:
    pass # Pass is just a no-op. Usually you would do recovery here.
except (TypeError, NameError):
    pass # Multiple exceptions can be handled together, if required.
else: #Optional clause to the try/except block. Must follow all except blocks
    print("All good!") # Runs only if the code in try raises no exceptions
finally: # Execute under all circumstances
    print("We can clean up resources here")

# Instead of try/finally to cleanup resources you can use a with statement
with open("myfile.txt") as f:
    for line in f:
        print(line)
# Python offers fundamental abstraction called the iterable.
# An iterable is an object that can be treated as a sequence.
# The object returned the range function, is an iterable.

filled_dict = {"one": 1, "two": 2, "three": 3}
our_iterable = filled_dict.keys()
print(our_iterable) # => dict_keys(['one', 'two', 'three']). This is an object
# that implements our ITerable interface

# We can loop over it.
for i in our_iterable:
    print(i) # Prints one, two, three

# However we cannot address elements by index.
our_iterable[1] #Raises a TypeError

# An iterable is an object that knows how to create an iterator.
our_iterator = iter(our_iterable)

# Our iterator is an object taht can remember the state as we traverse through it.
# We can get the next object with "next()".
next(our_iterator) # => "one"

# It maintains state as we iterate.
next(our_iterator) # => "two"
next(our_iterator) # => "three"

# After the iterator has returned all of its data, it gives you a StopIterator Exception
next(our_iterator) # Raises StopIteration

# You can grab all the elements of an iterator by calling list() on it.
list(filled_dict.keys()) # => Returns ["one", "two", "three"]

# 4. Functions

# Use "def" to create new functions
def add(x, y):
    print("x is {} and y is {}".format(x, y))
    return x + y # Return values with a return statement

# Calling functions with parameters
add(5, 6) # => prints out "x is 5 and y is 6" and returns 11

# Another way to call functions is with keyword arguments
add(y=6, x=5) # Keyword arguments can arrive in any order.

# You can define functions that take a variable number of position arguments
def varargs(*args):
    return args

varargs(1, 2, 3) # => (1, 2, 3)

# You can define functions that take a variable number of keyword arguments
def keyword_args(**kwargs):
    return kwargs

# Let's call it to see what happens
keyword_args(big="foot", loch="ness") # => {"big": "foot", "loch": "ness"}

# You can do both at once, if you like
def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)

"""
all_the_args(1, 2, a=3, b=4) prints:
    (1,2)
    {"a": 3, "b": 4}
"""

# When calling functions, you can do the opposite of args/kwargs!
# Use * to expand tuples and use ** to expand kwargs.
args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args) # equivalent to foo(1, 2, 3, 4)
all_the_args(**kwargs) # equivalent to foo(a=3, b=4)
all_the_args(*args, **kwargs) # equivalent to foo(1, 2, 3, 4, a=3, b=4)

# Returning multiple values (with tuple assignments)
def swap(x, y):
    return y, x # Return multiple values as a tuple without the parentheses.
    # (Note: parentheses have been excluded but can be included)

x = 1
y = 2
x, y = swap(x, y) # => x = 2, y = 1
# (x, y) = swap(x, y) #Parentheses have been excluded but can be included.

# Function Scope
x = 5

def set_x(num):
    # Local var x not the same as global variable x
    x = num # => 43
    print(x) # => 43

def set_global_x(num):
    global x
    print(x) # => 5
    x = num # global var x is now set to 6
    print(x) # => 6

set_x(43)
set_global_x(6)

# Python has first class functions
def create_adder(x):
    def adder(y):
        x + y
    return adder

add_10 = create_adder(10)
add_10(3) # => 13

# There are also anonymous functions
(lambda x: x > 2)(3) # => True
(lambda x, y: x ** 2 + y ** 2)(2,1) # => 5

# There are built-in higher order functions
list(map(add_10, [1, 2, 3])) # => [11, 12, 13]
list(map(max, [1, 2 ,3], [4, 2, 1])) # => [4, 2, 3]
list(filter(lambda x: x > 5, [3, 4, 5, 6, 7])) # => [6, 7]

# We can use list comprehensions for nice maps and filters
# List comprehension stores the output as a list which can itself be a nested list
[add_10(i) for i in [1, 2, 3]] # => [11, 12, 13]
[x for x in [3, 4, 5, 6, 7]] if x > 5] # => [6, 7]

# You can construct set and dict comprehensions as well.
{x for x in 'abcddeef' if x not in 'abc'} # => {'d', 'e', 'f'}
{x: x**2 for x in range(5)} # => {0: 0,  1: 1, 2: 4, 3: 9, 4: 16}

# 5. Modules
import math
print(math.sqrt(16)) # => 4.0

# You can get specific functions from a module
from math import ceil, floor
print(ceil(3.7)) # => 4.0
print(floor(3.7)) # => 3.0

# You can import all functions from a module.
# Warning: this is not recommended
from math import *

# You can shorten module names
import math as m
math.sqrt(16) == m.sqrt(16) # => True

# Python modules are just ordinary python files.
# You can write your own, and import them.
# The name of the module is the same as the name of the file

# You can find out which functions and attributes defines a module.
import math
dir(math)

# If you have a Python script named math.py in teh same folder as your current script,
# the file math.py will be loaded instead of the built-in Python module.
# This happens because the local folder has priority over Python's built-in libraries.

# 6. Classes
class Human:
    # A class attribute. It is shared by all instances of this class
    species = "H. sapiens"

    # Basic initializer, this is called when this class is intantiated.
    # Note that the edouble leading and trailing underscores denote obejcts
    # or attributes that are used by python but that live in user-controlled namespaces
    # Methods(or objects or atteibutes) like: __init__, ___str__,
    # __repr__ etc. are called magic methods (sometimes called dunder methods)
    # You should not invent such names on your own.
    def __init__(self, name):
        self.name = name
        self.age = 0

    # An instance method. All methods take "self" as the first argument.
    def say(self, msg):
        print("{name}:{message}".format(name=self.name, message=msg))

    # Another instance method
    def sing(self):
        return "Hey, I was doing just fine before I met you. I drank too much and that's an issue but I'm okay."

    # A class method is shared among all instances
    # They are called with the calling class as the first argument
    @classmethod
    def get_species(cls):
        return cls.species

    # A static method is called without a class or instance reference
    @staticmethod
    def grunt():
        return "*grunt*"

    # A property is just like a getter.
    # It turns the method age() into a read-only attribute of the same name

    @property
    def age(self):
        return self._age

    # This allows the property to be set
    @age.setter
    def age(self, age):
        self._age = age

    #This allows the property to be deleted
    @age.deleter
    def age(self):
        del self._age

    # When a Python interpreter reads a source file it executes all its code.
    # This __name__ check makes sure this code block is only executed when this
    # module is the main program.

    if __name__ == '__main__':
        # Instantiate a class
        i = Human(name="Ian")
        i.say("hi") # "Ian: hi"
        j = Human("Joel")
        j.say("hello") # "Joel: hello"
        # i and j are instances of type Human, or in other words: they are Human objects

        i.say(i.get_species()) # "Ian: H. sapiens"
        Human.species = "Homo sapiens"
        i.say(i.get_species()) # "Ian: Homo sapiens"
        j.say(i.get_species()) # "Joel: Homo sapiens"

        # Call the static method
        print(Human.grunt()) # => "*grunt*"
        print(i.grunt()) # => "*grunt*"

        i.age = 42
        i.say(i.age) # "Ian: 42"
        j.say(j.age) # "Joel: 0"
        # Delete the property
        del i.age
        # i.age would raise an AttributeError

# 6.1 Multiple Inheritance
class Bat:

    species = 'Baty'

    def __init__(self, can_fly=True):
        self.fly = can_flya

    # This class also has a say method
    def say(self, msg):
        msg = '... ... ...'
        return msg

    # And its own method as well
    def sonar(self):
        return '))) ... ((('

if __name__ == '__main__':
    b = Bat()
    print(b.say('hello'))
    print(b.fly)

# from "filename-without-extension" import "function-or-class"
from human import Human
from bat import Bat

# Batman inherits from both Human and Bat
class Batman(Human, Bat):

    # Batman has its own value for the species attribute
    species = 'Superhero'

    def __init__(self, *args, **kwargs):
        #Typically to inherit attributes you have to call super:
        # super(Batman, self).__init(*args, **kwargs)
        # However, we are dealing with multiple inheritance here, and super()
        # only works with the next base class in the MRO list.
        # So instaed we explicitly call __init__ for all ancestors.
        # The use of *args and **kwargs allows for a clean way to pass arguments,
        # with each parent "peeling a layer of the onion"

        Human.__init__(self, 'anonymous', *args, **kwargs)
        Bat.__init__(self, *args, can_fly=False, **kwargs)
        # override the value for the name attribute
        self.name = 'Sad Affleck'

    def sing(self):
        return 'nan nan nan nan nan batman!'

if __name__ == '__main__':
    sup = Batman()

    #Instance type checks
    if isinstance(sup, Human):
        print('I am human')
    if isinstance(sup, Bat):
        print('I am bat')
    if type(sup) is Batman:
        print('I am Batman')

    # Get the Method Resolution search Order used by both getattr() and super().
    # This attribute is dynamic and can be updated
    print(Batman.__mro__) # => (<class'__main__.Batman'>, <class 'human.Human'>, <class'bat.Bat'>, <class 'object'>)

    # Calls parent method but uses its own class attribute
    print(sup.get_species()) # => Superhero

    # Calls overloaded method
    print(sup.sing())

    # Calls method from Human, because inheritance order matters
    sup.say('I agree') # => Sad Affleck: I agree

    # Call method that only exists in 2nd ancestors
    print(super.sonar()) # => ))) ... (((

    # Inherited class attribute
    sup.age = 100
    print(sup.age) # => 100

    # Inherited attribute from 2nd ancestors whose default value was overridden.
    print('Can I fly? ' + str(sup.fly))

# 7. Advanced

# Generators help you make lazy code.
def double_numbers(iterable):
    for i in iterable:
        yield i + i

# Generators are memory-efficient because they only load the data needed to
# process the next value in the iterable. This allows them to perform operations
# on otherwise prohibitively large value ranges.
# 'range' replaces 'xrange' in Python 3.
for i in double_numbers(range(1,9000000000)):
    # 'range' is a generator
    print(i)
    if i>= 30:
        break

# Just as you can create a list comprehension, you can create generator
# comprehensions as well.
values = (-x for x in [1,2,3,4,5])
for x in values:
    print(x) # prints -1 -2 -3 -4 -5 to terminal

# You can also cast a generator comprehension directly to a list.
values = (-x for x in [1,2,3,4,5])
gen_to_list = list(values)
print(gen_to_list) # => [-1, -2, -3, -4, -5]

# Decorators
# In this example 'beg' wraps 'say'. If say_please is True then it
# will change the returned message.
from functools import wraps

def beg(target_function):
    @wraps(target_function)
    def wrapper(*args, **kwargs):
        msg, say_please = target_function(*args, **kwargs)
        if say_please:
            return "{} {}".format(msg, "Please I am poor :()")
        return msg
    return wrapper

@beg
def say(say_please=False):
    msg = "Can you buy me a beer?"
    return msg, say_please

print(say()) # Can you buy me a beer?
print(say(say_please=True)) # Can you buy me a beer please?
