#!/usr/bin/python
# -*- coding: utf-8 -*-
 
class operacion:

	def __init__(self):
		print "-----Bienvenido al juego 2048-----"

	def iniciarJuego(self):
		import random
		global n
		n = 4
		global matriz
		matriz = [[0] * n for f in range(n)]		
		for f in range(n):
		    for c in range(n):
		    	num=random.randint(0, 2)
		        matriz[f][c] = num * 2

	def imprimir(self):
		for fila in matriz:
			print(' '.join([str(elem) for elem in fila]))

	def izquierda(self):
		for f in range(n):
			for c in range(n):
				if(c < 3):
					if (matriz[f][c] == 2048):
						pass
					else:
						if (matriz[f][c] == matriz[f][c+1]):			
							matriz[f][c] = matriz[f][c] + matriz[f][c+1]
							globals()["matriz"][f][c+1] = 0
	
	def derecha(self):
		for f in range(n):
			for c in range(3,0,-1):
				if(c > 0):
					if (matriz[f][c] == 2048):
						pass
					else:
						if (matriz[f][c] == matriz[f][c-1]):			
							matriz[f][c] = matriz [f][c] + matriz[f][c-1]
							globals()["matriz"][f][c-1] = 0					
		
	def arriba(self):
		for f in range(n):
			for c in range(n):
				 if (f < 3):
				 	if (matriz[f][c] == 2048):
				 		pass
				 	else:
				 		if (matriz[f][c] == matriz[f+1][c]):
				 			matriz[f][c] = matriz[f][c] + matriz[f+1][c]
							globals()["matriz"][f+1][c] = 0

	def abajo(self):
		for f in range(3,0,-1):
			for c in range(n):
				if (f > 0):
					if (matriz[f][c] == 2048):
						pass
					else:
						if (matriz[f][c] == matriz[f-1][c]):
							matriz[f][c] = matriz[f][c] + matriz[f-1][c]
							globals()["matriz"][f-1][c] = 0

	

	def acomodArriba(self):
		f = 4
		while  f> 0:
			f -= 1
			for c in range(n):
				if(f > 0):
					if (matriz[f][c] > 0 and matriz[f-1][c]==0):	
						globals()["matriz"][f-1][c] = matriz[f][c] 
						globals()["matriz"][f][c] = 0
						c=4
						f=4
						break

	def acomodAbajo(self):
		f=-1
		while f < 4:
			f+=1
			for c in range(n):
				if(f < 3):
					if (matriz[f][c] > 0 and matriz[f+1][c]==0):			
						globals()["matriz"][f+1][c] = matriz[f][c] 
						globals()["matriz"][f][c] = 0
						c=4
						f=-1
						break

 	def acomodDerecha(self):
		for f in range(n):
			c=-1
			while c < 4:
				c+= 1
				if(c < 3):
					if (matriz[f][c] > 0 and matriz[f][c+1]==0):			
						globals()["matriz"][f][c+1] = matriz[f][c] 
						globals()["matriz"][f][c] = 0
						c=-1

	def acomodIzquierda(self):
		for f in range(n):
			c=4
			while c > 0:
				c-=1
				if(c > 0):
					if (matriz[f][c] > 0 and matriz[f][c-1]==0):			
						globals()["matriz"][f][c-1] = matriz[f][c] 
						globals()["matriz"][f][c] = 0
						c=4

	def nuevaCasilla(self):
		encontrado=0
		for f in range(n):
			c=-1
			while c < 3:
				c+=1
				if(matriz[f][c]==0):					
					globals()["matriz"][f][c] = 2
					encontrado=1
					c=4
					f=4
					break
			if (encontrado==1):
				break

	def calcularMovimientos(self, num):
		res=0
		res=(10 ** 2)
		if(1 <= num and num <= res):
			return num
		else:
			return 0

	def terminarJuego(self):
		print "\nTus movimientos terminaron\nFin del Juego"

	def validarNumeros(self,mensaje):
		while True:
			num= raw_input(mensaje)
			try:
				num=int(num)
				return num
				break
			except ValueError:
				print "Error: Ingresa solo numeros"

	def jugar(self):
		self.iniciarJuego()
		self.imprimir()
		numM =self.validarNumeros("Introduce el numero de movimientos: ")
		num=self.calcularMovimientos(numM)
		while num > 0:
			num=num-1
			mover =self.validarNumeros("Elige un movimiento \n1.- Izquierda \n2.- Derecha \n3.- Arriba \n4.- Abajo\n ") 
			if 1 == mover:
				print "---Izquierda---"
				self.acomodIzquierda()
				self.izquierda()
				self.acomodIzquierda()
				self.nuevaCasilla()
				self.imprimir()
				num=num-1
			elif mover == 2:
				print "---Derecha---"
				self.acomodDerecha()
				self.derecha()
				self.acomodDerecha()
				self.nuevaCasilla()
				self.imprimir()
				num=num-1
			elif mover == 3:
				print "---Arriba---"
				self.acomodArriba()
				self.arriba()
				self.acomodArriba()
				self.nuevaCasilla()
				self.imprimir()
				num=num-1
			elif mover == 4:
				print "---Abajo---"
				self.acomodAbajo()
				self.abajo()
				self.acomodAbajo()
				self.nuevaCasilla()
				self.imprimir()
				num=num-1
			else:
				print "**Elige un movimiento valido**"
    			num+=1
    	
    
objOperacion=operacion()
objOperacion.jugar()
objOperacion.terminarJuego()


