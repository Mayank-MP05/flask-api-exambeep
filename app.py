from flask import Flask,request,render_template
from werkzeug.utils import secure_filename
from flask_cors import CORS
from flask_pymongo import PyMongo
import io
import csv

######### Modules Import ######### 
import user_auth
import uploaders
import profile_updator
import user_side_queries
import college_side_queries

app = Flask(__name__)


app.config["MONGO_URI"] = "mongodb://localhost:27017/weedDB"
app.config['UPLOAD_FOLDER'] = "files_here/"

mongo = PyMongo(app)
############### Demo ##########################3
@app.route('/')
def hello_world():
    return 'Hello, world Simple Flask API here!'

#################### User Auth ##################
@app.route("/api/login",methods=["POST"])
def loginHere():
    data = request.get_json()
    print(data)
    return user_auth.login(data["email"],data["pass1"],mongo)  

@app.route("/api/signup",methods=["POST"])
def SignupHere():
    data = request.get_json()
    print(data)
    return user_auth.signup(data["email"],data["pass1"],data["pass2"],data["isCollege"],mongo)  

@app.route("/api/getUserProfile",methods=["POST"])
def getUserProfile():
    data = request.get_json()
    print(data)
    return user_auth.getUserProfile(data["email"],mongo)  

################ Uploader Functions ########################
@app.route('/api/upload', methods=["POST"])
def uploadData():
    file = request.files["fileToBeUploaded"]
    data = request.get_json()
    coll = request.form["collection"]
    return uploaders.upload(file,coll,mongo)
    
    
################### User PRN Updator #######################
@app.route('/api/userUpdation', methods=["POST"])
def userUpdation():
    data = request.get_json()
    return profile_updator.updateProfile(data["email"],data["prn_no"],data["clg_id"],mongo)

################## Get User Profile ####################
@app.route('/api/getUserProfile', methods=["POST"])
def getProfileDetails():
    data = request.get_json()
    return profile_updator.getProfileFromStuds(data["clg_id"],data["prn_no"],mongo)

########### Student Side Exam and Result Quries #############
@app.route('/api/getExams', methods=["POST"])
def getExams():
    data = request.get_json()
    return user_side_queries.getExams(data["clg_id"],data["branch_id"],mongo)

@app.route('/api/getResults', methods=["POST"])
def getResults():
    data = request.get_json()
    return user_side_queries.getResults(data["clg_id"],data["branch_id"],mongo)

###################################################################
####################### College Side Queries #####################

@app.route('/api/collegeGetStudents', methods=["POST"])
def getCollegeStudents():
    data = request.get_json()
    return college_side_queries.getStudents(data["clg_id"],mongo)


@app.route('/api/collegeGetExams', methods=["POST"])
def getCollegeExams():
    data = request.get_json()
    return college_side_queries.getExams(data["clg_id"],mongo)

@app.route('/api/collegeGetResults', methods=["POST"])
def getCollegeResults():
    data = request.get_json()
    return college_side_queries.getResults(data["clg_id"],mongo)

if __name__ == "__main__":
    CORS(app)
    app.run(debug = True)