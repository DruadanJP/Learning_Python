# Sets have recently become more popular. 
# In Python 3.0, we can still use the built-in set function, but it also introduces a new set literal syntax using curly braces, previously used for dictionaries. 
# The following are equivalent:

>>> set([1, 2, 3, 4])            # Built-in: same as in 2.6
{1, 2, 3, 4}
>>> set(‘spam’)                  # Add all items in an iterable
{‘a’, ‘p’, ’s’, ‘m’}

>>> {1, 2, 3, 4}                 # Set literals: new in 3.0
{1, 2, 3, 4}
>>> S = {’s’, ‘p’, ‘a’, ‘m’}
>>> S.add(‘alot’)
>>> S
{‘a’, ‘p’, ’s’, ‘m’, ‘alot’}

# Set operations remain the same, but the result sets print differently:

>>> S1 = {1, 2, 3, 4}
>>> S1 & {1, 3}                  # Intersection
{1, 3}
>>> {1, 5, 3, 6} | S1            # Union
{1, 2, 3, 4, 5, 6}
>>> S1 - {1, 3, 4}               # Difference
{2}
>>> S1 > {1, 3}                  # Superset
True

# {} is still a dictionary. Empty sets print differently:

>>> S1 - {1, 2, 3, 4}            # Empty sets print differently
set()
>>> type({})                     # Because {} is an empty dictionary
<class ‘dict’>

>>> S = set()                    # Initialize an empty set
>>> S.add(1.23)
>>> S
{1.23}