from django.shortcuts import render, get_object_or_404
from survey.models import Survey, Question
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy, reverse



class HomeView(TemplateView):
    template_name = "home.html"

def surveys_list(request):
    surveys = Survey.objects.all()
    context = {
        "surveys":surveys
    }
    return render(request,"evaluations/survey_list.html",context)

def detail_view(request, id):
    survey = get_object_or_404(Survey, id=id)

    questions = Question.objects.filter(survey=survey)

    context = {
        "survey": survey,
        "questionss": questions,
    }
    return render(request, "evaluations/detail.html", context)


class QuestionCreate(CreateView):
    model = Question
    fields = '__all__'
    template_name = "evaluations/question_create.html"

    #form_class = QuestionForm

    def get_success_url(self):
        survey_id = self.kwargs['survey_id']
        return reverse_lazy("SurveysPlus:survey_questions_details", kwargs={"id": survey_id})

    #def form_valid(self, form):
        #survey = Survey.objects.get(id=self.kwargs['survey_pk'])
        #self.object = form.save(commit=False)
        #self.object.Survey = survey
        #self.object.save()

        messages.success(self.request, "You have successfully created an event")
        return super(EventCreateForAdmin, self).form_valid(form)

class SurveyCreate(CreateView):
    model = Survey
    fields = ['name','description','need_logged_user','editable_answers','display_method']
    template_name = "evaluations/survey_create.html"
    def get_success_url(self):
        return reverse('SurveysPlus:survey_list')

    def form_valid(self,form):
        self.object = form.save(commit=False)
        #self.object.user = self.request.user
        self.object.save()
        #send_mail(
            #    subject="A survey has been created",
            #    message="Go to the site to see the new survey",
            #    from_email="test@test.com",
        #     recipient_list=[self.request.user.email,]
        # )
        return super(SurveyCreate, self).form_valid(form)

