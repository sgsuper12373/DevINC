import flask from Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def calculate():
    data = request.get_json()
    #convert json file into dictionary in python

    # Notify if wrong dataformat is give
    if not data or 'num1' not in data or 'num2' not in data or 'operation' not in data:
        return jsonify({'error': 'Missing required parameters'}), 400  #bad request error message
    #getting values of num1, num2 and opration 
    num1 = float(data['num1'])
    num2 = float(data['num2'])
    operation = data['operation']


    # Perform the operation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            return jsonify({'error':"Can't divide by zero"}), 400
        result = num1 / num2
    else:
        return jsonify({'error': 'Invalid operation'}), 400

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
