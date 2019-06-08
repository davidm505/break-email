from datetime import datetime

#Date Variables
date = datetime.today().strftime('%Y%m%d')
month = datetime.today().strftime('%B')
day = datetime.today().strftime('%d')
year = datetime.today().strftime('%Y')

#Show Metadata Variables
shooting_day = str(input('Enter Shooting Day: '))
episode = str(input('Enter Episode: '))
show_code = 'BP'
show_name = 'Briarpatch'

#Media Variables
trt = str(input('Please enter the TRT: '))
circle_trt = str(input("Please enter the Circle TRT: "))
gigabytes = float(input('Please enter the GB: '))

class Organizer():

        def __init__(self,media):

                self.media = media
        
        def del_comma_space(self):
                '''
                Returns: 
                        A string with commas and spaces removed.
                '''

                self.media = self.media.replace(",", "")
                self.media = self.media.replace(' ', '')

                return str(self.media)
        
        def del_comma_replace_space(self):
                '''
                Returns:
                         string with comma removed and space 
                         replaced with new line.
                '''

                self.media = self.media.replace(',','')
                self.media = self.media.replace(' ', '\n')
                
                return str(self.media)

        def __str__(self):

                return self.media

def shuttle_organizer():
        '''
        Returns:
                Organized shuttle(s), and displays them on their 
                own line.
        '''

        shuttle_drives = str(input("Please Enter Shuttle Drives: "))

        s = Organizer(shuttle_drives)
        new_shuttles = s.del_comma_space()

        appended_shuttle_list = ''

        for drive in new_shuttles:
                appended_shuttle_list += "Shuttle Drive: " + drive + '\n'

        return appended_shuttle_list

def camera_roll_organizer():
        '''
        Calls for input of camera roll(s).

        Returns:
                Camera roll(s), and displays them on their
                own line.
        '''

        camera_rolls = str(input('Please Enter Camera Rolls: '))

        new_camera_rolls = Organizer(camera_rolls)
        return new_camera_rolls.del_comma_replace_space().upper()

def sound_roll_organizer():
        '''
        Calls for input of sound rolls.

        Returns:
                Sound roll(s) on their own line.
        '''

        sound_rolls = str(input("Please Enter Sound Rolls: "))

        new_sound_roll = Organizer(sound_rolls)
        return new_sound_roll.del_comma_replace_space().upper()

def discrepancy():
        '''
        Calls for input of discrepancies

        Returns:
                If no discrepancies, returns N/A.
                Else returns the discrepancies.
        '''

        discrep = str(input("Enter Discrepancies. If none, enter N: "))

        if discrep.upper() == 'N':
                discrep = 'N/A'
        
        return discrep


def complete_email():

        camera_rolls = camera_roll_organizer()
        sound_rolls = sound_roll_organizer()
        shuttles = shuttle_organizer()
        discrepancies = discrepancy()

        print('\n')
        
        print(f'{show_code}_{date}_{episode}_{shooting_day} - Dailies Complete\n')

        print(f"{show_name}\nShoot Date: {date}\nTransfer Date: {date}\n")
        print(f"All dailies work for {show_name} {episode} Day {shooting_day}, {month} {day}, {year} is now complete.\n")
        print(f'Discrepancy Highlights: {discrepancies}\n')
        print(f'Editorial Files: All Editorial Dailies for {show_name} {episode} Day {shooting_day}, have been transferred over Aspera and can be found on The ISIS.\n')
        print(f"PIX: All PIX Screeners for {show_name} {episode}, Day {shooting_day}, have been uploaded to the Dailies unreleased folder.\n")
        print('The Break & Wrap On Set Rotation Drives are available for pickup from the dailies office at any time.  Building A room 211.\n')
        print('Reports:  Please find all attached reports from production and the dailies lab. The following Rotation Drives and Camera Rolls have been received, backed up, and QC’d at the lab.\n')
        print(f'Drives Received:\n{shuttles}')
        print(f'Camera Rolls Completed:\n{camera_rolls}\n')
        print(f'Sound Rolls:\n{sound_rolls}\n')
        print(f'Running Times:\n{episode} Day {shooting_day}\nTotal Viewing TRT: {circle_trt}\nTotal Editorial TRT: {trt}\n{gigabytes} GBs')

complete_email()
