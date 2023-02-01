import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(
    img,
    "The Sun",
    (40,100),
    fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=3,
    color=(0,0,255)
)

cv2.putText(
    img,
    "Mercury",
    (40,200),
    fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=1,
    color=(0,255,255)
)

cv2.putText(
    img,
    "Venus",
    (183,180),
    fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=1,
    color=(255,255,255)
)

cv2.putText(
    img,
    "Earth",
    (280,270),
    fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=1,
    color=(255,0,0)
)

cv2.putText(
    img,
    "Mars",
    (373,180),
    fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=1,
    color=(255,0,0)
)

cv2.putText(
    img,
    "Jupiter",
    (475,400),
    fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=2,
    color=(255,255,255)
)

cv2.putText(
    img,
    "Saturn",
    (750,100),
    fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=1,
    color=(0,100,100)
)

cv2.putText(
    img,
    "Uranus",
    (952,300),
    fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=1,
    color=(250,200,200)
)

cv2.putText(
    img,
    "Neptune",
    (1095,137),
    fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
    fontScale=1,
    color=(250,100,100)
)

cv2.imshow("output",img)
cv2.waitKey(0)