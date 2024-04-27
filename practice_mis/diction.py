#Today we will practice List, Tuple, Set, Dictionaries
#1. List

list = ['anuj', 22, 'MCA', 'MCA', 'anuj']   #duplicate  allowed, mutable[]
# print(list[0])
# print(len(list))
# list.append('Full Name: Anuj Pal')
# list.remove(list[len(list)-1])

# print(list)

tuple = ('anuj', 22, 'MCA', 'MCA')          #duplicate allowed , but immutable
# print(tuple[0])

# print(tuple)
# coor = (3,4)
# x,y = coor
# print(x, y)

set1 = {1,2,3,4,5}
set2 = {9,8,7,6,5}
# union = set1.union(set2)
# print(union)
# intersect = set1.intersection(set2)
# print(intersect)
# diff = set1.difference(set2)
# print(diff)
# set.add(6)
# print(set)

dic = {
    'name': 'Anuj', 
    'age': 22, 
    'religion': 'Hindu',
    'Place': 'Noida'
}
# print(dic)

# for i , j in dic.items():
#     print(i,"--->",j)

my_server = [
        {
            'server-name': 'ec2-instance-00a1',
            'operating-system': 'Linux-2020-v:1.0.12',
            'memory-used': 't2.micro',
            'security-Group': 'wizard-ec2-tokyo'
        },
        {
              'server-name': 'ec2-instance-00a2',
            'operating-system': 'Win-2020-v:1.0.12',
            'memory-used': 't3.medium',
            'security-Group': 'wizard-ec2-mumbai'
        },
          {
            'server-name': 'ec2-instance-00a3',
            'operating-system': 'Win-2022-v:1.0.12',
            'memory-used': 't2.medium',
            'security-Group': 'wizard-ec2-mumbai'
        }
]
# print(my_server[0]['server-name'])
for itm in my_server:
    for key, value in itm.items():
        print(value)
    print("---------------")
