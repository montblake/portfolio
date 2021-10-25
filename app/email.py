from flask_mail import Message
from app import app, mail


def send_resume(recipient):
    msg = Message('You requested a resume?', recipients=[recipient])
    msg.body = ('Here is your resume. Thanks!')
    msg.html = ('<h1>Here is your resume.</h1> <p>Thanks!</p>')
    
    with app.open_resource("static/resources/blake_montgomery_resume_092421.pdf") as bm_resume:
        msg.attach("static/resources/blake_montgomery_resume_092421.pdf", "text/pdf", bm_resume.read())
    
    mail.send(msg)


def send_message(form):
    subject = form.subject.data
    sender = app.config['MAIL_DEFAULT_SENDER']
    msg = Message(subject, sender=sender, recipients=[sender])
    msg.body = """
        From: %s <%s>
        %s
        """ %(form.name.data, form.email.data, form.message.data)
    mail.send(msg)



