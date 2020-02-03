import sqlite3


def sorgu(query,param=[]):
    db=sqlite3.connect('db_1.db')
    im=db.cursor()
    im.execute(query,param)
    res=im.fetchall()
    db.close()
    return res

def calistir(query="",param=[]):
    try:

        db=sqlite3.connect('db_1.db')
        im=db.cursor()
        im.execute(query,param)
        db.commit()
        db.close()
        return True
    except:
        return False


