# ics date shifting practice

## Setting up your environment
```sh
pip3 install ics
pip3 install arrow
pip3 install datetime
```

go to the folder with the python file
add ics file into folder
```sh
python3 cal_shift.py
```
enter the file name and start date

## Function
- takes as arbitrary input: ICS file and start date (eg. date for the first event)
- generates output: ICS file that is shifted such that the first calendar event is on the new input date. All calendar events should be shifted appropriately, see example below.
