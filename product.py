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
		self.c.execute("INSERT INTO product VALUES(?, ?, ?)",(self.product, self.main_price, self.sell_price))
		self.conn.commit()

	def delete_product(self,product):
		self.product = product
		self.c.execute("DELETE FROM product WHERE product=?",(self.product,))
		self.conn.commit()

	def sell(self,product,finalPrice):
		self.c.execute("CREATE TABLE IF NOT EXISTS sell(product TEXT, main_price REAL, sell_price REAL, win REAL, count INTEGER)")
		self.product = product
		self.sell_price =finalPrice
		self.c.execute("SELECT main_price FROM product WHERE product=?",(self.product,))
		self.main_price = self.c.fetchone()[0]
		self.win = self.sell_price - self.main_price
		################################ Hir The Break ################################
		self.c.execute("SELECT count FROM sell WHERE product=?",(self.product,))
		print(self.c.fetchone())


	def mainPrice(self,product):
		self.product = product
		self.c.execute("SELECT main_price FROM product WHERE product=?",(self.product,))
		for i in self.c.fetchall():
			print(str(self.product)+" : "+str(i[0]))

	def bestSelling(self):
		pass
