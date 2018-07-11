from product import *
from users import *
import time

h = Product()
#l = User("ziad","????")
#there is problem in user shit
k = Admin()

h.addProduct("chemise 1/2",80.00) #work
#h.sell("chemise 1/2",90)  #sqlite3.OperationalError: near "VALUES": syntax error
time.sleep(2)
h.mainPrice("chemise 1/2") #sqlite3.OperationalError: near "VALUES": syntax error
h.delete_product("chemise 1/2")