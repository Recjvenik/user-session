## User Session
This README provides an overview of the User Session Processor, a Python script designed to analyze user session logs and generate a report detailing the total number of sessions and total session duration for each user.

## Overview
The User Session Processor script reads a log file containing user session start and end times, processes this data, and outputs a report summarizing each user's session activity. The script is designed to handle log files with entries in the format HH:MM:SS User Start|End, where HH:MM:SS represents the time of the session event, User is the username, and Start|End indicates the beginning or end of a session.

## Features
  - Session Processing: Parses log entries to identify session start and end times for each user.
  - Report Generation: Generates a report detailing the total number of sessions and total session duration for each user.
  - Error Handling: Gracefully handles parsing errors and missing session end times.

## Usage
To use the User Session Processor, run the script from the command line with the path to the log file as an argument:

`python user_session.py <log_file_path>`
