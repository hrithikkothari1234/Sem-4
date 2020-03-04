import numpy as np

class myMatrix:

	def __init__(self, rows=1, cols=1):
		self.rows = rows
		self.cols = cols
		self.matrix = np.random.random((rows, cols))

	def add(self, add_matr):
		self.matrix = np.add(self.matrix, add_matr.matrix)
	
	def subtr(self, subtr_matr):
		self.matrix = np.subtract(self.matrix, subtr_matr.matrix)

	def mult(self, multi_matr):
		self.matrix = np.multiply(self.matrix, multi_matr.matrix)

	def display_matr(self):
		print(self.matrix)
		print("\n")

	def gen_inverse(self):
		inv_obj = myMatrix()
		inv_obj.matrix = np.linalg.inv(self.matrix)
		return inv_obj

class sqMatrix(myMatrix):

	def __init__(self, rows=1, cols=1):
		super().__init__(rows, cols)
		if self.rows != self.cols:
			print("Not a square Matrix")

	def gen_inverse(self):
		inv_obj = sqMatrix()
		inv_obj.matrix = np.linalg.inv(self.matrix)
		return inv_obj

	def eigenvals(self):
		print(np.linalg.eig(self.matrix))
		
matr1 = myMatrix(3,3)
matr2 = myMatrix(3,3)

print("Matr1")
matr1.display_matr()
print("Matr2")
matr2.display_matr()

print("Matr1 after adding to Matr2")
matr1.add(matr2)
matr1.display_matr()

print("Matr2 after subtracting matr1 from it")
matr2.subtr(matr1)
matr2.display_matr()

print("Matr1 X Matr2")
matr1.mult(matr2)
matr1.display_matr()

print("Matr2 inverse")
inv_obj = matr2.gen_inverse()
inv_obj.display_matr()

print("SQMATR1")
sqmatr1 = sqMatrix(3,3)
sqmatr1.display_matr()

print("SQMatr1 Inverse")
sqmatr12inv = sqmatr1.gen_inverse()
sqmatr12inv.display_matr()

print("SQMatr1 Eigen Values")
sqmatr1.eigenvals()
