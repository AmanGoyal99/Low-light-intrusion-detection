
import time
import cv2
scale_factor = 1.16
min_neighbors = 5
min_size = (10, 10)
webcam=False 
def detect(path):
    cascade = cv2.CascadeClassifier(path)
    if webcam:
        video_cap = cv2.VideoCapture(0) 
    else:
        video_cap = cv2.VideoCapture("low_light_clip1.mp4")
    output = "face_output.avi"
    fourcc = cv2.VideoWriter_fourcc(*'DIVX') 
    ret, img = video_cap.read()
    height, width, channels = img.shape
    out = cv2.VideoWriter(output, fourcc, 5,(width,height))

    while True:
        
        ret, img = video_cap.read()
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        rects = cascade.detectMultiScale(gray, scaleFactor=scale_factor, minNeighbors=min_neighbors,
                                         minSize=min_size)
        
        if len(rects) >= 0:
        
            for (x, y, w, h) in rects:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            
            cv2.imshow('Face Detection on Video', img)
            out.write(img)
            time.sleep(0.05)
        
            if cv2.waitKey(1) & 0xFF == ord('c'):
                break
    video_cap.release()
    out.release()
def main():
    cascadeFilePath="haarcascade_frontalface_default.xml"
    detect(cascadeFilePath)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()