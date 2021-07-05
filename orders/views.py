from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ReminderForm
from .tasks import reminder_send_mail


# HT 12. Celery
def reminder(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            subject = 'Reminder'
            from_email = 'antonov@gmail.com'
            message = form.cleaned_data['text']
            recipient_list = [form.cleaned_data['email']]
            time_sending = form.cleaned_data['time_sending']
            reminder_send_mail.apply_async((subject, message, from_email, recipient_list), eta=time_sending)
            messages.success(request, 'Reminder successfully created!')
            return redirect('reminder')
        else:
            messages.error(request, 'Reminder not created!')
    else:
        form = ReminderForm()
    return render(request, 'reminder.html', {'form': form})
