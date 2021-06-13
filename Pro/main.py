# importing Flask and other modules
from flask import Flask, request, render_template

# Flask constructor
app = Flask(__name__)


# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods=["GET", "POST"])
def getData():
    if request.method == "POST":
        # getting ticket no and email in HTML form
        t_no = request.form.get("ticket_no")
        email = request.form.get("email_id")
        return "Ticket no: " + t_no + " Email id is: " + email
    return render_template("ManageBooking.html")


if __name__ == '__main__':
    app.run()