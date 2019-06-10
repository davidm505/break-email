from datetime import datetime

#Date Variables
date = datetime.today().strftime('%Y%m%d')
month = datetime.today().strftime('%B')
day = datetime.today().strftime('%-d')
year = datetime.today().strftime('%Y')

#Show Metadata Variables
shooting_day = str(input('Enter Shooting Day: '))
episode = str(input('Enter Episode: '))
show_code = 'BP'
show_name = 'Briarpatch'

#Media Variables
gigabytes = float(input('Please Enter The GB: '))

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
    Prompts for user input.

    Returns:
        the trt as a string.
    '''

    trt = str(input("Please enter the TRT: "))

    while len(trt) != 11:
        print("Please double check your TRT")
        trt = str(input('Please Enter TRT: '))

    return trt

def camera_rolls():
    '''
    Prompts for user input. 

    Returns:
        Camera roll(s) as a string.
    '''

    cr = ''

    while cr == '':
        cr = input("Please Enter The Camera Roll(s): ")
         
    return cr.upper()

def sound_rolls():
    '''
    Prompts for user input. 

    Returns:
        Sound rolls as a string.
    '''

    sr = ''

    while sr == '':
        sr = str(input("Please Enter The Sound Roll(s): "))

    return sr.upper()


def received_email():

    am_pm_break = break_wrap()
    trt = runtime()
    cr = camera_rolls()
    sr = sound_rolls()

    #Create TXT File
    f = open("break.txt", 'w')
    f.write(f"\n{show_code}_{date}_{episode}_{shooting_day} - {am_pm_break} Received\n{show_name} {episode} Day {shooting_day}, {month} {day}, {year} - {am_pm_break} Received.\n\nTotal Footage Received and Transferred: {trt} ({gigabytes} GBs).\n\nCamera Rolls {cr} and Sound Roll {sr} have been received at the lab.")
    f.close()

    print(f"\n{show_code}_{date}_{episode}_{shooting_day} - {am_pm_break} Received\n")

    print(f'{show_name} {episode} Day {shooting_day}, {month} {day}, {year} - {am_pm_break} Received.\n\nTotal Footage Received and Transferred: {trt} ({gigabytes} GBs).\n\nCamera Rolls {cr} and Sound Roll {sr} have been received at the lab.')

received_email()