from logging import Logger
from app import app
from flask import render_template, request, flash, session
from app.forms import ContactForm, RequestResumeForm
from app.email import send_resume, send_contact_form, forward_email
import requests


@app.route('/')
@app.route('/index')
def index():
    app.logger.info('%s has arrived', request.remote_addr)
    return render_template('index.html', title='home')


# /////////////////////////////// CONTACT AND RESUME-REQUEST /////////////////////////////
# both routes need email to handle request
# AT SOME POINT, separate email function to a separate file


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form, title='contact')
        else:
            send_contact_form(form)
            return render_template('contact.html', success=True, title='contact')
           
    elif request.method == 'GET':
        return render_template('contact.html', form=form, title='contact')

    return render_template('contact.html', form=form, title='contact')


@app.route('/resume', methods=['GET', 'POST'])
def resume():
    form = RequestResumeForm()
    if form.validate_on_submit():
        print('Yes, valid!')
        recipient_name = form.name.data  
        recipient_addr = form.email.data
        send_resume(recipient_name, recipient_addr)
        return render_template('request-resume.html', success=True, recipient=recipient_name, title='request sent')
           
    else:
        print('NOPE!!!')
        return render_template('request-resume.html', form=form, title='request resume')



#/////////////////////// PROJECT VIEW FUNCTIONS //////////////////////////
# portfolio directory
@app.route('/projects')
def projects():
    return render_template('projects.html', title='projects')


#  individual project pages
@app.route('/projects/6dkb')
def project_six_degrees():

    # r1 = requests.get('https://six-degrees-flask-react.herokuapp.com')
    # r2 = requests.get('https://six-degrees-flask.herokuapp.com')
    # print('R1:', r1)
    # print('R2:', r2)
    return render_template('projects/sixdegrees.html', title='6DKB')

@app.route('/projects/chartreuse')
def project_chartreuse():
    # r1 = requests.get('https://infinite-cove-47012.herokuapp.com')
    # print('R1:', r1)
    return render_template('projects/chartreuse.html', title='CHARTREUSE')

@app.route('/projects/forking-cocktails')
def project_cocktails():
    # r1 = requests.get('https://salty-inlet-99632.herokuapp.com')
    # print('R1:', r1)
    return render_template('projects/forking-cocktails.html', title='COCKTAILS')

@app.route('/projects/django-and-flask')
def project_django_and_flask():
    # r1 = requests.get('https://flask-detective-react-frontend.herokuapp.com')
    # r2 = requests.get('https://server-only-dj-and-flask.herokuapp.com/')
    # print('R1:', r1)
    # print('R2:', r2)
    return render_template('projects/django-and-flask.html', title='DJANGO AND FLASK')


# /////////////////////// PROJECTS CURRENTLY OFFLINE ///////////////////////
@app.route('/projects/marketplace')
def project_marketplace():
    return render_template('projects/marketplace.html', title='MARKETPLACE')

@app.route('/projects/code-green')
def project_code_green():
    return render_template('projects/code-green.html', title='CODE GREEN')
    
    
# ////////////////// FUTURE ROUTES ///////////////////////////////////// 
@app.route('/blog')
def blog():
    return render_template('blog.html', title='blog')


# ////////////////////// RECEIVE EMAIL ///////////////////////////////////
@app.route('/email', methods=['POST'])
def receive_email():
   
    print('FORWARDED!!!!!!For Real.')
    msg_to = request.form['to']
    msg_from = request.form['from']
    msg_subj = request.form['subject']
    msg_text = request.form['text']

    print('to: ', msg_to)
    print('from: ', msg_from)
    print('subject: ', msg_subj)
    print('message: ', msg_text)
    
    forward_email(msg_to, msg_from, msg_subj, msg_text)
    return ""



# /////////////////// DASHBOARD ///////////////////
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', title="dashboard")