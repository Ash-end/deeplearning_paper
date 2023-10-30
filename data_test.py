from pymysql import Connection
# 获取到MySQL数据库的连接对象
conn = Connection(
    host = 'localhost', #主机名 (或IP地址)
    port = 3306,       #端口,默认3306
    user = 'root',     #账户名
    password = 'Zhanglizhi6@' #密码
    # autocommit = True 设置自动提交
)
# 打印MySQL数据库软件信息
print(conn.get_server_info())
# 获取游标对象
cursor = conn.cursor()
conn.select_db("world") #先选择数据库
# 使用游标对象，执行sql语句
# cursor.execute("CREATE TABLE test_pymysql(id INT , info VARCHAR(255))")
cursor.execute("SELECT * FROM city ")
#单独插入一行数据，但是直接执行不会生效，需要进行代码确认
#cursor.execute("insert into student values(10001,'周杰伦',31,男)")
#通过commit确认
conn.commit()
# 获取查询结果
results: tuple = cursor.fetchall()
for r in results:
    print(r)
# 关闭到数据库的链接
conn.close()