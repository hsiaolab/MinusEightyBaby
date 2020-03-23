# MinusEightyBaby

### Instructions on how to build an extreme temperature (-200°C to 260°C) remote monitor Twitter Bot for your lab freezers

---

Part List for each Freezer:
    
* 1 x [Thermocouple T-Type –200C to 260C sensor @ $20](https://www.amazon.com/gp/product/B075QBB99D/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1)
* 1 x [Raspberry PI Bundle - includes charger, SD card with preloaded OS, HDMI Cable @ $100](https://www.amazon.com/gp/product/B07YRSYR3M/ref=ppx_yo_dt_b_asin_title_o02_s04?ie=UTF8&psc=1)
* 1 x [MCC-134 Thermocouple Measurement HAT for Raspberry Pi @ $150](https://www.mccdaq.com/DAQ-HAT/MCC-134.aspx)

Setup Accessories:

* A Display or TV with HDMI input
* USB Mouse
* USB Keyboard
* A tiny flat head screwdriver

#### Setup a Twitter Developer account while you wait for your hardware

1. After creating a Twitter account, add your email and phone number to your profile (Dev accounts need both to be entered)
2. Go to [Twitter Apps](https://developer.twitter.com/apps) to signup to be a developer and create an app, fill in minimum requirements
3. After successful app creation, go to the App's Keys and Tokens section and save the Consumer keys and generated Access token/secrets somewhere for later:

#### Install the Hardware: 

1. Push the GPIO Stacking Header from the MCC-134 kit all the way down into the Raspberry PI's pins and then push the MCC-134 into the Stacking Header
    ![GPIO Stacking Header](https://github.com/hsiaolab/MinusEightyBaby/blob/master/images/1first.jpg?raw=true)
2. Unscrew the Male Flat Lead Connector on the Thermocouple and make note which wire is (+) and (-)
    ![Male Flat Lead Connector](https://github.com/hsiaolab/MinusEightyBaby/blob/master/images/2mcc134.jpg?raw=true)
3. Put the (+) wire into CH0H and the (-) wire into the CH0L ports of the MCC-134 Board. Screw them down so they are secure.
    ![Thermocouple ports](https://github.com/hsiaolab/MinusEightyBaby/blob/master/images/3setup.jpg?raw=true)
4. String the sensor end of the Thermocouple into the fridge
    ![Freezer](https://github.com/hsiaolab/MinusEightyBaby/blob/master/images/5freeze.jpg?raw=true)
5. Insert the micro SD card, attach power supply, and ethernet cable if not using wifi

#### Setup the PI, install the MCC-134 Libraries

1. Connect a keyboard, mouse, and display and turn on the Raspberry PI
2. Follow the onscreen instructions on adding a password and connecting to your network. You can skip the rest.
3. Open the terminal app, enter one line at a time to create your folder and install the MCC-134 libraries:

`cd ~/Documents`

`mkdir freezercheck`

`sudo cp /usr/bin/python3 /usr/bin/python`

`git clone https://github.com/mccdaq/daqhats.git`

`cd daqhats`

`sudo ./install.sh`

### Install the bot script

`cd ~/Documents/freezercheck`

`wget https://raw.githubusercontent.com/hsiaolab/MinusEightyBaby/master/scripts/freezerbot.py`

### Edit the script

* Open /Documents/freezercheck/freezerbot.py in a text editor and update the variables up top if you like
* Replace 'XXX' with your Twitter Bot Keys from above

### Run the script and check your Twitter page if it worked

`python3 client.py`

---

## Advanced Notes

### Using WiFi?

1. Setup the PI to reconnect to WiFi if it goes down. Open the terminal app and enter this line by line, the machine will reboot:

`cd /etc/ifplugd/action.d/`

`sudo mv ifupdownifupdown.original`

`sudo cp /etc/wpa_supplicant/ifupdown.sh ./ifupdown`

`sudo reboot`

---
 
### Remote access and auto-loading

1. Change the hostname in /etc/hostname if you have multiple fridges and want to connect remotely

2. Add the following before the exit line in /etc/rc.local before so the script runs automatically when the Raspberry Pi boots up:

`cd /home/pi/Documents/freezercheck`

`python3 client.py &`

---

### Alerts

* Instead of posting directly to Twitter we actually post the data to our internal server every minute and that server handles consolidating the temperatures and alerting us via email if there are any problems.
