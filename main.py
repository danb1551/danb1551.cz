from dotenv import load_dotenv
import os
from src.app import create_app

load_dotenv(".env")

DEBUG = os.getenv("DEBUG") == "True"

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port= 80 if not DEBUG else 8080, debug=DEBUG)