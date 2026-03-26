from flask import Flask, render_template, request, redirect, url_for, session, flash
from src.dataset_analysis import get_dummy_dataset_results

app = Flask(__name__)
app.secret_key = "smarthire_secret_key"


# Temporary student-level in-memory users
# Later you can store them in file/database
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
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

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
        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()

        if not username or not email or not password:
            flash("Please fill all fields.", "danger")
            return redirect(url_for("register"))

        if username in users:
            flash("Username already exists!", "danger")
            return redirect(url_for("register"))

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
        flash("Please login first.", "danger")
        return redirect(url_for("login"))

    history_data = [
        {
            "type": "Realtime",
            "date": "2026-03-25 15:27",
            "result": "77.9 BPM average"
        },
        {
            "type": "Dataset",
            "date": "2026-03-24 11:10",
            "result": "81.2% average accuracy"
        },
        {
            "type": "Realtime",
            "date": "2026-03-23 17:03",
            "result": "95.8 BPM average"
        }
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
        flash("Please login first.", "danger")
        return redirect(url_for("login"))

    monitor_data = {
        "current_bpm": 68,
        "min_bpm": 41,
        "avg_bpm": 63,
        "max_bpm": 86,
        "signal_quality": 100,
        "buffer_status": "150/150 frames",
        "status_text": "Normal heart rate"
    }

    return render_template(
        "monitor.html",
        title="Real-Time Monitor",
        user=session["user"],
        monitor_data=monitor_data
    )


@app.route("/dataset")
def dataset():
    if "user" not in session:
        flash("Please login first.", "danger")
        return redirect(url_for("login"))

    summary = get_dummy_dataset_results()

    return render_template(
        "dataset.html",
        title="Dataset Analysis",
        summary=summary
    )


@app.route("/model-info")
def model_info():
    if "user" not in session:
        flash("Please login first.", "danger")
        return redirect(url_for("login"))

    model_details = {
        "project_name": "SmartHire rPPG Heart Rate Monitor",
        "face_detection": "OpenCV Face Detection / planned DL upgrade",
        "roi_region": "Forehead Region of Interest (ROI)",
        "signal_used": "Green Channel Signal",
        "bpm_method": "FFT Based Estimation",
        "dataset": "UBFC-rPPG Dataset",
        "frontend": "HTML, CSS, JavaScript",
        "backend": "Flask (Python)"
    }

    return render_template(
        "dataset.html",
        title="Model Info",
        summary=get_dummy_dataset_results(),
        model_details=model_details
    )


@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully.", "success")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
