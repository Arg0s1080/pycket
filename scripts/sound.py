from os import getcwd
from os.path import dirname, join
from subprocess import Popen, PIPE
import wave
from subprocess import STDOUT, check_output
from math import ceil
from threading import Timer
from time import sleep

import os
sounds_pathX = join(getcwd().replace("scripts", ""), "sounds")
xxxx = join("/".join(getcwd().split("/")[:-1]), "sounds")
print(xxxx)
alarm_wav = join(sounds_pathX, "alarm.wav")
alarm_clock_wav = join(sounds_pathX, "alarm-clock-short.wav")
bicycle_wav = join(sounds_pathX, "bicycle-bell-2.wav")
button_chi_wav = join(sounds_pathX, "buttonchime02up.wav")
extreme_wav = join(sounds_pathX, "extreme-alarm.wav")
microwave_wav = join(sounds_pathX, "microwave-beep.wav")
tone_wav = join(sounds_pathX, "tone-beep.wav")

class Sound:
    def __init__(self, wave_name):
        self.wave_file = self._get_file(wave_name)

    @staticmethod
    def _get_file(filename: str):
        sounds_path = join("/".join(getcwd().split("/")[:-1]), "sounds")
        return join(sounds_path, "%s.wav" % filename.replace(" ", "-").lower())

    def duration(self):
        # milliseconds
        with wave.open(self.wave_file) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            return ceil(10 * frames / float(rate)) * 100

    def play_wav(self) -> Popen:
        return Popen(["aplay", self.wave_file], stdout=open(os.devnull, 'w'), stderr=STDOUT)


print(Sound("Extreme Alarm").duration())