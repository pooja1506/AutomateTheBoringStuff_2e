#Enabling API
import ezgmail, os
os.chdir(r'C:\path\to\credentials_json_file')
ezgmail.init()

#sending mail
ezgmail.send('recipient@example.com', 'Subject line', 'Body of the email',['attachment1.jpg', 'attachment2.mp3'])

ezgmail.send('recipient@example.com', 'Subject line', 'Body of the email',cc='friend@example.com', bcc='otherfriend@example.com,someoneelse@example.com')

#To check configuration
ezgmail.EMAIL_ADDRESS

#To read email
unreadThreads = ezgmail.unread() # List of GmailThread objects.
ezgmail.summary(unreadThreads)

len(unreadThreads)
str(unreadThreads[0])
len(unreadThreads[0].messages)
str(unreadThreads[0].messages[0])
unreadThreads[0].messages[0].subject
unreadThreads[0].messages[0].body
unreadThreads[0].messages[0].timestamp
unreadThreads[0].messages[0].sender
unreadThreads[0].messages[0].recipient