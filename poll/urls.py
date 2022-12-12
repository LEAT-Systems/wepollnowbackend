from urllib.parse import urlparse
from poll.views import *
from django.urls import path

urlpatterns = [
    path('user_polls/', GetPollsForVoters.as_view(), name="user_polls"),
    path('poll_candidates/', GetPollPartiesAndCandidates.as_view(), name="poll_candidates"),
    path("poll_category/", PollCategoryList.as_view(), name="poll_category"),
    path("create_poll/", Polls.as_view(), name="create_poll"),
    path("rud_poll/<int:pk>", PollRetrieveUpdateDelete.as_view(), name="retrieve_update_delete_poll"),

    path("candidatesList/", CandidatesList.as_view(), name="candidatesList"),
    path("get_polls/", AllPollsList.as_view(), name="get_polls"),
    path("poll_category_party/" , GetPartiesAndCandidatesForPollCategory.as_view(), name="poll_category_party"),
    path("poll_result/", PollResult.as_view(), name="poll_result"),
    path("poll_result_filter/", PollResultFilter.as_view(), name="poll_result_filter"),
    path("poll_survey_category/", SurveyCategoryView.as_view(), name="poll_survey_category"),
    path("survey_category/", AllSurveyCategoryListView.as_view(), name="survey_category"),
    path("poll_survey_category/<int:poll_id>", SurveyCategoryListView.as_view(), name="poll_survey_category_list"),
    path("rud_survey_category/<int:pk>", SurveyCategoryRetrieveUpdateDelete.as_view(), name="retrieve_update_delete_surveyCategory"),
    path("poll_survey_response/", SurveyResponseView.as_view(), name="poll_survey_response")
    
]


