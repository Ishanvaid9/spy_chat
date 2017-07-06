from datetime import datetime

#creating class for spy data

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

#creating class for conversation between spy

class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

#default spy

spy = Spy('ishan', 'Mr.', 21, 4.0)

#defalt friend 

friend_one = Spy('sant', 'Mr.', 20, 4.9)
friend_two = Spy('paramjeet', 'Ms.', 21, 4.3)

friends = [friend_one, friend_two]

