#got from example pytest on class github
import subprocess
from pathlib import Path
import pytest
import shutil

DUR = '1'

EXE = shutil.which('ffmpeg')
if not EXE:
    raise FileNotFoundError('ffmpeg not found')


@pytest.fixture
def genpat(tmpdir) -> Path:
    """
    generate test video
    """
    vidfn = tmpdir / 'bars.avi'

    subprocess.check_call([EXE, '-v', 'warning', '-f', 'lavfi', '-i', 'smptebars', '-t', DUR, str(vidfn)])

    return vidfn
