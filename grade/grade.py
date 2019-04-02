f = open("sci_grade.txt")

content_number_of_Ap = 0
content_number_of_A = 0
content_number_of_Am = 0
content_number_of_Bp = 0
content_number_of_B = 0
content_number_of_Bm = 0
content_number_of_Cp = 0
content_number_of_C = 0
content_number_of_Cm = 0
content_number_of_Dp = 0
content_number_of_D = 0
content_number_of_Dm = 0

working_number_of_Ap = 0
working_number_of_A = 0
working_number_of_Am = 0
working_number_of_Bp = 0
working_number_of_B = 0
working_number_of_Bm = 0
working_number_of_Cp = 0
working_number_of_C = 0
working_number_of_Cm = 0
working_number_of_Dp = 0
working_number_of_D = 0
working_number_of_Dm = 0

grading_number_of_Ap = 0
grading_number_of_A = 0
grading_number_of_Am = 0
grading_number_of_Bp = 0
grading_number_of_B = 0
grading_number_of_Bm = 0
grading_number_of_Cp = 0
grading_number_of_C = 0
grading_number_of_Cm = 0
grading_number_of_Dp = 0
grading_number_of_D = 0
grading_number_of_Dm = 0

teaching_number_of_Ap = 0
teaching_number_of_A = 0
teaching_number_of_Am = 0
teaching_number_of_Bp = 0
teaching_number_of_B = 0
teaching_number_of_Bm = 0
teaching_number_of_Cp = 0
teaching_number_of_C = 0
teaching_number_of_Cm = 0
teaching_number_of_Dp = 0
teaching_number_of_D = 0
teaching_number_of_Dm = 0

for line in f:
	if line == "Content:	A+\n":
		content_number_of_Ap+=1
	elif line == "Content:	A\n":
		content_number_of_A+=1
	elif line == "Content:	A-\n":
		content_number_of_Am+=1
	elif line == "Content:	B+\n":
		content_number_of_Bp+=1
	elif line == "Content:	B\n":
		content_number_of_B+=1
	elif line == "Content:	B-\n":
		content_number_of_Bm+=1
	elif line == "Content:	C+\n":
		content_number_of_Cp+=1
	elif line == "Content:	C\n":
		content_number_of_C+=1
	elif line == "Content:	C-\n":
		content_number_of_Cm+=1
	elif line == "Content:	D+\n":
		content_number_of_Dp+=1
	elif line == "Content:	D\n":
		content_number_of_D+=1
	elif line == "Content:	D-\n":
		content_number_of_Dm+=1
	elif line == "Grading:	A+\n":
		grading_number_of_Ap+=1
	elif line == "Grading:	A\n":
		grading_number_of_A+=1
	elif line == "Grading:	A-\n":
		grading_number_of_Am+=1
	elif line == "Grading:	B+\n":
		grading_number_of_Bp+=1
	elif line == "Grading:	B\n":
		grading_number_of_B+=1
	elif line == "Grading:	B-\n":
		grading_number_of_Bm+=1
	elif line == "Grading:	C+\n":
		grading_number_of_Cp+=1
	elif line == "Grading:	C\n":
		grading_number_of_C+=1
	elif line == "Grading:	C-\n":
		grading_number_of_Cm+=1
	elif line == "Grading:	D+\n":
		grading_number_of_Dp+=1
	elif line == "Grading:	D\n":
		grading_number_of_D+=1
	elif line == "Grading:	D-\n":
		grading_number_of_Dm+=1
	elif line == "Workload:	A+\n":
		working_number_of_Ap+=1
	elif line == "Workload:	A\n":
		working_number_of_A+=1
	elif line == "Workload:	A-\n":
		working_number_of_Am+=1
	elif line == "Workload:	B+\n":
		working_number_of_Bp+=1
	elif line == "Workload:	B\n":
		working_number_of_B+=1
	elif line == "Workload:	B-\n":
		working_number_of_Bm+=1
	elif line == "Workload:	C+\n":
		working_number_of_Cp+=1
	elif line == "Workload:	C\n":
		working_number_of_C+=1
	elif line == "Workload:	C-\n":
		working_number_of_Cm+=1
	elif line == "Workload:	D+\n":
		working_number_of_Dp+=1
	elif line == "Workload:	D\n":
		working_number_of_D+=1
	elif line == "Workload:	D-\n":
		working_number_of_Dm+=1
	elif line == "Teaching:	A+\n":
		teaching_number_of_Ap+=1
	elif line == "Teaching:	A\n":
		teaching_number_of_A+=1
	elif line == "Teaching:	A-\n":
		teaching_number_of_Am+=1
	elif line == "Teaching:	B+\n":
		teaching_number_of_Bp+=1
	elif line == "Teaching:	B\n":
		teaching_number_of_B+=1
	elif line == "Teaching:	B-\n":
		teaching_number_of_Bm+=1
	elif line == "Teaching:	C+\n":
		teaching_number_of_Cp+=1
	elif line == "Teaching:	C\n":
		teaching_number_of_C+=1
	elif line == "Teaching:	C-\n":
		teaching_number_of_Cm+=1
	elif line == "Teaching:	D+\n":
		teaching_number_of_Dp+=1
	elif line == "Teaching:	D\n":
		teaching_number_of_D+=1
	elif line == "Teaching:	D-\n":
		teaching_number_of_Dm+=1

print ("------content-------\n",
content_number_of_Ap,"\n",
content_number_of_A,"\n",
content_number_of_Am,"\n",
content_number_of_Bp,"\n",
content_number_of_B,"\n",
content_number_of_Bm,"\n",
content_number_of_Cp,"\n",
content_number_of_C,"\n",
content_number_of_Cm,"\n",
content_number_of_Dp,"\n",
content_number_of_D,"\n",
content_number_of_Dm,"\n",
"------workload-------\n",
working_number_of_Ap,"\n",
working_number_of_A,"\n",
working_number_of_Am,"\n",
working_number_of_Bp,"\n",
working_number_of_B,"\n",
working_number_of_Bm,"\n",
working_number_of_Cp,"\n",
working_number_of_C,"\n",
working_number_of_Cm,"\n",
working_number_of_Dp,"\n",
working_number_of_D,"\n",
working_number_of_Dm,"\n",
"------grade-------\n",
grading_number_of_Ap,"\n",
grading_number_of_A,"\n",
grading_number_of_Am,"\n",
grading_number_of_Bp,"\n",
grading_number_of_B,"\n",
grading_number_of_Bm,"\n",
grading_number_of_Cp,"\n",
grading_number_of_C,"\n",
grading_number_of_Cm,"\n",
grading_number_of_Dp,"\n",
grading_number_of_D,"\n",
grading_number_of_Dm,"\n",
"------teach-------\n",
teaching_number_of_Ap,"\n",
teaching_number_of_A,"\n",
teaching_number_of_Am,"\n",
teaching_number_of_Bp,"\n",
teaching_number_of_B,"\n",
teaching_number_of_Bm,"\n",
teaching_number_of_Cp,"\n",
teaching_number_of_C,"\n",
teaching_number_of_Cm,"\n",
teaching_number_of_Dp,"\n",
teaching_number_of_D,"\n",
teaching_number_of_Dm,"\n",)
	