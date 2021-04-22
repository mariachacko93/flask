# from pymongo import MongoClient

# from flask import Flask
# app=Flask(__name__)



# # collectionname = "trying"

# client=MongoClient("127.0.0.1",27017)

# db=client["test"]

# @app.route("/users",methods=["GET"])
# def create_user():    
#     user={"name":"sachin","lastname":"sebastian"}
#     db["users"].save(user)
#     return "x"



# if __name__=="__main__":
#     app.run(debug=True)


from flask import Flask
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify,request
from werkzeug.security import generate_password_hash,check_password_hash


app=Flask(__name__)
app.secret_key="secretkey"
app.config['MONGO_URI'] = "mongodb://localhost:27017/test"
mongo = PyMongo(app)


@app.route("/add",methods=["POST"])
def add_user():
    _json=request.json
    _name=_json['name']
    _email=_json['email']
    _password=_json['password']

    if _name and _email and _password and request.method=='POST':
        _hashed_password=generate_password_hash(_password)
        
        id=mongo.db.usertable.insert({'name':_name,'email':_email,'password':_hashed_password})
        resp=jsonify("user added successfully!!")

        resp.status_code=200
        return resp
    else:
        return not_found()


@app.route('/userslist',methods=['GET'])
def users():
        users=mongo.db.usertable.find()
        resp=dumps(users)
        return resp

@app.route('/users/<id>',methods=["GET"])
def user(id):
    user=mongo.db.usertable.find_one({'_id':ObjectId(id)})
    resp=dumps(user)
    return resp

@app.route('/update/<id>',methods=["PUT"])
def update_user(id):
    _id=id 
    _json=request.json
    
    _name=_json['name']
    _email=_json['email']
    _password=_json['password']

    if _name and _email and _password and request.method=='PUT':
        _hashed_password=generate_password_hash(_password)
        mongo.db.usertable.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)},
                         {'$set': {'name': _name, 'email': _email, 'password': _hashed_password}})   
        resp=jsonify("user updated successfully!!")

        resp.status_code=200
        return resp
    else:
        return not_found()

@app.route('/userdelete/<id>',methods=["DELETE"])
def delete_user(id):
    user=mongo.db.usertable.delete_one({'_id':ObjectId(id)})
    resp=jsonify("user deleted successfully!!")

    resp.status_code=200
    return resp

@app.errorhandler(404)
def not_found(error=None):
    message={
        'status':404,
        'message':'not found'+request.url

    }
    resp=jsonify(message )
    resp.status_code=200
    return resp



@app.route('/search', methods = ['GET'])
def search():
    search = mongo.db.usertable
    name=request.args.get('name')
    email=request.args.get('email')

    output = []
    for q in search.find({"$or":[{'name':name},{'email':email}]}):   
        output.append({'name' : q['name'], 'email' : q['email']})
    if len(output)!=0 :
        return jsonify({'result' : output})
    else:
        return jsonify({'result' : 'No Results Found'})


if __name__=="__main__":
    app.run(debug=True)





