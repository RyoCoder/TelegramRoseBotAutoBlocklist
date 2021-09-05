from telethon import TelegramClient
import time

# User specific values.
# 
# You can get those three from my.telegram.org!
api_id = 1111111
api_hash = 'API_HASH'
phone = '+111111111111'

# Path to your word list
fileName = 'filename.txt'

client = TelegramClient(phone, api_id, api_hash)

async def sendMessage(user, message):
    await client.send_message(user, message)

with client:
    roseUsername = '@MissRose_bot'
    
    file = open(fileName, 'r')
    
    cnt = 0
    
    for line in file.readlines():
        command = "/addblocklist \"" + line.strip() + "\"" 
        
        print(command) 
        client.loop.run_until_complete(sendMessage(roseUsername, command))
        cnt += 1
        
        if cnt % 20 == 0:
            print("Waiting")
            time.sleep(10)
