from scipy.optimize import linprog as lin
import time as t


x  = [7,1,1,4,2,3,5,6,6,8,8,2,4,3,7,3,4,2,5,8,8,1,4,7,6]
quantityStock = [70,46,39,41,55]
quantityOrdered = [23,38,30,15,8]
    
a_ub = [[1,1,1,1,1, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                     [0,0,0,0,0, 1,1,1,1,1, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                     [0,0,0,0,0, 0,0,0,0,0, 1,1,1,1,1, 0,0,0,0,0, 0,0,0,0,0],
                     [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 1,1,1,1,1, 0,0,0,0,0],
                     [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 1,1,1,1,1]] 
 
a_eq = [[1,0,0,0,0, 1,0,0,0,0, 1,0,0,0,0, 1,0,0,0,0, 1,0,0,0,0],
                     [0,1,0,0,0, 0,1,0,0,0, 0,1,0,0,0, 0,1,0,0,0, 0,1,0,0,0],
                     [0,0,1,0,0, 0,0,1,0,0, 0,0,1,0,0, 0,0,1,0,0, 0,0,1,0,0],
                     [0,0,0,1,0, 0,0,0,1,0, 0,0,0,1,0, 0,0,0,1,0, 0,0,0,1,0],
                     [0,0,0,0,1, 0,0,0,0,1, 0,0,0,0,1, 0,0,0,0,1, 0,0,0,0,1]] 
        

start = t.time() # Время начала выполнения 
print(lin( x,  a_ub,  quantityStock,  a_eq,  quantityOrdered)) # Результат
stop = t.time() # Время завершения выполнения
print ("Время выполнения:")
print( stop -  start)
        
