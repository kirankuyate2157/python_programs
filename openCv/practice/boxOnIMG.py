
import numpy as np
import cv2 as cv

# createing blank image .......
blank = np.zeros((500, 500, 3), dtype='uint8')
# draw rectangle....
# img = cv.rectangle(blank, (10, 0), (120, 200), (23, 255, 350), thickness=3)
# cv.imshow("myimg", img)

# show color any where on img...
# blank[234:456,232:345]=34,45,452
# cv.imshow("my pik",blank)

# draw circle on image...
# img2=cv.circle(blank,(250,250),130,(0,234,45),thickness=3)
# cv.imshow("img2",img2)

# draw line on image....
# img3=cv.line(blank,(0,0),(250,250),(230,340,255),thickness=4)
# cv.imshow("circle img",img3)

# write name on images
img4 = cv.putText(blank, "kiran", (120, 156), cv.FONT_HERSHEY_PLAIN, 4,
                  (75, 233, 453), 4)
cv.imshow("text", img4)

cv.waitKey(0)