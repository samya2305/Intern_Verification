from flask import Blueprint

dashboard_bp = Blueprint("dashboard",__name__)

@dashboard_bp.route("/dashboard")
def dashboard():

    return{

        "Total":0,
        "Verified":0,
        "Pending":0,
        "Rejected":0

    }