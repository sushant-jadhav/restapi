# from django.contrib.auth.models import User
from api.models import Question,User,Answer,Like
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'first_name', 'last_name', 'email','password','about')
		depth=1

class QuestionSerializer(serializers.ModelSerializer):
	#question = serializers.HyperlinkedRelatedField(many=True, view_name='question-detail', read_only=True)
 	class Meta:
 		model=Question
 		fields = ('id','title','about','date_create','user_id')
 		depth=2
 		def get_related_field(self, model_field):
 			return QuestionSerializer()

class AnswerSerializer(serializers.ModelSerializer):
	#question = serializers.HyperlinkedIdentityField( view_name='user-details')
	class Meta:
		model= Answer
		fields = ('id','ans_text','date','q_id','user_id')
		depth=3
		def get_related_field(self, model_field):
 			return AnswerSerializer()

class LikeSerializer(serializers.ModelSerializer):
	class Meta:
		model= Like
		fields = ('id','user_id','ans_id','is_like')
		depth=3