#The author is Cody Brown, Quiz 6 code 1
import dbm
db1 = dbm.open("photo_category","c")
db1['animals.png'] = 'contains pictures of animals'
db1['trees.png'] = 'containts pictures of trees'
db1['fruit.png'] = 'containts pictures of fruits'

# for item in db1.keys():
#     print(item, db1[item])

#Before update, prints:
# b'animals.png' b'contains pictures of animals'
# b'trees.png' b'containts pictures of trees'
# b'fruit.png' b'containts pictures of fruits'

db1['animals.png'] = 'animals located here'
db1['trees.png'] = 'trees located here'
db1['fruit.png'] = 'fruits located here'

for item in db1.keys():
    print(item, db1[item])

#This prints:
# b'animals.png' b'animals located here'
# b'trees.png' b'trees located here'
# b'fruit.png' b'fruits located here'
