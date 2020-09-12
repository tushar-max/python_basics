## Introduction

### Math Operators

Table 1-1: Math Operators from Highest to Lowest Precedence

![math_operators](/automate_boring_stuff\images\table1_math_operators.png)

>The order of operations (also called precedence) of Python math operators is similar to that of mathematics. The ** operator is evaluated first; the *, /, //, and % operators are evaluated next, from left to right; and the + and - operators are evaluated last (also from left to right).

### Variable Names

You can name a variable anything as long as it obeys the following three rules:

* It can be only one word with no spaces.
* It can use only letters, numbers, and the underscore (_) character.
* It can’t begin with a number.

Though Spam is a valid variable you can use in a program, it is a Python convention to start your variables with a lowercase letter.

### The input() function

The input() function waits for the user to type some text on the keyboard and press ENTER.

This function call evaluates to a string equal to the user’s text, and the line of code assigns the myName variable to this string value.

### str() int() and float()

The str(), int(), and float() functions will evaluate to the string, integer, and floating-point forms of the value you pass, respectively.