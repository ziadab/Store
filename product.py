import sqlite3

class Product():
	conn = sqlite3.connect('store.db')
	c = conn.cursor()

	def __init__(self):
		self.c.execute("CREATE TABLE IF NOT EXISTS product(id integer primary key AUTOINCREMENT, product TEXT, main_price REAL, sell_price REAL)")

	def addProduct(self,product,main_price,sell_price=None):
		self.product = product.title()
		self.main_price = main_price
		self.sell_price = sell_price
		self.c.execute("INSERT INTO product VALUES(null,?, ?, ?)",(self.product, self.main_price, self.sell_price))
		self.conn.commit()

	def delete_product(self,product):
		self.product = product.title()
		self.c.execute("DELETE FROM product WHERE product=?",(self.product,))
		self.conn.commit()

	def sell(self,product,finalPrice):
		self.c.execute("CREATE TABLE IF NOT EXISTS sell(id integer primary key AUTOINCREMENT, product TEXT, main_price REAL, sell_price REAL, win REAL, count INTEGER)")
		self.product = product.title()
		self.sell_price =float(finalPrice)
		try:
			dt = self.c.execute("SELECT main_price FROM product WHERE product=?",(self.product,)).fetchall()
			self.main_price = dt[0][0]
			self.win = self.sell_price - self.main_price
		except:
			print("Something Go Wrong")
		############################### Hir The Break ################################
		data = self.c.execute("SELECT * FROM sell").fetchall()
		if len(data) == 0:
			self.count = 1
			self.c.execute("INSERT INTO sell VALUES(null,?,?,?,?,?)",(self.product, self.main_price, self.sell_price, self.win, self.count))
			self.conn.commit()
		else:
			self.c.execute("SELECT * FROM sell")
			for rows in self.c.fetchall():
				if rows[1] ==str(self.product) and rows[3] == self.sell_price:
					self.count = rows[-1] + 1
					self.c.execute("""UPDATE sell SET count = ? WHERE id = ?""",(self.count, rows[0]))
					self.conn.commit()
				else:
					self.count = 1
					self.c.execute("INSERT INTO sell VALUES(null,?,?,?,?,?)",(self.product, self.main_price, self.sell_price, self.win, self.count))
					self.conn.commit()


	def mainPrice(self,product):
		self.product = product.title()
		self.c.execute("SELECT main_price FROM product WHERE product=?",(self.product,))
		for i in self.c.fetchall():
			print(str(self.product)+" : "+str(i[0]))

	def bestSelling(self):
		pass
