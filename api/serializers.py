# from django.contrib.auth.models import User
from api.models import Question,User,Answer,Comment
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'first_name', 'last_name', 'email','password','about','image')
	def create(self, validated_data):
		return User.objects.create(**validated_data)

class QuestionSerializer(serializers.ModelSerializer):
	# user = serializers.PrimaryKeyRelatedField(many=True,queryset=User.objects.all())
 	class Meta:
 		model=Question
 		fields = ('id','title','about','date_create','user_id')
 		depth=1

class QuestionListSerializer(serializers.ModelSerializer):
	# user = serializers.PrimaryKeyRelatedField(many=True,queryset=User.objects.all())
 	class Meta:
 		model=Question
 		fields = ('id','title','about','date_create','user_id')
 		# depth=1

class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model= Comment
		fields = ('id','user_id','ans_id','comment_text','date_comm')
		depth=1
	# def create(self, validated_data):
	# 	return Comment(**validated_data)
class CommentListSerializer(serializers.ModelSerializer):
	class Meta:
		model= Comment
		fields = ('id','user_id','ans_id','comment_text','date_comm')
		# depth=1

class AnswerListSerializer(serializers.ModelSerializer):
	# qid=QuestionSerializer(many=True,read_only=True)
	comment = CommentSerializer(many=True,read_only=True)
	class Meta:
		model= Answer
		fields = ('id','ans_text','date','q_id','user_id','comment')
		depth=2
class AnswerSerializer(serializers.ModelSerializer):
	# qid=QuestionSerializer(many=True,read_only=True)
	# userid = UserSerializer(many=True,read_only=True)
	class Meta:
		model= Answer
		fields = ('id','ans_text','date','q_id','user_id',)
