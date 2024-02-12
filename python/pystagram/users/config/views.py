from django.shortcuts import render

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return redirect("posts:feeds")
    else :
        return redirect("users:login")
    # context = {
    #     "of_course" : "of_course"
    # }
    # return render(request, 'config/index.html', context)