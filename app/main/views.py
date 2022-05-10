om app.main.forms import CommentForm, UpdateProfile
from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required,current_user
from .. import db,photos
from ..models import User,Comment



@main.route('/pitch/comment/new/<int:id>', methods=['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    pitch = Comment.pitch_id
    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data

        #updated comment instance
        new_comment = Comment(pitch_id=pitch.id,pitch_title =title,pitch_review = comment,user=current_user)

        #save review method
        new_comment.save_comment()
        return redirect(url_for('.pitch',id = pitch.id))

    title = f'{pitch.title} comment'
    return render_template('new_comment.html',title=title,comment_form=form,pitch=pitch)