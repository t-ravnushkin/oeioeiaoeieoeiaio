import cv2

CONSOLE_WIDTH = 26 * 3

vidObj = cv2.VideoCapture("other_cat.mp4")

print("FPS: ", vidObj.get(cv2.CAP_PROP_FPS))
print("Frame count: ", vidObj.get(cv2.CAP_PROP_FRAME_COUNT))
print("Width: ", vidObj.get(cv2.CAP_PROP_FRAME_WIDTH))
print("Height: ", vidObj.get(cv2.CAP_PROP_FRAME_HEIGHT))

success = 1
ind = 0
while success:
    success, image = vidObj.read()
    if not success:
        break

    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    a_channel = lab[:, :, 1]
    th = cv2.threshold(a_channel, 100, 255, cv2.THRESH_BINARY)[1]
    image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    image[th == 0] = [0, 0, 0, 0]
    image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)

    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    dst = cv2.normalize(
        lab[:, :, 1],
        dst=None,
        alpha=0,
        beta=255,
        norm_type=cv2.NORM_MINMAX,
        dtype=cv2.CV_8U,
    )
    dst_th = cv2.threshold(dst, 100, 255, cv2.THRESH_BINARY_INV)[1]
    lab[:, :, 1][dst_th == 255] = 127
    image = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # hsv_image[..., 1] = hsv_image[..., 1] * 2
    image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
    cv2.imwrite("other_frames/frame%d.png" % ind, image)
    comprimg = cv2.resize(image, (CONSOLE_WIDTH, CONSOLE_WIDTH))
    cv2.imwrite("other_small_frames/frame%d.png" % ind, comprimg)
    ind += 1

cv2.destroyAllWindows()
vidObj.release()
