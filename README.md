"# Telegram Dungeons and Dragons Helper" 

notes;

1. Add a default keyboard for removing and displaying items 
    and replace the keyboard and /remove displays your items 
    read to be removed.    

3. Is it possible to remove the keyboard
    if there are no items left to delete?
4. Delete commands so they don't show up in chat
Add a delay to deleted items - make sure the person can see 
what just happened in the chat, then delete. 

Delete all commands. 

5. Once this is all done try and run some natural language processing. 
Unsure of what the aim might be for that but it would be cool. 
That can be tomorrow's task. 

6. NLP on chat. Originally it was to parse messages
and if the players were rewarded after a kill the items
would be added to the inventory. I'm unsure of the future of chat D&D
but I think there is a place for NLP in the chats.

I could plot graphs based on the length of messages, or analyse the sentiment 
on a day to day basis. I could analyse the average lengths of each person's messages.

I could make summaries of the messages I've missed so I don't have to read through them all. 
Now, that would be really good. A group chat summarizer bot. 

I could try sentiment analysis per text to begin with, just as an exercise. 
Grab each message using the bot and run sentiment analysis and hope for the best. 

You are nobody until you get something done. Show someone the results. 
Messages contain information. If you group messages by the individual you lose the meaning from the group. 
You gain other information but lose the essence. What am I even saying? God. A whole bunch of nothing. 

Anyway, start with grouping messages by the individual. Parse through the HTML. 

Encoding troubles. 
codec can't encode character '\u010e'

# START HERE
First things first, 

# some messages are grouped together, so assume user has not changed unless otherwise started
# iterate linearly

# we want to get each message tagged by "message"
div class = 'message' id = message* 'title'

# date tagged by "title" in class 'date details'
div class = 'date details'

# name of user
div class = 'from_name'

# message by user
div class = 'text'


Python is simple. The syntax is easy to understand. 
But things don't want to work. I'm trying to read in an html file. It doesn't work. 
I try a couple of methods. Doesn't work. 
It's been hours. Still not working. What shit. 
Slow progress but I cannot stop.  

# soup.find_all
# soup.find('text')


