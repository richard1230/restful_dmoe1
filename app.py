from flask import Flask,render_template,url_for
from flask_restful import Api,Resource

app = Flask(__name__)
api = Api(app)


class LoginView(Resource):
    def post(self,username=None):
        return {"username":"richard"}

api.add_resource(LoginView,'/login/<username>/','/regist/')
#,endpoint='login'

# with app.test_request_context():
#     print(url_for('loginview',username='richard'))




@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
