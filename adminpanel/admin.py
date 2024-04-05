# admin.py
from django.contrib import admin
from .models import UserProfile
from .models import AuditForm
from .models import alert
from .models import TestForm
from .models import TestQuestion
from .models import TestEvaluation
from .models import sop
from .models import video
from .models import formsCard

admin.site.register(UserProfile)
admin.site.register(AuditForm)
admin.site.register(alert)
admin.site.register(TestQuestion)
admin.site.register(TestForm)
admin.site.register(TestEvaluation)
admin.site.register(sop)
admin.site.register(video)
admin.site.register(formsCard)
