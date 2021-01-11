from flask import Flask, render_template, jsonify
from auth import loginClass
from extern import query
import pickle
from sklearn import tree


app=Flask(__name__)


@app.route("/",methods=["POST","GET"])
def index():
    return render_template("maps_template.html")

@app.route("/login",methods=["POST","GET"])
def login():
    return render_template("login.html")

@app.route("/profileData",methods=["POST","GET"])
def profileData():
    sql="SELECT * FROM user_data WHERE user_id=1 ORDER BY id DESC LIMIT 30"
    data=query(sql,"select",[])
    return jsonify(data)

@app.route("/predictdib",methods=['POST','GET'])
def predictDiabets():
    with open('model.pickle', 'rb') as handle:
        clf2 = pickle.load(handle)
        ##'age','anaemia','high_blood_pressure','sex','smoking','time','creatinine_phosphokinase','ejection_fraction','serum_creatinine','serum_sodium'
        ##clf2.predict([[75.0, 0, 1, 1, 0, 4, 582, 20, 1.9, 130]])
        print(clf2.predict([[75.0, 0, 1, 1, 0, 4, 582, 20, 1.9, 130]]))
    return "You have diabet"

@app.route("/auth/login",methods=["POST","GET"])
def loginAuth():
    if request.method=="POST":
        username=request.form['username']
        password=request.form['password']
        loginClass(username,pasword)
        return redirect(url_for("index"))
    else:
        return False

if __name__ == "__main__":
    app.run(debug=True)