from telethon import TelegramClient, events
import random
import os

api_id = os.getenv('ID')
api_hash = os.getenv('HASH')


with TelegramClient('session_name', api_id, api_hash) as client:
    @client.on(events.NewMessage())
    async def handler(event):
        message = event.message.message
        if  'Блин' == message[:4]:
            if random.random() < 0.1:
                print('sent blin')
                await event.respond(file='blin.jpg')
            else:
                print('sent gosling')
                await event.respond(file='400.gif')
        elif 'блин' == message[:4].lower():
            if random.random() < 0.1:
                print('sent blin')
                await event.respond(file='blin.jpg')
            else:
                print('sent gosling')
                await event.respond(file='300.gif')
        elif 'капец' == message[:5].lower():
            await event.respond(file='kapets.gif')

    client.run_until_disconnected()
