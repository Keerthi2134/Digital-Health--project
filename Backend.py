import sqlite3
import schedule
import time
from datetime import datetime
from plyer import notification

# Connect to SQLite database
conn = sqlite3.connect('medication_tracker.db')
cursor = conn.cursor()

def send_reminder(med_name, dosage):
    notification.notify(
        title="Medication Reminder",
        message=f"Time to take your {med_name}, Dosage: {dosage}",
        timeout=10
    )

def check_reminders():
    cursor.execute("SELECT * FROM medications")
    rows = cursor.fetchall()
    for row in rows:
        schedule_time = row[3]
        current_time = datetime.now().strftime("%H:%M")
        if schedule_time == current_time:
            send_reminder(row[1], row[2])

# Schedule the reminder check every minute
schedule.every(1).minutes.do(check_reminders)

while True:
    schedule.run_pending()
    time.sleep(1)
