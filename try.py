from main import app
from waitress import serve

try:
    serve(app)
except RuntimeError:
    pass    