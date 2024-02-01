from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    send_mail(
    "Testing Mail",
    "Yo chai testing ko lagi maile pathako ho hai.",
    "basnetpravatkiran@gmail.com",
    ["pravatjungbasnet@gmail.com"],
    fail_silently=False,
)


    return render(request,'mail/home.html')