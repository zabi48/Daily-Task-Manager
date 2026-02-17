from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np

app = Flask(__name__)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

tasks = []
task_counter = 0  

@app.route("/", methods=["GET", "POST"])
def index():
    global task_counter
    if request.method == "POST":
        if "add_task" in request.form:
            task_name = request.form.get("task_name")
            deadline = int(request.form.get("deadline"))
            importance = int(request.form.get("importance"))
            effort = int(request.form.get("effort"))

            X_new = np.array([[deadline, importance, effort]])
            priority_num = model.predict(X_new)[0]
            priority = {1: "HIGH", 2: "MEDIUM", 3: "LOW"}.get(priority_num, "LOW")

            task_counter += 1
            tasks.append({
                "id": task_counter,
                "name": task_name,
                "deadline": deadline,
                "importance": importance,
                "effort": effort,
                "priority": priority,
                "done": False
            })

        elif "done_task" in request.form:
            task_id = int(request.form.get("done_task"))
            for task in tasks:
                if task["id"] == task_id:
                    task["done"] = True
                    break

        priority_order = {"HIGH": 1, "MEDIUM": 2, "LOW": 3}
        tasks.sort(key=lambda x: (x["done"], priority_order[x["priority"]], x["deadline"]))

    return render_template("index.html", tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)