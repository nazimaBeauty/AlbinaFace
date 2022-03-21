import cv2
from facerec import SimpleFacerec
from datetime import datetime, timedelta

sfr = SimpleFacerec()
# sfr.load_encoding_images("bmFirst/")
capture = cv2.VideoCapture("http://192.168.43.1:8080/video")
# capture = cv2.VideoCapture(2)

# lesson time
lesson1s = datetime.strptime('8:00:00', "%H:%M:%S")
lesson1f = datetime.strptime('8:45:00', "%H:%M:%S")

lesson2s = datetime.strptime('8:55:00', "%H:%M:%S")
lesson2f = datetime.strptime('9:40:00', "%H:%M:%S")

lesson3s = datetime.strptime('9:50:00', "%H:%M:%S")
lesson3f = datetime.strptime('10:30:00', "%H:%M:%S")

lesson4s = datetime.strptime('10:45:00', "%H:%M:%S")
lesson4f = datetime.strptime('11:30:00', "%H:%M:%S")

lesson5s = datetime.strptime('11:40:00', "%H:%M:%S")
lesson5f = datetime.strptime('12:25:00', "%H:%M:%S")

lesson6s = datetime.strptime('13:30:00', "%H:%M:%S")
lesson6f = datetime.strptime('14:15:00', "%H:%M:%S")

lesson7s = datetime.strptime('14:25:00', "%H:%M:%S")
lesson7f = datetime.strptime('15:10:00', "%H:%M:%S")

lesson8s = datetime.strptime('15:20:00', "%H:%M:%S")
lesson8f = datetime.strptime('16:05:00', "%H:%M:%S")

lesson9s = datetime.strptime('16:15:00', "%H:%M:%S")
lesson9f = datetime.strptime('17:0:00', "%H:%M:%S")

lesson10s = datetime.strptime('17:10:00', "%H:%M:%S")
lesson10f = datetime.strptime('17:55:00', "%H:%M:%S")

lesson11s = datetime.strptime('18:05:00', "%H:%M:%S")
lesson11f = datetime.strptime('18:50:00', "%H:%M:%S")

lesson12s = datetime.strptime('19:00:00', "%H:%M:%S")
lesson12f = datetime.strptime('19:45:00', "%H:%M:%S")

# current_date = datetime.now().day  month day

#  week day
week_day = datetime.today().weekday() + 1
print(week_day)
i = 0
while i < 5:

    # current time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    now_main = datetime.strptime(current_time, "%H:%M:%S")

    sfrChecker = True

    # day 1

    if lesson4s <= now_main <= lesson4f:
        if week_day == 1 and sfrChecker:
            print("bm304")
            sfr.load_encoding_images("bmThird/")

    elif lesson5s <= now_main <= lesson5f:
        if week_day == 1 and sfrChecker:
            print("bm304")
            sfr.load_encoding_images("bmThird/")

    # day 2

    if lesson2s <= now_main < lesson2f:
        if week_day == 2 and sfrChecker:
            print("bm402")
            sfr.load_encoding_images("bmFourth/")

    elif lesson3s <= now_main < lesson3f:
        if week_day == 2 and sfrChecker:
            print("bm402")
            sfr.load_encoding_images("bmFourth/")

    elif lesson4s <= now_main < lesson4f:
        if week_day == 2 and sfrChecker:
            print("bm402")
            sfr.load_encoding_images("bmFourth/")

    elif lesson5s <= now_main < lesson5f:
        if week_day == 2 and sfrChecker:
            print("bm402")
            sfr.load_encoding_images("bmFourth/")

    elif lesson6s <= now_main < lesson6f:
        if week_day == 2 and sfrChecker:
            print("bm102")
            sfr.load_encoding_images("bmFirst/")

    elif lesson7s <= now_main < lesson7f:
        if week_day == 2 and sfrChecker:
            print("bm102")
            sfr.load_encoding_images("bmFirst/")

    elif lesson8s <= now_main < lesson8f:
        if week_day == 2 and sfrChecker:
            print("bm102")
            sfr.load_encoding_images("bmFirst/")

    # day 3

    if lesson2s <= now_main < lesson2f:
        if week_day == 3 and sfrChecker:
            print("bm376")
            sfr.load_encoding_images("bmThird/")

    elif lesson3s <= now_main < lesson3f:
        if week_day == 3 and sfrChecker:
            print("bm376")
            sfr.load_encoding_images("bmThird/")

    elif lesson4s <= now_main < lesson4f:
        if week_day == 3 and sfrChecker:
            print("bm376")
            sfr.load_encoding_images("bmThird/")

    elif lesson6s <= now_main < lesson6f:
        if week_day == 3 and sfrChecker:
            print("bm108")
            sfr.load_encoding_images("bmFirst/")
    elif lesson7s <= now_main < lesson7f:
        if week_day == 3 and sfrChecker:
            print("bm108")
            sfr.load_encoding_images("bmFirst/")

    # day 4
    if lesson1s <= now_main < lesson1f:
        if week_day == 4 and sfrChecker:
            print("bm310")
            sfr.load_encoding_images("bmThird/")

    elif lesson2s <= now_main < lesson2f:
        if week_day == 4 and sfrChecker:
            print("bm310")
            sfr.load_encoding_images("bmThird/")

    elif lesson3s <= now_main < lesson3f:
        if week_day == 4 and sfrChecker:
            print("bm310")
            sfr.load_encoding_images("bmThird/")

    elif lesson4s <= now_main < lesson4f:
        if week_day == 4 and sfrChecker:
            print("bm310")
            sfr.load_encoding_images("bmThird/")

    elif lesson5s <= now_main < lesson5f:
        if week_day == 4 and sfrChecker:
            print("bm310")
            sfr.load_encoding_images("bmThird/")

    # day 5

    if lesson2s <= now_main < lesson2f:
        if week_day == 5 and sfrChecker:
            print("bm106")
            sfr.load_encoding_images("bmFirst/")

    elif lesson3s <= now_main < lesson3f:
        if week_day == 5 and sfrChecker:
            print("bm106")
            sfr.load_encoding_images("bmFirst/")

    newDate = now_main + timedelta(seconds=55)

    while True:
        lessonChecker = True
        _, frame = capture.read()

        location, name = sfr.detect_known_faces(frame)

        for loc, name in zip(location, name):
            y1, x2, y2, x1 = loc[0], loc[1], loc[2], loc[3]

            cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1,
                        (0, 255, 0), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
            if name != "Your lesson not today" and lessonChecker:
                text_file = open("data.txt", "w")
                text_file.write(name)
                text_file.close()
                lessonChecker = False

        cv2.imshow('livestream', frame)

        # current time
        now2 = datetime.now()
        current_time2 = now2.strftime("%H:%M:%S")
        now_main2 = datetime.strptime(current_time2, "%H:%M:%S")

        if now_main2 == newDate:
            print("break")
            break
        if cv2.waitKey(1) == ord("q"):
            break

    capture.release()
    cv2.destroyAllWindows()

    i = i + 10


