import  mysql.connector;
class DB:
    con=None
    def main():
        try:
            DB.con=mysql.connector.connect(user='root',
                                           password='root123',
                                           host='127.0.0.1',
                                           database='student')
            print('database connected')
            cur=DB.con.cursor()
            query='select * from account'
            cur.execute(query)
            ta=cur.fetchall()
            for record in ta:
                for field in record:
                    print(field)
            DB.con.commit()
            print('record printed successfully')
        except Exception as msg:
            print(msg)
        finally:
            if DB.con != None:
                DB.con.close()
                print('connection released ')
        return
DB.main()
