from telethon.sync import TelegramClient
from telethon.tl.functions.contacts import GetContactsRequest
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Fetch sensitive information from environment variables
api_id = os.getenv('API_ID')  # Fetch API ID from the environment variable
api_hash = os.getenv('API_HASH')  # Fetch API Hash from the environment variable
phone = os.getenv('PHONE_NUMBER')  # Fetch Phone Number from the environment variable

# Initialize the Telegram client
client = TelegramClient('session_name', api_id, api_hash)


async def backup_chat(chat_name, file_name='chat_backup.txt'):
    # Connect to Telegram
    await client.start(phone=phone)

    # Search for the chat
    chat = await client.get_entity(chat_name)

    # Get messages from the chat
    async for message in client.iter_messages(chat):
        with open(file_name, 'a', encoding='utf-8') as f:
            # Write message sender's name and message content
            sender = await message.get_sender()
            sender_info = f'{sender.first_name} {sender.last_name} ({sender.phone})'
            f.write(f'{message.date} - {sender_info}: {message.text}\n')

    print(f'Backup of "{chat_name}" saved to {file_name}')


async def get_contacts():
    contacts = await client(GetContactsRequest(hash=0))
    for user in contacts.users:
        print(f'{user.first_name} {user.last_name} - {user.phone}')


# Run the backup
with client:
    client.loop.run_until_complete(backup_chat('CHAT_NAME_OR_USERNAME'))

    # Uncomment this if you also want to get the contact list and their phone numbers
    # client.loop.run_until_complete(get_contacts())
