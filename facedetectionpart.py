import cv2

cap= cv2.VideoCapture(0)#for value 1 it showsup a black screen cause it is not using external camera

#cascade classfier imported
cascade= cv2.CascadeClassifier('anuhar.xml')

while cap.isOpened():
    result, frame= cap.read()
    # print(result)
    # print(frame)
    
    if result:
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #dtect face in gray screen
        faces= cascade.detectMultiScale(grey, 1.3,5,0,minSize=(120,120),maxSize=(350,350))
        #rectangular box
        #faces will return array values x,y,w,h
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0), 4)


        cv2.imshow("frame", frame)
        if cv2.waitKey(5)==ord('q'):
            break
cap.release()#I donot want to store value in my cache
cv2.destroyAllWindows()#destroying all windows using our camera

