stdname=input('Name of Student is: ')
USN=input('USN of Student is: ')
noOfsubjects=int(input('Enter number of subjects: '))
markslist = []
subjectList=[]

for i in range(noOfsubjects):

    print("Enter the subject: ")
    A=input()
    subjectList.append(A) 


for i in range(noOfsubjects):
    print("Enter the marks: ")
    B=int(input())
    markslist.append(B)

print("Student name is",stdname) 
print("Student USN is",USN)
print("Number of subjects is",noOfsubjects)
print("Total marks is",sum(markslist))
print("Total percentage is",sum(markslist)/len(markslist), '%')

    