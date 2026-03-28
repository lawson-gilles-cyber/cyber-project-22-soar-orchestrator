# Playbook execution

from core.actions import block_ip, notify_soc, log_response

def execute_playbook(alert):

    # Brute force playbook
    if "Brute force" in alert:
        block_ip("45.33.32.1")
        notify_soc(alert)
        log_response("Brute force handled")

    # Data access playbook
    elif "Sensitive data" in alert:
        notify_soc(alert)
        log_response("Data access monitored")

    else:
        log_response("No action required")
