from django.shortcuts import render , HttpResponse
from Calculator.forms import AddNumbersForm
# Create your views here.

def Home(request):
    return render(request,template_name='Cal/InnerBase.html')

def Base_Page(request):
    return render(request,template_name='Base.html')


def add_numbers(request):
    form = AddNumbersForm()
    result = None

    if request.method == 'POST':
        form = AddNumbersForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            result =num1 + num2

    return render(request, 'base.html', {'form': form, 'result': result})
