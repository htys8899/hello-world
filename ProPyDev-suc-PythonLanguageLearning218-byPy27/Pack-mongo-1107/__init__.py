# coding=utf-8
# mongod --dbpath=f:\mymongodata\db  running at cmd firstly
import pymongo
import random
import json

conn = pymongo.Connection("127.0.0.1",27017)   # 27017 ��DAY5������ģʽ�²���ʱ����Ҫ�Ķ˿ڵ�2222 ��
print conn.PORT 
print conn.__module__ 
# db = conn.tage      #���ӿ⣬ 20161116����databases, ����ʾ ��tage��
db = conn.test     #���ӿ⣬ 20161116����databases, ����ʾ ��tage��

print  "��ִ��db.authenticate(tage,123) ������Except������ô�����ݿ�Ҫ��ǰ��ʲô���ã�"
db.user.drop()     # ��show collections ������ʾ "user" ;
db.person.drop()     # ��show collections ������ʾ "user" ;
db.user.save({'id':1,'name':'kaka','sex':'male'})
db.person.save({'id':1,'name':'kaka','sex':'male'})

for id in xrange(2,12):
    name = random.choice(['steve','koby','owen','tody','rony','hylon','data58','cybersun'])
    sex = random.choice(['male','female','undecision'])
    db.user.insert({'id':id,'name':name,'sex':sex})
    db.person.insert({'id':id,'name':name,'sex':sex}) 
    
content = db.user.find()
content1=db.person.find()
    #��ӡ��������
for i in content:
    print i
for i in content1:
    print i


single = {"name":"jack","password":"12345","age":20,
        "address":{"province":"anhui","city":"hefei"},"favourite":["apple","banana"] }

db.user.save(single)   #����һ����򣬲��ң�����һ������save
db.person.save(single)   #����һ����򣬲��ң�����һ������save

single1={"name":"wang","password":"12345","age":22,
        "address":{"province":"anhui","city":"hefei"},
        "favourite":["apple","banana9999"]}
db.user.insert(single1)
db.person.insert(single1)

print db.user.find()
print db.person.find()

#ͨ��ѭ������һ������
content = db.user.find()
content1=db.person.find()

#��ӡ��������
for i in content:
    print i
for i in content1:
    print i
    
print  "end ok!!"
