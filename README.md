# TikTok View and Share Bot

A Python tool designed to simulate engagement on TikTok videos by sending view and share requests to the TikTok API.

## Features

- Generate artificial views and shares for TikTok videos
- Customizable thread count for parallel processing
- Support for HTTP, SOCKS4, and SOCKS5 proxies
- Real-time statistics display
- Random user agent and device simulation for more realistic requests

## Requirements

- Python 3.6+
- Required Python packages:
  - requests
  - pystyle
  - urllib3
  - queue
  - threading

## Installation

1. Download Repo to Your Computer

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Add proxies to the `proxies.txt` file (one proxy per line) in the format:
```
ip:port
```

##  Usage

1. Run the script:
```bash
python main.py
```

2. Follow the prompts to enter:
   - TikTok video link
   - Number of requests to send (0 for infinite)
   - Number of threads to use
   - Type of engagement (views or shares)
   - Proxy type (HTTP, SOCKS4, SOCKS5)

3. Monitor the progress in the console

## ⚙️ Configuration

You can modify the following files to customize the bot:
- `.\Data/UserAgent.py`: Add or remove user agents
- `.\Data/Lists.py`: Modify device types, platforms, and API domains

## Disclaimer

This tool is created for **educational purposes only**. Using this bot may violate TikTok's Terms of Service and could result in account restrictions or bans. The author takes no responsibility for any misuse of this software or any consequences that may arise from using it.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.


**⭐ Star this repository if you find it useful!**







