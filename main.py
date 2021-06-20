from flask import Flask

app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    return'<h1>Thi si flask application</h1>'


if __name__=='__main__':
    app.run()