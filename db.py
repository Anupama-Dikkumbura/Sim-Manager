import sqlite3

class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS sims (id INTEGER PRIMARY KEY, account text, email text, sim text, profile text)")
        self.conn.commit()
    
    def fetch(self):
        self.cur.execute("SELECT * FROM sims")
        rows = self.cur.fetchall()
        return rows
    
    def insert(self, account, email, sim, profile):
        self.cur.execute("INSERT INTO sims VALUES(NULL, ?,?,?,?)",(account, email, sim, profile))
        self.conn.commit()
    
    def remove(self, id):
        self.cur.execute("DELETE FROM sims WHERE id=?",(id,))
        self.conn.commit()
    
    def update(self, id, account, email, sim, profile):
        self.cur.execute("UPDATE sims SET profile =?, email=?, sim=?, profile=? WHERE id=?",(account, email, sim, profile, id))
        self.conn.commit()
    
    def __del__(self):
        self.conn.close()


# db =  Database('store.db')
# db.insert("anupama","anupama@anupama.com","0777111222","fiverr")
# db.insert("neranjan","neranjan@neranjan.com","0771234563","fiverr/paypal")
# db.insert("salidu","salidu@salidu.com","0713310097","paypal")
# db.insert("gihan","gihan@gihan.com","0779880904","ebay")
# db.insert("kanchana","kanchana@kanchana.com","0712342878","micro")

