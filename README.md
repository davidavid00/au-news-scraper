# Basic Python Australian News Scraper

The program that's been created currently looks at the "Just In" pages of ABC News, 7 News, 9 News, Weekly Times Now, The Land, The Riverine Grazier and Stock Journal. More sites will be added to the list as time goes on. Unfortunately these are all configured manually, so you will need intermediate knowledge of HTML and basic python in order to add more sites. 

WARNING: Running this script can cause your IP to be blocked from these sites if you have the schedule the script to run too frequently. You can use an IP rotator to avoid detection. You shouldn't have any problems if it's running every 60/120 minutes, however, I will be looking to add an email notification in future once a website has banned your IP. Typically these blocks are temporary and will be resolved in time.

In order to get this program working, you will need to install the latest version of Python3 from https://www.python.org/downloads/windows/

Note: If you're on Apple silicone, you will need to type python3-intel64 instead of just python3.

Once this has been installed, you will need to ensure `pip` is installed in your terminal of choice. If you are on Windows, you might be using Anaconda. On a Mac, you will need to follow these instructions to install pip https://www.geeksforgeeks.org/how-to-install-pip-in-macos/ 


### Install the required packages
1. Open your terminal (Anaconda, Terminal, etc)
2. Change your directory to the folder where the files are located
3. (Optional) Activate a specified virtual environment
4. Run `pip install requirements.txt` to install the required packages

### Set up the email notification
In order to run the script, you will need to add your email credentials. You can clone or rename the credentials-template.txt to credentails.txt\
You will need to update the sender email, password, SMTP, port and to fields with the below convention:
```
username=username@domain.com
password=password
to=email@domain.com
smtp=smtp.domain.com
port=465
```
The main_function.py script will extract the credentials from the .txt file and use them for sending emails. The script will need to be open and running in your terminal in order for new articles to be examined. When the script runs, it will create a new database with all news headlines/descriptions that match the specified keywords. If the script stops running, and is restarted, emails will not be resent from news articles that already exist in the database.

### Run the script
1. Open your terminal
2. (Optional) Activate the specified virtual environment with requirements.txt install
3. Run the script with `python3 main_function.py` (Terminal) or `main_function.py`
4. Do not close this window, or the function will stop running
