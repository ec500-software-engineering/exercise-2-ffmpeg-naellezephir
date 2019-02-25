from ffmpeg import ffmpeg_convert
import queue 
import pytest
import duration

def test_ffmpeg(genpat):
	q = queue.Queue()
	vid = str(genpat)
	q.put(vid)
	original_duration = duration.find_dur(vid)
	dur = ffmpeg_convert(q,vid)
	assert original_duration == dur

if __name__ == '__main__':
	pytest.main(['-x',__file__])