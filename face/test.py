import cv2
import face_recognition
import pandas as pd
import csv
from IPython.display import display

# open webcam (웹캠 열기)
webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not webcam.isOpened():
    print("Could not open webcam")
    exit()

sample_num = 0
captured_num = 0
face_encodings = pd.DataFrame()
# loop through frames
while webcam.isOpened():

    # read frame from webcam
    status, frame = webcam.read()
    sample_num = sample_num + 1

    if not status:
        break

    # display output

    face_location = face_recognition.face_locations(frame)
    face_encodings = face_encodings.append(pd.DataFrame(face_recognition.face_encodings(frame, face_location)))
    name='JHC'

    if len(face_encodings) == 10:
        face_encodings['name']=name
        face_encodings.to_csv('./result.csv')
        print("저장됨")
    if face_location:
        print(face_location)
        display(face_encodings)
        for (top, right, bottom, left) in face_location:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.imwrite(name + str(captured_num) + '.jpg', frame)


    cv2.imshow(f"captured frames", frame)
    if sample_num == 4:
        captured_num = captured_num + 1

        sample_num = 0

    # press "Q" to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release resources
webcam.release()
cv2.destroyAllWindows()