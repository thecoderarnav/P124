from flask import Flask, jsonify, request
app = Flask(__name__)
tasks =[
    {
        "id":1, 
        "name":"Raju",
        "contact":"26342635",
        "done": False
    },
    {
        "id":2, 
        "name":"Rahul",
        "contact":"26352636",
        "done": False
    }
]
@app.route("/")

@app.route("/add-data", methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"provide data"
        },400)
    task = {
        "id":tasks[-1]["id"]+1,
        "name":request.json["name"],
        "contact": request.json.get("contact",""),
        "done":False
    }
    tasks.append(task)
    return jsonify({
         "status":"success",
        "message":"contact added"
    })    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })

if (__name__ == "__main__"):
    app.run(debug = True)
