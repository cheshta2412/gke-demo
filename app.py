from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

# from flask import Flask

# app=Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello World,This is App 1'

# if __name__ =='__main__':
#     app.run(debug=True,port=8080,host='0.0.0.0')
