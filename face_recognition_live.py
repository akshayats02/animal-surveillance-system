cam = cv2.VideoCapture(0)
# recognizer = cv2.face.LBPHFaceRecognizer_create()
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, im =cam.read()
 
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        if(conf<70):
            if(Id==1):
                Id="akshaya"
                
            
            
        else:
            Id="Unknown"
            ser.write(b"u#")
        cv2.putText(im, str(Id), (x,y-40), font, 1, (255,255,255), 3)
        
	
    im=cv2.resize(im,(600,400))
    
    cv2.imshow('face',im) 
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break
    
cam.release()
cv2.destroyAllWindows()
