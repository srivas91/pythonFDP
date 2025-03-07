import mysql.connector as conn
con=conn.connect(host='localhost',user='root',password='',database='pce')
cursor=con.cursor()
# cursor.execute('select * from staff')
# rows=cursor.fetchall()
# for i in rows:
#     print('stid:',i[0])
#     print('stname:', i[1])
#     print('dept:', i[2])
sql='insert into staff (stid,stname,dept)values(%s,%s,%s)'
values=(333,'geetha','cse')
cursor.execute(sql,values)
con.commit()
print('data insertion success')