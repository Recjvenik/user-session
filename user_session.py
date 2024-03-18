import os
import sys
import re
from datetime import datetime


def process_user_session(file_path):
    user_sessions = {}
    session_report = {}
    earliest_time = None

    with open(file_path, 'r') as file:
        for line in file:
            match = re.match(r'(\d{2}:\d{2}:\d{2}) (\w+) (Start|End)', line.strip())
            if match:
                time_str, user, status = match.groups()
                
                try:
                    time = datetime.strptime(time_str, '%H:%M:%S')
                except:
                    continue

                if earliest_time is None or time < earliest_time:
                    earliest_time = time

                if user not in user_sessions:
                    user_sessions[user] = []

                if user not in session_report:
                    session_report[user] = {}
            
                if status == 'Start':
                    user_sessions[user].append(time)
                else:
                    if user_sessions.get(user):
                        start_time = user_sessions[user].pop()
                        total_time = (time - start_time).total_seconds()
                        session_report[user]['total_sessions'] = 1 + session_report[user].get('total_sessions', 0)
                        session_report[user]['total_seconds'] = total_time + session_report[user].get('total_seconds', 0)
                    else:
                        total_time = (time - earliest_time).total_seconds()
                        session_report[user]['total_sessions'] = 1 + session_report[user].get('total_sessions', 0)
                        session_report[user]['total_seconds'] = total_time + session_report[user].get('total_seconds', 0)
                    
    for user, session_times in user_sessions.items():
        if session_times:
            session_report[user]['total_sessions'] = 1 + session_report[user].get('total_sessions', 0)
            session_report[user]['total_seconds'] = 0 + session_report[user].get('total_seconds', 0)
    
    return session_report

def print_report(session_report):
    for user, user_data in session_report.items():
        print(f"{user} {user_data['total_sessions']} {int(user_data['total_seconds'])}")

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python user_session.py <log_file_path>")
        sys.exit(1)

    log_file_path = sys.argv[1]
    if not os.path.exists(log_file_path):
        print("Error: File not found.")
        sys.exit(1)

    report = process_user_session(log_file_path)
    print_report(report)
