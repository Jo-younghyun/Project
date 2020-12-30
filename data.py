import sys
import pandas as pd
import numpy as np
from db import DataDBConn
from db import MemberDBconn

"""
DB 연결
db.py를 실행시키고 시작해야 함
"""
dbConn = DataDBConn()
dbConn.create_tables()


"""
데이터 전처리
DataFrame
"""
df_aladin = pd.read_csv("C:/Users/SMT027/Desktop/PYQT/test/data/알라딘_주간+베스트_국내도서_2020년8월1주_20200806.csv")
df_aladin = df_aladin[:100] # 마지막 행 제거 index slicing

# change order of columns
# ['순번/순위', '구분', '상품명', 'ISBN', 'ISBN13', '부가기호', '출판사/제작사', '저자/아티스트','정가', '판매가', '할인액', '할인율', '마일리지', '출간일', '세일즈포인트']
# 책 번호, 제목, 작가, 출판사, ISBN, 무게, 랭킹, 책 소개, 목차, 장르 번호, 리뷰 키워드, 예스24 링크, 알라딘 링크, 교보문고 링크
# genre_id_list = [] # TODO

cols = ['상품명', '저자/아티스트', '출판사/제작사', 'ISBN13', '순번/순위', '구분',]
df_aladin = df_aladin[cols] # df_aladin.reindex(columns=cols)
df_aladin['ISBN13'] = df_aladin['ISBN13'].astype(np.int64)
df_aladin['순번/순위'] = df_aladin['순번/순위'].astype(int)

df_aladin.to_csv("aladin.csv", encoding='utf-8')# 글짜 깨지는거 변환
df_aladin = pd.read_csv("aladin.csv")
#print(df_aladin.head(5))

for idx in range(df_aladin.shape[0]):
    #print(df_aladin.iloc[idx].values) # 값 확인
    #print(df_aladin.iloc[idx,1]) # 제목만 출력

    #db.insert_book(df_aladin.iloc[idx].values) # DataFrame 행 한 개씩
    #print(df_aladin.iloc[idx,0])
    #print(df_aladin.iloc[idx,6])

    #
    title_aladin = df_aladin.iloc[idx,1] 
    author_aladin = df_aladin.iloc[idx,2] 
    publisher_aladin = df_aladin.iloc[idx,3] 
    isbn_aladin = df_aladin.iloc[idx,4]
    ranking_aladin = df_aladin.iloc[idx,5]
    genre_id_aladin = 10

    # book테이블에 넣을 엑셀 자료엑셀자료
    dbConn.insert_book(title_aladin, author_aladin, publisher_aladin, isbn_aladin, ranking_aladin, genre_id_aladin)

#print(df_aladin.iloc[1,5])
# result2 = dbConn.insert_keyword('악몽을 먹고 자란 소년')
#print(result2['AUTHOR'])
# print(result2)

