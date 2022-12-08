from django.contrib import admin
from poll.models import *

# Register your models here.
@admin.register(PollCategory)
class PollCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    pass

admin.site.register(Votes)
admin.site.register(VoteCount)
admin.site.register(SurveyCategory)
admin.site.register(SurveyResponse)
