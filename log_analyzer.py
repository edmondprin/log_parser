class LogEntry(): # Represents one log line, validates level
    def __init__(self, date, time, level, message):
        self.date = date
        self.time = time
        self.level = level
        self.message = message

    @property
    def level(self):
        return self._level
    
    @level.setter
    def level(self, value):
        valid = ["INFO", "WARNING", "ERROR"]
        if value.strip().upper() not in valid:
            print("Not acceptable. Defaulting to 'INFO'")
            self._level = "INFO"
        else:
            self._level = value

    def __str__(self):
        return f"{self.date}, {self.time}: {self.message} | {self.level}"

    def is_error(self):
        return self.level == "ERROR"

class LogParser(): # Reads the file, creates LogEntry objects
    def __init__(self, filename):
        self.filename = filename
        self.entries = []

    def parse(self):
        with open (self.filename, "r") as f:
            for line in f:
                parts = line.strip().split(" ", 3)
                entry = LogEntry(parts[0], parts[1], parts[2], parts[3])
                self.entries.append(entry)
            return self.entries

# parts = text.split()          # clean all whitespace first
# date, time, level = parts[0], parts[1], parts[2]
# message = " ".join(parts[3:]) # reassemble the message cleanly  

class LogAnalyser(): # Filters and summarizes the parsed entries
    def __init__(self, parser):
        # self.parser = parser 
        self.entries = parser.entries

    def get_errors(self):
        error_list = []
        for l in self.entries:
            if l.is_error():
                error_list.append(l) 
        return error_list
    
    def get_by_level(self, level):
        level_list = []
        for l in self.entries:
            if l.level == level:
               level_list.append(l)
        return level_list
    
    def get_by_date(self, date):
        date_list = []
        for l in self.entries:
            if l.date == date:
                date_list.append(l)
        return date_list
    
    def summary(self):
        print("=== Log Summary ===")
        info = self.get_by_level("INFO")
        warning = self.get_by_level("WARNING")
        error = self.get_by_level("ERROR")
        print(f"Total entries: {len(self.entries)}")
        print(f"INFO: {len(info)}")
        print(f"WARNING: {len(warning)}")
        print(f"ERROR: {len(error)}")
    
def main():
    analyser = LogParser("system.log")
    analyser.parse()
    log = LogAnalyser(analyser)
   
    while True:
        print("=== Log File Analyser ===\n 1. Show Summary\n 2. Show all errors\n 3. Filter by level\n 4. Filter by date\n 5. Quit")
        choice = input("Pick an option from the menu: ")
        try:
            choice = int(choice)
            if choice == 1:
                log.summary()
            elif choice == 2:
                for entry in log.get_errors():
                    print(entry)
            elif choice == 3:
                level = input("Enter level (INFO/WARNING/ERROR): ").strip().upper()
                for entry in log.get_by_level(level):
                    print(entry)
            elif choice == 4:
                date = input("Enter date (YYYY-MM-DD): ").strip()
                for entry in log.get_by_date(date):
                    print(entry)
            elif choice == 5:
                break
            else:
                print("Make sure to enter a number from 1 to 5 only. Try again.")
        except ValueError:
            print("Please enter a number from 1 to 5 only. Try again.")


if __name__ == "__main__":
    main()


#  A command-line tool that parses system log files, categorizes entries by severity, flags errors, and generates summaries. Built with Python OOP.
