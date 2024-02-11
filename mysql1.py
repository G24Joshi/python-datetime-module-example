import pymysql
try:
    con=pymysql.connect(host="localhost",user="root","password="password",database="userdb132")
                        print("connect")
except Exception as ex:
    print(ex)
finally:
    con.close()