import cv2


def lab00():
    device_id = 1
    cap = cv2.VideoCapture(device_id)

    if not cap.isOpened():
        print(f"Could not open camera {device_id}")
        return
    else:
        print(f"Successfully opened camera {device_id}")
    
    window_title = "Lab 0: Introduction to Python and OpenCV"
    cv2.namedWindow(window_title, cv2.WINDOW_GUI_NORMAL)


    while True:
        success, frame = cap.read()

        if not success:
            print(f"The Image capture did not succeed. Is the camera ok?")
            break


        edges = cv2.Canny(frame, 100, 200)
        blurry = cv2.blur(frame, ksize=(200,200))
        cv2.imshow(window_title, blurry)
        #cv2.imshow("Edges", edges)

        delay_ms = 10
        key = cv2.waitKey(delay_ms)

        if key >= 0:
            break

    cap.release()
    cv2.destroyAllWindows()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    lab00()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
