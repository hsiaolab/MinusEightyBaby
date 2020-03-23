# MinusEightyBaby Twitter Bot

import time, sys
from daqhats import mcc134, hat_list, HatIDs, TcTypes
import tweepy

###### SET THESE VARIABLES
SLEEP_MINUTES = 20          # every 20 minutes
FRIDGE_LABEL = 'fridge_a'   # set a label for your fridge
CONSUMER_KEY = "XXX"        # change XXX to your Twitter Consumer Key
CONSUMER_SECRET = "XXX"     # change XXX to your Twitter Consumer Secret
ACCESS_TOKEN = "XXX"        # change XXX to your Twitter Access Token
ACCESS_SECRET = "XXX"       # change XXX to your Twitter Access Key
#######

sleep_seconds = SLEEP_MINUTES * 60
channel = 0
tc_type = TcTypes.TYPE_T

# Find the MCC 134
hats = hat_list(filter_by_id=HatIDs.MCC_134)
if not hats:
    print('No MCC 134 found, quiting')
    sys.exit()
else:
    print('Found MCC134')

board = mcc134(hats[0].address)

# Configure the thermocouple type on the channel 0
board.tc_type_write(channel, tc_type)

while True:
    temperature = board.t_in_read(channel)
    if temperature == mcc134.OPEN_TC_VALUE:
        print('MC143 Error - Open')
    elif temperature == mcc134.OVERRANGE_TC_VALUE:
        print('MC143 Error - Over range')
    elif temperature == mcc134.COMMON_MODE_TC_VALUE:
        print('MC143 Error - Common mode')
    else:
        temp_val = "{:.2f}".format(temperature)
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        api = tweepy.API(auth)
        api.update_status(status="%s is at %s" % (FRIDGE_LABEL, temp_val))

    time.sleep(sleep_seconds)
