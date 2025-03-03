# Telegram Credit Card Scraper

This is a Python script that uses the `Telethon` library to scrape messages from a specified Telegram channel or group and extract credit card information using a regex pattern. The script is designed to run asynchronously for efficiency and includes retry logic for handling potential network issues.

## Features

- **Asynchronous Processing**: Uses `asyncio` for efficient message processing.
- **Regex Pattern Matching**: Extracts credit card information with various separators.
- **Batch Processing**: Processes messages in batches to avoid rate limiting.
- **Retry Logic**: Implements retry logic for fetching messages in case of failures.
- **Output**: Saves extracted credit card information to a file (`cards.txt`).

## Prerequisites

Before running the script, ensure you have the following:

- Python 3.7 or higher installed.
- A Telegram API ID and hash. You can obtain these by creating an application on [my.telegram.org](https://my.telegram.org).
- A valid phone number associated with your Telegram account.
- The `Telethon` library installed.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Install the required dependencies**:
   ```bash
   pip install telethon
   ```

3. **Configure the script**:
   - Open the script and update the following variables with your credentials:
     ```python
     api_id = 'YOUR_API_ID'
     api_hash = 'YOUR_API_HASH'
     phone_number = 'YOUR_PHONE_NUMBER'
     channel_username = 'TARGET_CHANNEL_USERNAME'
     ```

## Usage

To run the script, simply execute the following command:

```bash
python script_name.py
```

Replace `script_name.py` with the actual name of your script file.

### Configuration Options

- **BATCH_SIZE**: Controls the number of messages fetched in each batch. Default is `100`.
- **channel_username**: The username of the Telegram channel or group you want to monitor.
- **Regex Pattern**: The script uses a predefined regex pattern to match credit card information. You can modify this pattern in the `card_pattern` variable if needed.

## Output

The script will save any extracted credit card information to a file named `cards.txt` in the same directory as the script. Each line in the file will contain a formatted credit card entry.

## Example

```plaintext
Found card: 4111111111111111|12|2023|123
Found card: 5111111111111111-01-2024-456
```

## Notes

- **Legal Considerations**: Ensure you have permission to scrape data from the target Telegram channel or group. Unauthorized scraping may violate Telegram's terms of service or local laws.
- **Rate Limiting**: The script includes a delay between batches to avoid being rate-limited by Telegram. Adjust the delay as necessary.
- **Error Handling**: The script includes basic error handling and retry logic. However, you may need to add additional error handling depending on your use case.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Please ensure your code follows the existing style and includes appropriate documentation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to customize this `README.md` to better fit your project's needs. If you have any questions or need further assistance, please don't hesitate to reach out!
