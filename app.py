from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app, origins=["*"])  # This allows all origins


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    input = request.form.get('input')
    data = {"Form-Input":input}
    post_request = requests.post("https://jfmyiqt6rb.execute-api.us-east-1.amazonaws.com/Add-Task", json=data)
    return redirect(url_for('index')) 

@app.route('/view-task', methods=['GET'])
def view_task():
    get_request = requests.get("https://jfmyiqt6rb.execute-api.us-east-1.amazonaws.com/Get-Task")
    Json_obj = json.loads(get_request.text)
    print(type(Json_obj))
    FIlter_task_dictionary =  [dictionary for dictionary in Json_obj if dictionary['task_description'] != ''] ##Remove empty tasks
    tasks =  [dictionary['task_description'] for dictionary in FIlter_task_dictionary]
    # Example structure: {"tasks": ["Buy milk", "Call mom"]}
    
    return render_template("view-task.html", tasks=tasks)


if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000, debug=False)