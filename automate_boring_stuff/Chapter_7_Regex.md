### Regular Expressions (Regex)

See file automate_boring_stuff\exercicies\regex.py

While there are several steps to using regular expressions in Python, each step is fairly simple.

Import the regex module with import re.
Create a Regex object with the re.compile() function. (Remember to use a raw string.)
Pass the string you want to search into the Regex object’s search() method. This returns a Match object.
Call the Match object’s group() method to return a string of the actual matched text.

The \( and \) escape characters in the raw string passed to re.compile() will match actual parenthesis characters. In regular expressions, the following characters have special meanings:

    .  ^  $  *  +  ?  {  }  [  ]  \  |  (  )

You can think of the ? as saying, “Match zero or one of the group preceding this question mark.”

While * means “match zero or more,” the + (or plus) means “match one or more.” Unlike the star, which does not require its group to appear in the matched string, the group preceding a plus must appear at least once. 

Python’s regular expressions are greedy by default, which means that in ambiguous situations they will match the longest string possible. The non-greedy (also called lazy) version of the braces, which matches the shortest string possible, has the closing brace followed by a question mark.

    >>> greedyHaRegex = re.compile(r'(Ha){3,5}')
    >>> mo1 = greedyHaRegex.search('HaHaHaHaHa')
    >>> mo1.group()
    'HaHaHaHaHa'

    >>> nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
    >>> mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
    >>> mo2.group()
    'HaHaHa'

Note that the question mark can have two meanings in regular expressions: declaring a non-greedy match or flagging an optional group. These meanings are entirely unrelated.

#### findall() Method

To summarize what the findall() method returns, remember the following:

* When called on a regex with no groups, such as \d\d\d-\d\d\d-\d\d\d\d, the method findall() returns a list of string matches, such as ['415-555-9999', '212-555-0000'].
* When called on a regex that has groups, such as (\d\d\d)-(\d\d\d)-(\d\d\d\d), the method findall() returns a list of tuples of strings (one string for each group), such as [('415', '555', '9999'), ('212', '555', '0000')].

### Character Classes

![characther_class](/automate_boring_stuff\images\characters_class.png)

The character class [0-5] will match only the numbers 0 to 5; this is much shorter than typing (0|1|2|3|4|5). Note that while \d matches digits and \w matches digits, letters, and the underscore, there is no shorthand character class that matches only letters. (Though you can use the [a-zA-Z] character class, as explained next.)

You can also include ranges of letters or numbers by using a hyphen. For example, the character class [a-zA-Z0-9] will match all lowercase letters, uppercase letters, and numbers.

Note that inside the square brackets, the normal regular expression symbols are not interpreted as such. This means you do not need to escape the ., *, ?, or () characters with a preceding backslash.

By placing a caret character (^) just after the character class’s opening bracket, you can make a negative character class.

You can also use the caret symbol (^) at the start of a regex to indicate that a match must occur at the beginning of the searched text. Likewise, you can put a dollar sign ($) at the end of the regex to indicate the string must end with this regex pattern. And you can use the ^ and $ together to indicate that the entire string must match the regex—that is, it’s not enough for a match to be made on some subset of the string.

I always confuse the meanings of these two symbols, so I use the mnemonic “Carrots cost dollars” to remind myself that the caret comes first and the dollar sign comes last.

The . (or dot) character in a regular expression is called a wildcard and will match any character except for a newline.

#### Matching Everything with Dot-Star

Sometimes you will want to match everything and anything. For example, say you want to match the string 'First Name:', followed by any and all text, followed by 'Last Name:', and then followed by anything again. You can use the dot-star (.*) to stand in for that “anything.”

    >>> nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
    >>> mo = nameRegex.search('First Name: Al Last Name: Sweigart')
    >>> mo.group(1)
    'Al'
    >>> mo.group(2)
    'Sweigart'

#### Matching Newlines with the Dot Character

The dot-star will match everything except a newline. By passing re.DOTALL as the second argument to re.compile(), you can make the dot character match all characters, including the newline character.

    >>> newlineRegex = re.compile('.*', re.DOTALL)
    >>> newlineRegex.search('Serve the public trust.\nProtect the innocent.
    \nUphold the law.').group()
    'Serve the public trust.\nProtect the innocent.\nUphold the law.'

#### Review of Regex Symbols

This chapter covered a lot of notation, so here’s a quick review of what you learned about basic regular expression syntax:

* The ? matches zero or one of the preceding group.
* The * matches zero or more of the preceding group.
* The + matches one or more of the preceding group.
* The {n} matches exactly n of the preceding group.
* The {n,} matches n or more of the preceding group.
* The {,m} matches 0 to m of the preceding group.
* The {n,m} matches at least n and at most m of the preceding group.
* {n,m}? or *? or +? performs a non-greedy match of the preceding group.
* ^spam means the string must begin with spam.
* spam$ means the string must end with spam.
* The . matches any character, except newline characters.
* \d, \w, and \s match a digit, word, or space character, respectively.
* \D, \W, and \S match anything except a digit, word, or space character, respectively.
* [abc] matches any character between the brackets (such as a, b, or c).
* [^abc] matches any character that isn’t between the brackets.

![cheatsheet](/automate_boring_stuff\images\regex_cheatsheet.png)

#### Case-Insensitive Matching

But sometimes you care only about matching the letters without worrying whether they’re uppercase or lowercase. To make your regex case-insensitive, you can pass re.IGNORECASE or re.I as a second argument to re.compile(). 

    >>> robocop = re.compile(r'robocop', re.I)

#### The sub() Method

The sub() method for Regex objects is passed two arguments. The first argument is a string to replace any matches. The second is the string for the regular expression. The sub() method returns a string with the substitutions applied.

    >>> namesRegex = re.compile(r'Agent \w+')
    >>> namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
    'CENSORED gave the secret documents to CENSORED.'

Sometimes you may need to use the matched text itself as part of the substitution. In the first argument to sub(), you can type \1, \2, \3, and so on, to mean “Enter the text of group 1, 2, 3, and so on, in the substitution.”

    >>> agentNamesRegex = re.compile(r'Agent (\w)\w*')
    >>> agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent
    Eve knew Agent Bob was a double agent.')
    A**** told C**** that E**** knew B**** was a double agent.'

#### Managing Complex Regexes

You can spread the regular expression over multiple lines with comments like this:

    phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?            # area code
        (\s|-|\.)?                    # separator
        \d{3}                         # first 3 digits
        (\s|-|\.)                     # separator
        \d{4}                         # last 4 digits
        (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
        )''', re.VERBOSE)

#### Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE

Including all three options in the second argument will look like this:

    >>> someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

