import pymysql


def query(sql,typeRequest,listWords):
    db = pymysql.connect(host ="localhost", user ="root", password ="", database ="pooproject",port =3308)
    cursor = db.cursor()
    row=""
    try:
        cursor.execute(sql,listWords)
        if typeRequest=="select":
            row = cursor.fetchall()
        elif typeRequest=="insert":
            db.commit()
        elif typeRequest=="update":
            db.commit()
    except pymysql.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        return False
    finally:
        cursor.close()
        db.close()

    if typeRequest == "select":
        return row
    else:
        return True