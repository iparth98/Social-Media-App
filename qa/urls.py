from django.urls import path
from . import views


urlpatterns = [
    path("answered/", views.QuestionAnsListView.as_view(), name="index_ans"),
    path("indexed/", views.QuestionsIndexListView.as_view(), name="index_all"),
    path("", views.QuestionListView.as_view(), name="index_noans"),
    path(
        "question-detail/<int:pk>/",
        views.QuestionDetailView.as_view(),
        name="question_detail",
    ),
    path(
        "propose-answer/<int:question_id>/",
        views.CreateAnswerView.as_view(),
        name="propose-answer",
    ),
    path("ask-question/", views.CreateQuestionView.as_view(), name="ask_question"),
]
