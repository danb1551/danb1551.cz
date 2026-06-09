from flask import Flask, render_template, send_file, url_for

def create_app() -> Flask:
    app = Flask(__name__)

    @app.errorhandler(404)
    def NotFound():
        return render_template("errors/404.html"), 404

    @app.route('/', methods=["GET"])
    def home():
        return render_template("index.html"), 200

    @app.route('/projects', methods=["GET"])
    def projects():
        return render_template("projects.html"), 200

    @app.route('/cv', methods=["GET"])
    def cv():
        return render_template("cv.html"), 200
    
    @app.route("/image/<nameOfTheImage>")
    def imageDown(nameOfTheImage):
        return send_file("templates/index.html", as_attachment=False, download_name="h.htm")

    return app