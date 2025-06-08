from flask import (
    Blueprint, redirect, render_template, request, url_for, abort
)


bp = Blueprint('taskman', __name__, url_prefix='/taskman')

@bp.route('/')
def index():
    data: dict = dict(
        name="John Doe",
        ip_address=f'1.1.1.1',
    )
    return render_template('hello.html', data=data)


@bp.route('/about', methods=('GET',))
def about():
    return "<p>About TASKMAN</p>"