import sys # 시스템정보관련 모듈 가져오기
from PyQt5.QtWidgets import * # Qt프로그램 구동을 위한 도구모음
from PyQt5 import uic, QtCore, QtGui, QtWidgets # ui를 다룰수있는 도구모음
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from db import *
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEnginePage, QWebEngineSettings

from PyQt5.QtWidgets import QTableWidgetItem


dbConn = MemberDBconn()
dbConn2 = DataDBConn()
# dbConn2.modify_user_table()

# ui 파일의 설정값을 가져오기
login_class = uic.loadUiType('UI/login.ui')[0]
join_class = uic.loadUiType('UI/join.ui')[0]
joincheck_class = uic.loadUiType('UI/joincheck.ui')[0]
mainwindow_class = uic.loadUiType('UI/MainWindow.ui')[0]

# 초기 로그인 화면
class Start_Class(QDialog,login_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_login.clicked.connect(self.mainwindow_show) #시그널 연결 
        self.btn_Join.clicked.connect(self.join_show)
        self.setWindowTitle("Book bug")
        self.setWindowIcon(QIcon("image/icon.png"))
        qPixmapVar = QPixmap()
        qPixmapVar.load("image/로그인.jpg")
        self.image_label.setPixmap(qPixmapVar)

        
    
    def mainwindow_show(self): #슬롯 , 동작
        inputId = self.txt_User_ID.text()
        inputPw = self.txt_User_PW.text()
        name = dbConn.login_select(inputId, inputPw)
        if name == 0:
            Start.login_result.setText('로그인 실패')
        else:
            MainWindow.show()
            Start.close()
        self.txt_User_ID.setText('')
        self.txt_User_PW.setText('')
        self.name = name
        MainWindow.main_User_name.setText(f"{self.name}회원님 환영합니다")
        MainWindow.label_2.setText(f"{self.name}님의 독서등급")

    def join_show(self):
        Join.show()
        Start.close()


class Join_class(QDialog,join_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_join_back.clicked.connect(self.login_show)
        self.btn_join.clicked.connect(self.joinCheck_show)
        self.setWindowTitle("Book bug")
        self.setWindowIcon(QIcon("image/icon.png"))
        qPixmapVar = QPixmap()
        qPixmapVar.load("image/회원가입.jpg")
        self.join_image.setPixmap(qPixmapVar)

    def joinCheck_show(self):
        inputId = self.join_id.text()
        inputPw = self.join_pw.text()
        inputName = self.join_name.text()
        inputAge = self.join_age.text()
        result= dbConn.join_insert(inputId, inputPw, inputName, inputAge)
        if result == 0:
            join.result.setText("가입 실패")
        else:
            Start.show()
            JoinCheck.show()
            self.join_id.setText('')
            self.join_pw.setText('')
            self.join_name.setText('')
            self.join_age.setText('')
            Join.close()

    def login_show(self):
        Start.show()
        Join.close()
        
class Joincheck_class(QDialog,joincheck_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Book bug")
        self.setWindowIcon(QIcon("image/icon.png"))
        

class MainWindow_Class(QMainWindow,mainwindow_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Book bug")
        self.setWindowIcon(QIcon("image/icon.png"))
        qPixmapVar = QPixmap()
        qPixmapVar.load("image/회원관리.png")
        #self.babo_label.setPixmap(qPixmapVar)
        self.btn_logout.clicked.connect(self.login)
        self.pages_widget.setCurrentWidget(self.search_page)
        self.btn_search.clicked.connect(self.search_p)
        self.btn_rcnd.clicked.connect(self.rcnd_p)
        self.btn_event.clicked.connect(self.event_p)
        self.btn_user.clicked.connect(self.user_p)
        self.btn_user_info_change.clicked.connect(self.user_change_p)
        qPixmapVar = QPixmap()
        qPixmapVar.load("image/회원가입.jpg")
        self.change_image.setPixmap(qPixmapVar)
        self.btn_change.clicked.connect(self.updatesucess_show)
        self.btn_taste_input.clicked.connect(self.taste_p)
        qPixmapVar.load("image/메인로고.jpg")
        self.search_menu_image.setPixmap(qPixmapVar)
        self.btn_search_input.clicked.connect(self.result_search)
        self.btn_keyword_input.clicked.connect(self.inputbooklist)
        self.btn_keyword_delete.clicked.connect(self.deletebooklist)
        self.btn_keyword_delete.clicked.connect(self.taste_p)
        qPixmapVar.load("image/top_icon.png")
        self.top_image.setPixmap(qPixmapVar)
        self.btn_main.clicked.connect(self.main_change_p)
        stylesheet = "::section{Background-color:rgb(35,35,35)}"
        self.resultSearch.horizontalHeader().setStyleSheet(stylesheet)
        self.resultSearch.verticalHeader().setStyleSheet(stylesheet)
        htmlString1 = """
            <iframe width="891" height="571" src="https://www.youtube.com/embed/wBy9KGvixPw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
             """
        self.webEngineView_1.setHtml(htmlString1)


    def main_menu(self):
        self.pages_widget.setCurrentWidget(self.main_page)
        
        
        

    def deletebooklist(self):
        keyword = self.keyword_input.text()
        dbConn.delete_keyword2(keyword)


    def inputbooklist(self):
        keyword = self.keyword_input.text()
        dbConn.insert_keyword2(keyword)
        keywordresult = dbConn.select_keyword()
        if keywordresult == 0:
            print("결과없음")
        else:
            self.taste_label.setText(str(keywordresult[0]['keywords']))

        


    def result_search(self):# 제목으로 도서 검색
        self.frame_7.hide()
        inputSearch = self.seach_bar.text()
        
        Search_result = dbConn2.select_title(inputSearch)
        self.resultSearch.setRowCount(len(Search_result))
        self.resultSearch.setColumnCount(5)

        # print(Search_result)
        for row_number, row_data in enumerate(Search_result):
            for col_number, col_data in enumerate(row_data):
                self.resultSearch.setItem(row_number, col_number, QTableWidgetItem(str(row_data[col_data])))

    def updatesucess_show(self):
        inputId = self.text_change_id.text()
        inputPw = self.text_change_pw.text()
        inputName = self.text_change_name.text()
        inputAge = self.text_change_age.text()
        dbConn.update_All(inputId,inputPw,inputName,inputAge)
        self.change_result.setText("수정 완료")




    #키워드 불러오는곳
    def taste_p(self):
        """
        아무거나!
        """
        self.pages_widget.setCurrentWidget(self.user_taste_page)
        keywordresult = dbConn.select_keyword()
        if keywordresult == 0:
            print("결과없음")
        else:
            self.taste_label.setText(str(keywordresult[0]['keywords']))



    def user_change_p(self):
        self.pages_widget.setCurrentWidget(self.user_change_page)

    def main_change_p(self):
        self.pages_widget.setCurrentWidget(self.search_page)
        self.frame_7.show()

        

    def search_p(self):
        self.pages_widget.setCurrentWidget(self.search_page)
        self.frame_7.hide()
        stylesheet = "::section{Background-color:rgb(35,35,35)}"
        self.resultSearch.horizontalHeader().setStyleSheet(stylesheet)
        self.resultSearch.verticalHeader().setStyleSheet(stylesheet)

    def rcnd_p(self):
        self.pages_widget.setCurrentWidget(self.rcnd_page)
        keywords = dbConn.select_user_keywords()
        keywords = keywords.lstrip(',')
        keyword_list = keywords.split(',')
        print(keyword_list)
        rcnd_result = dbConn.get_recommendation_by_keywords(keyword_list)
        self.rcnd_Search.setRowCount(len(rcnd_result))
        self.rcnd_Search.setColumnCount(5)
        stylesheet = "::section{Background-color:rgb(35,35,35)}"
        self.rcnd_Search.horizontalHeader().setStyleSheet(stylesheet)
        self.rcnd_Search.verticalHeader().setStyleSheet(stylesheet)

        print(len(rcnd_result))
        for row_number, row_data in enumerate(rcnd_result):
            for col_number, col_data in enumerate(row_data):
                self.rcnd_Search.setItem(row_number, col_number, QTableWidgetItem(str(row_data[col_data])))

    def event_p(self):
        self.pages_widget.setCurrentWidget(self.event_page)
        qPixmapVar = QPixmap()
        qPixmapVar.load("image/bestseller.png")
        self.best.setPixmap(qPixmapVar)

    def user_p(self):
        self.pages_widget.setCurrentWidget(self.user_page)
        qPixmapVar = QPixmap()
        qPixmapVar.load("image/k1.png")
        self.label_a.setPixmap(qPixmapVar)
        qPixmapVar.load("image/무게.png")
        self.label_5.setPixmap(qPixmapVar)
        self.btn_read_book.clicked.connect(self.insert_weight)
        weightresult = dbConn.select_user_weight()
        self.user_weight.setText(f"현재 읽은 무게는 : {str(weightresult)}")
        if weightresult < 3000 :
            qPixmapVar = QPixmap()
            qPixmapVar.load("image/k1.png")
            self.label_a.setPixmap(qPixmapVar)
            self.user_k.setText("현재등급 : 도토리")
        elif weightresult >= 3000 and weightresult < 6000:
            qPixmapVar = QPixmap()
            qPixmapVar.load("image/k2.png")
            self.label_a.setPixmap(qPixmapVar)
            self.user_k.setText("현재등급 : 새싹")
        elif weightresult >= 6000 and weightresult < 15000:
            qPixmapVar = QPixmap()
            qPixmapVar.load("image/k3.png")
            self.label_a.setPixmap(qPixmapVar)
            self.user_k.setText("현재등급 : 줄기")
        elif weightresult >= 15000 and weightresult < 20000:
            qPixmapVar = QPixmap()
            qPixmapVar.load("image/k4.png")
            self.label_a.setPixmap(qPixmapVar)
            self.user_k.setText("현재등급 : 덤불")
        elif weightresult >= 20000 and weightresult < 30000:
            qPixmapVar = QPixmap()
            qPixmapVar.load("image/k5.png")
            self.label_a.setPixmap(qPixmapVar)
            self.user_k.setText("현재등급 : 나무")
        elif weightresult >= 30000:
            qPixmapVar = QPixmap()
            qPixmapVar.load("image/k6.png")
            self.label_a.setPixmap(qPixmapVar)
            self.user_k.setText("현재등급 : 숲")


    def insert_weight(self):
        print("insert weight")

        title = self.read_book.text()
        print(title)
        # dbConn.select_weight(insert_w)
        # sql = select from book where weight
        dbConn.insert_weight(title)
        weightresult = dbConn.select_user_weight()
        self.user_weight.setText(f"현재 읽은 무게는 : {str(weightresult)}")
        if weightresult < 3000 :
            qPixmapVar = QPixmap()
            qPixmapVar.load("image/k1.png")
            self.label_a.setPixmap(qPixmapVar)
            self.user_k.setText("현재등급 : 도토리")
        elif weightresult >= 3000 and weightresult < 6000:
            qPixmapVar = QPixmap()
            qPixmapVar.load("image/k2.png")
            self.label_a.setPixmap(qPixmapVar)
            self.user_k.setText("현재등급 : 새싹")
        elif weightresult >= 6000 and weightresult < 15000:
            qPixmapVar = QPixmap()
            qPixmapVar.load("image/k3.png")
            self.label_a.setPixmap(qPixmapVar)
            self.user_k.setText("현재등급 : 줄기")
        elif weightresult >= 15000 and weightresult < 20000:
            qPixmapVar = QPixmap()
            qPixmapVar.load("image/k4.png")
            self.label_a.setPixmap(qPixmapVar)
            self.user_k.setText("현재등급 : 덤불")
        elif weightresult >= 20000 and weightresult < 30000:
            qPixmapVar = QPixmap()
            qPixmapVar.load("image/k5.png")
            self.label_a.setPixmap(qPixmapVar)
            self.user_k.setText("현재등급 : 나무")
        elif weightresult >= 30000:
            qPixmapVar = QPixmap()
            qPixmapVar.load("image/k6.png")
            self.label_a.setPixmap(qPixmapVar)
            self.user_k.setText("현재등급 : 숲")
            

        
    
    def login(self):
        MainWindow.close()
        Start.show()


if __name__ == "__main__":
    # pyQt를 동작시켜주는 역할
    app = QApplication(sys.argv)
    Start = Start_Class() # Ui가 적용된 화면
    # window = QWidget()
    # layout = QHBoxLayout(window)
    # layout.addWidget(button)
    # window.show()
    MainWindow = MainWindow_Class()
    Join = Join_class()
    JoinCheck = Joincheck_class()
    Start.show() # 보여줘라

    # 동작
    sys.exit(app.exec_())