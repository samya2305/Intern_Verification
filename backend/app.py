from flask import Flask
from flask_cors import CORS

from routes.email_routes import email_bp
from routes.verify_routes import verify_bp
from routes.dashboard_routes import dashboard_bp
from routes.excel_routes import excel_bp

app = Flask(__name__)

CORS(app)

app.register_blueprint(email_bp)
app.register_blueprint(verify_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(excel_bp)

@app.route("/")
def home():
    return {
        "Project":"Intern Verification System",
        "Status":"Running"
    }

if __name__ == "__main__":
    app.run(debug=True)