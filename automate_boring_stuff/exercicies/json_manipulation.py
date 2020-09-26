stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'

import json

# translate a string containing JSON data into a Python value

jsonDataAsPythonValue = json.loads(stringOfJsonData)

print(jsonDataAsPythonValue)

# translate a Python value into a string of JSON-formatted data

pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}

stringOfJsonData_1 = json.dumps(pythonValue)
print(stringOfJsonData_1)