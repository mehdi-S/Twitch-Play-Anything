#Define the imports
import twitch
import keypresser
import keyholder

t = twitch.Twitch();
k = keypresser.Keypresser();

#Enter your twitch username and oauth-key below, and the app connects to twitch with the details.
#Your oauth-key can be generated at http://twitchapps.com/tmi/
username = "anyUsername";
key = "oauth:XXX";
t.twitch_connect(username, key);

#The main loop
while True:
    #Check for new messages
    new_messages = t.twitch_recieve_messages();

    if not new_messages:
        #No new messages...
        continue
    else:
        for message in new_messages:
            #Wuhu we got a message. Let's extract some details from it
            msg = message['message'].lower()
            username = message['username'].lower()
            print(username + ": " + msg);

            #This is where you change the keys that shall be pressed and listened to.
            #The code below will simulate the key q if "q" is typed into twitch by someone
            #.. the same thing with "w"
            #Change this to make Twitch fit to your game!
            if msg == ">": keyholder.holdForSeconds('right_arrow', 2)
            if msg == "<": keyholder.holdForSeconds('left_arrow', 2)
            if msg == "enter": keyholder.holdForSeconds(msg, 2)
