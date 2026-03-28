# Orchestrator logic

from core.playbooks import execute_playbook

def handle_alert(alert):

    print(f"[SOAR] Processing alert: {alert}")

    # Select playbook based on alert type
    execute_playbook(alert)
