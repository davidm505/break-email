from datetime import datetime, timedelta
import re
import os.path

#FilPath Variables
cwd = os.getcwd()
filePath = os.path.dirname(os.path.realpath(__file__))

print("Current Working Directory is: " + cwd)
print("File path is: " + filePath)

#Date Variables
date = datetime.today().strftime('%Y%m')
month = datetime.today().strftime('%B')
year = datetime.today().strftime('%Y')

#Show Metadata Variables
shooting_day = str(input('Enter Shooting Day: '))
episode = str(input('Enter Episode: '))
show_code = 'BP'
show_name = 'Briarpatch'

#Media Variables
gigabytes = float(input('Please Enter The GB: '))

def day_check():
    '''
        Checks the current hour and adjust the day if it past midnight and before noon.
    '''

    hour = datetime.today().strftime('%-H')
    hour = int(hour)
    
    if hour in range(0,13):
        yesterday = datetime.today() - timedelta(days=1)
        return yesterday.strftime('%-d')
    else:
        return datetime.today().strftime('%-d')

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
    camRegEx = re.compile(r'[a-zA-Z]\d\d\d')
    cr = ''

    while cr == '':
        cr = input("Please Enter The Camera Roll(s): ")
        mo = camRegEx.findall(cr)
        mo.sort()
        sortedRoll = ', '.join(mo)
        return sortedRoll.upper()
         
def sound_rolls():
    '''
    Prompts for user input. 

    Returns:
        Sound rolls as a string.
    '''

    srRegEx = re.compile(r'[a-zA-Z]+\d\d\d')
    sr = ''

    while sr == '':
        sr = str(input("Please Enter The Sound Roll(s): "))

        if (sr == 'n/a' or sr == 'N/A'):
            return sr
        else:
            mo = srRegEx.findall(sr)
            mo.sort()
            sortedSR = ', '.join(mo)
            return sortedSR.upper()


def received_email():

    am_pm_break = break_wrap()
    day = day_check()
    trt = runtime()
    cr = camera_rolls()
    sr = sound_rolls()

    #Create TXT File
    fullName = os.path.join(filePath,"break.txt")
    f = open(fullName, 'w')
    f.write(f'''\n{show_code}_{date+day}_{episode}_{shooting_day} - {am_pm_break} Received\n\n{show_name} {episode} Day {shooting_day}, {month} {day}, {year} - {am_pm_break} Received.\n\nTotal Footage Received and Transferred: {trt} ({gigabytes} GBs).\n\nCamera Rolls {cr} and Sound Roll {sr} have been received at the lab.''')
    f.close()

    print("a txt file titled, \"break.txt\" has been created in the location of this program.")

received_email()