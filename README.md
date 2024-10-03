# Telegram Chat Backup Script

This Python script allows you to back up chats from Telegram, including messages, sender names, and phone numbers, using the **Telethon** library. The project also uses environment variables to securely store sensitive information like API keys and phone numbers.

## Features

- Export chat history (messages, dates, and sender information)
- Retrieve contacts and their phone numbers
- Use environment variables to keep sensitive data secure

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Python 3.x
- A Telegram account
- `pip` for installing Python packages

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/barbodimani81/telegram-export-app.git
   cd telegram-chat-backup
   
2. **Install the dependencies**
    ```bash
   pip install -r requirements.txt