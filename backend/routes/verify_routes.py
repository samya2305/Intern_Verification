from flask import Blueprint

verify_bp = Blueprint("verify",__name__)

@verify_bp.route("/verify")
def verify():

    return{
        "message":"Verification Module Working"
    }
    