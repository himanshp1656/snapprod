from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=50)
    usertype = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    def __str__(self):
        return self.user.username
    

class AuditForm(models.Model):
    audittype = models.CharField(max_length=100)
    sessionid = models.CharField(max_length=100)
    callstartday = models.DateField()
    Agent_ID = models.CharField(max_length=100)
    Sale_Owner_Name = models.CharField(max_length=100)
    Responsible_advisor_Name = models.CharField(max_length=100)
    Encrypted_Mobile = models.CharField(max_length=100)
    Disposition = models.CharField(max_length=100)
    Is_Disposition_Correct = models.CharField(max_length=100)
    Correct_Disposition = models.CharField(max_length=100)
    Niro_Stage = models.CharField(max_length=100)
    Sale_Done = models.CharField(max_length=100)
    Customer_Intent = models.CharField(max_length=100)
    P1_Need_Creation = models.CharField(max_length=100)
    P2_Benefit_Selling = models.CharField(max_length=100)
    P3_Eligibility_Check = models.CharField(max_length=100)
    P4_Application_filling_steps = models.CharField(max_length=100)
    P5_Bank_selfie_upload_steps = models.CharField(max_length=100)
    Rejection_Reason = models.CharField(max_length=100)
    Advisor_Error_Major = models.CharField(max_length=100)
    Advisor_Error_Minor = models.CharField(max_length=100)
    Advisor_Error_Fatal = models.CharField(max_length=100)
    fatal = models.CharField(max_length=100)
    Any_rude_Tone = models.CharField(max_length=100)
    Mention_Process_Gap = models.CharField(max_length=100)
    Call_Observations = models.TextField()
    Mention_Good_Practice = models.TextField()
    Offers_Pitched = models.CharField(max_length=100)
    Remarks_For_Offer_Errors = models.TextField()
    DT_Followed = models.CharField(max_length=100)
    incorrect_DT_error_Remarks = models.TextField()
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submitted_audit_forms', blank=True, null=True)
    submitted_date = models.DateField(default=timezone.now, null=True)
    recheck=models.CharField(max_length=20,null=True)
    correction_field=models.TextField(null=True)
    def __str__(self):
        return f"Audit Form - {self.sessionid}"


from django.db import models
from django.utils.text import slugify

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class alert(models.Model):
    alert_id = models.AutoField(primary_key=True)
    alertvalue = models.TextField()
    alertcompany = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    seen_by = models.TextField(blank=True)  # Comma-separated usernames of users who have seen the alert
    acknowledge_by = models.TextField(blank=True)  # Comma-separated usernames of users who have acknowledged the alert
    view_date = models.DateTimeField(blank=True, null=True)  # Date and time when the alert was viewed
    submitted_date = models.DateField(default=timezone.now, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.alertvalue)  # Generate slug based on alertvalue
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Alert ID: {self.alert_id}, Company: {self.alertcompany}"


from django.db import models

class TestForm(models.Model):
    form_id = models.AutoField(primary_key=True)
    test_name=models.CharField(max_length=100)
    dept = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    submitted_date = models.DateField(default=timezone.now, null=True)
    # Add other fields as needed

    def __str__(self):
        return f"Test Form - {self.form_id}"


class TestQuestion(models.Model):
    form = models.ForeignKey(TestForm, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct_answer = models.IntegerField(choices=[(1, 'Option 1'), (2, 'Option 2'), (3, 'Option 3'), (4, 'Option 4')])
    # Add other fields as needed
    def __str__(self):
        return f"{self.question_text}"

from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User
from .models import TestForm

class TestEvaluation(models.Model):
    test_form = models.ForeignKey(TestForm, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    marks = models.IntegerField()
    percentage = models.DecimalField(max_digits=5, decimal_places=2,null=True)  # Decimal field for percentage

    def __str__(self):
        return f"TestForm ID: {self.test_form.form_id}, User: {self.user.username}, Marks: {self.marks}, Percentage: {self.percentage}%"



class sop(models.Model):
    sopvalue=models.TextField()
    sop_company=models.CharField(max_length=100)
    sop_dept=models.CharField(max_length=100)

    def __str__(self):
        return f"Department: {self.sop_dept}, Company: {self.sop_company}"
    

class video(models.Model):
    video_file = models.FileField(upload_to='adminpanel/videos/')
    video_title=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    dept=models.CharField(max_length=100)
    video_desc=models.TextField()
    submitted_date = models.DateField(default=timezone.now, null=True)
    def __str__(self):
        return f"title: {self.video_title}"
    




class formsCard(models.Model):
    company=models.CharField(max_length=50)
    form_name=models.CharField(max_length=50)
    form_link=models.CharField(max_length=50)
    def __str__(self):
        return f"{self.form_name}"
