from flask import Blueprint

excel_bp = Blueprint("excel",__name__)

@excel_bp.route("/excel")
def excel():

    return{
        "message":"Excel Module Working"
    }