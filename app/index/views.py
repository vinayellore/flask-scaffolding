import logging
from flask import (
    Blueprint, render_template, request
)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
index_blueprint = Blueprint(
    'index', __name__,
    template_folder='templates',
    # static_folder='static',
    # static_url_path='/static'
)


@index_blueprint.route('/')
def index():
    print("here")
    logger.info("Checking the flask scaffolding logger")
    logger.critical("its critical")
    logger.warning("its a warning")
    logger.error("its a error")
    return render_template("index.html")
