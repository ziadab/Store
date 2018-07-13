import hashlib, sqlite3

class User():
	conn = sqlite3.connect('store.db')
	c = conn.cursor()

	def __init__(self):
		self.c.execute("CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT ,permition INTEGER) ")
		
	def changePassword(self, username, currentPassword, newPassword):
		self.currentPassword = str(hashlib.md5(str(currentPassword).encode("utf-8")))
		self.newPassword = str(hashlib.md5(str(newPassword).encode("utf-8")))
		if (self.currentPassword == self.newPassword): 
			self.c.execute("UPDATE users SET password =? WHERE password = ?",(str(self.newPassword), str(self.currentPassword)))
			self.conn.commit()
		else:
			print("Sorry But The Password is Not The Same")


	def search(self,product,sell_price=None):
		self.product = product
		self.sell_price = sell_price
		self.c.execute("SELECT * FROM product WHERE product=? OR sell_price=?",(str(self.product),self.sell_price))
		data = self.c.fetchall()
		for i in data:
			print(i)

	#def sell(self,iD,product,price): 
	#	self.product = product
	#	self.price = price
	#	self.id = iD 
	#	self.c.execute('CREATE TABLE IF NOT EXISTS sell(product TEXT, main_price REAL, sell_price REAL, win REAL)')
	#	self.c.execute("SELECT main_price FROM products(rowid, product, main_price, sell_price) WHERE rowid = VALUES(?)",(self.id))
	#	self.sell_price = c.fetchone()
	#	self.win = (self.price - self.sell_price)
	#	self.c.execute("INSERT INTO sell VALUES(?, ? ,? ,?)",(self.product, self.sell_price, self.price, self.win ))#DONT MISS ME HIR
	#	self.conn.commit()
		



class Admin(User):
	conn = sqlite3.connect('store.db')
	c = conn.cursor()

	def __init__(self):
		self.c.execute("CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT ,permition REAL) ")

	def addUser(self,username,password,permition=0):
		self.username = username
		self.password = hashlib.md5(str(password).encode("utf-8")).hexdigest()
		self.permition = permition
		self.c.execute("INSERT INTO users VALUES (?, ?, ?)",(self.username, self.password, self.permition))
		self.conn.commit()

	def deleteUser(self,username,password,permition=0):
		self.username = username
		self.password = hashlib.md5(str(password).encode("utf-8")).hexdigest()
		self.permition = permition
		self.execute("DELETE FROM users WHERE username=? AND password=? AND permition=?",self.username, self.password, self.permition)
		self.conn.commit()
		

	
