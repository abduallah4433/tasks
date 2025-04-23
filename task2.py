nums = [11,2,3,34,5,6,7,8,9,10]
nums.sort(reverse=True)
print(nums)

print(len(nums))

name =['ali','ahmed','hamd']
age = [22,24,26]
city = ['ryadh','damam','jeddah']

l1= list(zip(name,age,city))
print(l1)

new_list=[]
for i in range(2,20+1,2):
    new_list.append(i)
print(new_list)