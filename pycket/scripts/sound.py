#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# GNU General Public License v3.0
# http://www.gnu.org/licenses
#
# (ɔ) Iván Rincón 2019

from os import devnull
from os.path import join
from subprocess import Popen, STDOUT
from pycket.misc.paths import SOUNDS_PTH
import wave
from math import ceil


class Sound:
    def __init__(self, wave_name):
        self.wave_file = self._get_file(wave_name)

    @staticmethod
    def _get_file(filename: str):
        return join(SOUNDS_PTH, "%s.wav" % filename.replace(" ", "-").lower())

    def duration(self):
        # milliseconds
        with wave.open(self.wave_file) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            return ceil(10 * frames / float(rate)) * 100

    def play_wav(self) -> Popen:
        return Popen(["aplay", self.wave_file], stdout=open(devnull, 'w'), stderr=STDOUT)
