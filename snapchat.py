import cv2

cap= cv2.VideoCapture(0)#for value 1 it showsup a black screen cause it is not using external camera

#cascade classfier imported
cascade= cv2.CascadeClassifier('anuhar.xml')
chasma_ori=cv2.imread('chasma.png', -1)
churot_ori=cv2.imread('cigar.png', -1)
junga_ori=cv2.imread('mus.png', -1)

#transparentoverlay function 
def transparent_Overlay(src, overlay, pos=(0,0), scale=1):
    overlay=cv2.resize(overlay,(0,0),fx=scale,fy=scale)
    #3D image so pass underscore _
    h,w= overlay.shape[:2] # size of foreground image
    rows,cols,_= src.shape #size of background image
    y,x=pos[0],pos[1]

    for i in range(h):
        for j in range(w):
            if x+i > rows or y+j >= cols:
                continue
            if overlay.shape[-1]==2:
                alpha=1
            else:
                alpha=float(overlay[i][j][3] / 255)
            #read the alpha channel
            #deleting the pixels coming from background image and putting foreground image on that.
            src[x + i, y + j] = alpha + overlay[i][j][:3]+[1-alpha] * src[x+i][y+j]
    return src
     
while cap.isOpened():
    result, frame= cap.read()
    # print(result)
    # print(frame)
    
    if result:
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #dtect fae in gray screen
        faces= cascade.detectMultiScale(grey, 1.3,5,0,minSize=(120,120),maxSize=(350,350))
        #rectangular box
        #faces will return array values x,y,w,h
        for (x,y,w,h) in faces:

            #cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255), 6)
            if h>0 and w>0:
                chasma_symin= int(y+ 1.5*h/5)
                chasma_symax=int(y+2.5*h/5)
                sh_chasma=chasma_symax-chasma_symin

                churot_symin= int(y+ 4.5*h/6)
                churot_symax=int(y+5.9*h/6)
                sh_churot=churot_symax-churot_symin


                junga_symin= int(y+ 3.5*h/6)
                junga_symax=int(y+5*h/6)
                sh_junga=junga_symax-junga_symin

                #putting this oientation on a particular frame
                face_chasma_ori= frame[chasma_symin:chasma_symax,x:x+w]
                churot_glass_ori= frame[churot_symin:churot_symax,x:x+w]
                mus_chasma_ori= frame[junga_symin:junga_symax,x:x+w]


                #resizing the orientation of different object 

                chasma = cv2.resize(chasma_ori,(w,sh_chasma),interpolation=cv2.INTER_CUBIC)
                churot = cv2.resize(churot_ori,(w,sh_churot),interpolation=cv2.INTER_CUBIC)
                junga = cv2.resize(junga_ori,(w,sh_junga),interpolation=cv2.INTER_CUBIC)


                #transparent the particular location of our frame: an also overlaying
                transparent_Overlay(face_chasma_ori,chasma)

                transparent_Overlay(mus_chasma_ori,junga)
                transparent_Overlay(churot_glass_ori, churot)
                




        
            


        cv2.imshow("frame", frame)
        if cv2.waitKey(1)==ord('q'):
            break
cap.release()#I donot want to store value in my cache
cv2.destroyAllWindows()#destroying all windows using our camera

