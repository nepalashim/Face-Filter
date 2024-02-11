import cv2

cap= cv2.VideoCapture(0)#for value 1 it showsup a black screen cause it is not using external camera

while cap.isOpened():
    result, frame= cap.read()
    # print(result)
    # print(frame)
    if result:
        cv2.imshow("frame", frame)
        if cv2.waitKey(5)==ord('q'):
            break
cap.release()#I donot want to store value in my cache
cv2.destroyAllWindows()#destroying all windows using our camera

