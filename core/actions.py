# Response actions

from datetime import datetime

def block_ip(ip):
    print(f"[ACTION] Blocking IP: {ip}")

def notify_soc(message):
    print(f"[ACTION] Notifying SOC: {message}")

def log_response(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("logs/response_log.txt", "a") as file:
        file.write(f"{timestamp} - {message}\n")
