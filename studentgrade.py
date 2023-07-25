#Wapp for student grading program

students = int(input("Enter the no.of students whose grade you want to calculate : "))
for i in range (1, students+1):
		marks = int(input("Enter student marks: "))	
		if (marks < 0) or (marks > 100):
				print("Invalid marks ")	
		else:
			if marks >90:
				print("Grade is A+ ")
			elif marks in [80,81,82,83,84,85,86,87,88,89] :
				print("Grade is A ")
			elif (marks >= 70) and(marks <=79) :
				print("Grade is B ")
			elif (marks >= 60) and (marks <=69 ):
				print("Grade is C ")
			elif(marks >= 50) and (marks <=59):
				print("Grade is D ")
			elif marks < 50 :
				print("Fail")
