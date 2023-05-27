Other than the randint() and randrange() methods, we can build a code to generate random four-digit numbers simply with the help of the Python string module, digits function in the string module, join operation, the choice function of the random module, and a for loop.

First, we can import the choice method from the random module.

`from random import choice`
In the next step, we need to get numbers from 0 to 9 to generate a random four-digit number. To do that, we can use the digits method of the string module.

The `digits()` method provides a text string, including the numbers from 0 to 9.

First, we import the string module to the code.

`import string`
Then we use the string.digits() method to get the numbers. We can assign it to a variable for ease of use.

`numbers = string.digits`
Now we can select four random numbers from the numbers variable using the choice() method and join them as a string. We use the join method, choice method, and a for loop.

`randomNumber = ''.join(choice(numbers) for _ in range(4))`
Here the value 4 in the for loop is the number of digits of the output we want. If we change it to five, we get a random number with five digits.

But in our case, we only need to generate four-digit numbers, so we have added four as the value.

Then we can print the value using a print function.
