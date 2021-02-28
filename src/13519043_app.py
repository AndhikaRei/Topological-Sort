#------------------********************   Fungsi dan Prosedur   ********************------------------#
###########################    Kelompok Kerja Manajemen Node dan Edge     #############################
def unvisited(node):
	# I.S node merupakan sebuah course_id yang akan dicek apakah sudah pernah dikunjungi atau belum
  # F.S Mengirimkan true jika node belum pernah dikunjungi, false jika sudah
	for course in visitedNodes:
		if (node == course):
			return False
	return True

def addEdge(edge,u,v): 
	# I.S edge adalah dictionary , u adalah key dan v adalah valuenya
  # F.S value dari dictionary "edge" elemen "u" akan ditambah dengan v
	# Salah satu kegunaan fungsi ini adalah mereprsentasikan node(course) "u" terhubung dengan node "v" dengan "v" adalah prequisisite dari "u" 
	edge[u].append(v) 
	
def findZeroPrereqCourse():
	# Merupakan fungsi untuk mencari course yang prereqnya sudah 0
	# Course yang dipilih haruslah course yang belum pernah dikunjungi
	for i in range(len(prereqCount)):
		if(prereqCount[i] == 0 and unvisited(uniqueCourseId[i])):
			return uniqueCourseId[i]
	# Tidak ada course yang prereqnya 0, dipastikan graf bukan DAG
	return None
######################################################################################################
#------------------********************--------------------------********************----------------#

#------------------********************       Main Program        ********************---------------#                                                  
print("                                                                                            88             ")  
print("                                                                                            ``             ")              
print("8b,dPPYba,  ,adPPYYba,  8b,dPPYba,    ,adPPYba,  ,adPPYYba,  8b,dPPYba,    ,adPPYb,d8       88  8b,dPPYba, ")  
print("88P`   `Y8  ``     `Y8  88P`   ``8a  a8`     ``  ``     `Y8  88P`   ``8a  a8`    `Y88       88  88P`   ``8a")  
print("88          ,adPPPPP88  88       88  8b          ,adPPPPP88  88       88  8b       88       88  88       88")  
print("88          88,    ,88  88       88  `8a,   ,aa  88,    ,88  88       88  `8a,   ,d88  888  88  88       88")  
print("88          ``8bbdP`Y8  88       88   ``Ybbd8``  ``8bbdP`Y8  88       88   ``YbbdP`Y8  888  88  88       88")  
print("                                                                           aa,    ,88                      ")  
print("                                                                            `Y8bbdP`                       ")
print("                          rancang.in ~ Aplikasi perancang mata kuliah untukmu                              ")
print('============================================================================================================')
print('Pastikan anda sudah Membaca Readme terlebih dahulu!')
print('Made by Reihan Andhika Putra 13519043 --- Enjoy')
print('============================================================================================================')  																																                   
# Import library
from collections import defaultdict 
from time import sleep
import os
import roman # library yang harus di download -> untuk romawi di semester

# Deklarasi Variabel-Variabel Global
originaledge = defaultdict(list)    # dictionary yang merepresentasikan edge antara course dan prereqnya (original) 
edge = defaultdict(list)            # mirip seperti originaledge namun data edge akan dinamis sesuai algoritma TopoSort 
listOfMatkul = defaultdict(list)    # Dictionary antara course_id dan course_fullname
uniqueCourseId = []                	#	Kumpulan course_id unik dari input file
prereqCount = []                    # Jumlah prereq tiap modul
semValue = []                      	# Semester paling rendah tiap course_id
visitedNodes = []                   # Node yang sudah dikunjungi
coursePrereqs =[]

# Transition
sleep(3)
os.system("cls")

#  Membaca input dari file txt 
os.chdir("..") # Pindah ke directory atas
filename = input("Masukkan nama file (tanpa ekstensi): ")
inputss = open('test/'+ filename +'.txt','r').read().split('\n')
listMatkul = open('test/'+ "List Matkul" +'.txt','r').read().split('\n')

# Parsing input ( Membagi mana yang course_id dan mana yang preq_id dan memasukkan kebutuhan lainnya)
for inputs in inputss:
	inputs = inputs.replace(' ', '')
	inputs = inputs.replace('.','')
	courseSpec = inputs.split(',')
	courseId = courseSpec[0]
	uniqueCourseId.append(courseId)
	prereqCount.append(len(courseSpec)-1)
	semValue.append(1)
	coursePrereq =  courseSpec[1:]
	coursePrereqs.append(coursePrereq)
	for course in coursePrereq:
		addEdge(edge,courseId,course)
		addEdge(originaledge,courseId,course)

# Parsing input (Membentuk dictionary antara course_id dan course_fullname dari file "List Matkul")
for matkul in listMatkul:
	matkul = matkul.replace('\t', '')
	infoMatkul = matkul.split("-")
	addEdge(listOfMatkul,infoMatkul[0],infoMatkul[1])

# Transition
print("Membaca data pada file")
sleep(3)
os.system("cls")

# Algoritma Topological Sort dengan Pendekatan Decrease and Conquer
# Decrease and Conquer yang digunakan adalah decrease by constant (n=1)
def decreaseAndConquer(visitedNodes):
	# Base case : Semua node sudah dikunjungi
	if(len(visitedNodes)==len(uniqueCourseId)):
		print("Decrease and Conquer ~ selesai")
	else:
		print("Melakukan Decrease and Conquer ~ " + str(len(uniqueCourseId)-len(visitedNodes))+ " node yang harus dikunjungi")
		sleep(0.125)
		# Decrease : Ambil satu node(matkul) yang semua prequisisite nya sudah terpenuhi / tidak punya prequisisite
		# Masukkan ke daftar node yang sudah dikunjungi dan jangan proses node itu lagi
		zeroPrereqCourse = findZeroPrereqCourse()
		if zeroPrereqCourse is None:
			print("Siklus ditemukan!!!")
			print("Anda tidak memasukkan DAG")
			sleep(3)
			quit()
		visitedNodes.append(zeroPrereqCourse)
		# Proses node(matkul) lain yang berhubungan dengan node yang baru saja dikunjungi
		for course in edge:
			for prereq in edge[course]:
				if (prereq == zeroPrereqCourse):
					# Kurangi jumlah prequisisite tersisa dari matkul yang prequisisitenya adalah node(matkul) yang baru saja dikunjungi 
					prereqCount[uniqueCourseId.index(course)]-=1
					# Pastikan bahwa semua semester pelaksanaan suatu matkul haruslah setelah matkul prequisisitenya dilaksanakan
					if (semValue[uniqueCourseId.index(course)] <= semValue[uniqueCourseId.index(zeroPrereqCourse)]):
						semValue[uniqueCourseId.index(course)] = semValue[uniqueCourseId.index(zeroPrereqCourse)] + 1
					# Hilangkan edge(hubungan prequisisite) dari node(matkul) yang terhubung dengan node yang baru saja dikunjungi
					edge[course].pop((edge[course].index(prereq)))
		# Conquer : Secara rekursif, selesaikan hingga semua node dikunjungi
		decreaseAndConquer(visitedNodes)

# Inisialisasi Decrease and Conquer
decreaseAndConquer(visitedNodes)

# Transition
sleep(3)
os.system("cls")

# Menulis hasil Decrease and Conquer sesuai aturan
# Tulis peringatan apabila dibutuhkan lebih dari 8 semester untuk menyelesaikan semua matkul
print("  ____      _                                  _           _                                  ")
print(" |  _ \ ___| | _____  _ __ ___   ___ _ __   __| | __ _ ___(_)                                 ")
print(" | |_) / _ \ |/ / _ \| '_ ` _ \ / _ \ '_ \ / _` |/ _` / __| |                                 ")
print(" |  _ <  __/   < (_) | | | | | |  __/ | | | (_| | (_| \__ \ |                                 ")
print(" |_| \_\___|_|\_\___/|_| |_| |_|\___|_| |_|\__,_|\__,_|___/_|                                 ")
print("  ____                                  _     _ _               __  __       _   _          _ ")
print(" |  _ \ ___ _ __   __ _  __ _ _ __ ___ | |__ (_) | __ _ _ __   |  \/  | __ _| |_| | ___   _| |")
print(" | |_) / _ \ '_ \ / _` |/ _` | '_ ` _ \| '_ \| | |/ _` | '_ \  | |\/| |/ _` | __| |/ / | | | |")
print(" |  __/  __/ | | | (_| | (_| | | | | | | |_) | | | (_| | | | | | |  | | (_| | |_|   <| |_| | |")
print(" |_|   \___|_| |_|\__, |\__,_|_| |_| |_|_.__/|_|_|\__,_|_| |_| |_|  |_|\__,_|\__|_|\_\\__,_|_|")
print("                  |___/                                                                       ")
print("")
if(max(semValue)>8):
	print("Warning!! Untuk dapat menyelesaikan semua matkul dibutuhkan lebih dari 8 Semester")
elif(max(semValue)<8):
	print("Hooray!! Kamu bisa lulus tanpa harus sampai 8 Semester :)")
for i in range (max(semValue)):
	first = True
	print("Semester " + roman.toRoman(i+1)+": ", end="")
	for course in uniqueCourseId:
		if(semValue[uniqueCourseId.index(course)]==i+1):
			if (first):
				print(*listOfMatkul[course], end="")
				first = False
			else :
				print(", ", end="")
				print(*listOfMatkul[course], end="")
	print("")