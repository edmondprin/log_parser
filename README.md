# Log File Analyser

## About
- A command-line tool that parses system log files, categorizes entries by severity, flags errors, and generates summaries.
- Built with Python OOP.


## Requirements
- Python installed on your machine: https://www.python.org/downloads/
  
## How to run
- python3 log_analyser.py

## Skills demonstrated
- OOP with classes, objects, and encapsulation.
- Composition: Three classes working together with clear responsibilities. 
- Data validation via @property and setter.
- File I/O: Reading and parsing raw text files. 
- CLI menu with input handling and separation of concerns.

## Features
- Parses standard log format: date, time, severity level, message.
- Get a summary or find specific logs via CLI.
- Supports multiple search types (date, level).
- Invalid log levels rejected at class level — defaults to INFO.
