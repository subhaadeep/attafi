# Attafi - Wi-Fi Attack Automation Toolkit 🚀

Attafi is a Python-based script designed to automate common Wi-Fi attack steps using the aircrack-ng toolkit. It simplifies tasks like monitor mode switching, scanning networks, capturing WPA handshakes, performing deauthentication attacks, and password cracking using rockyou.txt.

> **Note**: This is not a standalone hacking tool. Attafi leverages existing tools (like `airodump-ng`, `aireplay-ng`, and `aircrack-ng`) via subprocess automation and does not perform low-level packet processing or injection natively.

![attafi](https://github.com/subhaadeep/share/blob/main/attafi.png)

> ⚡ Built for **ethical hacking** and **educational purposes only**.

---

## 🧪 Features

* Automatically sets your adapter to monitor mode
* Scan for access points and connected clients
* Scans and lists available Wi-Fi networks
* Select target BSSID and client
* Launches deauthentication and handshake capture attacks in parallel
* Attempts WPA/WPA2 cracking using `aircrack-ng` with `rockyou.txt`
* User-friendly CLI prompts

---

## 🧪 How to Use

### 1. Clone this repository

```bash
git clone https://github.com/subhaadeep/attafi
cd attafi
git clone https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
```

### 2. Setup

Make sure `rockyou.txt` is in the same directory as the script. If not, modify the path in the Python script.

### 3. Run the Script

```bash
sudo attafi.py
```

### 4. Follow the Prompts

* Enter your Wi-Fi interface (e.g., wlan0)
* The script sets it to monitor mode
* Scans nearby networks for 15 seconds
* Enter BSSID, channel number, and a filename
* Tool starts both `airodump-ng` and `aireplay-ng` in parallel
* Press `Ctrl+C` after handshake is captured
* Script runs `aircrack-ng` to attempt cracking the password


---

#

---

## 🧠 License



This project is **not licensed for commercial use**. Use it **responsibly** and **ethically**.

---

## 💡 Notes

* Place `rockyou.txt` inside the same folder or update the path in the script.
* You can change scan time by editing the `scan_networks()` function.
* The tool works best when the target network has active connected clients.
* Cracking speed and success depend on password strength and dictionary used.

### **🔑 Wordlist Requirement**

This tool uses the popular \`\` wordlist for password cracking. It is **not included in this repository** due to its large size.

You can find it in Kali Linux at:

```bash

/usr/share/wordlists/rockyou.txt.gz
```


To use it:

1. Decompress the file:

```bash

gunzip /usr/share/wordlists/rockyou.txt.gz
```

2. Then copy it to your project directory:

```bash

cp /usr/share/wordlists/rockyou.txt /path/to/attafi/
```


Or download from a public mirror and then move it to your project directory:

📥 [Download rockyou.txt from GitHub (SecLists)](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Leaked-Databases/rockyou.txt.tar.gz)

---

Happy Hacking! 🚀


---

## 🚫 Disclaimer

This projct is for **educational use only**. Unauthorized access to networks is **illegal and unethical**.
Always use with explicit **permission**.

---

## ⭐ Contribute

Pull requests, suggestions, and improvements are welcome. Please ensure your changes are clean and comply with ethical hacking guidelines.

---

## 📬 Contact

* GitHub: [subhaadeep](https://github.com/subhaadeep)
* Repo: [Attafi](https://github.com/subhaadeep/attafi)

---

## 🧠 License

This project is **not licensed for commercial use**. Use it **responsibly** and **ethically**.

---

☕ Buy Me a Coffee

If you find Attafi helpful or interesting, consider supporting my work with a coffee: https://coff.ee/subhaadeep

Your support helps me maintain and improve open-source projects like this. Thank you! 🙌

---

Happy Hacking! 🚀
