# Human Computer Interaction

Leap Motion applications

download and install leap motion developer sdk for python from 
https://developer.leapmotion.com/windows-vr

Work for linux mint and Windows.
Working on Python 2.7.4

# Prequisities

`pip install -r requirements.txt`


# Instruction to run

open any file/files with vlc media player

Enable web interface from 
    `view` -> `add interface` -> `web`
    
Connect leap motion device.
make sure leap motion is working.

run `leap_vlc.py` file (`python leap_vlc.py`)

### Error
if error comes while running the `leap_vlc.py` file than copy files from 
`lib`/ and paste them to `lib/x86` , `lib/x64`



# Gesture

#### `close hand to pause or play`
#### `roll your right hand finger for volume up`
#### `roll your left hand finger for volume down`
#### `move your hand toward right side for next song`
#### `move your hand toward left for previous song`



#### Modification

for linux user , change `cls` command to `clear` on line 137.

Volume level can be change by changing volume value , for volume value 4 volume changes by two level approx.
