import cv2
import mediapipe as mp

from pycaw.pycaw import AudioUtillities, IAudioEndpointValue
from comtypes import CLSCTX_ALL
from math import hypot
import screen_brightness_control as sbc

mp_hands = mp.solutions.hands
hands = mp.hands.Hands(min_detection_confidence = 0.7, min_tracking_confidence = 0.7)
mp.draw = mp.solution.drawing_utils

try:
    devices = AudioUtillities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointValue._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointValue)
    volume_range = volume.GetVolumeRange()
    min_vol = volume_range(0)
    max_vol = volume_range(1)

expect Exception as e:
    