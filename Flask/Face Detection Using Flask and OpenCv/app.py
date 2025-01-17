from flask import Flask,render_template,Response
import cv2

app=Flask(__name__)

camera=cv2.VideoCapture(0)

def stream():
    while True:
        success,frame=camera.read() #Used for reading the camera frame
        if not success:
            break
        else:
            face_detector=cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
            eye_detector=cv2.CascadeClassifier('Haarcascades/haarcascade_eye.xml')
            faces=face_detector.detectMultiScale(frame,1.1,7)
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

            # Drawing rectangle around the face
            for (x,y,w,h) in faces:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray=gray[y:y+h,x:x+w]
                roi_color=frame[y:y+h,x:x+w]
                eyes=eye_detector.detectMultiScale(roi_gray,1.1,3)
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()
            yield(b'--frame\r\n'
                  b'Content-Type: image/jpeg\r\n\r\n'+frame+b'\r\n')        

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/video_feed')
def video():
    return Response(stream(),mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__=='__main__':
    app.run(debug=True)