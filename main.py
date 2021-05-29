# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////
import sqlite3
import sys
import os
import platform
import threading
import cv2
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
import face_recognition
import numpy as np

from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%



# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global face_locations
        global face_names
        global widgets
        global selected_name
        widgets = self.ui
        face_locations = []
        face_names = []
        selected_name = ''
        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "PyDracula - Modern GUI"
        description = "FaceLink - 얼굴인식 자동로그인"
        # APPLY TEXTS
        self.setWindowTitle(title)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
#        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_bookmark.clicked.connect(self.buttonClick)
        widgets.function_button.clicked.connect(self.buttonClick)
        widgets.complete.clicked.connect(self.buttonClick)
        widgets.editbutton1.clicked.connect(self.buttonClick)
        widgets.editbutton1_2.clicked.connect(self.buttonClick)
        widgets.editbutton1_3.clicked.connect(self.buttonClick)
        widgets.editbutton1_4.clicked.connect(self.buttonClick)
        widgets.editbutton1_5.clicked.connect(self.buttonClick)
        widgets.editbutton1_6.clicked.connect(self.buttonClick)
        widgets.delbutton1.clicked.connect(self.buttonClick)
        widgets.delbutton1_2.clicked.connect(self.buttonClick)
        widgets.delbutton1_3.clicked.connect(self.buttonClick)
        widgets.delbutton1_4.clicked.connect(self.buttonClick)
        widgets.delbutton1_5.clicked.connect(self.buttonClick)
        widgets.delbutton1_6.clicked.connect(self.buttonClick)
        widgets.bookpage1.clicked.connect(self.link_bookmark)
        widgets.bookpage2.clicked.connect(self.link_bookmark)
        widgets.bookpage3.clicked.connect(self.link_bookmark)
        widgets.bookpage4.clicked.connect(self.link_bookmark)
        widgets.bookpage5.clicked.connect(self.link_bookmark)
        widgets.bookpage6.clicked.connect(self.link_bookmark)
        widgets.complete_2.clicked.connect(self.edit_bookmark)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))
        global running
        running = True
        th = threading.Thread(target=self.run)
        th.start()
        print("started..")

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def run(self):
        known_face_encodings = [np.load(f"./encodings/{path}") for path in os.listdir("./encodings")]
        known_face_names = [os.path.splitext(path)[0] for path in os.listdir("./encodings")]
        # Initialize some variables
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        widgets.camLabel.resize(width, height)
        global captured_img
        global face_locations
        global face_names
        global face_encodings
#
        face_encodings = []

        process_this_frame = True
        while running:
            ret, img = cap.read()
            small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = small_frame[:, :, ::-1]
            if process_this_frame:
                last_locations = face_locations.copy()
                last_names = face_names.copy()
                last_encodings = face_encodings.copy()
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
                face_names = []
                for face_encoding in face_encodings:
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    name = "Unknown"
                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    if face_distances.size:
                        best_match_index = np.argmin(face_distances)
                        if matches[best_match_index]:
                            name = known_face_names[best_match_index]
                    face_names.append(name)
            process_this_frame = not process_this_frame
            if not len(face_locations):
                face_locations = last_locations
                face_names = last_names
                face_encodings = last_encodings
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                captured_img = img
                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4
                # Draw a box around the face
                cv2.rectangle(img, (left, top), (right, bottom), (146, 101, 57), 2)
                # Draw a label with a name below the face
                cv2.rectangle(img, (left, bottom - 25), (right, bottom), (146, 101, 57), cv2.FILLED)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(img, name, (left + 6, bottom-5), font, 0.8, (255, 255, 255), 1)
            img_converted = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            h, w, c = img.shape
            qImg = QImage(img_converted.data, w, h, w * c, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qImg)


            # draw rounded rect on new pixmap using original pixmap as brush

            widgets.camLabel.setPixmap(pixmap)
        cap.release()

    def buttonClick(self):
        # GET BUTTON CLICKED
        global running
        running = False
        btn = self.sender()
        btnName = btn.objectName()
        global btnNumber
        try:
            number = int(btnName[-1])
        except:
            number = 0

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            running = True
            th = threading.Thread(target=self.run)
            th.start()
            print("started..")

        elif btnName == "complete":
            # user add start
            uname = np.array(selected_encoding)
            np.save(f"./encodings/{widgets.adduserName.text()}", uname)
            ins = 'INSERT INTO student (name, ID, PW, url) VALUES(?, ?, ?, ?)'
            for i, url in zip(range(1,7),
                             [
                              'https://eis.cbnu.ac.kr/cbnuLogin',
                              'https://www.naver.com/',
                              'https://www.instagram.com/',
                              'https://www.daum.net/',
                              'https://cbnu.blackboard.com/',
                              'https://everytime.kr/'
                              ]):
                curs.execute(ins, (widgets.adduserName.text()+str(i), '', '', url))
            conn.commit()

            print('데이터가 저장되었습니다.')
            widgets.stackedWidget.setCurrentWidget(widgets.bookmark)
            UIFunctions.resetStyle(self, "btn_bookmark")
            widgets.btn_bookmark.setStyleSheet(UIFunctions.selectMenu(widgets.btn_bookmark.styleSheet()))

        elif btnName == "function_button":
            if selected_name == "Unknown":
                widgets.stackedWidget.setCurrentWidget(widgets.add)
            else:
                widgets.stackedWidget.setCurrentWidget(widgets.bookmark)
                UIFunctions.resetStyle(self, "btn_bookmark")
                widgets.btn_bookmark.setStyleSheet(UIFunctions.selectMenu(widgets.btn_bookmark.styleSheet()))
        elif btnName.find('edit') != -1:
            btnNumber = number
            widgets.stackedWidget.setCurrentWidget(widgets.pageinfo)
            UIFunctions.resetStyle(self, btnName)
        elif btnName.find('del') != -1:
            ins = f'SELECT * FROM student WHERE name = {selected_name}{number}'
            curs.execute(ins)
            rows = curs.fetchall()
            if rows:
                ins = f'DELETE FROM student WHERE name = {selected_name}{number}'
                curs.execute(ins)
                #팝업창print("삭제하였습니다.")
            else:
                pass
                #팝업창print("해당 학번의 학생은 존재하지 않습니다.")
            conn.commit()
        # SHOW WIDGETS PAGE
        elif btnName == "btn_bookmark":
            widgets.stackedWidget.setCurrentWidget(widgets.bookmark)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # AUTO LOGIN
    def link_bookmark(self):
        btn = self.sender()
        btnName = btn.objectName()
        print(1)
        number = int(btnName[-1])
            # 자동화 로그인 하고 싶은 url 입력.
        curs.execute(f'SELECT * FROM student WHERE name = {selected_name}{number}')
        rows = curs.fetchall()
        if len(rows):
            for (ID, PW, url) in rows:
                self.autologin(ID, PW, url)
        else:
            #팝업으로 아이디 비밀번호 등록 필요!
            pass

    def edit_bookmark(self):
        btn = self.sender()
        btnName = btn.objectName()
        number = int(btnName[-1])
        print(selected_name+str(btnNumber))
        ins = f'UPDATE student SET ID="{widgets.adduserName_2.text()}", PW="{widgets.adduserName_3.text()}" WHERE name = "{selected_name}{str(btnNumber)}"'
        curs.execute(ins)
        conn.commit()
        widgets.stackedWidget.setCurrentWidget(widgets.bookmark)
        UIFunctions.resetStyle(self, btnName)
        btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

    # AUTO LOGIN EVENTS
    def autologin(self, ID, PW, url):
        driver = webdriver.Chrome('c:/informs/chromedriver.exe')
        driver.implicitly_wait(3)

        driver.get(url)
        id = ID
        pw = PW
        # CBNU Blackboard
        if url == "https://cbnu.blackboard.com/":
            driver.find_element_by_name('uid').send_keys(id)
            time.sleep(1)
            driver.find_element_by_name('pswd').send_keys(pw)
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="entry-login"]').click()

        # CBNU 개신누리
        if url == "https://eis.cbnu.ac.kr/cbnuLogin":
            time.sleep(1)
            driver.find_element_by_name('uid').send_keys(id)
            time.sleep(1)
            driver.find_element_by_name('pswd').send_keys(pw)
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="commonLoginBtn"]').click()
        # Daum
        # ty 선택 카카오계정으로 로그인 OR 다음계정으로 로그인
        if url == "https://www.daum.net/":
            driver.get("https://logins.daum.net/accounts/ksso.do?url=https%3A%2F%2Fwww.daum.net%2F")
            driver.find_element_by_name('email').send_keys(id)
            time.sleep(1)
            driver.find_element_by_name('password').send_keys(pw)
            time.sleep(1)
            driver.find_element_by_class_name('btn_g').click()

        # Instargram
        if url == "https://www.instagram.com/":
            driver.find_element_by_name('username').send_keys(id)
            time.sleep(1)
            driver.find_element_by_name('password').send_keys(pw)
            time.sleep(1)
            driver.find_element_by_class_name('Igw0E').click()

        # Naver
        if url == "https://www.naver.com/":
            time.sleep(1)
            driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
            # 아이디 입력폼
            tag_id = driver.find_element_by_name('id')
            tag_pw = driver.find_element_by_name('pw')
            tag_id.click()
            pyperclip.copy(id)
            tag_id.send_keys(Keys.CONTROL, 'v')
            time.sleep(1)
            tag_pw.click()
            pyperclip.copy(pw)
            tag_pw.send_keys(Keys.CONTROL, 'v')
            time.sleep(1)
            driver.find_element_by_id('log.login').click()
            time.sleep(2)

        # Everytime
        if url == "https://everytime.kr/":
            time.sleep(1)
            driver.get("https://everytime.kr/login")
            driver.find_element_by_name('userid').send_keys(id)
            time.sleep(1)
            driver.find_element_by_name('password').send_keys(pw)
            time.sleep(1)
            driver.find_element_by_class_name('submit').click()


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        global face_locations
        global face_names
        global selected_encoding
        global selected_name
        self.dragPos = event.globalPos()
        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if running:
            x = event.x() - widgets.camLabel.x() - widgets.leftMenuBg.width()
            y = event.y() - widgets.camLabel.y() - widgets.contentTopBg.height()
            for (top, right, bottom, left), name, encoding in zip(face_locations, face_names, face_encodings):
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4
                if (right >= x >= left) and (bottom >= y >= top):
                    print(name)
                    selected_name = name
                    slicedImg = captured_img[top:bottom, left:right]
                    slicedImg = cv2.cvtColor(slicedImg, cv2.COLOR_BGR2RGB)
                    h, w, c = slicedImg.shape
                    qImg = QImage(slicedImg.data, w, h, w * c, QImage.Format_RGB888)
                    pixmap = QPixmap.fromImage(qImg)
                    widgets.slicedPicture.setPixmap(pixmap)
                    widgets.selectedId.setText(QCoreApplication.translate("MainWindow", name, None))
                    selected_encoding = encoding
                    if name == "Unknown":
                        widgets.function_text.setText(QCoreApplication.translate("MainWindow", "회원가입", None))
                    else:
                        widgets.function_text.setText(QCoreApplication.translate("MainWindow", "로그인", None))



if __name__ == "__main__":
    with sqlite3.connect('school.db') as conn:
        curs = conn.cursor()
        curs.execute('''CREATE TABLE IF NOT EXISTS student
            (name VARCHAR(20) PRIMARY KEY, ID VARCHAR(20), PW VARCHAR(20), url VARCHAR(100))''')
        app = QApplication(sys.argv)
        app.setWindowIcon(QIcon("icon.ico"))
        window = MainWindow()
        sys.exit(app.exec())
        conn.commit()
        conn.close()
