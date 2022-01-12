import cv2


def camera():

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    eyeCascade = cv2.CascadeClassifier("haarcascade_eye.xml")

    if not cap.isOpened():
        print("Cannot not find camera...")
        return

    while(True):

        try:

            ret, frame = cap.read()
            if not ret:
                print("No signal! Exiting..")
                break

            eyeRect = eyeCascade.detectMultiScale(frame, 1.2, 3)

            eye_img = frame

            for(x, y, w, h) in eyeRect:

                eye_img = frame[y-10:y+h+10, x-10:x+h+10]
                eye_img = cv2.resize(eye_img, (0, 0), fx=2.0, fy=2.0)

                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            cv2.imshow("camera", frame)

            cv2.imshow("eye_window", eye_img)

            if cv2.waitKey(100) == ord('e'):
                cv2.imwrite('./outputData/eye.jpg', eye_img)
                cap.release()
                cv2.destroyAllWindows()
                break

        except:
            continue


if __name__ == '__main__':
    camera()
