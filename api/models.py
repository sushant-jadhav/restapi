from django.db import models
class User(models.Model):
	# username=models.CharField(max_length=1000,null=True)
	first_name=models.CharField(max_length=1000,null=True)
	last_name=models.CharField(max_length=1000,null=True)
	email=models.CharField(max_length=1000,null=True)
	about=models.CharField(max_length=2000,null=True)
	password = models.CharField(max_length=1000,null=True)

class Question(models.Model):
 	title = models.CharField(max_length='1000',null=True)
 	about = models.CharField(max_length='1000',null=True)
 	date_create = models.DateTimeField(null=True)
 	user_id = models.ForeignKey(User,related_name='user',null=True)

class Answer(models.Model):
 	ans_text = models.CharField(max_length='10000',null=True)
 	date = models.DateTimeField(null=True)
 	q_id = models.ForeignKey(Question,related_name='questionid',null=True)
 	user_id = models.ForeignKey(User,related_name='questionUser',null=True)
 	def __unicode__(self):
 		return '%s %s' % (self.date,self.ans_text)

class Comment(models.Model):
	user_id = models.ForeignKey(User,related_name='Answeruser',null=True)
	ans_id = models.ForeignKey(Answer,related_name='answer',null=True)
	comment_text = models.CharField(max_length='6000',null=True)