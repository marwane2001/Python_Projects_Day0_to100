import tkinter as tk
import time
from plyer import notification

class AlarmClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")

        self.alarm_time = ""
        self.alarm_set = False
        self.alarm_active = False

        
        self.time_label = tk.Label(self.root, text="", font=("Helvetica", 48))
        self.time_label.pack(pady=20)

        
        self.entry_label = tk.Label(self.root, text="Set Alarm (HH:MM):", font=("Helvetica", 14))
        self.entry_label.pack()
        self.entry = tk.Entry(self.root, font=("Helvetica", 14))
        self.entry.pack()

        
        self.set_button = tk.Button(self.root, text="Set Alarm", command=self.set_alarm)
        self.set_button.pack(pady=10)

        self.stop_button = tk.Button(self.root, text="Stop Alarm", command=self.stop_alarm, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        self.snooze_button = tk.Button(self.root, text="Snooze", command=self.snooze_alarm, state=tk.DISABLED)
        self.snooze_button.pack(pady=10)

        
        self.update_time()

    def update_time(self):
        current_time = time.strftime("%H:%M:%S")
        self.time_label.config(text=current_time)
        self.root.after(1000, self.update_time)  

         
        if self.alarm_active and time.strftime("%H:%M") == self.alarm_time:
            self.alarm_active = False
            self.activate_alarm()

    def set_alarm(self):
        self.alarm_time = self.entry.get().strip()
        self.entry.delete(0, tk.END)
        self.alarm_set = True
        self.set_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

    def stop_alarm(self):
        self.alarm_set = False
        self.stop_button.config(state=tk.DISABLED)
        self.snooze_button.config(state=tk.DISABLED)

    def snooze_alarm(self):
        self.stop_alarm()
        time.sleep(300)  # Snooze for 5 minutes 
        if self.alarm_set:
            self.activate_alarm()

    def activate_alarm(self):
        notification_title = "Alarm!"
        notification_message = "Wake up!"
        notification.notify(
            title=notification_title,
            message=notification_message,
            app_name="Alarm Clock",
            timeout=10  # Notification 
        )
        self.snooze_button.config(state=tk.NORMAL)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmClockApp(root)
    app.run()
