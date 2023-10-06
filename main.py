
from fastapi import FastAPI
from pydantic import BaseModel



import urllib.request
import cv2
import cv2.data


app = FastAPI()
class Item(BaseModel):
    img_url: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

def face_detect(image):
    i = 0
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,1.3,5)
    print(faces)

    if len(faces) > 0:
        print('anh ok day')
        return {"image": 1}
    return {"image": 0}


    for (x, y, w, h) in faces:
        i = i+1
        cv2.rectangle(img, (x, y), (x + w, y + h), (95, 207, 30), 3)
        cv2.rectangle(img, (x, y - 40), (x + w, y),(95, 207, 30) , -1)
        cv2.putText(img, 'F-'+str(i), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)
    cv2.imshow("Faces found", img)
    cv2.waitKey(0)

@app.post("/img/")
def download_temp_img(item: Item):
    urllib.request.urlretrieve(item.img_url, "local-filename1.jpg")
    print(item.img_url)
    #face_detect('local-filename1.jpg')
    i = 0
    img = cv2.imread('local-filename1.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,1.3,5)
    print(faces)

    if len(faces) > 0:
        print('anh ok day')
        return True
    return False


    for (x, y, w, h) in faces:
        i = i+1
        cv2.rectangle(img, (x, y), (x + w, y + h), (95, 207, 30), 3)
        cv2.rectangle(img, (x, y - 40), (x + w, y),(95, 207, 30) , -1)
        cv2.putText(img, 'F-'+str(i), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)
    cv2.imshow("Faces found", img)
    cv2.waitKey(0)



