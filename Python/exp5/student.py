class student:

	def __init__(self, rollno, number, score):
		self.rollno = rollno
		self.number = number
		self.score = score

	def calcgrade(self):
		if self.score >= 80 and self.score <= 100:
			grade = "A"
		elif self.score >= 60 and self.score <= 79:
			grade = "B"
		elif self.score >= 40 and self.score <=59:
			grade = "C"
		
		else:
			grade = "D"
		print(grade)

stud = student(8677, "Hritik", 84)
stud.calcgrade()