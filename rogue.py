import os
import psutil
import pyfiglet
from termcolor import colored
import time
import signal
import sys
from datetime import datetime

def signal_handler(sig, frame):
    print("\nExiting...")
    sys.exit(0)

def print_banner():
    rogue_text = pyfiglet.figlet_format("Rogue", font="slant")
    
    person_text = """
      _____
     /     \\
    | () () |
     \\  ^  /
      |||||
      |||||
    """
    
    combined_lines = rogue_text.splitlines()
    person_lines = person_text.splitlines()
    
    if len(person_lines) < len(combined_lines):
        person_lines += [' ' * len(person_lines[0])] * (len(combined_lines) - len(person_lines))
    
    combined_text = '\n'.join(f"{line}   {person_line}" for line, person_line in zip(combined_lines, person_lines))
    
    colored_banner = colored(combined_text, color='red')
    
    shift_amount = 5
    shifted_banner = '\n'.join(' ' * shift_amount + line for line in colored_banner.splitlines())
    
    author = "By: Str4ngerX - v1.0.0"
    linkedin_url = "🔗 https://www.linkedin.com/in/alaloghmari/"
    github_url = "🌐 https://github.com/LoghmariAla/"
    
    author_shift = shift_amount + 17
    links_shift = shift_amount + 5
    
    shifted_author = ' ' * author_shift + author
    shifted_links = ' ' * links_shift + linkedin_url + '\n' + ' ' * links_shift + github_url
    
    print(shifted_banner)
    print(shifted_author)
    print("\n" * 1)
    print(shifted_links)
    print("\n" * 2)
    print(f"{'Start Time':<25}{'PID':<10}{'  User':<25}CMD")
    print("-" * 80)

def color_user(user):
    if user == 'root':
        return colored(user, 'red')
    elif user in get_current_users():
        return colored(user, 'blue')
    else:
        return colored(user, 'white')

def get_current_users():
    current_users = set()
    try:
        with open('/etc/passwd', 'r') as f:
            for line in f:
                parts = line.split(':')
                user = parts[0]
                if int(parts[2]) >= 1000 and not user.startswith('nobody'):
                    current_users.add(user)
    except IOError:
        pass
    return current_users

def format_start_time(create_time):
    try:
        return datetime.fromtimestamp(create_time).strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        return "N/A"

def list_processes():
    existing_pids = set()
    
    print_banner()
    
    try:
        while True:
            new_pids = set()
            for process in psutil.process_iter(['pid', 'cmdline', 'username', 'create_time']):
                try:
                    pid = process.info['pid']
                    new_pids.add(pid)
                    
                    if pid not in existing_pids:
                        user = process.info['username'] if process.info['username'] else "N/A"
                        cmdline = ' '.join(process.info['cmdline'])[:49]
                        
                        if not cmdline:
                            continue
                        
                        start_time = format_start_time(process.info['create_time'])
                        user_colored = color_user(user)
                        
                        print(f"{start_time:<25} {pid:<10} {user_colored:<25} {cmdline:<50}")
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
            
            existing_pids.update(new_pids)
            
            time.sleep(2)
    
    except KeyboardInterrupt:
        signal_handler(None, None)

def main():
    signal.signal(signal.SIGINT, signal_handler)
    list_processes()

if __name__ == "__main__":
    main()
