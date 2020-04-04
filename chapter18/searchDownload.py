#Search 
import ezgmail
resultThreads = ezgmail.search('RoboCop')
len(resultThreads)
ezgmail.summary(resultThreads)

#Download
import ezgmail
threads = ezgmail.search('vacation photos')
threads[0].messages[0].attachments
threads[0].messages[0].downloadAttachment('tulips.jpg')
threads[0].messages[0].downloadAllAttachments(downloadFolder='vacation2019')