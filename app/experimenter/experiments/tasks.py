from celery.utils.log import get_task_logger

from experimenter.celery import app
from experimenter.experiments import email, bugzilla


logger = get_task_logger(__name__)

@app.task
def send_review_email_task(experiment_name, experiment_url, needs_attention):
		logger.info('Sending email')
		email.send_review_email(experiment_name, experiment_url, needs_attention)
		logger.info('Email sent')


@app.task
def create_experiment_bug_task(experiment_id):
    logger.info('Creating Bugzilla ticket')
    bugzilla.create_experiment_bug(experiment_id)
    logger.info('Bugzilla ticket created')
