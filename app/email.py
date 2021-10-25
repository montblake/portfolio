from flask_mail import Message
from app import app, mail


def send_resume(recipient_name, recipient_addr):
    recipient = recipient_name + '<' + recipient_addr + '>'
    msg = Message('You requested a resume?', recipients=[recipient])
    msg.body = ('Here is your resume. Thanks!'
                'Blake Montgomery.'
                'software engineer | full-stack web development'
                '__________________________________________________'
                'proficiences'
                'ReactJS, vanilla JavaScript, HTML5, CSS/SCSS'
                'Python, Flask, SQLAlchemy, SQLite, PodstgreSQL'
                'NodeJS, Express, Mongoose, MongoDB'
                'Ruby on Rails, Git'
                )
                
    msg.html = ('<p>Here is your resume. Thanks!</p> <h1>Blake Montgomery</h1> <h2>software engineer | full-stack web development</h2> <hr /> <h3>proficiences</h3> <ul> <li>ReactJS, vanilla JavaScript, HTML5, CSS/SCSS</li> <li>Python, Flask, SQLAlchemy, SQLite, PostgreSQL</li> <li>NodeJS, Express, Mongoose, MongoDB</li> <li>Ruby on Rails, Git</li>')
    
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



