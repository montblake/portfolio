from logging import Logger
from app import app
from flask import render_template, request, flash
from app.forms import ContactForm, RequestResumeForm
from app.email import send_resume, send_contact_form, forward_email


@app.route('/')
@app.route('/index')
def index():
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
    return render_template('projects/sixdegrees.html', title='6DKB')

@app.route('/projects/chartreuse')
def project_chartreuse():
    return render_template('projects/chartreuse.html', title='CHARTREUSE')

@app.route('/projects/forking-cocktails')
def project_cocktails():
    return render_template('projects/forking-cocktails.html', title='COCKTAILS')

@app.route('/projects/django-and-flask')
def project_django_and_flask():
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
    # forward_email()
    print('FORWARDED!!!!!!For Real.')
    print("message: ", request.form)
    return ""