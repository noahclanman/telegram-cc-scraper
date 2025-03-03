import re
import asyncio
from telethon import TelegramClient, events

# Configuration
api_id = xxx
api_hash = 'xxx'
phone_number = 'xxx'
channel_username = 'xxx'  # Channel/group to monitor

# Configuration for scraping
BATCH_SIZE = 100

# Regex pattern for credit cards with various separators
card_pattern = re.compile(
    r'(?:\b|^)([345]\d{2,3}(?:\d{11,13}))\s*([:|/|\\|,|\||-]?)\s*(\d{1,2})\2\s*(\d{2,4})\2\s*(\d{3,4})(?:\b|$)',
    re.MULTILINE
)

async def process_message(message):
    matches = card_pattern.findall(message)
    
    for match in matches:
        card_number = match[0]
        separator = match[1]
        month = match[2]
        year = match[3]
        cvv = match[4]
        
        # Validate card length based on type
        if card_number.startswith('3') and len(card_number) != 15:
            continue
        if card_number.startswith(('4', '5')) and len(card_number) != 16:
            continue
        
        # Format the card information
        formatted_card = f"{card_number}{separator}{month}{separator}{year}{separator}{cvv}"
        
        # Save results
        with open('cards.txt', 'a') as f:
            f.write(f"{formatted_card}\n")
        print(f"Found card: {formatted_card}")

async def get_channel_messages(client, channel, offset_id=0, retry_count=3):
    """Get messages from channel with retry logic"""
    for attempt in range(retry_count):
        try:
            messages = await client.get_messages(channel, limit=BATCH_SIZE, offset_id=offset_id)
            return messages
        except Exception as e:
            if attempt == retry_count - 1:
                print(f"Failed to get messages after {retry_count} attempts: {str(e)}")
                return None
            print(f"Attempt {attempt + 1} failed, retrying in 5 seconds...")
            await asyncio.sleep(5)

async def main():
    client = TelegramClient('session_name', api_id, api_hash)
    await client.start(phone_number)
    
    print("Starting message scraping...")
    
    try:
        print("Getting channel information...")
        channel = await client.get_entity(channel_username)
        print(f"Successfully connected to channel: {channel.title}")
        
        offset_id = 0
        total_processed = 0
        
        while True:
            print(f"\nFetching messages from offset {offset_id}...")
            messages = await get_channel_messages(client, channel, offset_id)
            
            if not messages:
                break
            
            print(f"Processing batch of {len(messages)} messages...")
            for message in messages:
                if message.text:
                    await process_message(message.text)
                total_processed += 1
                
            if len(messages) < BATCH_SIZE:
                break
                
            offset_id = messages[-1].id
            print(f"Total messages processed: {total_processed}")
            
            # Add delay between batches to avoid rate limiting
            await asyncio.sleep(2)
    
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        
    finally:
        print(f"\nFinished processing. Total messages processed: {total_processed}")
        await client.disconnect()

if __name__ == '__main__':
    asyncio.run(main())
