"""
author: CMWY
date:2021.04.11
"""


import pymysql
import ex1.ex1 as m



def write(a,db):
    try:
        conn=pymysql.connect(host='localhost',user='cmwy',passwd='cmwy',database=db,port=3306,charset='utf8')
        cur=conn.cursor()


        cur.execute('create database if not exists cdk')
        conn.select_db('cdk')


        # sql = "create table cdk (id int(11) primary key, cdk varchar(50))"
        # cur.execute(sql)


        for i in range(len(a)):
            #sql="insert into user (id,cdk) values ('i',a[i])"
            cur.execute("INSERT INTO cdk (id, cdk) VALUES (%s,%s)", (i+1,a[i]))


        cur.close()

        conn.commit()
        conn.close()

    except pymysql.Error as e:
        print("Mysql Errror %d;%s " % (e.args[0],e.args[1]))



def read(db):
    conn = pymysql.connect(host='localhost', user='cmwy', passwd='cmwy', database=db, port=3306, charset='utf8')
    cur = conn.cursor()
    sql = "select * from cdk"
    cur.execute(sql)


    result = cur.fetchall()
    for c in result:

        print(c)


if __name__=='__main__':

    s=m.ran(200,20)
    #write(s,'cdk')
    read('cdk')