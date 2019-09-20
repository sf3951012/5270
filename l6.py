import threading
import time

N=0

lock = threading.Lock() # mutex mutual exclusion object

def worker():
	global N
	print(threading.currentThread().getName(), 'Starting', N)
	lock.acquire() #safe region
	M = N
	print(M)
	N = M+1
	lock.release() # end safe region
	time.sleep(1)
	print(threading.currentThread().getName(), 'Exitng', N)


for i in range(5):
	w = threading.Thread(target=worker)
	w.start()




data =[3,1,4,1,5,9,2,6,5,3]

def worker1(p):
	global data
	if data[p-1] > data[p]:
		temp = data[p-1]
		data[p-1] =data[p]
		data[p] = temp

for j in range(5):
	threads = []
	for i in range(5):
		w = threading.Thread(target=worker1, args = [2*i+1])
		w.start()
		threads.append(w)
	for w in threads:
		w.join()
	print(data)
	threads = []
	for i in range(4):
		w = threading.Thread(target=worker1, args = [2*i+2])
		w.start()
		threads.append(w)
	for w in threads:
		w.join()
	print(data)


# implement word count program


