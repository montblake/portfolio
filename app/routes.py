from app import app, mail
from flask import render_template, request, flash
from app.forms import ContactForm, RequestResumeForm
from flask_mail import Message

SENDER = app.config['MESSAGE_SENDER']


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='home')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form, title='contact')
        else:
            msg = Message(form.subject.data, sender=SENDER, recipients=[SENDER])
            msg.body = """
            From: %s <%s>
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)

            return render_template('contact.html', success=True, title='contact')
           
    elif request.method == 'GET':
        return render_template('contact.html', form=form, title='contact')

    return render_template('contact.html', form=form, title='contact')

@app.route('/resume', methods=['GET', 'POST'])
def resume():
    form = RequestResumeForm()

    if form.validate_on_submit():
        print('Yes, valid!')
        msg = Message("Resume Requested!!!", sender=SENDER, recipients=[form.email.data])
        msg.body = """
        Here is the resume you requested %s 
        """ % (form.email.data)

        with app.open_resource("static/resources/blake_montgomery_resume_092421.pdf") as bm_resume:
            msg.attach("static/resources/blake_montgomery_resume_092421.pdf", "text/pdf", bm_resume.read())

        mail.send(msg)
        return render_template('request-resume.html', success=True, requesting_address=form.email.data, title='request sent')
           
    else:
        print('NOPE!!!')
        return render_template('request-resume.html', form=form, title='request resume')


@app.route('/blog')
def blog():
    return render_template('blog.html', title='blog')

@app.route('/projects')
def projects():
    return render_template('projects.html', title='projects')

@app.route('/projects/6dkb')
def project_six_degrees():
    return render_template('projects/sixdegrees.html', title='6DKB')


@app.route('/projects/chartreuse')
def project_chartreuse():
    return render_template('projects/chartreuse.html', title='CHARTREUSE')

@app.route('/projects/code-green')
def project_code_green():
    return render_template('projects/code-green.html', title='CODE GREEN')

@app.route('/projects/forking-cocktails')
def project_cocktails():
    return render_template('projects/forking-cocktails.html', title='COCKTAILS')

@app.route('/projects/django-and-flask')
def project_django_and_flask():
    return render_template('projects/django-and-flask.html', title='DJANGO AND FLASK')

@app.route('/projects/marketplace')
def project_marketplace():
    return render_template('projects/marketplace.html', title='MARKETPLACE')