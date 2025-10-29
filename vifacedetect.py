import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(cv2.CAP_ANY) 
# 
# To use a video file as input
# cap = cv2.VideoCapture('filename.mp4')
if not cap.isOpened():
    print('Cannot open camera. Make sure you have a webcam, ')
    print("and that it's not being used by another app.")
    exit()
    
while True:
    # Read the frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Error reading frame. Exiting ...")
    # Display
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray)
    print('detected face(s) at:', faces)
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 5)
    cv2.imshow('q to quit', frame)
    # Stop if q key is pressed
    if cv2.waitKey(30) == ord('q'):
        break
# Release the VideoCapture object
cap.release()
cv2.destroyAllWindows()
