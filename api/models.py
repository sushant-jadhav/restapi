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
 	ans_text = models.CharField(max_length='1000',null=True)
 	date = models.DateTimeField(null=True)
 	# u_id = models.ForeignKey(User,related_name='User',null=True)
 	q_id = models.ForeignKey(Question,related_name='Question',null=True)
 	user_id = models.ForeignKey(User,related_name='QuestionUser',null=True)

class Like(models.Model):
	user_id = models.ForeignKey(User,related_name='Answeruser',null=True)
	ans_id = models.ForeignKey(Answer,related_name='answer',null=True)
	is_like = models.SmallIntegerField()