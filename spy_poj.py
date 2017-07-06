from spy_det import spy, Spy, ChatMessage, friends
from steganography.steganography import Steganography
from datetime import datetime
from termcolor import colored



print colored("WELCOME CANDIDATE",'blue',attrs=['underline'])
spy_name=raw_input("enter your name ")
print colored('you enter name=%s',"red",'on_white')%(spy_name)
length=len(spy_name)
if spy_name.isalpha():
 print 'length of name ='+\
      str(length)
 if length==0:
    print spy_name
    print "empty"
    exit()
 else :
    print "what should we call you!!"
    gen=(raw_input("1 for Male or 2 For female"))
    if gen.isdigit():
       gen=int(gen)
       if gen==1 :
         print colored("Hello Mr." +  spy_name.upper() +" READY TO GO ",'cyan','on_grey')
       elif gen==2 :
           print colored(" welcome Mrs "+spy_name.upper() + " everything is ready to go ",'magenta','on_white')
       else:
        print 'wrong choise'
        exit()
    else:
        print "enter appropaite number"
        exit()
else:
    print colored("WARNING!!!!!! ENTER ALPHABETS",'red')
    exit()
spy_status=False
#spy age
spy_age=(raw_input("enter  age="))
if spy_age.isdigit():
   print spy_name.upper() +" age "\
      +str(spy_age)
else:
    print'wrong choice'
    exit()
# spy rating
spy_rating=(raw_input("enter the rating of "+colored(spy_name.upper(),"blue") + " from 1 to 5 "))
if len(spy_rating)<1:
    print "enter rating from 1-5"
else:
 spy_rating=int(spy_rating)

if spy_rating==1 and spy_rating<2:
    print spy_name +" Need to improve its skills"
elif spy_rating==2 and spy_rating<3:
    print spy_name+" good for handling equipments"
elif spy_rating==3 and spy_rating<4:
    print spy_name+" Always ready for battel"
elif spy_rating==4 and spy_rating<=5:
    print " Perfect SPY "
else:
    print " Out of range ","RE-ENTER THE DATA"
    exit()
spy_status=True
print " Welcome to SPY ACADMEY "+ spy_name.upper()+ " REGISTER SUCESSFULLY "+" RECORD FOUND " \
      +str(spy_name.upper())+" age "\
      +str(spy_age) +" RATING  "\
      +str(spy_rating)

question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
existing = raw_input(question)

STATUS_MESSAGES = ['Avaliable', 'False Alarm']

def add_status():

    updated_status_message = None

    if spy.current_status_message != None:

        print 'Current status message is %s \n' % (spy.current_status_message)
    else:
        print 'Don\'t have any status message yet \n'

    default = raw_input("Want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = raw_input("What message do you want to set? ")


        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nSelect from the above messages "))


        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print 'invalid option!! Enter y or n'

    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'NO status update'

    return updated_status_message


def add_friend():

    new_friend = Spy('','',0,0.0)

    new_friend.name = raw_input("add your friend's name: ")
    new_friend.salutation = raw_input(" Mr. or Ms.?: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        print 'Invalid entry.'

    return len(friends)


def select_a_friend():
    item_number = 0

    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation, friend.name,
                                                   friend.age,
                                                   friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position


def send_message():

    friend_choice = select_a_friend()

    original_image = raw_input("What is the name of the image?")
    output_path = "output.jpg"
    text = raw_input("What do you want to say? ")
    Steganography.encode(original_image, output_path, text)

    new_chat = ChatMessage(text,True)

    friends[friend_choice].chats.append(new_chat)

    print "Your secret message image is ready!"


def read_message():

    sender = select_a_friend()

    output_path = raw_input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)

    new_chat = ChatMessage(secret_text,False)

    friends[sender].chats.append(new_chat)

    print "Your secret message has been saved!"


def read_chat_history():

    read_for = select_a_friend()

    print '\n'

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print '[%s] %s: %s' % (colored(chat.time.strftime("%d %B %Y"),'blue'), 'You said:', chat.message)
        else:
            print '[%s] %s said: %s' % (colored(chat.time.strftime("%d %B %Y"),'blue'), colored(friends[read_for].name,'red'), chat.message)


def start_chat(spy):

    spy.name = spy.salutation + " " + spy.name


    if spy.age > 12 and spy.age < 50:


        print "Authentication complete. Welcome " + colored(spy.name,'blue') + " age: " \
              + colored(str(spy.age),"red") + " and rating of: " + colored(str(spy.rating),'blue') + " Good to see you"

        show_menu = True

        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n\n"
            menu_choice = raw_input(menu_choices)
            if menu_choice.isdigit():

             if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                else:
                    show_menu = False
            else:
                print  ' WRONG MENU CHOICE!!!' \
                       'SELECT AGAIN'

                show_menu
    else:
        print 'Age not perfect'

if (existing.upper() == "Y") & (existing.isalpha()):
    start_chat(spy)

elif(existing.upper() == "N") & (existing.isalpha()):

    spy = Spy('','',0,0.0)


    spy.name = raw_input("Welcome to spy chat, enter your spy name first: ")

    if len(spy.name) > 0:
        spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")

        spy.age = raw_input(" your age?")
        if len(spy.age)<0:
            print 'Fill the proper age'
            exit()
        else:
         spy.age = int(spy.age)

        spy.rating = raw_input("spy rating?")
        spy.rating = float(spy.rating)

        start_chat(spy)
    else:
        print 'Please add a valid spy name'
else:
    print "wrong input"
