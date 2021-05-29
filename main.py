import subprocess
import sys
from pathlib import Path
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser # ver. < 3.0

settings = ConfigParser()
settings.read('settings.ini')

QuickBMS = settings.get('Config', 'quickbmsdir')
Output = settings.get('Config', 'outputdir')
DyingLight = settings.get('Config', 'dyinglightdir')

if not Path(QuickBMS).is_dir():
   raise ValueError("QuickBMS Directory not found")

if not Path(Output).is_dir():
   raise ValueError("Output Directory not found")

if not Path(DyingLight).is_dir():
   raise ValueError("Dying Light Directory not found")

if not Path(QuickBMS + '/dying_light.bms').is_file():
    raise ValueError("BMS Script not found")

if not Path(QuickBMS + '/quickbms.exe').is_file():
    raise ValueError("QuickBMS not found")

CSBs = [
    'all_in_maps_1.csb',
    'all_in_maps_2.csb',
    'all_in_maps_3.csb',
    'all_in_maps_persistant.csb',
    'Menu.csb',
    'Music_1.csb',
    'Music_2.csb',
    'Music_3.csb',
]

for i in range(len(CSBs)):
    Path(Output + "/" + CSBs[i]).mkdir()
    result = subprocess.run([QuickBMS+"/quickbms.exe", QuickBMS+"/dying_light.bms", DyingLight+"/DW/Data/" + CSBs[i], Output + "/" + CSBs[i]], capture_output=True)
    
    sys.stdout.buffer.write(result.stdout)
    sys.stderr.buffer.write(result.stderr)
    


