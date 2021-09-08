'''
Login commands for user

@author: Avi J Choksi
'''

from __future__ import print_function
import os.path
import src.user.globals
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from pathlib import Path


class login(object):
    def __init__(self):
        src.user.globals.initialize()
        self.SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
    
    # Login user
    def login(self):
        
        src.user.globals.initialize()
        data_folder = Path(os.path.dirname(__file__))
        s = str(data_folder.parent.absolute())
        file_to_open = s + "//externalFiles//credentials.json"
        
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(src.user.globals.userToken):  # @UndefinedVariable
            creds = Credentials.from_authorized_user_file(src.user.globals.userToken, self.SCOPES)# @UndefinedVariable
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            flow = InstalledAppFlow.from_client_secrets_file(
                file_to_open, self.SCOPES)
            creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(src.user.globals.userToken, 'w') as token: #@UndefinedVariable
                token.write(creds.to_json())
              
        src.user.globals.creds = creds
        return True
    
    # Logout certain user      
    def logout(self, userNum):
        fileName = "tokens\\token" + str(userNum) + ".json"
        os.remove(fileName)
        if src.user.globals.userToken == fileName: # @UndefinedVariable
            src.user.globals.userToken = 'token0.json'
    
    # Add new user    
    def addUser(self):
        src.user.globals.userCount += 1
        fileName = "tokens\\token" + str(src.user.globals.userCount) + ".json" # @UndefinedVariable
        src.user.globals.userToken = fileName
    
    # Switch to different user    
    def switchUser(self, userNum):
        src.user.globals.userToken = "tokens\\token" + str(userNum) + ".json"
    
    # Check if user is logged in    
    def isLoggedIn(self):
        try:
            if src.user.globals.creds == None: # @UndefinedVariable
                return False
            else:
                return True
        except:
            return False;
        