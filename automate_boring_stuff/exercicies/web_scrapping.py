import webbrowser
# open() function can launch a new browser to a specified URL.
webbrowser.open("https://inventwithpython.com/")

import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

print(type(res))

print(res.status_code == requests.codes.ok)

print(len(res.text))

print(res.text[:250])

# Write in a file what you donwload

playFile = open("RomeoAndJulie.txt", "wb")

for chunk in res.iter_content(100000):
    playFile.write(chunk)


playFile.close()

