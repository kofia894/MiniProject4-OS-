# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask,jsonify, request

app = Flask(__name__)


@app.route('/')
def index():
    # Use a breakpoint in the code line below to debug your script.
    return "Mini Project 4: Docker Based Web Application" # Press Ctrl+F8 to toggle the breakpoint.

@app.route("/permissions/<code>", methods=['GET','POST'])
def permissions(code):

    permission = {'0': '[]',
                  '1': '[execute]',
                  '2': '[execute,write]',
                  '3': '[write]',
                  '4': '[read]',
                  '5':'[read, execute]',
                  '6':'[read, write]',
                  '7':'[read,write,execute]' }

    users = {0: 'owner',
             1: 'group',
             2: 'other'}
    i = 0
    out = {}
    for j in code:
        out[users[i]] = permission[j]
        i += 1

    if (request.method == 'GET'):
        data = out
        return jsonify({'data': data})



@app.route("/parity/<b1>&<b2>&<b3>&<b4>", methods=['GET','POST'])
def parity(b1, b2, b3, b4):
    bits = [b1, b2, b3, b4]

    bit1 = []
    bit2 = []

    parity_bit = " "
    j = 0
    for i in range(0, len(bits)):
        bit1[j] = i[0]
        bit2[j] = i[1]
        j += 1

    k = 0
    parity1 = bit1[k] ^ bit1[k+1] ^ bit1[k+2] ^ bit1[k+3]
    parity2 = bit2[k] ^ bit2[k+1] ^ bit2[k+2] ^ bit2[k+3]

    parity_bit += str(parity2) + str(parity1)

    return parity_bit




if __name__ == "__main__":
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
