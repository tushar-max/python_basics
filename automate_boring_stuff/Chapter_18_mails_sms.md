## Sending and Receiving Email with the Gmail API

You can find full details on EZGmail at https://github.com/asweigart/ezgmail/. EZGmail is not produced by or affiliated with Google; find the official Gmail API documentation at https://developers.google.com/gmail/api/v1/reference/.

To install EZGmail, run pip install --user --upgrade ezgmail on Windows 

## Enabling the Gmail API

Before you write code, you must first sign up for a Gmail email account at https://gmail.com/. Then, go to https://developers.google.com/gmail/api/quickstart/python/, click the Enable the Gmail API button on that page, and fill out the form that appears.

After you’ve filled out the form, the page will present a link to the credentials.json file, which you’ll need to download and place in the same folder as your .py file. The credentials.json file contains the Client ID and Client Secret information, which you should treat the same as your Gmail password and not share with anyone else.

Then, in the interactive shell, enter the following code:

    >>> import ezgmail, os
    >>> os.chdir(r'C:\path\to\credentials_json_file')
    >>> ezgmail.init()

Make sure you set your current working directory to the same folder that credentials.json is in and that you’re connected to the internet. The ezgmail.init() function will open your browser to a Google sign-in page. Enter your Gmail address and password. The page may warn you “This app isn’t verified,” but this is fine; click Advanced and then Go to Quickstart (unsafe). 

A token.json file will be generated to give your Python scripts access to the Gmail account you entered.

## Sending Mail from a Gmail Account

Once you have a token.json file, the EZGmail module should be able to send email with a single function call:

If you want to attach files to your email, you can provide an extra list argument to the send() function:

    >>> ezgmail.send('recipient@example.com', 'Subject line', 'Body of the email',
    ['attachment1.jpg', 'attachment2.mp3'])

Note that as part of its security and anti-spam features, Gmail might not send repeated emails with the exact same text (since these are likely spam) or emails that contain .exe or .zip file attachments (since they are likely viruses).

You can also supply the optional keyword arguments cc and bcc to send carbon copies and blind carbon copies:

    >>> import ezgmail
    >>> ezgmail.send('recipient@example.com', 'Subject line', 'Body of the email',
    cc='friend@example.com', bcc='otherfriend@example.com,someoneelse@example.com')

If you need to remember which Gmail address the token.json file is configured for, you can examine ezgmail.EMAIL_ADDRESS. Note that this variable is populated only after ezgmail.init()

## Searching Mail from a Gmail Account

Like unread() and recent(), the search() function returns a list of GmailThread objects. You can also pass any of the special search operators that you can enter into the search box to the search() function, such as the following:

* 'label:UNREAD' For unread emails
* 'from:al@inventwithpython.com' For emails from al@inventwithpython.com
* 'subject:hello' For emails with “hello” in the subject
* 'has:attachment' For emails with file attachments

You can view a full list of search operators at https://support.google.com/mail/answer/7190?hl=en/.

## Downloading Attachments from a Gmail Account

The GmailMessage objects have an attachments attribute that is a list of filenames for the message’s attached files. You can pass any of these names to a GmailMessage object’s downloadAttachment() method to download the files. You can also download all of them at once with downloadAllAttachments(). By default, EZGmail saves attachments to the current working directory, but you can pass an additional downloadFolder keyword argument to downloadAttachment() and downloadAllAttachments() as well

EZGmail contains additional features, and you can find the full documentation at https://github.com/asweigart/ezgmail/.

## SMTP

Much as HTTP is the protocol used by computers to send web pages across the internet, Simple Mail Transfer Protocol (SMTP) is the protocol used for sending email. SMTP dictates how email messages should be formatted, encrypted, and relayed between mail servers and all the other details that your computer handles after you click Send. You don’t need to know these technical details, though, because Python’s smtplib module simplifies them into a few functions.

SMTP just deals with sending emails to others. A different protocol, called IMAP, deals with retrieving emails sent to you and is described in “IMAP” on page 424.

In addition to SMTP and IMAP, most web-based email providers today have other security measures in place to protect against spam, phishing, and other malicious email usage. These measures prevent Python scripts from logging in to an email account with the smtplib and imapclient modules. However, many of these services have APIs and specific Python modules that allow scripts to access them. This chapter covers Gmail’s module

## Connecting to an SMTP Server

he domain name for the SMTP server will usually be the name of your email provider’s domain name, with smtp. in front of it. For example, Verizon’s SMTP server is at smtp.verizon.net.


|Provider|SMTP server domain name|
|---|---|
|Gmail*|smtp.gmail.com|
|Outlook.com/Hotmail.com*|smtp-mail.outlook.com|

Once you have the domain name and port information for your email provider, create an SMTP object by calling smptlib.SMTP(), passing the domain name as a string argument, and passing the port as an integer argument. The SMTP object represents a connection to an SMTP mail server and has methods for sending emails. For example, the following call creates an SMTP object for connecting to an imaginary email server:

    >>> smtpObj = smtplib.SMTP('smtp.example.com', 587)
    >>> type(smtpObj)
    <class 'smtplib.SMTP'>

Entering type(smtpObj) shows you that there’s an SMTP object stored in smtpObj. You’ll need this SMTP object in order to call the methods that log you in and send emails. If the smptlib.SMTP() call is not successful, your SMTP server might not support TLS on port 587. In this case, you will need to create an SMTP object using smtplib.SMTP_SSL() and port 465 instead.

    >>> smtpObj = smtplib.SMTP_SSL('smtp.example.com', 465)

## Sending the SMTP “Hello” Message

Once you have the SMTP object, call its oddly named ehlo() method to “say hello” to the SMTP email server. This greeting is the first step in SMTP and is important for establishing a connection to the server.

    >>> smtpObj.ehlo()
    (250, b'mx.example.com at your service, [216.172.148.131]\nSIZE 35882577\
    n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nCHUNKING')

## Starting TLS Encryption

If you are connecting to port 587 on the SMTP server (that is, you’re using TLS encryption), you’ll need to call the starttls() method next. This required step enables encryption for your connection. If you are connecting to port 465 (using SSL), then encryption is already set up, and you should skip this step.

Here’s an example of the starttls() method call:

    >>> smtpObj.starttls()
    (220, b'2.0.0 Ready to start TLS')

The starttls() method puts your SMTP connection in TLS mode. The 220 in the return value tells you that the server is ready.

Logging In to the SMTP Server
Once your encrypted connection to the SMTP server is set up, you can log in with your username (usually your email address) and email password by calling the login() method.

    >>> smtpObj.login('my_email_address@example.com', 'MY_SECRET_PASSWORD')
    (235, b'2.7.0 Accepted')

## Sending an Email

Once you are logged in to your email provider’s SMTP server, you can call the sendmail() method to actually send the email. The sendmail() method call looks like this:

    >>> smtpObj.sendmail('my_email_address@example.com
    ', 'recipient@example.com', 'Subject: So long.\nDear Alice, so long and thanks for all the fish.
    Sincerely, Bob')
    {}

The sendmail() method requires three arguments:

* Your email address as a string (for the email’s “from” address)
* The recipient’s email address as a string, or a list of strings for multiple recipients (for the “to” address)
* The email body as a string

## Disconnecting from the SMTP Server

Be sure to call the quit() method when you are done sending emails. This will disconnect your program from the SMTP server.

    >>> smtpObj.quit()
    (221, b'2.0.0 closing connection ko10sm23097611pbd.52 - gsmtp')

The 221 in the return value means the session is ending.


## IMAP

Just as SMTP is the protocol for sending email, the Internet Message Access Protocol (IMAP) specifies how to communicate with an email provider’s server to retrieve emails sent to your email address. Python comes with an imaplib module, but in fact the third-party imapclient module is easier to use. This chapter provides an introduction to using IMAPClient; the full documentation is at https://imapclient.readthedocs.io/.

The imapclient module downloads emails from an IMAP server in a rather complicated format. Most likely, you’ll want to convert them from this format into simple string values. The pyzmail module does the hard job of parsing these email messages for you. You can find the complete documentation for PyzMail at https://www.magiksys.net/pyzmail/.

Install imapclient and pyzmail from a Terminal window with pip install --user -U imapclient==2.1.0 and pip install --user -U pyzmail36== 1.0.4 on Windows 

## Connecting to an IMAP Server

Just like you needed an SMTP object to connect to an SMTP server and send email, you need an IMAPClient object to connect to an IMAP server and receive email. First you’ll need the domain name of your email provider’s IMAP server.

|Provider|IMAP server domain name|
|---|---|
|Gmail*|imap.gmail.com|
|Outlook.com/Hotmail.com*|imap-mail.outlook.com|

Most email providers require SSL encryption, so pass the ssl=True keyword argument. Enter the following into the interactive shell (using your provider’s domain name):

    >>> import imapclient
    >>> imapObj = imapclient.IMAPClient('imap.example.com', ssl=True)

## Logging In to the IMAP Server

Once you have an IMAPClient object, call its login() method, passing in the username (this is usually your email address) and password as strings.

    >>> imapObj.login('my_email_address@example.com', 'MY_SECRET_PASSWORD')
    'my_email_address@example.com Jane Doe authenticated (Success)'

## Selecting a Folder

Almost every account has an INBOX folder by default, but you can also get a list of folders by calling the IMAPClient object’s list_folders() method. This returns a list of tuples. Each tuple contains information about a single folder. Continue the interactive shell example by entering the following:

    >>> import pprint
    >>> pprint.pprint(imapObj.list_folders())
    [(('\\HasNoChildren',), '/', 'Drafts'),
    (('\\HasNoChildren',), '/', 'Filler'),
    ...

To select a folder to search through, pass the folder’s name as a string into the IMAPClient object’s select_folder() method.

    >>> imapObj.select_folder('INBOX', readonly=True)

## Performing the Search

With a folder selected, you can now search for emails with the IMAPClient object’s search() method. The argument to search() is a list of strings, each formatted to the IMAP’s search keys. 

Here are some example search() method calls along with their meanings:

* imapObj.search(['ALL']) Returns every message in the currently selected folder.
* imapObj.search(['ON 05-Jul-2019']) Returns every message sent on July 5, 2019.
* imapObj.search(['SINCE 01-Jan-2019', 'BEFORE 01-Feb-2019', 'UNSEEN']) Returns every message sent in January 2019 that is unread. (Note that this means on and after January 1 and up to but not including February 1.)
* imapObj.search(['SINCE 01-Jan-2019', 'FROM alice@example.com']) Returns every message from alice@example.com sent since the start of 2019.
* imapObj.search(['SINCE 01-Jan-2019', 'NOT FROM alice@example.com']) Returns every message sent from everyone except alice@example.com since the start of 2019.
* imapObj.search(['OR FROM alice@example.com FROM bob@example.com']) Returns every message ever sent from alice@example.com or bob@example.com.
* imapObj.search(['FROM alice@example.com', 'FROM bob@example.com']) Trick example! This search never returns any messages, because messages must match all search keywords. Since there can be only one “from” address, it is impossible for a message to be from both alice@example.com and bob@example.com.

        >>> UIDs = imapObj.search(['SINCE 05-Jul-2019'])    

## Size Limits

If your search matches a large number of email messages, Python might raise an exception that says imaplib.error: got more than 10000 bytes. When this happens, you will have to disconnect and reconnect to the IMAP server and try again.

This limit is in place to prevent your Python programs from eating up too much memory. Unfortunately, the default size limit is often too small. You can change this limit from 10,000 bytes to 10,000,000 bytes by running this code:

    >>> import imaplib
    >>> imaplib._MAXLINE = 10000000

## Fetching an Email and Marking It as Read

    >>> rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
    >>> import pprint
    >>> pprint.pprint(rawMessages)
    {40040: {'BODY[]': 'Delivered-To: my_email_address@example.com\r\n'
                    'Received: by 10.76.71.167 with SMTP id '
    --snip--
                    '\r\n'
                    '------=_Part_6000970_707736290.1404819487066--\r\n',
            'SEQ': 5430}}
            
## Getting Email Addresses from a Raw Message

    >>> import pyzmail
    >>> message = pyzmail.PyzMessage.factory(rawMessages[40041][b'BODY[]'])

    >>> message.get_subject()
    'Hello!'
    >>> message.get_addresses('from')
    [('Edward Snowden', 'esnowden@nsa.gov')]
    >>> message.get_addresses('to')
    [('Jane Doe', 'my_email_address@example.com')]
    >>> message.get_addresses('cc')
    []
    >>> message.get_addresses('bcc')
    []

## Deleting Emails

    ➊ >>> imapObj.select_folder('INBOX', readonly=False)
    ➋ >>> UIDs = imapObj.search(['ON 09-Jul-2019'])
    >>> UIDs
    [40066]
    >>> imapObj.delete_messages(UIDs)
    ➌ {40066: ('\\Seen', '\\Deleted')}
    >>> imapObj.expunge()
    ('Success', [(5452, 'EXISTS')])

## Disconnecting from the IMAP Server

When your program has finished retrieving or deleting emails, simply call the IMAPClient’s logout() method to disconnect from the IMAP server.

    >>> imapObj.logout()


## Sending Text Messages with Twilio

...

