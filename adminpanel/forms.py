# forms.py
from django import forms
from django.contrib.auth.forms import PasswordChangeForm

class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your current password'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your new password'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm your new password'})


from django import forms
from .models import AuditForm  # Import your model class her

class AuditFormForm(forms.ModelForm):
    class Meta:
        model = AuditForm  # Replace 'AuditForm' with the name of your model class
        fields = [
            'audittype',
            'sessionid',
            'callstartday',
            'Agent_ID',
            'Sale_Owner_Name',
            'Responsible_advisor_Name',
            'Encrypted_Mobile',
            'Disposition',
            'Is_Disposition_Correct',
            'Correct_Disposition',
            'Niro_Stage',
            'Sale_Done',
            'Customer_Intent',
            'P1_Need_Creation',
            'P2_Benefit_Selling',
            'P3_Eligibility_Check',
            'P4_Application_filling_steps',
            'P5_Bank_selfie_upload_steps',
            'Rejection_Reason',
            'Advisor_Error_Major',
            'Advisor_Error_Minor',
            'Advisor_Error_Fatal',
            'fatal',
            'Any_rude_Tone',
            'Mention_Process_Gap',
            'Call_Observations',
            'Mention_Good_Practice',
            'Offers_Pitched',
            'Remarks_For_Offer_Errors',
            'DT_Followed',
            'incorrect_DT_error_Remarks',
        ]
