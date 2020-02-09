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
	
	def display_matr(self):
		print(self.matrix)
		print("\n")

matr1 = myMatrix(3,3)
matr2 = myMatrix(3,3)

matr1.display_matr()
matr2.display_matr()

matr1.add(matr2)
matr1.display_matr()

matr1.subtr(matr2)
matr1.display_matr()

