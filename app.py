from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
from flask_script import Manager, Command, Shell
from flask_wtf import FlaskForm
from flask import Flask, render_template, redirect, url_for, flash


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'SECRET_KEY'

manager = Manager(app)

class ContactForm(FlaskForm):
# 	class Meta:
# 		csrf = False

	name = StringField("Name: ", validators=[DataRequired()])
	email = StringField("Email: ", validators=[Email()])
	message = TextAreaField("Message", validators=[DataRequired()])
	submit = SubmitField("Submit") 
	# SHELL # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
	# form = ContactForm(name='wan', email='test@test.test', message='mess', meta={'csrf': False})
	# or 
	# form = ContactForm(MultiDict([('name', 'spike'),('email', 'spike@mail.com')]), csrf_enabled=False)
	# form.validate()
	# form.errors
	# form = ContactForm()
	# Template("{{ form.name.label() }}").render(form=form)
	# <input id="name" name="name" required type="text" value="">
	# Template("{{ form.submit() }}").render(form=form)
	# Template("{% for error in form.name.errors %}{{ error }}{% endfor %}").render(form=form)
	# Template("{% for error in form.errors %}{{ error }}{% endfor %}").render(form=form)
	# Template('{{ form.name(class="input", id="simple-input") }}').render(form=form)
	# Template("{{ form.csrf_token() }}").render(form=form)
	# Template('{{ form.name.label(class="lbl") }}').render(form=form)
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def shell_context():
	from werkzeug.datastructures import MultiDict
	from jinja2 import Template
	from app import ContactForm

	return dict(ContactForm=ContactForm, MultiDict=MultiDict, app=app, Template=Template)

manager.add_command("shell", Shell(make_context=shell_context))	


@app.route('/form/', methods=['get', 'post'])
def form():
	form = ContactForm()
	if form.validate_on_submit():
		# form.data access to all data
		name = form.name.data
		email = form.email.data
		message = form.message.data
		print(name)
		print(email)
		print(message)
		print("\nData received. Now redirecting ...")
		flash("Message Received")
		flash("success")

		return redirect(url_for('form'))

	return render_template('form.html', form=form)



@app.route('/')
def index():
	return "Hello World"

if __name__=='__main__':
	manager.run()