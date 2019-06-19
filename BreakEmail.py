from datetime import datetime, timedelta
import re
import os.path
import json
import webbrowser
from bs4 import BeautifulSoup

# FilPath Variables
cwd = os.getcwd()
filePath = os.path.dirname(os.path.realpath(__file__))

print("Current Working Directory is: " + cwd)
print("File path is: " + filePath)

# JSON
json_path = os.path.join(filePath,"JSON/CrewList.json")

# Date Variables
date = datetime.today().strftime('%Y%m')
month = datetime.today().strftime('%B')
year = datetime.today().strftime('%Y')

# Show Metadata Variables
shooting_day = str(input('Enter Shooting Day: '))
episode = str(input('Enter Episode: '))
show_code = 'BP'
show_name = 'Briarpatch'

# Media Variables
gigabytes = float(input('Please Enter The GB: '))


def email_distro():

    email_distro_list = ''

    with open(json_path,'r') as f:
        distro_dict = json.load(f)

    for member in distro_dict["Break Email"]:
        email_distro_list += (member['Email'] + ' ')
    
    return email_distro_list


def day_check():
    '''
        Checks the current hour and adjust the day if it past midnight and before noon.
    '''

    hour = datetime.today().strftime('%H')
    hour = int(hour)
    
    if hour in range(0,13):
        yesterday = datetime.today() - timedelta(days=1)
        return yesterday.strftime('%d')
    else:
        return datetime.today().strftime('%d')


def break_wrap():
    '''
    Prompts user for input. 

    Returns:
        A string with either Break or Wrap.
    '''

    film_break = ''

    while film_break != 'Y' and film_break != 'N':
        film_break = input("Is this the break? Enter Y or N: ").upper()

    if film_break == 'Y':
        return "Break"
    else:
        return "Wrap"


def runtime():
    '''
    Prompts for user input. Checks input against a regular expression.

    Returns:
        the trt as a string.
    '''

    while True:
        trt = str(input("Please enter the TRT: "))
        trtRegEX = re.compile(r'\d\d:\d\d:\d\d:\d\d')
        mo = trtRegEX.search(trt)
        
        if mo:
            return trt
        else:
            continue


def camera_rolls():
    '''
    Prompts for user input. 

    Returns:
        Camera roll(s) as a string.
    '''
    camRegEx = re.compile(r'[a-z]\d\d\d', re.IGNORECASE)
    cr = ''

    while cr == '':
        cr = input("Please Enter The Camera Roll(s): ")
        mo = camRegEx.findall(cr)
        mo.sort()
        sorted_roll = ', '.join(mo)
        return sorted_roll.upper()


def sound_rolls():
    '''
    Prompts for user input. 

    Returns:
        Sound rolls as a string.
    '''

    sr_reg_ex = re.compile(r'(([a-z]{2})?\d\d\d)', re.IGNORECASE)

    sr = ''
    roll_list = []

    while sr == '':
        sr = str(input("Please Enter The Sound Roll(s): "))

        if sr == 'n/a' or sr == 'N/A':
            return sr
        elif sr == '':
            continue
        else:
            mo = sr_reg_ex.findall(sr)

            if mo:
                for roll in mo:
                    roll_list.append(roll[0])

                sorted_roll = ', '.join(roll_list)
                return sorted_roll
            else:
                sr = ''
                continue
            

def received_email_text():

    distro_list = email_distro()

    am_pm_break = break_wrap()
    day = day_check()
    trt = runtime()
    cr = camera_rolls()
    sr = sound_rolls()

    # Create TXT File
    full_name = os.path.join(filePath, "break.txt")
    f = open(full_name, 'w')

    f.write(distro_list)
    
    f.write(f'\n\n{show_code}_{date+day}_{episode}_{shooting_day} - {am_pm_break} Received')

    f.write(f"\n\n{show_name} {episode} Day {shooting_day}, {month} {day}, {year} - {am_pm_break} Received.")

    f.write(f"\n\nTotal Footage Received and Transferred: {trt} ({gigabytes} GBs).")

    f.write(f"\n\nCamera Rolls {cr} and Sound Roll {sr} have been received at the lab.")

    f.close()

    print("a txt file titled, \"break.txt\" has been created in the location of this program.")


def received_email_html():

    distro_list = email_distro()
    am_pm_break = break_wrap()
    day = day_check()
    trt = runtime()
    cr = camera_rolls()
    sr = sound_rolls()

    html_path = os.path.join(filePath, 'HTML/break.html')
    html_file = open(html_path, 'w')

    message = f'''
        <head>
            <title>Break Email</title>
        </head>
        <html>
            <body>
                <p>{distro_list}</p><br>
                <p>{show_code}_{date + day}_{episode}_{shooting_day} - {am_pm_break} Received</p><br>
                <p><strong>\"{show_name}\"</strong> {episode} Day {shooting_day}, {month} {day}, {year} - 
                <strong>{am_pm_break} Received</strong>.</p><br>
                <p>Total Footage Received and Transferred: {trt} ({gigabytes} GBs).</p><br>
                <p>Camera Rolls {cr} and Sound Roll {sr} have been received at the lab.</p>
            </body>
        </html>
        '''
    html_file.write(message)
    html_file.close()

    webbrowser.open_new_tab('/Users/davidmorales/Documents/Repos/Python/DailiesEmail/break-email/HTML/break.html')

# received_email_text()

received_email_html()
