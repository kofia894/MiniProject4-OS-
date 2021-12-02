# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask,jsonify, request

app = Flask(__name__)


@app.route('/')
def index():
    # Use a breakpoint in the code line below to debug your script.
    return "Mini Project 4: Docker Based Web Application" # Press Ctrl+F8 to toggle the breakpoint.

@app.route("/permissions", methods=['GET'])
def permissions():

    permission = {'0': '[]',
                  '1': '[execute]',
                  '2': '[execute,write]',
                  '3': '[write]',
                  '4': '[read]',
                  '5':'[read, execute]',
                  '6':'[read, write]',
                  '7':'[read,write,execute]'}

    users = {0: 'owner',
             1: 'group',
             2: 'other'}
    i = 0
    out = {}

    if 'code' in request.args:
        code = request.args['code']

        for j in code:
            out[users[i]] = permission[j]
            i += 1

        return jsonify(out)


@app.route("/parity", methods=['GET'])
def parity():
    bits = request.args.to_dict()

    bit1 = 0

    for i in bits:
        bit1 = bit1 ^ int(bits[i])

    return jsonify("Parity bit: " + str(bit1))

if __name__ == "__main__":
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
