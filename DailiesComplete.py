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

#QC Variables
discrep = str(input("Enter Discrepancies. If none, enter N: "))

#Media Variables
trt = str(input('Please enter the TRT: '))
circle_trt = str(input("Please enter the Circle TRT: "))
gigabytes = float(input('Please enter the GB: '))
camera_rolls = str(input('Please Enter Camera Rolls: '))
sound_rolls = str(input("Please Enter Sound Rolls: "))
shuttle_drives = str(input("Please Enter Shuttle Drives: "))

class Organizer():

        def __init__(self,media):

                self.media = media
        
        def del_comma_space(self):

                self.media = self.media.replace(",", "")
                self.media = self.media.replace(' ', '')

                return str(self.media)
        
        def del_comma_replace_space(self):

                self.media = self.media.replace(',','')
                self.media = self.media.replace(' ', '\n')
                
                return str(self.media)

        def __str__(self):

                return self.media

def shuttle_organizer():

        new_shuttles = Organizer(shuttle_drives)
        s = new_shuttles.del_comma_space()

        appended_shuttle_list = ''

        for drive in s:
                appended_shuttle_list += "Shuttle Drive: " + drive + '\n'

        return appended_shuttle_list

def camera_roll_organizer():

        new_camera_rolls = Organizer(camera_rolls)
        return new_camera_rolls.del_comma_replace_space().upper()

def sound_roll_organizer():

        new_sound_roll = Organizer(sound_rolls)
        return new_sound_roll.del_comma_replace_space().upper()

def discrepancy_check():
    global discrep

    if discrep.upper() == 'N':
        discrep = 'N/A'

def complete_email():

    camera_rolls = camera_roll_organizer()
    sound_rolls = sound_roll_organizer()
    shuttles = shuttle_organizer()
    discrepancy_check()

    print('\n')
    
    print(f'{show_code}_{date}_{episode}_{shooting_day} - Dailies Complete\n')

    print(f"{show_name}\nShoot Date: {date}\nTransfer Date: {date}\n")
    print(f"All dailies work for {show_name} {episode} Day {shooting_day}, {month} {day}, {year} is now complete.\n")
    print(f'Discrepancy Highlights: {discrep}\n')
    print(f'Editorial Files: All Editorial Dailies for {show_name} {episode} Day {shooting_day}, have been transferred over Aspera and can be found on The ISIS.\n')
    print(f"PIX: All PIX Screeners for {show_name} {episode}, Day {shooting_day}, have been uploaded to the Dailies unreleased folder.\n")
    print('The Break & Wrap On Set Rotation Drives are available for pickup from the dailies office at any time.  Building A room 211.\n')
    print('Reports:  Please find all attached reports from production and the dailies lab. The following Rotation Drives and Camera Rolls have been received, backed up, and QC’d at the lab.\n')
    print(f'Drives Received:\n{shuttles}')
    print(f'Camera Rolls Completed:\n{camera_rolls}\n')
    print(f'Sound Rolls:\n{sound_rolls}\n')
    print(f'Running Times:\n{episode} Day {shooting_day}\nTotal Viewing TRT: {circle_trt}\nTotal Editorial TRT: {trt}\n{gigabytes} GBs')

complete_email()
