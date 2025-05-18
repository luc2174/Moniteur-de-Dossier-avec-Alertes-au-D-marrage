import os
import time
import requests
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WEBHOOK_URL = "https://discord.com/api/webhooks/TON_WEBHOOK_ID/TON_TOKEN"
WATCHED_FOLDER = r"C:\Your_Path"

# Envoie un message sur Discord
def send_discord_alert(message):
    try:
        requests.post(WEBHOOK_URL, json={"content": message})
    except Exception as e:
        print("Erreur Discord:", e)

# Surveillance du dossier
class FolderMonitor(FileSystemEventHandler):
    def on_any_event(self, event):
        action = "modifié" if event.event_type == "modified" else \
                 "créé" if event.event_type == "created" else \
                 "supprimé" if event.event_type == "deleted" else "autre"
        send_discord_alert(f"📁 Fichier {action} : `{event.src_path}`")

def main():
    # Alerte de démarrage
    pc_name = os.getenv("COMPUTERNAME")
    user = os.getlogin()
    send_discord_alert(f"🖥️ PC démarré : `{pc_name}` - utilisateur : `{user}`")

    # Démarre l’observateur
    observer = Observer()
    observer.schedule(FolderMonitor(), WATCHED_FOLDER, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
