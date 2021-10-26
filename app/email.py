from flask_mail import Message
from app import app, mail


def send_resume(recipient_name, recipient_addr):
    recipient = recipient_name + '<' + recipient_addr + '>'
    msg = Message('You requested a resume?', recipients=[recipient])
    msg.body = ('Here is the resume for Blake Montgomery, software engineer. Thanks for taking a look! Please, let me know if you need anything else.')
    
    with app.open_resource("static/resources/blake_montgomery_resume_102621.pdf") as bm_resume:
        msg.attach("static/resources/blake_montgomery_resume_102621.pdf", "text/pdf", bm_resume.read())

    mail.send(msg)

    msg2 = Message("Hey Blake: someone requested your resume:", recipients=['blakemontgomery312@gmail.com'])
    msg2.body = """
        %s <%s>
        """ %(recipient_name, recipient_addr)
    mail.send(msg2)


def send_contact_form(form):
    subject = form.subject.data
    sender = app.config['MAIL_DEFAULT_SENDER']
    msg = Message(subject, sender=sender, recipients=['blakemontgomery312@gmail.com'])
    msg.body = """
        From: %s <%s>
        %s
        """ %(form.name.data, form.email.data, form.message.data)
    mail.send(msg)


def forward_email(msg_to, msg_from, msg_subj, msg_text):
    subject = "Forwarded Message from blakemontgomery.com"
    sender = app.config['MAIL_DEFAULT_SENDER']
    msg = Message(subject, sender=sender, recipients=['blakemontgomery312@gmail.com'])
    msg.body = """
    To: %s
    From: %s
    Subject: %s
    %s
    """ %(msg_to, msg_from, msg_subj, msg_text)
    mail.send(msg)