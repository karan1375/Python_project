import time
from plyer import notification

def water_reminder():
    while True:
        notification.notify(
            title="water reminder for karan",
            message="Drink to sip some water",
            timeout=10
        )
        time.sleep(5)

water_reminder()
