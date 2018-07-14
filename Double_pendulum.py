import cv2
import numpy as np
import math

# Dimensions of pendulum
# Length
r1 = 100
r2 = 100
# Mass
m1 = 10
m2 = 10
# Angles
a1 = math.pi/2
a2 = math.pi/4
a1_v = 0
a2_v = 0
# a1_a = 0.01
# a2_a = -0.001
g = 1

#px2 = 0
#py2 = 0

# Blank image
# window = np.ones([600,600,3], dtype=np.uint8)*255
prev = []
# height, width, layers = window.shape
# out = cv2.VideoWriter("output.avi", cv2.VideoWriter_fourcc(*"XVID"),60,(600,600))

def fram(a1,a2,a1_v,a2_v):

    window = np.ones([600,600,3], dtype=np.uint8)*255

    x1 = int(r1 * math.sin(a1))
    y1 = int(r1 * math.cos(a1))

    x2 = int(x1 + r2 * math.sin(a2))
    y2 = int(y1 + r2 * math.cos(a2))

    prev.append((x2,y2))

    cv2.line(window,(300,250),(300+x1,250+y1),(0,0,0),2)
    #cv2.circle(window,(300+x1,50+y1), m1, (0,0,0), -1)
    cv2.ellipse(window,(300+x1,250+y1), (m1,m1), 0,0,360,0, -1)

    cv2.line(window,(300+x1,250+y1),(300+x2,250+y2),(0,0,0),2)
    cv2.ellipse(window,(300+x2,250+y2), (m2,m2), 0,0,360,0, -1)

    if len(prev) > 1:
        for i in range(1,len(prev)):
            cv2.line(window,(300+prev[i-1][0],250+prev[i-1][1]),(300+prev[i][0],250+prev[i][1]),(0,0,0),2)

    cv2.imshow('Window', window)
    # cv2.waitKey(0)
    # out.write(window)



for i in range(1000):

	num1 = -g * (2 * m1 + m2) * math.sin(a1)
	num2 = -m2 * g * math.sin(a1 - 2 * a2)
	num3 = -2 * math.sin(a1 - a2) * m2
	num4 = a2_v * a2_v * r2 + a1_v * a1_v * r1 * math.cos(a1 - a2)
	den = r1 * (2 * m1 + m2 - m2 * math.cos(2 * a1 - 2 * a2))
	a1_a = (num1 + num2 + num3 * num4) / den

	num1 = 2 * math.sin(a1 - a2)
	num2 = (a1_v * a1_v * r1 * (m1 + m2))
	num3 = g * (m1 + m2) * math.cos(a1)
	num4 = a2_v * a2_v * r2 * m2 * math.cos(a1 -a2)
	den = r1 * (2 * m1 + m2 - m2 * math.cos(2 * a1 - 2 * a2))
	a2_a = (num1 * (num2 + num3 + num4)) / den
	# a2_a = 0
	a1_v += a1_a
	a2_v += a2_a

	a1 += a1_v
	a2 += a2_v

	fram(a1,a2,a1_v,a2_v)
	cv2.waitKey(0)

# out.release()
cv2.destroyAllWindows()
