import subprocess
import json

def find_dur(filein):
	meta_json = subprocess.check_output(['ffprobe', '-v', 'warning',
                      '-print_format', 'json',
                      '-show_streams',
                      '-show_format', filein],
                      universal_newlines=True)
	meta = json.loads(meta_json)
	duration = float(meta['streams'][0]['duration'])
	return duration
 