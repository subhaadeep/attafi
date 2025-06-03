# Attafi - Wi-Fi Attack Automation Toolkit 🚀

Attafi is an automated Wi-Fi penetration testing toolkit that simplifies the process of scanning networks, capturing handshakes, and attempting WPA/WPA2 password cracking using dictionary attacks.

![attafi](https://github.com/subhaadeep/share/blob/main/attafi.png)

> ⚡ Built for **ethical hacking** and **educational purposes only**.

---

## 🧪 Features

* Automatically sets your adapter to monitor mode
* Scans and lists available Wi-Fi networks
* Launches deauthentication and handshake capture attacks in parallel
* Attempts WPA/WPA2 cracking using `aircrack-ng` with `rockyou.txt`

---

## 🧪 How to Use

### 1. Clone this repository

```bash
git clone https://github.com/subhaadeep/attafi
cd attafi
```

### 2. Setup

Make sure `rockyou.txt` is in the same directory as the script. If not, modify the path in the Python script.

### 3. Run the Script

```bash
sudo python3 wifi_attack_launcher.py
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

## 💡 Notes

* Place `rockyou.txt` inside the same folder or update the path in the script.
* You can change scan time by editing the `scan_networks()` function.
* The tool works best when the target network has active connected clients.
* Cracking speed and success depend on password strength and dictionary used.

---

## 🚫 Disclaimer

This tool is for **educational use only**. Unauthorized access to networks is **illegal and unethical**.
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
