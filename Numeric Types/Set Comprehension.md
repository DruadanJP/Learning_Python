Set comprehensions, introduced in Python 3.0, are similar to list comprehensions but use curly braces instead of square brackets and create sets instead of lists. They run a loop and collect the result of an expression on each iteration, using a loop variable for access to the current iteration value. The result is a new set with the usual set behavior.

The expression {x ** 2 for x in [1, 2, 3, 4]} creates a set containing the squares of the numbers in the list. The loop is on the right, and the collection expression is on the left.

Comprehensions can also iterate over other types of objects, such as strings. For example, {x for x in ‘spam’} creates a set from the string ‘spam’.

>>> {x for x in ‘spam’}
{‘a’, ‘p’, ’s’, ‘m’}

>>> {c * 4 for c in ‘spam’}
{‘ssss’, ‘aaaa’, ‘pppp’, ‘mmmm’}

>>> {c * 4 for c in ‘spamham’}
{‘ssss’, ‘aaaa’, ‘hhhh’, ‘pppp’, ‘mmmm’}

>>> S = {c * 4 for c in ‘spam’}
>>> S | {‘mmmm’, ‘xxxx’}
{‘ssss’, ‘aaaa’, ‘pppp’, ‘mmmm’, ‘xxxx’}
>>> S & {‘mmmm’, ‘xxxx’}
{‘mmmm’}