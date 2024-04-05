from django.shortcuts import render
# views.py
from django.contrib.auth import logout
from django.shortcuts import redirect

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
# views.py
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ChangePasswordForm

from django.contrib import messages

# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
def adminpanel(request):
    return render(request,'adminpanel/index.html')

# @login_required
# def staff(request):
#     return render(request,'userpanel/index.html')
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile , formsCard

def login_view(request):
    if request.user.is_authenticated:
        # User is already logged in, redirect them to their respective group page
        user_profile = UserProfile.objects.get(user=request.user)
        company_forms = formsCard.objects.filter(company=user_profile.company)
        if user_profile.usertype == 'admin':
            return render(request, 'adminpanel/index.html',{'forms': company_forms,'first_name': request.user.first_name})
        elif user_profile.usertype == 'staff':
            return redirect('staff')
        else:
            return redirect('home')  # Redirect to home page if not in any specific group
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            user_profile = UserProfile.objects.get(user=user)
            if user_profile.usertype == 'admin':
                return render(request, 'adminpanel/index.html',{'first_name': request.user.first_name})
            elif user_profile.usertype == 'staff':
                redirect_url = 'staff'
                if request.GET:
                    redirect_url += '?' + request.GET.urlencode()
                return redirect(redirect_url)
            else:
                return redirect('/')  # Redirect to home page if not in any specific group
        else:
            error_message = 'Invalid username or password.'
            return render(request, 'adminpanel/login.html', {'error_message': error_message})
    else:
        return render(request, 'adminpanel/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')



@login_required
def change_password_view(request):
    success_message = None
    error_message = None

    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Update the session to prevent logout
            success_message = 'Your password was successfully updated!'
        else:
            error_message = 'Password change failed. Please check your old password or your new password must contain 1 special character with min 8 char'
    else:
        form = ChangePasswordForm(request.user)
    
    return render(request, 'adminpanel/change_password.html', {'form': form, 'success_message': success_message, 'error_message': error_message})



# views.py
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import UserProfile
import pandas as pd

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

@staff_member_required
def usercreation(request):
    print('hhhh')
    if request.method == 'POST' and request.FILES.get('file'):
        print('aha')
        # Read the uploaded Excel file
        excel_file = request.FILES['file']
        df = pd.read_excel(excel_file)
        # Iterate over rows and create user profiles
        for index, row in df.iterrows():
            print('oho')
            username = row['user']
            first_name=row['first_name']
            last_name=row['last_name']
            usertype = row['usertype']
            company = row['company']
            department = row['department']
            # Create user with default password '12345678'
            user = User.objects.create_user(username, password='12345678',first_name=first_name,last_name=last_name)
            # Create user profile
            UserProfile.objects.create(user=user, department=department, usertype=usertype, company=company)
        success_message = "User profiles have been created successfully."
        return render(request, 'adminpanel/usercreation.html', {'success_message': success_message})
    return render(request, 'adminpanel/usercreation.html')



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile




from django.shortcuts import render, redirect
from .forms import AuditFormForm


from django.shortcuts import render, redirect
from .models import UserProfile  # Import your UserProfile model
from .models import AuditForm  # Import your UserProfile model

def auditformniro(request):
    if request.user.is_authenticated:
        try:
            user_profile = request.user.userprofile
            if user_profile.usertype == 'admin':
                if request.method == 'POST':
                    # Extract form data from the request
                    audit_data = {
    'audittype': request.POST.get('audittype'),
    'sessionid': request.POST.get('sessionid'),
    'callstartday': request.POST.get('callstartday'),
    'Agent_ID': request.POST.get('Agent_ID'),
    'Sale_Owner_Name': request.POST.get('Sale_Owner_Name'),
    'Responsible_advisor_Name': request.POST.get('Responsible_advisor_Name'),
    'Encrypted_Mobile': request.POST.get('Encrypted_Mobile'),
    'Disposition': request.POST.get('Disposition'),
    'Is_Disposition_Correct': request.POST.get('Is_Disposition_Correct'),
    'Correct_Disposition': request.POST.get('Correct_Disposition'),
    'Niro_Stage': request.POST.get('Niro_Stage'),
    'Sale_Done': request.POST.get('Sale_Done'),
    'Customer_Intent': request.POST.get('Customer_Intent'),
    'P1_Need_Creation': request.POST.get('P1_Need_Creation'),
    'P2_Benefit_Selling': request.POST.get('P2_Benefit_Selling'),
    'P3_Eligibility_Check': request.POST.get('P3_Eligibility_Check'),
    'P4_Application_filling_steps': request.POST.get('P4_Application_filling_steps'),
    'P5_Bank_selfie_upload_steps': request.POST.get('P5_Bank_&_selfie_upload_steps'),
    'Rejection_Reason': request.POST.get('Rejection_Reason'),
    'Advisor_Error_Major': request.POST.get('Advisor_Error_Major'),
    'Advisor_Error_Minor': request.POST.get('Advisor_Error_Minor'),
    'Advisor_Error_Fatal': request.POST.get('Advisor_Error_Fatal'),
    'fatal': request.POST.get('fatal'),
    'Any_rude_Tone': request.POST.get('Any_rude_Tone'),
    'Mention_Process_Gap': request.POST.get('Mention_Process_Gap'),
    'Call_Observations': request.POST.get('Call_Observations'),
    'Mention_Good_Practice': request.POST.get('Mention_Good_Practice'),
    'Offers_Pitched': request.POST.get('offers_pitched'),
    'Remarks_For_Offer_Errors': request.POST.get('Remarks_For_Offer_Errors'),
    'DT_Followed': request.POST.get('DT_Followed'),
    'incorrect_DT_error_Remarks': request.POST.get('incorrect_DT_error_Remarks'),
}
                    audit_data['submitted_by'] = request.user
                    sessionid = request.POST.get('sessionid')
                    existing_audit = AuditForm.objects.filter(sessionid=sessionid).first()
                    if existing_audit:
                        existing_audit.delete()  # Delete older session ID form if it exists
                    
                    # Save the form data to the database
                    AuditForm.objects.create(**audit_data)  # Replace 'AuditFormModel' with your actual model name
                    # Redirect to a success page or render a success message
                    return redirect('/')  # Replace 'success_page' with the name of your success page URL
                else:
                    # Render the form template
                    users = UserProfile.objects.filter(company=user_profile.company, department='niro', usertype='staff')
                    return render(request, 'adminpanel/auditformniro.html', {'users': users})
            else:
                # Redirect or show error message to non-admin users
                return render(request, 'userpanel/index.html')  # Create this template with an appropriate error message
        except UserProfile.DoesNotExist:
            # Handle the case where UserProfile does not exist for the logged-in user
            return redirect('login')  # Create this template with an appropriate error message
    else:
        # Redirect to login page if user is not authenticated
        return redirect('login')



from django.shortcuts import render, redirect
from .models import alert
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden








from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from ckeditor.widgets import CKEditorWidget
from .models import alert

@login_required
def create_alert(request):
    if request.method == 'POST':
        alert_value = request.POST.get('alert_value')
        if not alert_value:
            return HttpResponseForbidden("Alert value is required.")
        
        user_profile = request.user.userprofile
        if user_profile.usertype != 'admin':
            return HttpResponseForbidden("You do not have permission to create alerts.")
        
        company = user_profile.company
        alert.objects.create(alertvalue=alert_value, alertcompany=company)
        return redirect('home')  # Redirect to wherever you want after saving the alert
    
    return render(request, 'adminpanel/create_alert.html', {'ckeditor_widget': CKEditorWidget()})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import alert

@login_required
def watch_alert(request):
    user_profile = request.user.userprofile
    company = user_profile.company
    
    # Fetch all alerts associated with the user's company
    alerts = alert.objects.filter(alertcompany=company).order_by('-submitted_date')
    
    return render(request, 'adminpanel/see_alert.html', {'alerts': alerts})

from django.shortcuts import render, get_object_or_404
from .models import alert

from django.shortcuts import render, get_object_or_404
from .models import alert

def alert_detail(request, alert_id):
    # Retrieve the alert object using the alert_id parameter
    alert_obj = get_object_or_404(alert, pk=alert_id)

    # Update the seen_by field with the current user's username if available
    if request.user.is_authenticated:
        if alert_obj.seen_by:
            seen_by_users = alert_obj.seen_by.split(',')
            if request.user.username not in seen_by_users:
                seen_by_users.append(request.user.username)
                alert_obj.seen_by = ','.join(seen_by_users)
        else:
            alert_obj.seen_by = request.user.username
    
        if request.method == 'POST' and 'acknowledge' in request.POST:
            if alert_obj.acknowledge_by:
                acknowledge_users = alert_obj.acknowledge_by.split(',')
                if request.user.username not in acknowledge_users:
                    acknowledge_users.append(request.user.username)
                    alert_obj.acknowledge_by = ','.join(acknowledge_users)
            else:
                alert_obj.acknowledge_by = request.user.username
            # Save the changes to the alert object
            alert_obj.save()
            return redirect('alert_detail', alert_id=alert_id)  # Redirect to the same page after acknowledgement

    # Save the changes to the alert objec
    # Save the changes to the alert object
    alert_obj.save()
    context = {
        'alert': alert_obj,
        'seen_by': alert_obj.seen_by.split(',') if alert_obj.seen_by else [],
        'acknowledge_by': alert_obj.acknowledge_by.split(',') if alert_obj.acknowledge_by else [],
        'usertype': request.user.userprofile.usertype
    }
    print(request.user.userprofile.usertype)

    return render(request, 'adminpanel/alert_detail.html', context)


from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import TestForm, TestQuestion
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from .models import TestForm, TestQuestion
@login_required
def create_test(request):
    if request.method == 'POST':
        # Check if the user is an admin
        if request.user.userprofile.usertype != 'admin':
            return HttpResponseForbidden("You don't have permission to access this page.")
        
        # Extract form data
        dept = request.POST.get('department')
        testname = request.POST.get('testname')
        
        company = request.user.userprofile.company
        
        # Create TestForm instance
        test_form = TestForm.objects.create(dept=dept, company=company ,test_name=testname)
        
        # Iterate over submitted questions and options
        for key, value in request.POST.items():
            if key.startswith('question'):
                question_text = value
                options = [request.POST[f'option{key[-1]}{i}'] for i in range(1, 5)]
                correct_answer = int(request.POST[f'correct_answer{key[-1]}'])
                
                # Create TestQuestion instance
                test_question = TestQuestion.objects.create(
                    form=test_form,
                    question_text=question_text,
                    option1=options[0],
                    option2=options[1],
                    option3=options[2],
                    option4=options[3],
                    correct_answer=correct_answer
                )
        
        return redirect('/')  # Redirect to a success page
    
    return render(request, 'adminpanel/create_test.html')


from django.shortcuts import render
from .models import TestForm
from django.contrib.auth.decorators import login_required

@login_required
def take_test(request):
    user_profile = request.user.userprofile
    department = user_profile.department
    company = user_profile.company
    
    # Filter test forms by the user's department and company
    test_forms = TestForm.objects.filter(dept=department, company=company).order_by('-form_id')
    
    return render(request, 'adminpanel/take_test.html', {'test_forms': test_forms})


# views.py
from django.shortcuts import render, get_object_or_404
from .models import TestForm, TestQuestion

from django.shortcuts import get_object_or_404, render
from .models import TestForm, TestQuestion

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import TestEvaluation
from django.shortcuts import render, get_object_or_404, redirect
from .models import TestForm, TestQuestion, TestEvaluation
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import TestForm, TestQuestion, TestEvaluation
from django.contrib.auth.models import User
from django.http import HttpResponse

def test_detail(request, form_id):
    test_form = get_object_or_404(TestForm, form_id=form_id)
    questions = TestQuestion.objects.filter(form=test_form)

    if request.method == 'POST':
        if TestEvaluation.objects.filter(test_form=test_form, user=request.user).exists():
            return HttpResponse("You have already taken this test.")
        total_marks = 0
        user_answers = {}
        question_number = 1  # Initialize question number counter
        
        for question in questions:
            answer_key = f'answer{question_number}'
            selected_option = request.POST.get(answer_key)
            user_answers[question.pk] = selected_option
            
            correct_option = str(question.correct_answer)
            if selected_option == correct_option:
                total_marks += 1
            
            question_number += 1  # Increment question number

        # Calculate percentage
        total_questions = len(questions)
        percentage = (total_marks / total_questions) * 100

        # Save evaluation results
        test_evaluation = TestEvaluation.objects.create(
            test_form=test_form,
            user=request.user,
            marks=total_marks,
            percentage=percentage
        )

        # Redirect to evaluation detail page
        user_profile = UserProfile.objects.get(user=request.user)
        if user_profile.usertype == 'admin':
            return redirect(f'/?marks={total_marks}')
        elif user_profile.usertype == 'staff':
            return redirect(f'/staff/?marks={total_marks}')


    return render(request, 'adminpanel/test_detail.html', {'test_form': test_form, 'questions': questions})


from .models import sop

def create_sop(request):
    if request.method == 'POST':
        sop_dept = request.POST.get('sop_dept')
        sop_value = request.POST.get('create_sop')
        company_name = request.user.userprofile.company
        # Save the SOP
        new_sop = sop.objects.create(sop_dept=sop_dept, sopvalue=sop_value, sop_company=company_name)
        new_sop.save()
        
        # Optionally, you can redirect the user to a success page or back to the SOP creation form.
        # return redirect('success_page')  # Replace 'success_page' with the URL name of your success page
        
    return render(request, 'adminpanel/create_sop.html')


from .models import sop

def watch_sop(request):
    # Get the logged-in user's company and department from the UserProfile
    user_company = request.user.userprofile.company
    user_dept = request.user.userprofile.department
    
    # Filter SOPs based on the user's company and department
    sop_list = sop.objects.filter(sop_company=user_company, sop_dept=user_dept)
    
    # Pass the filtered SOPs to the template for rendering
    return render(request, 'adminpanel/watch_sop.html', {'sop_list': sop_list})

from .models import video

def create_video(request):
    if request.method == 'POST':
        # Extract form data from request
        video_file = request.FILES.get('video')
        title = request.POST.get('title')
        description = request.POST.get('description')
        dept = request.POST.get('dept')
        company= request.user.userprofile.company
        print(company)


        
        # Check if all required fields are provided
        if video_file and title:
            # Save video data to the database
            video_obj = video(video_file=video_file, video_title=title, video_desc=description,dept=dept,company=company)
            video_obj.save()
            # Redirect to success page or any other page
            return redirect('/')
    
    # Render the form page
    return render(request, 'adminpanel/create_video.html')

def watch_video(request):
    user_department = request.user.userprofile.department  # Assuming userprofile has a 'dept' field
    company=request.user.userprofile.company
    userttype=request.user.userprofile.usertype
    print(user_department,company)
    # Filter videos based on the department of the user
    videos = video.objects.filter(dept=user_department,company=company).order_by('-id')
    return render(request, 'adminpanel/watch_video.html', {'videos': videos , 'usertype':userttype})




from django.shortcuts import render
from .models import AuditForm
from django.db.models import Count
from django.shortcuts import render
from .models import AuditForm
from django.db.models import Count
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
from datetime import datetime, timedelta
from .models import AuditForm

def profile(request):
    if request.user.is_authenticated and request.user.userprofile.usertype == 'admin':
        if request.method == 'POST':
            # Handle form submission
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            start_datetime = datetime.strptime(start_date, '%Y-%m-%d')
            end_datetime = datetime.strptime(end_date, '%Y-%m-%d') + timedelta(days=1)

            # Filter form submissions based on the selected date range
            form_submissions = AuditForm.objects.filter(
                submitted_date__range=(start_datetime, end_datetime)
            ).values('submitted_date').annotate(submission_count=Count('id'))

            # Extract dates and counts for plotting
            dates = [submission['submitted_date'] for submission in form_submissions]
            counts = [submission['submission_count'] for submission in form_submissions]

            # Render the template with the data
            return render(request, 'adminpanel/adminprofile.html', {'dates': dates, 'counts': counts})
        else:
            # Default date range: 3 days ago to today
            three_days_ago = datetime.now() - timedelta(days=3)
            default_start_date = three_days_ago.strftime('%Y-%m-%d')
            default_end_date = datetime.now().strftime('%Y-%m-%d')

            # Filter form submissions from three days ago to today
            form_submissions = AuditForm.objects.filter(
                submitted_date__range=(three_days_ago, datetime.now())
            ).values('submitted_date').annotate(submission_count=Count('id'))

            # Extract dates and counts for plotting
            dates = [submission['submitted_date'] for submission in form_submissions]
            counts = [submission['submission_count'] for submission in form_submissions]

            # Render the template with the default data
            return render(request, 'adminpanel/adminprofile.html', {'dates': dates, 'counts': counts, 'default_start_date': default_start_date, 'default_end_date': default_end_date})
    else:
        # Redirect or show error message for non-admin users
        return redirect('/')



def delete_alert(request, alert_id):
    # Retrieve the alert object using the alert_id parameter
    alert_obj = get_object_or_404(alert, pk=alert_id)
    
    # Check if the request method is POST and the delete parameter is present
    if request.method == 'POST' and 'delete' in request.POST:
        # Delete the alert object
        alert_obj.delete()
        # Redirect to a success URL after deleting the alert
        return redirect('/')  # Replace 'success_url' with the appropriate URL

    # If the request method is not POST or the delete parameter is not present,
    # or if the alert object is not found, redirect to an error page or handle the error as needed
    return redirect('error_url')  # Replace 'error_url' with the appropriate URL


from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import video

def delete_video(request, pk):
    # Get the video object
    vid = get_object_or_404(video, pk=pk)

    if request.method == 'POST' and 'delete' in request.POST:
        # Delete the video
        vid.delete()
        # Redirect to a success page or any other appropriate action
        return HttpResponse("Video deleted successfully")

    # Handle other cases if needed


from django.shortcuts import render
from django.http import HttpResponse

from django.http import HttpResponse
from .models import AuditForm

def recheck_view(request, sessionid):
    if request.method == 'POST':
        # Retrieve the AuditForm instance using the sessionid
        try:
            audit_form = AuditForm.objects.get(sessionid=sessionid)
            # Set the 'recheck' field to True
            audit_form.recheck = True
            checked_fields = request.POST.getlist('fields')  # Get the list of checked fields from the form
            correction_field_value = ', '.join(checked_fields)  # Join the checked fields into a comma-separated string
            audit_form.correction_field = correction_field_value  
            audit_form.save()  # Save the changes to the database
            # Example: Print the updated data
            print("Session ID:", sessionid)
            print("Recheck data:", audit_form.recheck)
            # Add your processing logic here
            # Return a response
            return HttpResponse("recheck requested succefully")
        except AuditForm.DoesNotExist:
            return HttpResponse("Audit Form not found for the provided session ID")
    else:
        # Handle GET requests or render a different template
        return HttpResponse("This view only handles POST requests")


from django.shortcuts import render
from .models import AuditForm

def recheck_form(request):
    # Query all AuditForm instances submitted by the current user with recheck=True
    audit_forms = AuditForm.objects.filter(submitted_by=request.user, recheck=True)
    # Pass the audit_forms queryset to the template for rendering
    return render(request, 'adminpanel/recheck.html', {'audit_forms': audit_forms})




def recheck_done(request, sessionid):
    if request.method == 'POST':
        # Retrieve the AuditForm instance using the sessionid
        try:
            audit_form = AuditForm.objects.get(sessionid=sessionid)
            # Set the 'recheck' field to True
            audit_form.recheck = 'done'
            audit_form.save()  # Save the changes to the database
            # Example: Print the updated data
            print("Session ID:", sessionid)
            print("Recheck data:", audit_form.recheck)
            # Add your processing logic here
            # Return a response
            return HttpResponse("recheck done succefully")
        except AuditForm.DoesNotExist:
            return HttpResponse("Audit Form not found for the provided session ID")
    else:
        # Handle GET requests or render a different template
        return HttpResponse("This view only handles POST requests")


from django.shortcuts import render
from .models import formsCard

def admin_dashboard(request):
    # Get the user's company from the UserProfile
    user_company = request.user.userprofile.company

    # Filter formsCard objects based on company
    user_forms = formsCard.objects.filter(company=user_company)

    # Pass the filtered formsCard objects to the template
    return render(request, 'adminpanel/admin-dashboard.html', {'user_forms': user_forms})


def form_dashboard(request):
    # Get the user's company from the UserProfile
    user_company = request.user.userprofile.company

    # Filter formsCard objects based on company
    user_forms = formsCard.objects.filter(company=user_company)

    # Pass the filtered formsCard objects to the template
    return render(request, 'adminpanel/form-dashboard.html', {'user_forms': user_forms})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def updateprofile(request):
    if request.method == 'POST':
        # Assuming you have a User model with fields: first_name, last_name, email, username, password
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')
        user.set_password(request.POST.get('password'))  # Remember to hash the password
        user.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')  # Redirect to the user's profile page or any other desired page
    else:
        # Handle GET request if needed (e.g., render a form for updating profile)
        pass
