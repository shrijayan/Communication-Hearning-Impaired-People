import cv2
import numpy as np
from keras.models import load_model

CLASSES = ['background', 'aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car', 'cat', 'chair',
           'cow', 'diningtable', 'dog', 'horse', 'motorbike', 'person', 'pottedplant', 'sheep', 'sofa',
           'train', 'tvmonitor']

net = cv2.dnn.readNetFromCaffe('E:/Helmet detection/MobileNetSSD.prototxt.txt',
                               'E:/Helmet detection/MobileNetSSD.caffemodel')
loaded_model = load_model('E:/Helmet detection/helmetModel.h5')
loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

cap = cv2.VideoCapture("E:/Helmet detection/j3.mp4")
#cap = cv2.VideoCapture('rtsp://162it171:162it171@10.10.133.1:554/live')
# cap=cv2.VideoCapture(0)

count = 0

while True:
    ret, frame = cap.read()
    h = frame.shape[0]
    w = frame.shape[1]

    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)

    # pass the blob through the network and obtain the detections and predictions
    net.setInput(blob)

    detections = net.forward()  # getting the detections from the network

    persons = []
    motorbi = []
    boxes1 = []
    boxes2 = []

    # loop over the detections
    for i in np.arange(0, detections.shape[2]):

        # extract the confidence associated with the prediction
        confidence = detections[0, 0, i, 2]

        # filter out weak detections by ensuring the confidence
        # is greater than minimum confidence
        if confidence > 0.8:

            # extract index of class label from the detections
            idx = int(detections[0, 0, i, 1])

            if idx == 15 or idx == 14:
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
                # roi = box[startX:endX, startY:endY/4]
                # person_roi.append(roi)
                if idx == 14:
                    cv2.rectangle(frame, (startX, startY), (endX, endY), (170, 150, 30), 2)
                    cv2.putText(frame, "Bike", (startX, startY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (170, 150, 30), 2)

                    boxes1.append([startX, startY, endX, endY])

                if idx == 15:
                    cv2.rectangle(frame, (startX, startY), (endX, endY), (200, 55, 200), 2)
                    cv2.putText(frame, "person", (startX, startY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 55, 200), 2)

                    boxes2.append([startX, startY, endX, endY])

    boxA = boxes1
    boxB = boxes2
    for i in boxA:
        for j in boxB:
            xA = max(i[0], j[0])
            yA = max(i[1], j[1])
            xB = min(i[2], j[2])
            yB = min(i[3], j[3])
            # compute the area of intersection rectangle
            interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)
            # compute the area of both the prediction and ground-truth
            # rectangles
            boxAArea = (i[2] - i[0] + 1) * (i[3] - i[1] + 1)
            boxBArea = (j[2] - j[0] + 1) * (j[3] - j[1] + 1)
            # compute the intersection over union by taking the intersection
            # area and dividing it by the sum of prediction + ground-truth
            # areas - the intersection area
            iou = interArea / float(boxAArea + boxBArea - interArea)

            if iou > 0:

                startX = j[0]
                startY = j[1]
                endX = j[2]
                endY = j[3]
                img = frame
                img = img[startY:startY + 50, startX:endX]
                img_array = cv2.resize(img, (50, 50))
                gray_img = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
                img = np.array(gray_img).reshape(1, 50, 50, 1)
                img = img / 255.0
                prediction = loaded_model.predict([img])
                print(prediction)
                if prediction > 0.9:
                    cv2.rectangle(frame, (startX, startY - 20), (endX, startY + 50), (0, 255, 0), 2)
                    cv2.putText(frame, "helmet - " + str(prediction), (startX, startY), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                (0, 255, 0), 2)
                else:
                    cv2.rectangle(frame, (startX, startY - 20), (endX, startY + 50), (0, 0, 255), 2)
                    cv2.putText(frame, "no helmet - " + str(prediction), (startX, startY), cv2.FONT_HERSHEY_SIMPLEX,
                                0.5, (0, 0, 255), 2)
    cv2.imshow("Result", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
