"""CCC181 Week 2: a "Hello, Flask" starter app.

Run it with:
    flask --app app run --debug
then open http://127.0.0.1:5000
"""
from flask import Flask, abort, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = "dev-only-change-me" 

SERVICES = [
    {"id": 1, "name": "Sizing & Payment"},
    {"id": 2, "name": "Uniform Claiming / Pickup"},
]

# Sample data for the demo. A real app would load this from a database later.
# status is one of: waiting, called, served, no-show
TICKETS = [
    {
        "number": 1,
        "name": "Juane dela Craige",
        "email": "juan.delacraige@g.msuiit.edu.ph",
        "student_id": "2026-0001",
        "service_id": 1,
        "status": "waiting",
    },
    {
        "number": 2,
        "name": "Bam Bart",
        "email": "bam.bart@g.msuiit.edu.ph",
        "student_id": "2026-0002",
        "service_id": 2,
        "status": "waiting",
    },
]


@app.route("/")
def index():
    # render_template looks inside the templates/ folder and passes
    # keyword arguments to the template as variables.
    return render_template("index.html")


@app.get("/queue/<int:ticket_id>")
def ticket(ticket_id):
    t = next((t for t in TICKETS if t["number"] == ticket_id), None)
    if t is None:
        abort(404)
        
    ahead = [x for x in TICKETS
             if x["service_id"] == t["service_id"]
             and x["status"] == "waiting"
             and x["number"] < t["number"]]
             
    service = next(s for s in SERVICES if s["id"] == t["service_id"])
    position = len(ahead) + 1
    
    return render_template("ticket.html", ticket=t, service=service, ahead=len(ahead), position=position)

@app.post("/queue/<int:ticket_id>/leave")
def leave_queue(ticket_id):
    t = next((t for t in TICKETS if t["number"] == ticket_id), None)
    if t:
        t["status"] = "no-show"
        flash("You have left the queue.", "info")
    return redirect(url_for("index"))


@app.route("/hello")
def hello():
    # The plain-string version from the Routes slide.
    return "Hello, CCC181!"

@app.get("/join")
def join_form():
    return render_template("join.html", services=SERVICES, form={})


@app.post("/join")
def join():
    form = request.form
    name = form.get("name", "").strip()
    student_id = form.get("student_id", "").strip() 
    email = form.get("email", "").strip().lower()
    service_id = form.get("service_id", type=int)

    errors = {}
    if not name:
        errors["name"] = "Enter your name."
    if "@" not in email:
        errors["email"] = "Enter a valid email address."
    if not student_id:
        errors["student_id"] = "Enter your Student ID."
    if service_id not in [s["id"] for s in SERVICES]:
        errors["service_id"] = "Choose a service."
    
    if errors:
        flash("Please fix the highlighted fields.", "danger")
        return render_template("join.html", services=SERVICES, form=form, errors=errors), 400

    number = TICKETS[-1]["number"] + 1 if TICKETS else 1
    TICKETS.append({"number": number, "name": name, "email": email,
                    "service_id": service_id, "status": "waiting"})
    flash(f"You joined the queue. Your ticket is #{number}.", "success")
    return redirect(url_for("ticket", ticket_id=number))                

@app.get("/staff")
def staff_dashboard():
    service_id = request.args.get("service_id", type=int)
    queue = [t for t in TICKETS if t["status"] in ("waiting", "called")]
    if service_id:
        queue = [t for t in queue if t["service_id"] == service_id]
    names = {s["id"]: s["name"] for s in SERVICES}

    counts = {
        s["id"]: len([t for t in TICKETS if t["service_id"] == s["id"] and t["status"] == "waiting"])
        for s in SERVICES
    }
    total_waiting = sum(counts.values())
    return render_template("staff.html", queue=queue, services=SERVICES,
                           names=names, selected=service_id, counts=counts, total_waiting=total_waiting)


@app.post("/staff/tickets/<int:ticket_id>/<action>")
def staff_action(ticket_id, action):
    new_status = {"call": "called", "serve": "served", "no-show": "no-show"}.get(action)
    t = next((t for t in TICKETS if t["number"] == ticket_id), None)
    if t is None or new_status is None:
        abort(404)
    t["status"] = new_status
    flash(f"Ticket #{ticket_id} marked {new_status}.", "info")
    return redirect(url_for("staff_dashboard"))

if __name__ == "__main__":
    # Lets you also start the app with: python app.py
    app.run(debug=True)