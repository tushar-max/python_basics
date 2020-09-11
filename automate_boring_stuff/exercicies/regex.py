import re

# re.compile() returns a Regex pattern object (or simply, a Regex object).
phone_number_regex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d)")

# The mo variable name is just a generic name to use for Match objects.
mo = phone_number_regex.search("My number is 415-555-4242")


print("Phone number found: " + mo.group())
# Phone number found: 415-555-424

print(mo.group(1))
# 415

print(mo.group(2))
# 555-424

areaCode, mainNumber = mo.groups()

# findall method
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
# ['415-555-9999', '212-555-0000']



