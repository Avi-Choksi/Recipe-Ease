'''
Global variables for logging in

@author: Avi J Choksi
'''

import glob
import os
# Set global variables for user calendar
def initialize():
    global userCount
    global userToken
    global creds
    creds = None
    userCount = len(glob.glob1("tokens","*.json")) - 1
    if userCount < 0:
        userCount = 0
        
    if not os.path.exists('tokens'):
        os.makedirs('tokens')
    userToken = 'tokens\\token0.json'