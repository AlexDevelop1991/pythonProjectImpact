#Declaring datas
regist = []
student= {}
#read data from user
st_num = int(input("How many students do you want to add:"))
sub_num =int(input('How many subjects they have'))
#for cycle

for j in range(0, 5):
    #read names
    s_name = input('Name')
    student.update({'Name': s_name})

    for i in range(0, 5):
        #Read data about subj and mark
         subject = input('Subject')
         mark = int(input('Mark'))

        #Add this data to dictionary
         student.update({subject: mark})
    #Add students to register
    regist.append(student.copy)
#Print regist
print(regist)







