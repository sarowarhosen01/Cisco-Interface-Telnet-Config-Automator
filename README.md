# Cisco Telnet Config Automator

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![asyncio](https://img.shields.io/badge/asyncio-enabled-green)
![Telnet](https://img.shields.io/badge/Telnet-Cisco-orange)

A simple asynchronous Python script to configure Cisco devices via Telnet using `telnetlib3`.

## 📋 Overview

This project automates the process of:
- Logging into a Cisco device (user + enable mode)
- Entering configuration mode
- Assigning an IP address to `FastEthernet0/1`
- Bringing up the interface (`no shutdown`)

Built with `asyncio` and `telnetlib3` for non-blocking I/O.

## ✨ Features

- Fully asynchronous (non-blocking)
- Automatic login + enable mode
- Configures interface IP and enables it
- Proper connection cleanup
- Basic error handling

## 🛠️ Requirements

- Python 3.8 or higher
- `telnetlib3` library

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/sarowarhosen01/Cisco-Interface-Telnet-Config-Automator.git
cd cisco-telnet-config

# Install dependencies
pip install telnetlib3
