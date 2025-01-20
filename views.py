# myapp/views.py
from django.shortcuts import render, redirect
from .forms import JobApplicationForm
from django.http import JsonResponse



def submit_job_application(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        
        # Extract the dynamic fields from the request
        additional_fields = {}
        for key in request.POST:
            if key.startswith('dynamicField'):
                additional_fields[key] = request.POST[key]

        if form.is_valid():
            # Create the JobApplication object but don't save it yet
            job_application = form.save(commit=False)
            job_application.additional_fields = additional_fields  # Store dynamic fields
            job_application.save()  # Save the application to MongoDB

            return JsonResponse({'message': 'Job application submitted successfully!'})

    else:
        form = JobApplicationForm()

    return render(request, 'submit_job.html', {'form': form})



