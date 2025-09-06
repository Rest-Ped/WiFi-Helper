# 🌐 WiFi-Helper

**A powerful Linux tool for WiFi network analysis and security assessment**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Linux-lightgrey?logo=linux)](https://linux.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active%20Development-orange)](https://github.com/yourusername/wifi-helper)

## 🚀 Features

### 🔍 Network Intelligence
- **IP & Port Discovery** - Get your external IP and local port information
- **Network Type Detection** - Automatic detection of WiFi, Ethernet, or VPN connections
- **Traffic Analysis** - Monitor network traffic for suspicious activity

### 🛡️ Security Monitoring
- **ARP Monitoring** - Detect ARP spoofing and network anomalies
- **DNS Security Check** - Verify DNS resolution and detect poisoning attempts
- **Port Monitoring** - Identify unexpected open ports and services
- **Traffic Analysis** - Monitor bandwidth usage for unusual patterns

### ⚡ Quick Start

# Clone the repository
```bash
git clone https://github.com/yourusername/wifi-helper.git
```

# Navigate to directory
```bash
cd wifi-helper
```

# Install dependencies
```bash
pip install -r requirements.txt
```

# Run the tool
```bash
python3 wifi_helper.py
```

### 📦 Installation

# Ensure Python 3.8+ is installed
```bash
python3 --version
```

# Install system dependencies
```bash
sudo apt update
sudo apt install python3-pip python3-venv wireless-tools
```

# Installation Methods
# Method 1: Direct install
```bash
pip install git+https://github.com/yourusername/wifi-helper.git
```
# Method 2: From source
```bash
git clone https://github.com/yourusername/wifi-helper.git
cd wifi-helper
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 🎯 Usage
### Basic Usage

# Start the interactive menu
```bash
python3 wifi_helper.py
```

# Or run specific modules
```bash
python3 wifi_helper.py --scan
python3 wifi_helper.py --monitor
```
### Command Line Options

# Display help
```bash
python3 wifi_helper.py --help
```

# Network information
```bash
python3 wifi_helper.py --info
```

# Security scan
```bash
python3 wifi_helper.py --security-scan
```

# Continuous monitoring
```bash
python3 wifi_helper.py --monitor --timeout 300
```
