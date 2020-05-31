# -*- coding: utf-8 -*-
"""
Created on Sun May 31 13:46:43 2020

@author: Aaditree Jaisswal
"""

from gtts import gTTS
import os

mytext="Hello there"

language='en'

output = gTTS(text = mytext,lang=language,slow=False)

output.save("output.mp3")

os.system("start output.mp3")