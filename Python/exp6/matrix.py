import numpy as np

class myMatrix:

	def __init__(self, rows=1, cols=1):
		self.rows = rows
		self.cols = cols
		self.matrix = np.random.random((rows, cols))

	def add(self, add_matr):
		for i in range(0, self.rows):
			for j in range(0, self.cols):
				self.matrix[i][j] = self.matrix[i][j] + add_matr.matrix[i][j]
	
	def subtr(self, subtr_matr):
		for i in range(0, self.rows):
			for j in range(0, self.cols):
				self.matrix[i][j] = self.matrix[i][j] - subtr_matr.matrix[i][j]

	def mult(self, multi_matr):
		for i in range(0, self.rows):
			for j in range(0, self.cols):
				for k in range(0, self.cols):
					self.matrix[i][j] = self.matrix[i][k] * multi_matr.matrix[k][j]	
	
	def display_matr(self):
		print(self.matrix)
		print("\n")

	def gen_inverse(self):
		"""
		returns matrix object with matrix inverse of current obj
		"""
		inv_obj = myMatrix()
		inv_obj.matrix = np.linalg.inv(self.matrix)
		return inv_obj

matr1 = myMatrix(3,3)
matr2 = myMatrix(3,3)

matr1.display_matr()
matr2.display_matr()

matr1.add(matr2)
matr1.display_matr()

matr2.subtr(matr1)
matr2.display_matr()

matr1.mult(matr2)
matr1.display_matr()

inv_obj = matr2.gen_inverse()
inv_obj.display_matr()

