from flask import Flask, jsonify, request, render_template
import motor

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move():
    # Support both JSON and Form data
    if request.is_json:
        data = request.get_json()
        action = data.get('action')
    else:
        action = request.form.get('action')

    if action == 'forward':
        motor.forward()
    elif action == 'backward':
        motor.backward()
    elif action == 'left':
        motor.turnLeft()
    elif action == 'right':
        motor.turnRight()
    elif action == 'stop':
        motor.stop()
    
    print("motor is going %s" % action)

    return jsonify({'status': 'success', 'action': action})

@app.route('/domino', methods=['POST'])
def domino():
    if request.is_json:
        data = request.get_json()
        state = data.get('state') # boolean or 'on'/'off'
    else:
        state = request.form.get('state')

    if state == 'on' or state is True:
        motor.dominoRun()
        status = 'running'
    else:
        motor.dominoStop()
        status = 'stopped'
    
    return jsonify({'status': 'success', 'domino': status})


if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        motor.cleanup()
        print("Server stopped and GPIO cleaned up.")



