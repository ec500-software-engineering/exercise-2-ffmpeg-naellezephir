import queue
import threading
import subprocess
import os

q = queue.Queue()
path = '/Users/naellezephir/Desktop/GitHub/exercise-2/videos'
outpath = '/Users/naellezephir/Desktop/GitHub/exercise-2/videos/finished'

def fill_q():
	folder = os.listdir(path)
	for file in folder:
		q.put(file)

def ffmpeg_convert():
	while not q.empty():
		curr_file = q.get()
		vid720 = "ffmpeg -i "+path+"/"+curr_file+" -s hd720 -b:v 1M -r 30 "+outpath+"/"+curr_file[:-4]+"720.mp4"
		vid480 = "ffmpeg -i "+path+"/"+curr_file+" -s hd720 -b:v 1M -r 30 "+outpath+"/"+curr_file[:-4]+"480.mp4"
		vid1 = subprocess.call(vid720, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)
		print(curr_file + " 720 is finished")
		vid2 = subprocess.call(vid480, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)
		print(curr_file + " 480 is finished")


def main():
	fill_q()
	for i in range(2):
		worker = threading.Thread(target=ffmpeg_convert)
		worker.start()

if __name__ == "__main__":
	main()
	
