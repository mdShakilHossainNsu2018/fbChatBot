from fbchat import Client
from fbchat.models import *
client = Client('shakilesemail@gmail.com', 'shakilnsu2018')
import time

if not client.isLoggedIn():
    client.login('shakilesemail@gmail.com', 'shakilnsu2018')
#
# print('Own id: {}'.format(client.uid))
# client.send(Message(text='valo tui?'), thread_id='100007826251418', thread_type=ThreadType.USER)

# users = client.searchForUsers('MD Musa Islam')
# user = users[0]
# print("User's ID: {}".format(user.uid))
# print("User's name: {}".format(user.name))
# print("User's profile picture url: {}".format(user.photo))
# print("User's main url: {}".format(user.url))

# client.send(Message(text='<message>'), thread_id='<group id>', thread_type=ThreadType.GROUP)
# client.logout();

# Fetches a list of the 20 top threads you're currently chatting with

threads = client.fetchThreadList()
print("Threads: {}".format(client.fetchUnread()[0]))

# client.listen()



#!/usr/local/bin/python

from fbchat import Client

EMAIL = 'shakilesemail@gmail.com'
PASSWORD = 'shakilnsu2018'

class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(author_id, thread_id)
        self.markAsRead(author_id)
        print(message_object)

        # don't reply on our own messages
        if author_id != self.uid:
            self.send(Message('fjkdalhflak'), thread_id=thread_id, thread_type=thread_type)

client = EchoBot(EMAIL, PASSWORD)
client.listen()
#
# while True:
#     time.sleep(1.5)
#     # print(client.fetchUnseen().count(0))
#     # print(client.listen())
#     print(client.onMessage())
#     # if len(client.fetchUnseen()) == 0:
#     #     print('not ')
#     # else:
#     #     print("Threads: {}".format(client.fetchUserInfo(client.fetchUnseen()[0])))
