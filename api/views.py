from django.contrib.auth.models import User
import django_filters
from django.http import Http404
from api.models import Question,User,Answer,Comment
from api.serializers import UserSerializer,QuestionSerializer,AnswerSerializer,CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import status
# from api.permissions import IsOwnerOrReadOnly
from rest_framework import filters
from rest_framework import generics


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id',)

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id',)


class AnswerList(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('q_id','user_id')
    paginate_by = 10
    def get_paginate_by(self):
        """
        Use smaller pagination for HTML representations.
        """
        if self.request.accepted_renderer.format == 'html':
            return 20
        return 10
    def perform_create(self, serializer):
        serializer.save(user=self.request.queryset)
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = AnswerSerializer(queryset, many=True)
        return Response(serializer.data)

class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('q_id','user_id')

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

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

# class CommentList(APIView):
#     def get(self, request, format=None):
#         comment = Comment.objects.all()
#         serializer = CommentSerializer(comment, many=True)
#         filter_backends = (filters.DjangoFilterBackend,)
#         filter_fields = ('q_id')
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = CommentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         comment = self.get_object(pk)
#         comment.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class CommentDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Comment.objects.get(pk=pk)
#         except Comment.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         comment = self.get_object(pk)
#         comment = CommentSerializer(commnt)
#         filter_backends = (filters.DjangoFilterBackend,)
#         filter_fields = ['q_id','user_id']
#         return Response(comment.data)

#     def put(self, request, pk, format=None):
#         comment = self.get_object(pk)
#         serializer = CommentSerializer(comment, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         comment = self.get_object(pk)
#         comment.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)