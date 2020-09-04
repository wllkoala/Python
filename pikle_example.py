import pickle
# 写入pickle1
a_dict = {'da': 111, 2: [23, 1, 4], '23': {1: 2, 'd': 'sad'}}
file = open('pickle_example.pickle', 'wb')
pickle.dump(a_dict, file)
file.close()
# 写入pickle2
with open('pickle_example.pickle', 'wb') as file:
    pickle.dump(a_dict, file)
# 从pickle读取1
file = open('pickle_example.pickle', 'rb')
a_dict1 = pickle.load(file)
file.close()
print(a_dict1)
# 从pickle读取2
with open('pickle_example.pickle', 'rb') as file:
    a_dict1 = pickle.load(file)
print(a_dict1)
