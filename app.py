from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "secret"  # Used to add encryption to flash messages

tasks = ["Buy groceries", "Finish homework", "Walk the dog"]

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task = request.form["task"]
    tasks.append(task)
    flash("Task added successfully.")
    return redirect(url_for("index"))

@app.route("/delete", methods=["POST"])
def delete():
    task = request.form["task"]
    if task in tasks:
        tasks.remove(task)
        flash("Task deleted successfully.")
    else:
        flash("Task not found.")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
