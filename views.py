from django.shortcuts import render
from .forms import ApplicationForm
from .models import Application

def application_form(request):
    form = ApplicationForm()
    applications = Application.objects.all()
    return render(request, 'application_form.html', {'form': form, 'applications': applications})

def submit_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save()
            return render(request, 'partials/application_item.html', {'application': application})
    return render(request, 'partials/application_form.html', {'form': form})
