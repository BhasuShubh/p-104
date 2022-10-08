import cv2

system =cv2.imread("solar-system.jpg")
cv2.putText(system, "Mercury", (120, 190), cv2.FONT_HERSHEY_COMPLEX, 0.4, (255,255,255))
cv2.putText(system, "Venus", (190, 175), cv2.FONT_HERSHEY_COMPLEX, 0.4, (255,255,255))
cv2.putText(system, "Earth", (290, 160), cv2.FONT_HERSHEY_COMPLEX, 0.4, (255,255,255))
cv2.putText(system, "Mars", (380, 180), cv2.FONT_HERSHEY_COMPLEX, 0.4, (255,255,255))
cv2.putText(system, "Jupiter", (540, 30), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255,255,255))
cv2.putText(system, "Saturn", (780, 120), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,255,255))
cv2.putText(system, "Uranus", (950, 140), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,255,255))
cv2.putText(system, "Neptune", (1100, 140), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,255,255))
cv2.imshow("solar System",system)
cv2.waitKey(0)