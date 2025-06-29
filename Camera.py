# import cv2
# import time
#
# cap = cv2.VideoCapture(0)
#
# if not cap.isOpened():
#     print("Cannot open camera")
#     exit()
#
# # 循环直到视频结束
# while cap.isOpened():
#     # 读取下一帧
#     ret, frame = cap.read()
#
#     # 如果正确读取帧，ret为True
#     if not ret:
#         print("无法读取视频流或视频结束")
#         break
#
#     # 显示帧
#     cv2.imshow("Video", frame)
#
#     # 按'ESC'退出视频
#     if cv2.waitKey(10) & 0xFF == 27:
#         break
#
# cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)
# cap.set(cv2.CAP_PROP_FOCUS, 100)
#
# current_focus = cap.get(cv2.CAP_PROP_FOCUS)
# print("Current focus: ", current_focus)
#
# time.sleep(1)
#
# focus_value = current_focus + 10
# cap.set(cv2.CAP_PROP_FOCUS, focus_value)
#
# new_focus = cap.get(cv2.CAP_PROP_FOCUS)
# print("New focus: ", new_focus)
#
# cap.release()
# text = "@珐露珊瑚宫\u202d\u202d\u2067~喵\u2067\u202d 超市你"
# print(text)
import cv2
import time
import sys

# print("开始拍摄图片")
# images = []
# for i in range(10):
#     time.sleep(0.5)
#     images.append(cv2.VideoCapture(0).read()[1])

imgs = []
imgs.append(cv2.imread("1.jpg"))
imgs.append(cv2.imread("2.jpg"))
# imgs.append(cv2.imread("3.jpg"))

stitcher = cv2.Stitcher.create()
status, pano = stitcher.stitch(imgs)

if status == cv2.Stitcher_OK:
    cv2.imshow("pano", pano)
    cv2.waitKey(0)
else:
    sys.exit("Error during stitching")

cv2.imwrite("output.jpg", pano)
print("Done")
