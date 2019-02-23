from main import ffmpeg_convert
import queue 
import pytest

def test_ffmpeg(genpat):
	q = queue.Queue()
	vid = str(genpat)
	q.put(vid)
	dur = ffmpeg_convert(q,vid)
	assert dur == pytest.approx(1.)

if __name__ == '__main__':
	pytest.main(['-x',__file__])