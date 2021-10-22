from flask_mail import Message
from app import mail, app


SENDER = app.config['ADMINS'][0]


def send_resume(to_address):
    msg = Message("Resume Requested!!!", sender=SENDER, recipients=[to_address])
    msg.body = """
        Here is the resume you requested %s 
        """ %(to_address)
    
    with app.open_resource("static/resources/blake_montgomery_resume_092421.pdf") as bm_resume:
        msg.attach("static/resources/blake_montgomery_resume_092421.pdf", "text/pdf", bm_resume.read())
    
    mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body):
    pass



