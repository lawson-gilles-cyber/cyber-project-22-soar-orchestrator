# SOAR Orchestrator

from core.orchestrator import handle_alert

# Load alerts
with open("data/alerts.txt", "r") as file:
    alerts = file.readlines()

print("=== SOAR RESPONSE ENGINE ===\n")

# Process each alert
for alert in alerts:
    alert = alert.strip()
    handle_alert(alert)
