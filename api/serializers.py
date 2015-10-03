# from django.contrib.auth.models import User
from api.models import Question,User,Answer
from rest_framework import serializers

class QuestionSerializer(serializers.ModelSerializer):
	#user = UserSerializer(many=True)
	#question = serializers.HyperlinkedRelatedField(many=True, view_name='question-detail', read_only=True)
 	class Meta:
 		model=Question
 		fields = ('id','title','about','date_create','user_id')

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'first_name', 'last_name', 'email','password')

class AnswerSerializer(serializers.ModelSerializer):
	#que = serializers.PrimaryKeyRelatedField(many=True,queryset=Question.object.all(), read_only=True)
	class Meta:
		model= Answer
		fields = ('id','ans_text','date','q_id','user_id')