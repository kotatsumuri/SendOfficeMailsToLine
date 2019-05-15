from O365 import Account
import O365
from bs4 import BeautifulSoup
import time
from datetime import datetime
import calendar

from sendToLine import sendToLine

from info import getCredentials,getClassName

credentials = getCredentials()
account = Account(credentials)

className = getClassName()

mailbox = account.mailbox()
inbox = mailbox.inbox_folder()


while True:

    now = time.time()
    mailbox = account.mailbox()
    inbox = mailbox.inbox_folder()

    for message in inbox.get_messages(limit = 10):

        timeStamp = float(message.sent.strftime('%s'))

        
        if (now - timeStamp)/60 > 5:
            break
        
        fromName = None
        title = None
        body = None
        hasAttachments = False


        for to in message.to:
            #print(to)
            if className == str(to):

                fromName = str(message.sender)
                title = message.subject

                #print(message.body)
                text = BeautifulSoup(message.body,"html.parser")
                print(text.get_text())
                body = text.get_text()

                if message.has_attachments > 0:
                    hasAttachments = True
                
                sendToLine(fromName,title,body,hasAttachments)

                break         
                
        '''
        message.attachments.download_attachments()
        for attachment in message.attachments:
            attachment.save()
        '''

    time.sleep(5*60000)