import sqlite3

class Product():
	conn = sqlite3.connect('store.db')
	c = conn.cursor()

	def __init__(self):
		self.c.execute("CREATE TABLE IF NOT EXISTS product(product TEXT, main_price REAL, sell_price REAL)")

	def addProduct(self,product,main_price,sell_price=None):
		self.product = product
		self.main_price = main_price
		self.sell_price = sell_price
		self.c.execute("INSERT INTO product VALUES(?, ?, ?)",(self.product, self.main_price, self.main_price))
		self.conn.commit()

	def delete_product(self,product):
		self.product = product
		self.c.execute("DELETE FROM product WHERE product=?",(self.product,))
		self.conn.commit()

	def sell(self,product,finalPrice):
		self.c.execute("CREATE TABLE IF NOT EXISTS sell(product TEXT, main_price REAL, sell_price REAL, win REAL, count INTEGER)")
		self.product = product
		self.finalPrice = finalPrice
		self.execute("SELECT main_price FROM product WHERE product=?",(self.product))
		self.main_price = float(self.fetchone()[0])
		self.c.execute("SELECT product, sell_price FROM sell")
		for x in self.c.fetchall():
			if x[0] and x[1] == self.product, self.finalPrice:
				self.c.execute("SELECT count FROM sell WHERE product=? AND main_price=? AND sell_price=?",(self.product, self.main_price, self.finalPrice))
				if self.c.fetchone() == None:
					self.count = 1
				else:
					self.count +=1
				self.c.execute("UPDATE sell SET count=? WHERE product=? AND sell_price=?",(self.count, self.product, self.finalPrice))
				self.conn.commit()
			else:
				self.win = self.finalPrice - self.main_price
				self.count = 1
				self.c.execute("INSERT INTO sell VALUES(?, ?, ?, ?, ?)",(self.product, self.main_price, self.finalPrice, self.win, self.count ))

	def mainPrice(self,product):
		self.product = product
		self.c.execute("SELECT main_price FROM product WHERE product=?",(self.product,))
		for i in self.c.fetchall():
			print(str(self.product)+" : "+str(i[0]))

	def bestSelling(self):
		pass
