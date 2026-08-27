import time
from plyer import notification

# creat a function for the water reminder 
def water_reminder():
    while True: # Keep running the reminder continuously 
        notification.notify(
            title="water reminder for karan",
            message="Drink to sip some water",
            timeout=10
        )
        time.sleep(5) # Wait for 5 seconds before showing the notification again 
    

water_reminder()
