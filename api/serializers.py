# from django.contrib.auth.models import User
from api.models import Question,User,Answer,Comment
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'first_name', 'last_name', 'email','password','about')
	def create(self, validated_data):
		return User(**validated_data)


class QuestionSerializer(serializers.ModelSerializer):
	# user_id = serializers.PrimaryKeyRelatedField(read_only=True,many=True)
 	class Meta:
 		model=Question
 		fields = ('id','title','about','date_create','user_id')
 		# depth=1
 	def create(self, validated_data):
 		return Question(**validated_data)


class AnswerSerializer(serializers.ModelSerializer):
	qid=QuestionSerializer(many=True,read_only=True)
	userid = UserSerializer(many=True,read_only=True)
	class Meta:
		model= Answer
		fields = ('id','ans_text','date','q_id','user_id','qid','userid')
		depth=2
	def create(self, validated_data):
		que = validated_data.pop('q_id')
		question = Question.objects.create(**validated_data)
		Question.objects.create(question=question,**que)
		return question
    # def create(self, validated_data):
    #     tracks_data = validated_data.pop('tracks')
    #     album = Album.objects.create(**validated_data)
    #     for track_data in tracks_data:
    #         Track.objects.create(album=album, **track_data)
    #     return album
	# def update(self, instance, validated_data):
	# 	instance.ans_text=validated_data['ans_text']
	# 	instance.date=validated_data['date']
	# 	instance.q_id=validated_data['q_id']
	# 	instance.user_id=validated_data['user_id']
	# 	instance.save()
	# 	return instance

class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model= Comment
		fields = ('id','user_id','ans_id','comment_text')
		# depth=2
	# def create(self, validated_data):
	# 	return Comment(**validated_data)
