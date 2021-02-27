from flask import jsonify
import json
import random

#Login Function
def login(email,password,isCollege,mongo):
    getter = mongo.db.users.find_one({"email":email})
    #if user is not present in DB
    if getter is None:
        return jsonify({
            "err":f'No user exists with email {email}'
        })
    else:
        if getter["password"] == password:
            print(getter)
            # getter._id = None
            # getter.password = None
            ul = [] 
            for doc in getter:
                print(doc)
                ul.append(doc)
            return json.dumps(getter, default=str)
        else:
            return jsonify({
                "err":f'Wrong Password'
            })

#Signup Function
def signup(email,pass1,pass2,isCollege,mongo):
    dp = random.randint(0,8)
    if pass1 != pass2:
        return jsonify({
            "err":"Password do not match!",
        })
    getter = mongo.db.users.insert_one({
        "name": "",
        "password": pass1,
        "prn_no":"",
        "clg_id":"",
        "email": email,
        "profilePic": dp,
        "isCollege":isCollege
    }).inserted_id
    #if user is not present 
    if getter is None:
        return jsonify({
            "err":"Something error occured!"
        })
    else:
        setter = mongo.db.users.find_one({"_id":getter})
        return json.dumps(setter,default=str)
