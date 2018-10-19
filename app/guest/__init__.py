from flask import Blueprint


guest = Blueprint('guest', __name__, template_folder='templates', static_folder='static', static_url_path='/guest/static')

# Import the views after site has been defined. The views
# module will need to import 'site' so we need to make
# sure that we import views after site has been defined.
from . import views