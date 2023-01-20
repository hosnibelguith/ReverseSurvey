from .views import detail_view, surveys_list, QuestionCreate, SurveyCreate

from django.urls import path
from django.conf.urls import url

app_name = "SurveysPlus"
urlpatterns = [

    path("<int:id>/details/", detail_view, name='survey_questions_details'),
    path('',surveys_list,name="survey_list"),
    path('create_survey/', SurveyCreate.as_view(), name='survey_create'),

    path('<int:survey_id>/create_question/', QuestionCreate.as_view(), name='question_create'),

]