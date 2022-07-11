from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)


@errors.app_context_processor(404)
def error_404(error):
    return render_template('errors/404.html'), 404


@errors.app_context_processor(403)
def error_403(error):
    return render_template('errors/403.html'), 403


@errors.app_context_processor(500)
def error_500(error):
    return render_template('errors/500.html'), 500