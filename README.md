# Rumbler

This is an proof of concept experiment that ultimately attempts to use screen 
capture data to determine if you have taken damage while playing a game and 
trigger a chair shaker/transducer if so.

Currently, the plan is to get the software side working first, then send an api 
call to a hardware shaker/transducer device. Should this be successful, future 
iterations will attempt to create a well separated client-server model which 
allows for any type of physical device (or software) supporting the protocol to 
be triggered off of any supported in game event.

Since the software only uses what it sees on the screen it will have some 
distinct advantages and disadvantages. First, since it does not need to 
directly access or modify memory, it shouldn't violate any anti-cheat software 
or measures. This also means that any game ever made will technically be 
supported. Unfortunately this also means misdetections will likely be a big 
issue on games not specifically supported at least until a fairly large 
sampling of games become supported.

That said, these are only ideas and this is only a proof of concept. There is a 
much higher chance of failure or incompleteness than success.

To summarize, here are the goals:
 - Increase immersion
 - Use as an accessibility tool
 - Performant, minimal impact to system resources
 - Cross platform, eventually even supporting consoles
 - Loose coupling between client and server
 - Generic implementation/algorithm that supports any game
 - Support for multiple trigger types (i.e. damage taken, explosion nearby, 
   damage dealt, enemy killed, win, lose, etc)
 - Built on open standards
 - Extendable via anyone who wishes to make a hardware device supporting it

