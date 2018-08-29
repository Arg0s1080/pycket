from os import devnull
from os.path import dirname, join, pardir
from subprocess import Popen, PIPE, STDOUT, check_output
import wave
from math import ceil


class Sound:
    def __init__(self, wave_name):
        self.wave_file = self._get_file(wave_name)

    @staticmethod
    def _get_file(filename: str):
        sounds_path = join(pardir, "resources", "sounds")
        return join(sounds_path, "%s.wav" % filename.replace(" ", "-").lower())

    def duration(self):
        # milliseconds
        with wave.open(self.wave_file) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            return ceil(10 * frames / float(rate)) * 100

    def play_wav(self) -> Popen:
        return Popen(["aplay", self.wave_file], stdout=open(devnull, 'w'), stderr=STDOUT)
