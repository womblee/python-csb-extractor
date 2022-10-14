import subprocess
import sys
from pathlib import Path
from configparser import ConfigParser

settings = ConfigParser()
settings.read('settings.ini')

QuickBMSDir = settings.get('Config', 'quickbmsdir')
Output = settings.get('Config', 'outputdir')
ExtractDir = settings.get('Config', 'extractdir')
BMSScript = settings.get('Config', 'bmsscript')
BMSexe = settings.get('Config', 'quickbmsexe')

if not Path(QuickBMSDir).is_dir(): raise ValueError("QuickBMS Directory not found")
if not Path(Output).is_dir(): raise ValueError("Output Directory not found")
if not Path(ExtractDir).is_dir(): raise ValueError("Directory from wich we will extract not found")

if not Path(QuickBMSDir + '/' + BMSScript).is_file(): raise ValueError("BMS Script in: " + QuickBMSDir + "not found")
if not Path(QuickBMSDir + '/' + BMSexe).is_file(): raise ValueError("QuickBMS Exe in: " + QuickBMSDir + "not found")

if not Path(ExtractDir).glob('*.csb'):
    raise ValueError("There were no .csb files in the directory: " + ExtractDir)

for csb_file in Path(ExtractDir).glob('*.csb'):
    if Path(Output + "/" + csb_file.name).exists():
        if Path(Output + "/" + csb_file.name).glob('*.fsb'):
            for fsb_file in Path(Output + "/" + csb_file.name).glob('*.fsb'):            
                fsb_file.unlink()

    if not Path(Output + "/" + csb_file.name).exists():
        Path(Output + "/" + csb_file.name).mkdir()
    
    result = subprocess.run([QuickBMSDir + "/" + BMSexe, QuickBMSDir + "/" + BMSScript, ExtractDir + "/" + csb_file.name, Output + "/" + csb_file.name], capture_output=True)
    
    sys.stdout.buffer.write(result.stdout)
    sys.stderr.buffer.write(result.stderr)
