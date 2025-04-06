from bot import Bot

import threading
import requests
import time
 
def keep_alive():
    while True:
        try:
            requests.get("https://famous-addi-moxibeatz21-7ed6f21b.koyeb.app/")
        except:
            pass
        time.sleep(90)  # Ping every 5 minutes
 
threading.Thread(target=keep_alive, daemon=True).start()



Bot().run()
