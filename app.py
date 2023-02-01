from flask import Flask, jsonify, make_response, abort

app = Flask(__name__)

@app.route('/')
def home():
    return 'Home Page'

@app.route('/interfaces')
def interfaces():
    try:
        myfile = open("interfaces.txt", 'r')
    except OSError:
        abort(400)
    d = {}
    ipAddr = ""
    for line in myfile:
        v = line.split(" ")
        # for loop in the range of the split string to find ip address
        for i in range(len(v)):
            if "addr:" in v[i]:
                ipAddr = v[i][5:]
                break

        k = line.split(" ")[0]

        if k == "\n":
            continue
        else:
            d[k] = ipAddr

    myfile.close()
    d = {"ComputerInterfaces": d}
    res = make_response(jsonify(d), 200)
    return res

@app.route('/iproutes')
def iproutes():
    try:
        myfile = open("iproutes.txt", 'r')
    except OSError:
        abort(500)
    return myfile

@app.errorhandler(404)
def invalid_route(e):
    return jsonify({'errorCode' : 404, 'message' : 'Route not found'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

