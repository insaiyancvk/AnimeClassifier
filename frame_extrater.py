import cv2
vidcap = cv2.VideoCapture('D:\Downloads\DB dataset\chichi\chichi.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
  count += 20
  vidcap.set(1, count)
  success,image = vidcap.read()
  print(f'Read frame {count}: ', success)