from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = "smarthire_secret_key"

# temporary student-level dummy users
users = {
    "admin": {
        "password": "1234",
        "email": "admin@gmail.com"
    },
    "ganesh": {
        "password": "1234",
        "email": "ganarm2003@gmail.com"
    }
}


@app.route("/")
def home():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in users and users[username]["password"] == password:
            session["user"] = username
            session["email"] = users[username]["email"]
            flash("Login successful!", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid username or password", "danger")

    return render_template("login.html", title="Login")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        if username in users:
            flash("Username already exists!", "danger")
        else:
            users[username] = {
                "password": password,
                "email": email
            }
            flash("Registration successful! Please login.", "success")
            return redirect(url_for("login"))

    return render_template("register.html", title="Register")


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    history_data = [
        {"type": "Realtime", "date": "2026-03-25 15:27", "result": "77.9 BPM average"},
        {"type": "Dataset", "date": "2026-03-24 11:10", "result": "81.2% average accuracy"},
        {"type": "Realtime", "date": "2026-03-23 17:03", "result": "95.8 BPM average"},
    ]

    return render_template(
        "dashboard.html",
        title="Dashboard",
        user=session["user"],
        email=session["email"],
        history_data=history_data
    )


@app.route("/monitor")
def monitor():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("monitor.html", title="Real-Time Monitor", user=session["user"])


@app.route("/dataset")
def dataset():
    if "user" not in session:
        return redirect(url_for("login"))

    summary = [
        {"subject": "5-gt", "gt_hr": 77.3, "est_hr": 63.5, "error": 13.9, "accuracy": "82.1%"},
        {"subject": "6-gt", "gt_hr": 82.6, "est_hr": 68.0, "error": 14.6, "accuracy": "82.3%"},
        {"subject": "7-gt", "gt_hr": 94.7, "est_hr": 78.1, "error": 16.6, "accuracy": "82.5%"},
        {"subject": "8-gt", "gt_hr": 68.1, "est_hr": 52.3, "error": 15.9, "accuracy": "76.7%"},
    ]

    return render_template("dataset.html", title="Dataset Analysis", summary=summary)


@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully.", "success")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
