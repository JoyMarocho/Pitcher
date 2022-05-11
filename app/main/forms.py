from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired

class CommentForm(FlaskForm):
    
    title = StringField('Review title',validators=[DataRequired()])
    review = TextAreaField('Pitch review', validators=[DataRequired()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
class PitchForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    category = SelectField('Category', choices=[('Events','Interviews Pitches'),('Job','Pickup lines'),('Advertisement','Promotion Pitches')],validators=[DataRequired()])
    post = TextAreaField('Your Pitch', validators=[DataRequired()])
    submit = SubmitField('Pitch')
    
    