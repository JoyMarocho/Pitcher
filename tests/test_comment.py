import unittest
from app.models import Comment,User
from app import db


class CommentModelTest(unittest.TestCase):

        def setUp(self):
                self.user_Joy = User(username = 'bigbaby', password = 'New Password', email = 'joy@gmail.com')
        self.new_comment = Comment(pitch_id=123,pitch_title='Coding to save lives',pitch_review='Awesome pitch',posted='2021, 08, 25',user = self.user_Joy)

def tearDown(self):
        Comment.query.delete()
        User.query.delete()

def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.pitch_id,123)
        self.assertEquals(self.new_comment.pitch_title,'Coding to save lives')
        self.assertEquals(self.new_comment.pitch_review,'Awesome pitch')
        self.assertEquals(self.new_comment.posted,'2022, 05, 10')
        self.assertEquals(self.new_comment.user,self.user_Joy)

def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

def test_get_comment_by_id(self):

        self.new_comment.save_comment()
        got_comments = Comment.get_comments(123)
        self.assertTrue(len(got_comments) == 1)