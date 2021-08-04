from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

import requests

from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

from flaskr.zendesk import *

bp = Blueprint('count', __name__)


@bp.route('/count', methods = ('GET', 'POST'))
def index():
    if request.method == 'POST':
        print(request.form['datas'])
        return(render_template('count/count.html', ticket_count = count_ticket()))
    else:
        return render_template('count/count.html')

def count_ticket():
    response = requests.get('https://z3n-hack-in-place.zendesk.com/api/v2/tickets/count.json', auth=("eling@zendesk.com","REPLACE"))

    response_data = response.json()

    if response.status_code == 200:
        count = response_data['count']['value']
        return count
    else:
        return "ticket count API call failed :/"
