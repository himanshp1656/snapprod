from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def staff(request):
    
    return render(request,'userpanel/index.html',{'first_name': request.user.first_name})


from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from adminpanel.models import AuditForm  # Assuming AuditForm model is defined in userpanel/models.py
from adminpanel.models import TestEvaluation

from django.shortcuts import render
from adminpanel.models import TestEvaluation, AuditForm

# @login_required
# def profile(request):
#     # Get the current user
#     user = request.user

#     # Retrieve test evaluations for the current user
#     test_evaluations = TestEvaluation.objects.filter(user=user)

#     # Retrieve audit forms where the user is the responsible advisor
#     audit_forms = AuditForm.objects.filter(Responsible_advisor_Name=user.username).order_by('-id')
    
#     # Calculate average quality score for each audit form
#     audit_scores = []
#     for audit_form in audit_forms:
#         total_score = 0
#         num_parameters = 0
#         # Calculate score for each parameter, ignoring 'Na' values
#         for field_name in ['P1_Need_Creation', 'P2_Benefit_Selling', 'P3_Eligibility_Check',
#                            'P4_Application_filling_steps', 'P5_Bank_selfie_upload_steps']:
#             field_value = getattr(audit_form, field_name)
#             if field_value != 'Na':
#                 num_parameters += 4
#                 if field_value == 'H':
#                     total_score += 4
#                 elif field_value == 'M':
#                     total_score += 3
#                 elif field_value == 'L':
#                     total_score += 2
#                 elif field_value == 'P':
#                     total_score += 1
        
#         # Calculate average quality score
#         if num_parameters > 0:
#             average_score = total_score / num_parameters
#             audit_scores.append(average_score)
    
#     # Pass the test evaluations, audit forms, and audit scores to the template
#     return render(request, 'userpanel/profile.html', {'user': user, 'tests': test_evaluations, 'audits': zip(audit_forms, audit_scores)})


















from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime, timedelta
from adminpanel.models import TestEvaluation, AuditForm

@login_required
def profile(request):
    # Get the current user
    user = request.user

    # Initialize default dates
    default_start_date = (datetime.now() - timedelta(days=3)).strftime('%Y-%m-%d')
    default_end_date = datetime.now().strftime('%Y-%m-%d')
    
    # If the request is POST, get the selected date range
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
    else:
        # Default date range
        start_date = default_start_date
        end_date = default_end_date
    
    # Retrieve test evaluations for the current user within the selected date range
    test_evaluations = TestEvaluation.objects.filter(user=user, test_form__submitted_date__range=[start_date, end_date])
    print(test_evaluations)
    
    # Retrieve audit forms where the user is the responsible advisor within the selected date range
    audit_forms = AuditForm.objects.filter(Responsible_advisor_Name=user.username, submitted_date__range=[start_date, end_date]).order_by('-id')
    print(audit_forms)
    
    # Calculate average quality score for each audit form within the selected date range
    audit_scores = []
    for audit_form in audit_forms:
        total_score = 0
        num_parameters = 0
        # Calculate score for each parameter, ignoring 'Na' values
        for field_name in ['P1_Need_Creation', 'P2_Benefit_Selling', 'P3_Eligibility_Check',
                           'P4_Application_filling_steps', 'P5_Bank_selfie_upload_steps']:
            field_value = getattr(audit_form, field_name)
            if field_value != 'Na':
                num_parameters += 4
                if field_value == 'H':
                    total_score += 4
                elif field_value == 'M':
                    total_score += 3
                elif field_value == 'L':
                    total_score += 2
                elif field_value == 'P':
                    total_score += 1
        
        # Calculate average quality score
        if num_parameters > 0:
            average_score = total_score / num_parameters
            audit_scores.append(average_score)
    
    # Pass the test evaluations, audit forms, and audit scores to the template
    return render(request, 'userpanel/profile.html', {'user': user, 'tests': test_evaluations, 'audits': zip(audit_forms, audit_scores),
                                                      'default_start_date': default_start_date, 'default_end_date': default_end_date,
                                                      'start_date': start_date, 'end_date': end_date})

from django.shortcuts import render, get_object_or_404
# from .models import AuditForm

def audit_form_detail(request, session_id):
    # Retrieve the AuditForm object based on the session ID
    audit_form = get_object_or_404(AuditForm, sessionid=session_id)
    
    # Pass the audit_form object to the template
    return render(request, 'userpanel/audit_form_detail.html', {'audit_form': audit_form})


# views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from adminpanel.models import TestEvaluation
# from weasyprint import HTML

from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def generate_certificate(request, evaluation_id):
    # Retrieve TestEvaluation object based on evaluation_id
    test_evaluation = TestEvaluation.objects.get(pk=evaluation_id)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'

    # Create PDF document
    p = canvas.Canvas(response, pagesize=letter)
    
    # Draw certificate template
    p.setFont("Helvetica", 12)
    p.drawString(100, 700, "Certificate of Achievement")
    p.drawString(100, 680, f"This certifies that {test_evaluation.user.first_name} successfully passed the {test_evaluation.test_form.test_name}")
    p.drawString(100, 660, "Congratulations on your outstanding achievement!")

    # End PDF document
    p.showPage()
    p.save()
    
    return response





@login_required
def auditReports(request):
    # Get the current user's first name and last name
    user = request.user
    # Filter AuditForm objects where Responsible_advisor_Name is equal to the username of the current user
    audit_forms = AuditForm.objects.filter(Responsible_advisor_Name=user.username).order_by('-id')
    quality_scores = []
    for audit_form in audit_forms:
        # Initialize the score variables
        total_score = 0
        num_parameters = 0
        
        # Calculate score for each parameter, ignoring 'Na' values
        for field_name in ['P1_Need_Creation', 'P2_Benefit_Selling', 'P3_Eligibility_Check',
                           'P4_Application_filling_steps', 'P5_Bank_selfie_upload_steps']:
            field_value = getattr(audit_form, field_name)
            if field_value != 'Na':
                num_parameters += 4
                if field_value == 'H':
                    total_score += 4
                elif field_value == 'M':
                    total_score += 3
                elif field_value == 'L':
                    total_score += 2
                elif field_value == 'P':
                    total_score += 1
        
        # Calculate average quality score
        if num_parameters > 0:
            average_score = total_score / num_parameters
            quality_scores.append(average_score)
    
    # change
    # Pass the first name, last name, and audit_forms to the template
    return render(request, 'userpanel/audit_reports.html', {'audit_forms': zip(audit_forms, quality_scores)})





@login_required
def testReports(request):
    # Get the current user's first name and last name
    user = request.user
    test_evaluations = TestEvaluation.objects.filter(user=user).order_by('-id')
    # Pass the first name, last name, and audit_forms to the template
    return render(request, 'userpanel/test-reports.html', {'test_evaluations': test_evaluations,})



def userDashboard(request):
    return render(request,'userpanel/user-dashboard.html')