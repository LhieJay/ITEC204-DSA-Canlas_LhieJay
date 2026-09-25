incidents = [
    {"id": "INC1392939", "bot": "BOT-Inventory", "description": "Failed to generate the daily report"},
    {"id": "INC1392940", "bot": "BOT-Email", "description": "Failed to send the scheduled notification"},
    {"id": "INC1392941", "bot": "BOT-DataSync", "description": "Encountered an error during data transfer"},
    {"id": "INC1392942", "bot": "BOT-Invoice", "description": "Failed to process an invoice"},
    {"id": "INC1392943", "bot": "BOT-Report", "description": "Failed to generate the weekly report"},
    {"id": "INC1392944", "bot": "BOT-FileTransfer", "description": "Failed to upload the required file"},
    {"id": "INC1392945", "bot": "BOT-DataEntry", "description": "Encountered an error while entering records"},
    {"id": "INC1392946", "bot": "BOT-Backup", "description": "Failed to complete the scheduled backup"},
    {"id": "INC1392947", "bot": "BOT-Validation", "description": "Failed to validate the submitted records"},
    {"id": "INC1392948", "bot": "BOT-Notification", "description": "Failed to send the system alert"}
]


def add_incident():
    incident_id = input("Enter Incident ID: ")
    bot = input("Enter Bot: ")
    description = input("Enter Short Description: ")

    incidents.append({
        "id": incident_id,
        "bot": bot,
        "description": description
    })

    print("Incident ticket added successfully.")


def display_incidents():
    if not incidents:
        print("No active incidents.")
        return

    print("\n--- ACTIVE INCIDENT TICKETS ---")

    for incident in incidents:
        print(f"ID: {incident['id']}")
        print(f"Bot: {incident['bot']}")
        print(f"Description: {incident['description']}")
        print("-" * 45)


def search_incident():
    search_id = input("Enter Incident ID to search: ")

    for incident in incidents:
        if incident["id"] == search_id:
            print("\nIncident Found!")
            print(f"ID: {incident['id']}")
            print(f"Bot: {incident['bot']}")
            print(f"Description: {incident['description']}")
            return

    print("Incident not found.")


def remove_incident():
    remove_id = input("Enter Incident ID to remove: ")

    for incident in incidents:
        if incident["id"] == remove_id:
            incidents.remove(incident)
            print("Resolved incident removed successfully.")
            return

    print("Incident not found.")


def count_incidents():
    print(f"Active Incidents: {len(incidents)}")


while True:
    print("\n===== IT AUTOMATION INCIDENT TICKET MANAGER =====")
    print("1. Add Incident")
    print("2. Display Incidents")
    print("3. Search Incident")
    print("4. Remove Resolved Incident")
    print("5. Count Active Incidents")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_incident()
    elif choice == "2":
        display_incidents()
    elif choice == "3":
        search_incident()
    elif choice == "4":
        remove_incident()
    elif choice == "5":
        count_incidents()
    elif choice == "6":
        print("Program ended.")
        break
    else:
        print("Invalid choice. Please try again.")
