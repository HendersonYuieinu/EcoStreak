from ultralytics import YOLO
import cv2


cap = cv2.VideoCapture(0)
model = YOLO(r"runs\resultados5_ia\IDtrash_modelo-2\weights\best.pt")

while True:
    succes, img = cap.read()
    
    if succes:
        img = cv2.flip(img, 1)
        results = model(img)
        
        for result in results:
            img = result.plot()
        
        cv2.imshow("teste", img)
    k = cv2.waitKey(1)
    if k == ord("q"):
        break
    

cap.release()
cv2.destroyAllWindows()