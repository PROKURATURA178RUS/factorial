input_data = open('input.txt','r') 
data = input_data.read ()
data = data.split()
n = int(data[0])
pr = 1
pr_list = []
for i in range(1 , n + 1):
    pr *= i
    pr_list.append(pr)
    








output = open('output.txt', 'w') 
output.write(str(pr_list))

input_data.close() 
output.close()   