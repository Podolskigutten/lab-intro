import cv2


def lab00():
    device_id = 0
    cap = cv2.Videocapture(device_id)

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

        cv2.imshow(window_title, frame)

        delay_ms = 15
        key = cv2.waitKey(delay_ms)

        if key >= 0:
            break

    cap.release()
    cv2.destroyAllWindows()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    lab00()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
