# 민우 형 라이브러리 쓰게 되면 나한테 알려줘 일단 사용 안하는 걸로 알게
import pymysql as ps
#from data import *


# 승리
# DB 연동 코드 어려울 수도 있지만 다 하고 나면 분명 뿌듯할 거야~~
# python DB 연동은 현업 실무에서도 많이 쓸 테니까...
# 코드를 간결하게 짜주면 좋겠어 *^^* (희망사항)
# 객체지향 컨셉이 어려워서 그럴 수 있어.. 어려우면 얼마든지 물어봐 *^^*
#

# <이름 짓는 규칙>
# class AppleFarm: # 클래스
#     def __init__(self):
#         self.farm_owner = "승리" # 변수 이름
        
#     def sell_apple(self,): # 메서드(함수) 이름
#         pass
# def 메서드 아래 한줄 띄고
# class 아래 두줄 띄고
# import 할 때는 외부 라이브러리(PyQT, pymysql)를 먼저 적고
# 우리가 만든 라이브러리(data,db)는 나중에 적기
# import 다 하고 두 줄 띄고 코드 쭉쭉 작성하기~~
class DataDBConn:
    def __init__(self):
        self.db = ps.connect(host = '127.0.0.1',port = 3306,user = 'root',passwd = '1234',db = 'test',charset='utf8')
        self.cursor = self.db.cursor(ps.cursors.DictCursor)

    # def create_tables(self):
    #     """
    #     쓰면 다 끝장남...
    #     """
    #     #테이블 틀
    #     ####################################################
    #     #회원
    #     sql_USER_ID_DROP ="DROP TABLE IF EXISTS USER;"
    #     self.cursor.execute(sql_USER_ID_DROP) # sql 문 실행은 cursor
    #     # sql return 0 : 아무 영향을 못 미친 거고 1+: 그 개수(rows)만큼 영향을 미침
    #     #print(result) # VSCode에서 확인하고 싶으면 result 써서 출력하고 되고
    #     # 그냥 MySQL 켜서 확인할 거면 result 안 써도 되고
    #     sql_USER_ID_C = "CREATE TABLE USER(USER_ID INT unsigned not null auto_increment , ID VARCHAR(20) ,PW VARCHAR(20), NAME VARCHAR(20), GENRE_IDS VARCHAR(100), WEIGHT INT(10), KEYWORDS VARCHAR(1000),PRIMARY KEY(USER_ID) );"	
    #     self.cursor.execute(sql_USER_ID_C)
    #     self.db.commit()
    #     ########################################
    #     #장르
    #     sql_GENRE_DROP = "DROP TABLE IF EXISTS GENRE"
    #     self.cursor.execute(sql_GENRE_DROP)
    #     sql_GENRE_C = "CREATE TABLE GENRE (GENRE_ID INT(10) not null, GENRE_NAME VARCHAR(20), PRIMARY KEY(GENRE_ID) ) ;"
    #     self.cursor.execute(sql_GENRE_C)
    #     self.db.commit()
    #     #리뷰
    #     sql_REVIEW_DROP = "DROP TABLE IF EXISTS REVIEW"
    #     self.cursor.execute(sql_REVIEW_DROP)
    #     sql_REVIEW_C = "CREATE TABLE REVIEW (REVIEW_ID INT(200) not null, BOOK_ID INT(100), URL VARCHAR(200), REVIEW_TEXT VARCHAR(1000), PRIMARY KEY(REVIEW_ID) )"
    #     self.cursor.execute(sql_REVIEW_C)
    #     self.db.commit()
    #     #이벤트
    #     sql_EVENT_DROP = "DROP TABLE IF EXISTS EVENT"
    #     self.cursor.execute(sql_EVENT_DROP)
    #     sql_EVENT_C = "CREATE TABLE EVENT (EVENT_ID INT(100) not null, BOOK_ID INT(200), TITLE VARCHAR(200), START_DATE DATE, END_DATE DATE, BOOKSTORE VARCHAR(10), URL VARCHAR(200), URL_THUMBNAIL VARCHAR(200), PRIMARY KEY(EVENT_ID) )"
    #     self.cursor.execute(sql_EVENT_C)
    #     self.db.commit()
    #     #책
    #     sql_BOOK_DROP = "DROP TABLE IF EXISTS BOOK"
    #     self.cursor.execute(sql_BOOK_DROP)
    #     sql_BOOK_C = "CREATE TABLE BOOK (BOOK_ID INT(200) not null auto_increment, TITLE VARCHAR(200), AUTHOR VARCHAR(200), PUBLISHER VARCHAR(100), ISBN VARCHAR(15), WEIGHT INT(10), RANKING INT(10), BOOK_INFO VARCHAR(1000), CONTENTS VARCHAR(1000), GENRE_ID INT(10), REVIEW_KEYWORDS VARCHAR(1000), URL_YES24 VARCHAR(200), URL_ALADIN VARCHAR(200), URL_KYOBO VARCHAR(200), PRIMARY KEY(BOOK_ID) )"
    #     self.cursor.execute(sql_BOOK_C)
    #     self.db.commit()
    #     #추천목록
    #     sql_BOOK_RECOMMENDATION_DROP = "DROP TABLE IF EXISTS BOOK_RECOMMENDATION"
    #     self.cursor.execute(sql_BOOK_RECOMMENDATION_DROP)
    #     sql_BOOK_RECOMMENDATION_C = "CREATE TABLE BOOK_RECOMMENDATION (LIST_ID INT(10) not null, BOOK_LIST VARCHAR(200), MATCHING_RATE VARCHAR(10), PRIMARY KEY(LIST_ID) )"
    #     self.cursor.execute(sql_BOOK_RECOMMENDATION_C)
    #     self.db.commit()
    #     ########################################################


    def modify_user_table(self):
        #회원
        sql_USER_ID_DROP ="DROP TABLE IF EXISTS USER;"
        self.cursor.execute(sql_USER_ID_DROP) # sql 문 실행은 cursor
        # sql return 0 : 아무 영향을 못 미친 거고 1+: 그 개수(rows)만큼 영향을 미침
        #print(result) # VSCode에서 확인하고 싶으면 result 써서 출력하고 되고
        # 그냥 MySQL 켜서 확인할 거면 result 안 써도 되고
        sql_USER_ID_C = "CREATE TABLE USER(USER_ID INT unsigned not null auto_increment , ID VARCHAR(20) ,PW VARCHAR(20), NAME VARCHAR(20), GENRE_IDS VARCHAR(100), WEIGHT INT(10), KEYWORDS VARCHAR(1000),PRIMARY KEY(USER_ID) );"	
        self.cursor.execute(sql_USER_ID_C)
        self.db.commit()


    #책 정보 입력
    def insert_book(self, TITLE, AUTHOR, PUBLISHER, ISBN, RANKING, GENRE_ID):
        sql_insert = f"insert into book(TITLE, AUTHOR, PUBLISHER, ISBN, RANKING, GENRE_ID) values('{TITLE}', '{AUTHOR}', '{PUBLISHER}', '{ISBN}', {RANKING}, {GENRE_ID});"
        self.cursor.execute(sql_insert)
        self.db.commit()



     #책 제목 선택으로 책정보	
    # def select_title(self, title):	
    #     #sql = f"select * from BOOK where title='{title}'"	
    #     sql = f"select BOOK_ID, AUTHOR, PUBLISHER , ISBN from BOOK where title='{title}'"	

    #     #sql = f"select BOOK_ID, ISBN from BOOK where title='{title}'"
    #     result = self.cursor.execute(sql) # 값이 제대로 들어왓는지 확인
    #     data = self.cursor.fetchall()
    #     if result == 0:
    #         return 0
    #     else:
    #         return data[0]

     #책 제목 선택으로 책정보
    def select_title(self, title):
        #sql = f"select * from BOOK where CONCAT(title, author, publisher) REGEXP '{title}' "
        sql = f"SELECT BOOK_ID, TITLE, AUTHOR, PUBLISHER, ISBN \
                FROM BOOK WHERE (TITLE ='{title}') OR (AUTHOR = '{title}') OR (PUBLISHER = '{title}') OR ( ISBN = '{title}') OR ( BOOK_ID = '{title}') OR ( GENRE_ID = '{title}') OR\
                ( REVIEW_KEYWORDS LIKE '%{title}%')"
        #sql = f"select BOOK_ID, ISBN from BOOK where title='{title}'"
        result = self.cursor.execute(sql) # 값이 제대로 들어왓는지 확인
        data = self.cursor.fetchall()
        if result == 0:
            return 0
        else:
            return data

    #책 ISBN 선택으로 책정보
    def select_isbn(self, isbn):
        sql = f"select * from BOOK where ISBN='{isbn}'"
        #sql = f"select BOOK_ID, ISBN from BOOK where title='{title}'"
        result = self.cursor.execute(sql) # 값이 제대로 들어왓는지 확인
        data = self.cursor.fetchall()
        if result == 0:
            return 0
        else:
            return data[0]

    #책 출판사 선택으로 책정보
    def select_publisher(self, publisher):
        sql = f"select * from BOOK where PUBLISHER='{publisher}'"
        #sql = f"select BOOK_ID, ISBN from BOOK where title='{title}'"
        result = self.cursor.execute(sql) # 값이 제대로 들어왓는지 확인
        data = self.cursor.fetchall()
        if result == 0:
            return 0
        else:
            return data[0]

  


class MemberDBconn:
    """	
    회원 관련 함수가 들어있는 클래스	
    """
    def __init__(self):
        self.db = ps.connect(host = '127.0.0.1',port = 3306,user = 'root',passwd = '1234',db = 'test',charset='utf8')
        self.cursor = self.db.cursor(ps.cursors.DictCursor)
        self.user_id = ""
    
    #로그인
    def login_select(self, inputId, pw):
        #sql self 않붙이는 이유는 지역변수이기때문
        sql = f"select name from user where id='{inputId}' and pw='{pw}' "
        result = self.cursor.execute(sql) # 값이 제대로 들어왓는지 확인
        name = self.cursor.fetchall()
        if result == 0:
            return 0

        else:
            # login success
            self.user_id = inputId
            return name[0].get('name')

    def select(self, inputId):
        #sql self 않붙이는 이유는 지역변수이기때문
        sql = f"select * from user where id='{inputId}'"
        result = self.cursor.execute(sql) # 값이 제대로 들어왓는지 확인
        data = self.cursor.fetchall()
        if result == 0:
            return 0
        else:
            return data[0]

    #회원가입
    def join_insert(self,inputId,pw,name,age):
        sql = f"insert into user(id, pw, name) values('{inputId}','{pw}','{name}')"
        result = self.cursor.execute(sql)
        self.db.commit()
        return result

    #회원탈퇴
    def join_delete(self,inputId):
        sql = f"delete from user where id='{inputId}'"
        result = self.cursor.execute(sql)
        self.db.commit()
        return result

    #회원정보수정
    def info_update(self, update_choice, changeData, inputId):
        cols = ['pw','name']
        sql = f"update user set {cols[update_choice-1]}='{changeData}' where id = '{inputId}'"
        result = self.cursor.execute(sql)
        self.db.commit()
        return result

    

    def update_All(self, inputId, pwchange, namechange, agechange):
        sql = f"update user set pw = '{pwchange}', name = '{namechange}' where id = '{inputId}'"
        result = self.cursor.execute(sql)
        self.db.commit()
        return result


    def insert_keyword2(self, inputKeyword):
        sql = f"insert into USER(KEYWORDS) VALUES('{inputKeyword}')"
        sql_get_keywords = f"select keywords\
                             from user\
                             where id = '{self.user_id}'"
        result = self.cursor.execute(sql_get_keywords)
        data = self.cursor.fetchall()
        if data[0]['keywords'] == None:
            keywords = inputKeyword
        else:
            keywords = data[0]['keywords'] + ',' + inputKeyword
        sql_put_keywords = f"update user\
                             set keywords = '{keywords}'\
                             where id = '{self.user_id}'"
        result = self.cursor.execute(sql_put_keywords)
        self.db.commit()
        return result

    def delete_keyword2(self, inputKeyword2):
        sql_select_keywords = f"select keywords\
                                from user\
                                where id = '{self.user_id}'"
        result = self.cursor.execute(sql_select_keywords)
        data = self.cursor.fetchall()
        print(data[0])

        keywords = data[0]['keywords'].split(',')
        new_keywords = []
        for kw in keywords:
            if kw != inputKeyword2:
                new_keywords.append(kw)
        new_keywords = ','.join(new_keywords)
        print(new_keywords)

        sql_update_keywords = f"update user\
                                set keywords = '{new_keywords}'\
                                where id = '{self.user_id}'"
        result = self.cursor.execute(sql_update_keywords)
        if result == 0:
            print("삭제실패")
        else:
            self.db.commit()
    

    #키워드만 출력
    def select_keyword(self):
        sql_get_keywords = f"select keywords\
                             from user\
                             where id = '{self.user_id}'"
        result = self.cursor.execute(sql_get_keywords)
        data = self.cursor.fetchall()
        self.db.commit()
        return data

    def select_publisher(self, publisher):
        sql = f"select * from BOOK where PUBLISHER='{publisher}'"
        #sql = f"select BOOK_ID, ISBN from BOOK where title='{title}'"
        result = self.cursor.execute(sql) # 값이 제대로 들어왓는지 확인
        data = self.cursor.fetchall()
        if result == 0:
            return 0
        else:
            return data[0]
    

    def select_user_weight(self):
        print("select user weight")
        sql_get_user_weight = f"select weight\
                                from user\
                                where id = '{self.user_id}'"
        result = self.cursor.execute(sql_get_user_weight)
        data = self.cursor.fetchall()
        print(data)

        user_weight = 0
        if data[0]['weight'] == None:
            print("weight이 없는 경우")
        else :
            user_weight = data[0]['weight']
            print(f"weight 값 : {user_weight}")
        return user_weight


    # 무게 입력
    def insert_weight(self, title):
        # sql = f"insert into USER(weight) values({inputweight})"
        sql_get_user_weight = f"select weight\
                                from user\
                                where id = '{self.user_id}'"
        result = self.cursor.execute(sql_get_user_weight)
        print(result)
        data = self.cursor.fetchall()
        print(data)

        user_weight = 0
        if data[0]['weight'] == None:
            print("weight이 없는 경우")
        else :
            user_weight = data[0]['weight']
            print(f"weight 값 : {user_weight}")

        sql_get_book_weight = f"select weight\
                                from book\
                                where title = '{title}'"
        result = self.cursor.execute(sql_get_book_weight)
        data = self.cursor.fetchall()
        print(data)

        book_weight = data[0]['weight']
        print(book_weight)

        weight = int(user_weight) + int(book_weight)
        sql_put_weight = f"update USER\
                           set weight = '{weight}'\
                           where id = '{self.user_id}'"
        result = self.cursor.execute(sql_put_weight)
        self.db.commit()
        return result

    # Yuni
    def select_user_keywords(self):
        sql = f"select keywords \
                from user \
                where id = '{self.user_id}'"
        result = self.cursor.execute(sql)
        data = self.cursor.fetchall()
        if result == 0:
            return 0
        else:
            return data[0]['keywords']

    def get_recommendation_by_keywords(self, keyword_list):
        data_list = []
        for keyword in keyword_list:
            sql = f"select book_id, title, author, publisher, isbn \
                    from book \
                    where review_keywords LIKE '%{keyword}%'"
            result = self.cursor.execute(sql)
            data = self.cursor.fetchall()
            # print(data)
            if result != 0:
                data_list += data
        # print(data_list)

        # book_id_list = []
        # for data in data_list:
        #     book_id_list.append(data['book_id'])
        #     book_id_list

        return data_list
    
    

class DB:

    # 파일 이름이랑 같은 클래스는 다른 사람이 쓸 메서드만 구현하는 걸로
    def __init__(self):
        pass

    def create_table(self,name):
        pass

    # 승리가 혼자 쓸 함수를 만들어도 되고(선택)
    # 같이 쓸 함수(다른 파일에서)를 만드는 게 주 목적!!

    def get_data(self):
        # sql = "select * from review"
        # ...
        # {}, [] <= 형식은 추후에 정하기!!(약속)
        # return db_data
        pass


if __name__ == "__main__":
    # df = Data.get_df()
    # for ...:
    #     sql ="insert df[0]"
    pass