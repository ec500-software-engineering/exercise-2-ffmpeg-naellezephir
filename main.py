import queue
import threading
import subprocess
import os
import tests.duration as duration


Path = '/Users/naellezephir/Desktop/GitHub/exercise-2/videos'
outpath = '/Users/naellezephir/Desktop/GitHub/exercise-2/videos/finished'

def fill_q(Q):
	folder = os.listdir(Path)
	for file in folder:
		Q.put(Path+"/"+file)

def ffmpeg_convert(Q,path):
	while not Q.empty():
		curr_file = Q.get()
		vid720 = "ffmpeg -i "+curr_file+" -s hd720 -b:v 1M -r 30 "+curr_file[:-4]+"720.mp4"
		vid480 = "ffmpeg -i "+curr_file+" -s hd720 -b:v 1M -r 30 "+curr_file[:-4]+"480.mp4"
		name = curr_file[len(path):]
		print(name + " 720 is processing")
		subprocess.call(vid720, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)
		print(name + " 720 is finished")
		print(name + " 480 is processing")
		subprocess.call(vid480, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)
		print(name + " 480 is finished")
	return duration.find_dur(curr_file)

def main():
	q = queue.Queue()
	fill_q(q)
	for i in range(3):
		worker = threading.Thread(target=ffmpeg_convert, args=(q,Path))
		worker.start()

if __name__ == "__main__":
	main()
	
