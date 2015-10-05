from django.contrib.auth.models import User
import django_filters
from django.http import Http404
from api.models import Question,User,Answer,Like
from api.serializers import UserSerializer,QuestionSerializer,AnswerSerializer,LikeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.permissions import IsOwnerOrReadOnly
from rest_framework import filters
from rest_framework import generics


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id',)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id',)

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('user_id',)

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('user_id',)

class AnswerList(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('q_id','user_id')

class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('q_id','user_id')

class LikeList(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('ans_id','user_id')

class LikeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('ans_id','user_id')

# class UserList(APIView):
#     def get(self, request, format=None):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         filter_backends = (filters.DjangoFilterBackend,)
#         filter_fields = ('id','email')
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         user = self.get_object(pk)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class UserDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         user = self.get_object(pk)
#         user = UserSerializer(user)
#         return Response(user.data)

#     def put(self, request, pk, format=None):
#         user = self.get_object(pk)
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         user = self.get_object(pk)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class QuestionList(APIView):
#     def get(self, request, format=None):
#         question = Question.objects.all()
#         serializer = QuestionSerializer(question, many=True)
#         filter_backends = [DjangoFilterBackend]
#         filter_fields = ['title']
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = QuestionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         question = self.get_object(pk)
#         question.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
# class QuestionDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Question.objects.get(pk=pk)
#         except Question.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         question = self.get_object(pk)
#         question = QuestionSerializer(question)
#         filter_backends = [DjangoFilterBackend]
#         filter_fields = ['title']
#         return Response(question.data)

#     def put(self, request, pk, format=None):
#         question = self.get_object(pk)
#         serializer = QuestionSerializer(question, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         question = self.get_object(pk)
#         question.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class AnswerList(APIView):
#     def get(self, request, format=None):
#         answer = Answer.objects.all()
#         serializer = AnswerSerializer(answer, many=True)
#         filter_backends = (filters.DjangoFilterBackend,)
#         filter_fields = ('q_id')
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = AnswerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         answer = self.get_object(pk)
#         answer.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class AnswerDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Answer.objects.get(pk=pk)
#         except Answer.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         answer = self.get_object(pk)
#         answer = AnswerSerializer(answer)
#         filter_backends = (filters.DjangoFilterBackend,)
#         filter_fields = ['q_id','user_id']
#         return Response(answer.data)

#     def put(self, request, pk, format=None):
#         answer = self.get_object(pk)
#         serializer = AnswerSerializer(answer, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         answer = self.get_object(pk)
#         answer.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)