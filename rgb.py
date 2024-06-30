import cv2
import numpy as np 
  

video = cv2.VideoCapture(0) 
  

while True: 
  
  
    _, frame = video.read() 
  
    
    cv2.imshow("frame", frame)  
  
  
    b = frame[:, :, :1] 
    g = frame[:, :, 1:2] 
    r = frame[:, :, 2:] 
  
  
    b_mean = np.mean(b) 
    g_mean = np.mean(g) 
    r_mean = np.mean(r) 
  

    if (b_mean > g_mean and b_mean > r_mean): 
        print("Blue") 
    if (g_mean > r_mean and g_mean > b_mean): 
        print("Green") 
    else: 
        print("Red")