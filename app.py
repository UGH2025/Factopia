from flask import Flask, send_from_directory

app = Flask(__name__)

# Serve index.html from the root folder
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Serve any JSON file from the data folder
@app.route('/data/<filename>')
def get_data(filename):
    return send_from_directory('data', filename)

if __name__ == '__main__':
    print("Server running at http://127.0.0.1:5000")
    app.run(debug=True, port=5000)