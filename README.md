# TelegramRoseBotAutoBlocklist
This piece of code helps you create blocklists for groups for @MissRose_bot using Telegram API.

The program simply connects to Telegram API by Telethon, gets a list of banned words or sentences (each sentence/word in a new line), creates and sends commands to Rose Bot. At the end of execution, Rose will save all lines in the file as blocklisted words.



To use the code, replace api_id, api_hash, phone and fileName variables with your values. To get first three, visit my.telegram.org. Be sure you have a file containing desired blocklist filters seperated with newlines and it contains at most 200 lines. If it contains more lines, they will be sent to bot, however it won't be saved to bot due to the its 200 blocklist filter limitation. 

Later, use /connect command to use the blocklist commands in PM instead of group.

Lastly, run the code and wait for it to end. It takes a long time then expected because due to message limitations of the bot, delays are used. In total, 200 second of extra time is used.



After the execution ends, use /blocklist command on @MissRose_bot to check if everything is correct or not. 
