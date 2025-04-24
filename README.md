# Russian Roulette Destructive Script

***

**🚨 EXTREMELY DANGEROUS SCRIPT - DO NOT RUN 🚨**

**RUNNING THIS SCRIPT CAN AND LIKELY WILL PERMANENTLY DESTROY YOUR OPERATING SYSTEM AND DELETE ALL YOUR DATA. IT IS PROVIDED FOR EDUCATIONAL PURPOSES *ONLY* TO DEMONSTRATE POTENTIALLY HARMFUL CODE. DO NOT EXECUTE IT ON ANY SYSTEM YOU CARE ABOUT, INCLUDING VIRTUAL MACHINES UNLESS YOU FULLY UNDERSTAND THE RISKS AND CONSEQUENCES.**

***

## Description

This Python script simulates a game of Russian Roulette with a devastating twist. It iterates a set number of times (default 100), generating a random number in each iteration. If a specific number (`1`) is generated (approximately a 1 in 6 chance per iteration), the script attempts to execute a highly destructive command designed to wipe critical parts or the entirety of the host operating system.

## How it Works

1.  The script initializes a loop that runs `100` times (controlled by the `range_` variable).
2.  Inside the loop, it generates a random integer `x` between 0 and 5 (inclusive).
3.  If `x` is **not** equal to `1`, it prints "`<number> Click`" and proceeds to the next iteration.
4.  If `x` **is** equal to `1`, it prints "`1 Bang. Downloading more RAM please wait.....`" and triggers the destructive payload:
    * It checks the operating system using `platform.system()`.
    * **On Windows:** It attempts to execute `os.remove("C:\Windows\System32")`.
        * _Note:_ This specific command might fail as `os.remove` is for files, not directories, and requires elevated privileges. However, the *intent* is to delete critical system files, potentially rendering Windows unbootable.
    * **On macOS (Darwin):** It attempts to execute `sudo srm -rf /`. This command tries to securely and recursively delete the *entire* root filesystem (`/`), requiring administrator (`sudo`) password confirmation. This is catastrophic.
    * **On Linux:** It attempts to execute `sudo rm -rf /`. Similar to macOS, this command tries to recursively delete the *entire* root filesystem (`/`), requiring administrator (`sudo`) password confirmation. This is also catastrophic.
5.  The script counts how many times the "Bang" condition (`x == 1`) occurs.
6.  After the loop completes (or is likely interrupted by system failure if the destructive code runs successfully), it prints the total "Kills" (number of times `x` was 1), "Misses", the calculated "Kill Rate", and the script's execution time.

## Target Systems

* Windows
* macOS (Darwin)
* Linux

## Requirements

* Python 3
* Standard libraries: `random`, `math`, `platform`, `os`, `time`
* **Administrative privileges** (Run as Administrator on Windows, `sudo` access on macOS/Linux) are necessary for the destructive commands to potentially succeed.

## Usage

To run the script ( **EXTREMELY DISCOURAGED - FOR EDUCATIONAL VIEWING ONLY** ):

```bash
python your_script_name.py