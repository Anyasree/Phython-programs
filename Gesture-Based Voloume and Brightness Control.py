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

except Exception as e:
    print(f"Error initialising Pycaw: {e}")
    exit()

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error coyuld not access the webcam")
    exit()

while True:
    sucess, img = cap.read()
    if not success:
        print("Failed top read frame from webcam.")
        break

    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks and results.multi_handedness:
        for i, hand_landmarks in enumerate(results.multi_hand_landmarks):
            hand_label = results. multi_handedness[i].classification[0].label
        
            mp_draw.draw_landmarks(img,hand_landmarks, mp_hands.HAND_CONNECTIONS)
            thumb_tip = hand.landmarks.landmark[mp.hands.HandLandmark.THUMB_TIP]
            index_tip = hand.landmarks.landmark[mp.hands.HandLandmark.INDEX_FINGER_TIP]

            h, w, _ = img.shape
            thumb_pos = (int(thumb_tip.x * w), int(thumb_tip.y * h))
            index_pos = (int(index_tip.x * w), int(index_tip.y * h))
            
            cv2.circle(img, thumb_pos, 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, index_pos, 10, (255, 0, 0), cv2.FILLED)
            cv2.line(img, thumb_pos, index_pos, (0, 255, 0), 3)

            distance = hypot(index_pos[0] - thumb_pos(0), index_pos[1] - thumb_pos[1])
            if hand_label == "Right":
                vol = np.interp(distance, [30, 300], [min_vol], [max_vol])
                try:
                    volume.SetMasterVolumeLevel(vol, None)
                except Eception as e:
                        print("Error Adjusting Volume: {e}")

                vol_bar = interp(distance, [30, 300], [400, 150])
                cv2. rectangle(img, (50, 150), (85, 400), (255, 0, 0), 2)
                cv2. rectangle(img, (50, int(vol_bar)), (85, 400), (255, 0, 0), cv2.FILLED)
                cv2.putText(img, f'Volume: {int(np.interp(distance, [30, 300], [0, 100]))}%' , (40,450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

            elif hand_label == "Left" : 
                brightness = np.interp(distance, [30, 300], [0, 100])
                try:
                    sbc.set_brightness(brightness)
                except Exception as e:
                    print(f"Error adjusting brightness: {e}")

                brightness_bar = np.interp(distance, [30, 300], [400, 150])
                cv2.rectangle(img, (100, 150), (135, 400), (0, 255, 0), 2)
                cv2.rectangle(img, (100, int(brightness_bar)), (135, 400), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, f'Brightness: {int(brightness)}%', (90, 450), cv2.FONT_HERSHEYS_SIMPLEX, 1, (0, 255, 0), 3)

    cv.imshow("Gesture Volume and Brightness Controller", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
