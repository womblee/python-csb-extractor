# Description
This is a python script which automatically extracts every .csb in the folder you specified

# How to use
1. Create a settings.ini file in the directory which the python file is in.
Fill it with:
```ini
[Config]
quickbmsdir = Directory with QuickBMS
bmsscript = BMS Script name, example: script.bms
quickbmsexe = QuickBMS exe name, example: quickbms.exe
extractdir = Directory from which the .csb files will be extracted
outputdir = Output folder in which every .csb file will extract
```
Also, the bms script and QuickBMS exe must be in the same folder
3. Run main.py

# Requirements
QuickBMS,
Custom BMS Script

# PIP
pathlib,
configparser
