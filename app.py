from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hey there, you have reached Jerald's page after edits. this is gonna fail now!"

if __name__ == '__main__':
    app.run()
