import cv2
cap = cv2.VideoCapture(0)  # Sử dụng 0 để sử dụng camera mặc định, hoặc thay đổi thành tên file video
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
screen_width, screen_height = cap.get(3), cap.get(4)
distance_in_meters = 5
roi_width = int(screen_width)
roi_height = int(screen_height)

pixels_per_meter = 100
roi_width_pixels = int(roi_width * pixels_per_meter)
roi_height_pixels = int(roi_height * pixels_per_meter)

roi_x, roi_y = 0, 0  # Đặt vùng quan tâm ở góc trái trên của frame
roi_width, roi_height = roi_width_pixels, roi_height_pixels

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    boxes, weights = hog.detectMultiScale(frame, winStride=(8, 8), padding=(4, 4), scale=1.05)
    for (x, y, w, h) in boxes:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        if x > roi_x and y > roi_y and x+w < roi_x + roi_width and y+h < roi_y + roi_height:
            print("Người đã đi vào vùng quan tâm!")
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
