from flask import Flask, send_file
app = Flask(__name__)

@app.route('/', defaults={'_path': ''})
@app.route("/<path:_path>")
def aloha(_path):
    return send_file("aloha.jpg", mimetype="image/jpg")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
