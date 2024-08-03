# Rogue

**Rogue** is a command-line tool for monitoring processes on Linux systems. It provides a real-time view of running processes, including their launch time, PID, user, and command line arguments. The tool highlights new processes as they are detected and displays user information with different colors based on user type.

## Features

- **Real-time Monitoring**: Continuously monitors processes and updates the display.
- **Colored User Display**: Differentiates users with colors (red for root, blue for current users, and white for other users).

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/LoghmariAla/rogue.git
    ```

2. Navigate to the project directory:
    ```bash
    cd rogue
    ```

3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the tool with the following command:
```bash
python3 rogue.py
