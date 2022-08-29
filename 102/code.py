
import cv2
import dropbox
import time
import random
start_time=time.time()
def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name="img"+str(number)+".png"   
        cv2.imwrite(img_name,frame)
        start_time=time.time   
        result=False
    return img_name
    print("snapShort Taken")

    videoCaptureObject.release()
    cv2.destroyAllWindows()
def upload_files(img_name):
    access_token="sl.BOSlHGfDUsErP8o8tZs1OentMdLxD-EBpPcmKK0E3kNXimxIcgg7o3GYGRVbX-VCR2tXKEJv9wAjIwIuR4iK-AaX-zP_4EKTz-QUwp7J46QvLHcQyjIzE6485iI38HMt_cRP7NXGoSyy"
    file=img_name
    file_from=file
    file_to="/testfolder/"+(img_name)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,'rb')as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("files uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=300):
            upload_files(take_snapshot())

main()