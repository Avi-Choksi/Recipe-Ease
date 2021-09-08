'''
Grab info from user calendar

@author: Avi J Choksi
'''

import src.user.globals
from googleapiclient.discovery import build
import datetime

class userInfo(object):
    
    # Get number of seconds to next event on calendar (max 24hr)
    def getSecondsTillNextEvent(self, user):
        if user.isLoggedIn(self):
            service = build('calendar', 'v3', credentials=src.user.globals.creds) # @UndefinedVariable
    
            # Call the Calendar API
            now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
            events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=1, singleEvents=True,
                                        orderBy='startTime').execute()
            events = events_result.get('items', [])
            
            if not events:
                return 86400
            for event in events:
                start = event['start'].get('dateTime')
                if start[:7] != now[:7]:
                    return 86400
                else:
                    time = abs((int(start[8:10]) - int(now[8:10])) * 86400) + abs(((int(start[11:13]) + int(start[19:22])) - int(now[11:13])) * 3600) + abs(((int(start[14:16]) + int(start[19:20] + start[23:25])) - int(now[14:16])) * 60) + abs((int(start[17:19]) - int(now[17:19])))
                    return time
    
    
