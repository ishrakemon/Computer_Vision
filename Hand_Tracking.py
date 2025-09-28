import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

mp_hands = mp.solutions.hands #Initializing MediaPipe hands and drawing utilities
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

#Initializing time for FPS calculation
pTime = 0
cTime = 0


while True:
    success, img = cap.read()
    if not success:
        print("Error: Could not read frame.")
        break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #BGR to RGB convertion
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for id, lm in enumerate(hand_landmarks.landmark):
                #print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy)
                if id == 0:
                    cv2.circle(img, (cx, cy), 10,(255, 0, 255), cv2.FILLED)


            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS) #Draws the Hand Connection and land marks

    #FPS Calculation
    cTime = time.time()
    fps = 1 / (cTime - pTime) if (cTime - pTime) > 0 else 0
    pTime = cTime
    cv2.putText(img, f"FPS: {int(fps)}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()