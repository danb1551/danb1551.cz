from flask import Flask, render_template, send_file, url_for, request, jsonify, session
import redis
import os

def create_app() -> Flask:
    USE_REDIS = True
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY")

    if USE_REDIS:
        redis_cache = redis.Redis(
            host="redis",
            decode_responses=True
        )
        redis_cache.incr("visits")

    @app.errorhandler(404) # type: ignore
    def NotFound():
        return render_template("errors/404.html"), 404

    @app.route("/favicon.ico")
    def favicon():
        return url_for('static', filename="img/favicon.ico")

    @app.route("/", methods=["GET"])
    def home():
        if USE_REDIS:
            redis_cache.incr("visits")
        return render_template("index.html"), 200

    @app.route("/services", methods=["GET"])
    def services():
        return render_template("services.html"), 200

    @app.route("/projects", methods=["GET"])
    def projects():
        return render_template("projects.html"), 200

    @app.route("/portfolio")
    def portfolio():
        return render_template("portfolio.html")

    @app.route("/cv", methods=["GET"])
    def cv():
        return render_template("cv.html"), 200

    @app.route("/health")
    def health_check():
        """Verify Redis connection is working"""
        if redis_cache.exists("gg") == 0:
            return jsonify({'status': 'healthy', 'redis': 'connected'}), 200
        else:
            return jsonify({'status': 'unhealthy', 'redis': 'disconnected'}), 503

    @app.route("/lookup")
    def lookup():
        return jsonify({'lookup': redis_cache.get("visits")}), 200

    @app.route("/login") # type: ignore
    def login():
        if request.method == "GET":
            return render_template("login.html")
        # yeah, I know. Don't deserve heaven
        elif request.method == "POST" and request.form.get("username") == os.getenv("ADMIN_USERNAME") and request.form.get("password") == os.getenv("ADMIN_PASSWORD"):
            session["username"] = "ADMIN"
            return "success - loged in", 200

    @app.route("/admin")
    def admin():
        return render_template("admin/index.html")
        

    return app