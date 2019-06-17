from datetime import datetime, timedelta
import re

# Date Variables
date = datetime.today().strftime('%Y%m')
month = datetime.today().strftime('%B')
year = datetime.today().strftime('%Y')

# Show Metadata Variables
shooting_day = str(input('Enter Shooting Day: '))
episode = str(input('Enter Episode Block: '))
show_code = 'BP'
show_name = 'Briarpatch'

# Media Variables
gigabytes = float(input('Please enter the GB: '))


class Organizer:

    def __init__(self, media):
        self.media = media

    def shuttle_regex(self):
        """[Compares string to Shuttle Drive regular expression.]

        Returns:
            [string] -- [All shuttle drives sorted inside of a string on their own line.]
        """
        shuttle_regex = re.compile(r'''
        \d  # Shuttle Drive Number
        ''', re.VERBOSE | re.IGNORECASE)

        match_obj = shuttle_regex.findall(self.media)
        match_obj.sort()
        match_obj_string =  ''.join(match_obj)

        return match_obj_string

    def cam_reg_ex(self):
        """[Compares string to camera roll regular expression.]

        Returns:
            [string] -- [All camera rolls sorted inside of a string on their own line.]
        """

        cam_reg_ex = re.compile(r'''
        [a-z]   # Camera Letter
        \d{3}  # Camera Numerical Roll
        ''', re.IGNORECASE | re.VERBOSE)

        mtch_obj = cam_reg_ex.findall(self.media)
        mtch_obj.sort()
        mtch_obj_string = '\n'.join(mtch_obj)
        return mtch_obj_string

    def sound_regex(self):
        """[Compares string to sound roll regular expression.]

        Returns:
            [string] -- [All sound rolls sorted in a string on their own line.]
        """

        sound_regex = re.compile(r'''
        [a-z]+  # Sound roll letters
        \d{3}   # Sound Roll number
        ''', re.VERBOSE | re.IGNORECASE)

        mtch_obj = sound_regex.findall(self.media)
        mtch_obj.sort()
        mtch_obj_string = '\n'.join(mtch_obj)
        return mtch_obj_string

    def __str__(self):
        return self.media


def day_check():
    '''
        Checks the current hour and adjusts the day if it past midnight and before noon
    '''

    hour = datetime.today().strftime('%-H')

    hour = int(hour)

    if hour in range(0, 12):
        yesterday = datetime.today() - timedelta(days=1)
        return yesterday.strftime('%-d')
    else:
        return datetime.today().strftime('%-d')

def episode_gatherer():
    episodes = []

    while True:
        episode_num = str(input('Please Enter the Episode Number: '))
        episode_ctrt = str(input("Please Enter the Circle TRT: "))
        episode_trt = str(input("Please Enter the Total TRT: "))
        episodes.append((episode_num, episode_ctrt, episode_trt))

        cont = input("Are there more episode? [y/n]: ")
        if not cont.lower() in ('y' or 'yes'):
            return episodes

def episode_organizer(eps):

    organized_ep = ''

    for ep_block in eps:
        organized_ep += ('Running Times:\n'
                         + ep_block[0] + ' Day ' + shooting_day + '\n'
                         + "Total Viewing TRT: " + ep_block[1] + '\n'
                         + "Total Editorial TRT: " + ep_block[2] + '\n\n')

    return organized_ep

def shuttle_organizer():
    '''
        Returns:
                Organized shuttle(s), and displays them on their
                own line.
    '''

    shuttle_drives = ''

    while shuttle_drives == '':
        shuttle_drives = str(input("Please Enter Shuttle Drives: "))

        s = Organizer(shuttle_drives)
        new_shuttles = s.shuttle_regex()

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

    camera_rolls = ''

    while camera_rolls == '':
        camera_rolls = str(input('Please Enter Camera Rolls: '))

        new_camera_rolls = Organizer(camera_rolls)
        return new_camera_rolls.cam_reg_ex().upper()

def sound_roll_organizer():
    """[Prompts for sound roll input,]

    Returns:
        [string] -- [returns sound rolls formatted on a new line per roll]
    """

    sound_rolls = ''

    while sound_rolls == '':

        sound_rolls = str(input("Please Enter Sound Rolls: "))
        new_sound_roll = Organizer(sound_rolls)

        return new_sound_roll.sound_regex().upper()

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

    day = day_check()
    camera_rolls = camera_roll_organizer()
    sound_rolls = sound_roll_organizer()
    shuttles = shuttle_organizer()
    ep = episode_gatherer()
    ep_list = episode_organizer(ep)
    discrepancies = discrepancy()

    f = open('Complete.txt', 'w')
    f.write(
        f'{show_code}_{date + day}_{episode}_{shooting_day} - Dailies Complete\n\n\"{show_name}\"\nShoot Date: {date + day}\nTransfer Date: {date + day}\n\nAll dailies work for \"{show_name}\" {episode} Day {shooting_day}, {month} {day}, {year} is now complete.\n\nDiscrepancy Highlights: {discrepancies}\n\nEditorial Files: All Editorial Dailies for {show_name} {episode} Day {shooting_day}, have been transferred over Aspera and can be found on The ISIS.\n\nPIX: All PIX Screeners for {show_name} {episode}, Day {shooting_day}, have been uploaded to the Dailies unreleased folder.\n\nThe Break & Wrap On Set Rotation Drives are available for pickup from the dailies office at any time.  Building A room 216.\n\nReports:  Please find all attached reports from production and the dailies lab. The following Rotation Drives and Camera Rolls have been received, backed up, and QC’d at the lab.\n\nDrives Received:\n{shuttles}\nCamera Rolls Completed:\n{camera_rolls}\n\nSound Rolls:\n{sound_rolls}\n\n{ep_list}Total GB: {gigabytes}')
    f.close()

    print('A text file titled, \"Complete.txt\" has been created in the location of this script.')

    # print(f'{show_code}_{date+day}_{episode}_{shooting_day} - Dailies Complete\n')

    # print(f"{show_name}\nShoot Date: {date+day}\nTransfer Date: {date+day}\n")
    # print(f"All dailies work for {show_name} {episode} Day {shooting_day}, {month} {day}, {year} is now complete.\n")
    # print(f'Discrepancy Highlights: {discrepancies}\n')
    # print(f'Editorial Files: All Editorial Dailies for {show_name} {episode} Day {shooting_day}, have been transferred over Aspera and can be found on The ISIS.\n')
    # print(f"PIX: All PIX Screeners for {show_name} {episode}, Day {shooting_day}, have been uploaded to the Dailies unreleased folder.\n")
    # print('The Break & Wrap On Set Rotation Drives are available for pickup from the dailies office at any time.  Building A room 211.\n')
    # print('Reports:  Please find all attached reports from production and the dailies lab. The following Rotation Drives and Camera Rolls have been received, backed up, and QC’d at the lab.\n')
    # print(f'Drives Received:\n{shuttles}')
    # print(f'Camera Rolls Completed:\n{camera_rolls}\n')
    # print(f'Sound Rolls:\n{sound_rolls}\n')
    # print(f'{ep_list}')


complete_email()
