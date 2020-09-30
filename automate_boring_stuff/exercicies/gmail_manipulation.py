import ezgmail, os

os.chdir(r"C:\Users\Frede\OneDrive\Ambiente de Trabalho\Frederico Gago\Educação\Programação\python_basics\python_basics\automate_boring_stuff\exercicies")

print(os.getcwd())
ezgmail.init()

# Sending mail from a gmail account with files

#ezgmail.send("fredericogago@hotmail.com", "Assunto: Experiencia","Estou a exprimentar o modulo ezgmail\n Enviar mail's a partir de scripts de python, com anexos",["example1.csv","example.CSV"],cc="fredericogago@confere.pt", bcc="ritasabino@confere.pt")

unreadThreads = ezgmail.unread() # list of GmailThread objects
"""
The unread() function returns a list of GmailThread objects for all unread emails, which can then be passed to ezgmail.summary() to print a summary of the conversation threads in that list
"""
#print(ezgmail.summary(unreadThreads))

#print(len(unreadThreads))
#print(unreadThreads[0].messages)
#print(unreadThreads[0].messages[0].subject)
#print(unreadThreads[0].messages[0].body)
#print(unreadThreads[0].messages[0].timestamp)
#print(unreadThreads[0].messages[0].sender)
#print(unreadThreads[0].messages[0].recipient)
#print()
"""
ezgmail.recent() function will return the 25 most recent threads in your Gmail account. You can pass an optional maxResults keyword argument to change this limit
"""
recenThreads = ezgmail.recent(maxResults=100)
#print(len(recenThreads))

# Search emails
resulThreads = ezgmail.search("meetup")
#print(len(resulThreads))
#print(ezgmail.summary(resulThreads[0]))


# Downloading attachments

threads = ezgmail.search("from:ritasabino@confere.pt")

print(threads[0].messages[0].attachments)
threads[0].messages[0].downloadAttachment("example1.csv")
# ill create a folder in the current directory called vacation2020 with the attachements
threads[0].messages[0].downloadAllAttachments(downloadFolder='vacation2020')





