from logging import Logger
from app import app
from flask import render_template, request, flash, session
from app.forms import ContactForm, RequestResumeForm
from app.email import send_resume, send_contact_form, forward_email
import requests
from threading import Thread


@app.route('/')
@app.route('/index')
def index():
    app.logger.info(f'{request.remote_addr} has arrived')
    url1 = 'https://six-degrees-flask-react.herokuapp.com/'
    url2 = 'https://six-degrees-flask.herokuapp.com/'
    url3 = 'https://fleeting-communes.herokuapp.com/'
    url4 = 'https://spare-socket-server.herokuapp.com/'
    url5 = 'https://spare-peer-server.herokuapp.com/'
    url6 = 'https://intergalactic-transport.herokuapp.com/'
    url7 = 'https://salty-inlet-99632.herokuapp.com/' 
    Thread(target=make_async_request, args=(app, url1)).start()
    Thread(target=make_async_request, args=(app, url2)).start()
    Thread(target=make_async_request, args=(app, url3)).start()
    Thread(target=make_async_request, args=(app, url4)).start()
    Thread(target=make_async_request, args=(app, url5)).start()
    Thread(target=make_async_request, args=(app, url6)).start()
    Thread(target=make_async_request, args=(app, url7)).start()
    return render_template('index.html', title='Blake Montgomery', h2='Developer Portfolio', alignment='alignSpaceBetween')


# /////////////////////////////// CONTACT AND RESUME-REQUEST //////////////////
# @app.route('/contact', methods=['GET', 'POST'])
# def contact():
#     form = ContactForm()
    
#     if request.method == 'POST':
#         if form.validate() == False:
#             flash('All fields are required.')
#             return render_template('contact.html', form=form, title='contact')
#         else:
#             send_contact_form(form)
#             return render_template('contact.html', success=True, title='contact')
           
#     elif request.method == 'GET':
#         return render_template('contact.html', form=form, title='contact')

#     return render_template('contact.html', form=form, title='contact')


# @app.route('/resume', methods=['GET', 'POST'])
# def resume():
#     form = RequestResumeForm()
#     if form.validate_on_submit():
#         recipient_name = form.name.data  
#         recipient_addr = form.email.data
#         send_resume(recipient_name, recipient_addr)
#         return render_template('request-resume.html', success=True, recipient=recipient_name, title='request sent')
           
#     else:
#         return render_template('request-resume.html', form=form, title='request resume')



#/////////////////////// PROJECT VIEW FUNCTIONS //////////////////////////
# async requests
def make_async_request(app, url):
    with app.app_context():
        r = requests.get(url)
        print('contact url', url, r)


# portfolio directory
# @app.route('/projects')
# def projects():
#     return render_template('projects.html', title='projects')


#  individual project pages


# @app.route('/projects/chartreuse')
# def project_chartreuse():
#     url1 = 'https://infinite-cove-47012.herokuapp.com' 
#     Thread(target=make_async_request, args=(app, url1)).start()
#     return render_template('projects/chartreuse.html', title='CHARTREUSE')


# @app.route('/projects/django-and-flask')
# def project_django_and_flask():
#     url1 = 'https://flask-detective-react-frontend.herokuapp.com'
#     url2 = 'https://server-only-dj-and-flask.herokuapp.com'
#     Thread(target=make_async_request, args=(app, url1)).start()
#     Thread(target=make_async_request, args=(app, url2)).start()
#     return render_template('projects/django-and-flask.html', title='DJANGO AND FLASK')


# /////////////////////// PROJECTS CURRENTLY OFFLINE ///////////////////////
# @app.route('/projects/marketplace')
# def project_marketplace():
#     return render_template('projects/marketplace.html', title='MARKETPLACE')

# @app.route('/projects/code-green')
# def project_code_green():
#     return render_template('projects/code-green.html', title='CODE GREEN')
    
    
# ////////////////// FUTURE ROUTES ///////////////////////////////////// 
# @app.route('/blog')
# def blog():
#     return render_template('blog.html', title='blog')


# ////////////////////// RECEIVE EMAIL ///////////////////////////////////
# @app.route('/email', methods=['POST'])
# def receive_email():
#     msg_to = request.form['to']
#     msg_from = request.form['from']
#     msg_subj = request.form['subject']
#     msg_text = request.form['text']

#     print('to: ', msg_to)
#     print('from: ', msg_from)
#     print('subject: ', msg_subj)
#     print('message: ', msg_text)
    
#     forward_email(msg_to, msg_from, msg_subj, msg_text)
#     return "Email Forwarded"



# /////////////////// DASHBOARD ///////////////////
# @app.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html', title="dashboard")