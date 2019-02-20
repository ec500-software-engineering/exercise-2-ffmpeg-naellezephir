import queue
import threading
import subprocess
import os


path = '/Users/naellezephir/Desktop/GitHub/exercise-2/videos'
outpath = '/Users/naellezephir/Desktop/GitHub/exercise-2/videos/finished'

def fill_q(Q):
	folder = os.listdir(path)
	for file in folder:
		Q.put(file)

def ffmpeg_convert(Q):
	while True:
		curr_file = Q.get()
		vid720 = "ffmpeg -i "+path+"/"+curr_file+" -s hd720 -b:v 1M -r 30 "+outpath+"/"+curr_file[:-4]+"720.mp4"
		vid480 = "ffmpeg -i "+path+"/"+curr_file+" -s hd720 -b:v 1M -r 30 "+outpath+"/"+curr_file[:-4]+"480.mp4"
		print(curr_file + " 720 is processing")
		subprocess.call(vid720, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)
		print(curr_file + " 720 is finished")
		print(curr_file + " 480 is processing")
		subprocess.call(vid480, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)
		print(curr_file + " 480 is finished")


def main():
	q = queue.Queue()
	fill_q(q)
	for i in range(2):
		worker = threading.Thread(target=ffmpeg_convert, args=(q,))
		worker.start()

if __name__ == "__main__":
	main()
	
