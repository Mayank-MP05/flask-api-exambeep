import json

def updateProfile(email,prn_no,clg_id,mongo):
    getter = mongo.db.users.find_one({
        "email": email,
    })
    mongo.db.users.update_one({
    '_id': getter["_id"]
    },{
    '$set': {
        'prn_no':prn_no,
        'clg_id':clg_id,
    }
    }, upsert=False)
    getter = mongo.db.users.find_one({
        "email": email,
    })
    return json.dumps(getter,default=str)

def getProfileFromStuds(clg_id,prn_no,mongo):
    getter = mongo.db.students.find_one({
        "prn_no": prn_no,
        "clg_id":clg_id
    })
    return json.dumps(getter,default=str)