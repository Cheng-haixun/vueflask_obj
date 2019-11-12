from flask import Flask,jsonify,request,json
from flask_cors import CORS
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
CORS(app, supports_credentials=True)
db=SQLAlchemy(app)
migrate=Migrate(app,db)

class account(db.Model):
    __tablename__='account'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(100))
    password=db.Column(db.String(100))
    def to_dict(self):
        data={
            'id':self.id,
            'username':self.username,
            'password':self.password
        }
        return data

@app.route('/',methods=['GET'])
def hello_world():
    return jsonify('hello world!')

#登录
@app.route('/login',methods=['GET','POST'])
def login():
    username=request.json.get('username')
    password=request.json.get('password')
    if username and password:
        ac=account.query.filter_by(username=username,password=password).first()
        if ac:
            return jsonify({'code':200,'msg':'ok'})
    return jsonify({'code':400,'msg':'error'})


#获取用户列表
@app.route('/getaccounts',methods=['GET'])
def getaccounts():
    alist=[]
    accounts=account.query.all()
    for a in accounts:
        alist.append(a.to_dict())
    return jsonify({'accounts':alist})

#编辑
@app.route('/editaccount',methods=['POST','GET'])
def editaccount():
    if request.method=='GET':
        aid=request.args.get('aid')
        ac=account.query.filter(account.id==aid).first()
        print('ac',ac.to_dict)
        return jsonify({'ac':ac.to_dict(),'code':200})
    if request.method=='POST':
        aid=request.json.get('aid')
        username=request.json.get('username')
        password=request.json.get('password')
        a=account.query.filter_by(id=aid).first()
        a.username=username
        a.password=password
        db.session.commit()
        return jsonify({'code':200})

#删除
@app.route('/delete',methods=['GET','POST'])
def delete():
    if request.method=='POST':
        aid = request.json.get('aid')
        ac = account.query.filter(account.id == aid).first()
        db.session.delete(ac)
        db.session.commit()
        return jsonify({'code': 200})


if __name__ == '__main__':
    app.run()
