from datetime import datetime

#Date Variables
date = datetime.today().strftime('%Y%m%d')
month = datetime.today().strftime('%B')
day = datetime.today().strftime('%-d')
year = datetime.today().strftime('%Y')

#Show Metadata Variables
shooting_day = str(input('Enter Shooting Day: '))
episode = str(input('Enter Episode: '))
am_pm_break = ''
show_code = 'BP'
show_name = 'Briarpatch'

#Media Variables
trt = str(input('Please enter the TRT: '))
gigabytes = float(input('Please enter the GB: '))
camera_rolls = str(input('Please Enter Camera Rolls: '))
sound_rolls = str(input("Please Enter Sound Rolls: "))

def runtime_check():
    global trt
    while len(trt) != 11:
        print("Please double check your TRT")
        trt = str(input('Please Enter TRT: '))
    return trt

def break_wrap():
    film_break = ''
    while film_break != 'Y' and film_break != 'N':
        film_break = input("Is this the break? Enter Y or N: ").upper()
    if film_break == 'Y':
        return "Break"
    else:
        return "Wrap"

def subject_line():
    if break_wrap == True:
        filmbreak = 'Break'
    else:
        filmbreak = 'Wrap'
    
    sub_line = f"{show_code}_{date}_{episode}_{shooting_day} - {am_pm_break} Received\n"
    return sub_line

def body():
    if break_wrap == True:
        filmbreak = 'Break'
    else:
        filmbreak = 'Wrap'

    return f'{show_name} {episode} Day {shooting_day}, {month} {day}, {year} - {am_pm_break} Received.\n\nTotal Footage Received and Transferred: {trt} ({gigabytes} GBs).\n\nCamera Rolls {camera_rolls.upper()} and Sound Roll {sound_rolls.upper()} have been received at the lab.'

def received_email():
    global am_pm_break
    
    runtime_check()
    am_pm_break = break_wrap()
    print('\n')
    print(subject_line())
    print(body())

received_email()



