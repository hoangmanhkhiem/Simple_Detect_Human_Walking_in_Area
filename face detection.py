import cv2
cap = cv2.VideoCapture(0)  # Sử dụng 0 để sử dụng camera mặc định, hoặc thay đổi thành tên file video
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
roi_x, roi_y, roi_width, roi_height = 100, 100, 200, 200

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
