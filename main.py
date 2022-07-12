import cv2

trained_face_data = cv2.CascadeClassifier('haarcascade_Frontalface_cascade_default.xml')

# for live webcam video
webcam =  cv2.VideoCapture(0)

# for the video from the computer
# webcam = cv2.VideoCapture("vid1.mp4")


# iterate over the frames forever
while (True):
   
#    read the current frame
    successful_frame_read, frame =  webcam.read()

# must convert to graystyle
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    
    # detect faces
    face_cooradinates = trained_face_data.detectMultiScale(grayscaled_img)

# draw rectangles around faces
    for (x, y, w, h) in  face_cooradinates:
    
        cv2.rectangle(frame,(x, y), (x+w, y+h), (0, 255, 0), 2)
        
    cv2.imshow('clever programming face detector', frame)
    key = cv2.waitKey(1)

    if key == 81 or key == 113:
        break
    
webcam.release()
 