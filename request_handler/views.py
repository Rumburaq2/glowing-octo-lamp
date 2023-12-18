from datetime import datetime
from multiprocessing.reduction import register
from time import gmtime, strftime
from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

from request_handler.models import items, loans


def call_sevcik_template(request):
    if 'back' in request.POST:
        data = request.POST
        pk = data.get("back")
        loan_save = get_object_or_404(loans, pk=pk)
        loan_save.loan_is_finished = True
        loan_save.item_id.item_state = 0
        items_save = loan_save.item_id
        items_save.item_state = 0  # 0 = ready pujcit, 1 = zapujceno, 2 = cekani na potvrzeni o delsi pujcku
        items_save.save()
        loan_save.save()

    if 'confirm' in request.POST:
        data = request.POST
        pk = data.get("confirm")

        loan_save = get_object_or_404(loans, pk=pk)
        loan_save.loan_is_finished = False
        loan_save.item_id.item_state = 1
        loan_save.date_on_loan = datetime.now()

        items_save = loan_save.item_id
        items_save.item_state = 1  # 0 = ready pujcit, 1 = zapujceno, 2 = cekani na potvrzeni o delsi pujcku
        items_save.save()
        loan_save.save()

    ''' 
    all_loans = [get_object_or_404(loans, pk=1)]
    for x in range(2, loans.objects.count() + 1):
        all_loans.append(get_object_or_404(loans, pk=x))
    '''
    '''
    all_loans = []
    for x in range(1, loans.objects.count() + 1):
        all_loans.append(get_object_or_404(loans, pk=x))
        '''

    all_loans = loans.objects.all() # radek kde item_id v db == nase item_id
    context = {
        "loans": all_loans,
    }

    return render(request, 'test.html', context)


def call_index_template(request, s):

    if 'pujcit' in request.POST:
        data = request.POST
        pk = data.get("pujcit")
        print(pk)

        obj = items.objects.get(item_id=pk)
        item_st = obj.item_state
        item_des = obj.item_description
        print(item_st)
        print(item_des)
        obj.item_state = 1

        obj.save()#dana vec na naseveny stav = 1 aka pujceno
        #ted vytvorime vypujcku

        #print(user.email)
        email = data.get("email")
        username = data.get("username")
        print(email)
        today = strftime("%Y-%m-%d", gmtime())
        print(today)
        print(username)
        #student_obj = User.objects.get(email=email)
        student_obj = User.objects.get(username=username)
        item_obj = items.objects.get(item_id=pk)
        b = loans(due_date=today, loan_is_finished=False, student_id=student_obj, item_id=item_obj)
        b.save()

        return redirect("/verified")



    person = {'firstname': 'Craig', 'lastname': 'Daniels'}
    id_string = request.path #id veci
    id_string = id_string[1:]
    id_string = id_string[:-1]#parsujeme id veci
    #row = items.objects.all().filter(item_id=id_string)#radek kde item_id v db == nase item_id
    print(id_string)
    row_obj = items.objects.get(item_id=id_string)
    row_obj2 = get_object_or_404(items, item_id=id_string)
    item_idd = row_obj2.item_id
    print(item_idd)
    item_index_val = row_obj2.pk #not needed ig
    item_descriptionn = row_obj2.item_description

    context = {
        'person': person,
        'weather': id_string,
        'item_id': item_idd,
        'item_description': item_descriptionn,
        'item_index_val': item_index_val,
    }
    return render(request, 'chatgpt.html', context)


def show_verified(request):
    return render(request, 'verified.html')


def loan(request, s):
    print("hell")
    return HttpResponse("<h1>heloo world</h1>")


def detail(request, thing_id):
    if "confirm" in request.POST:
        return redirect('/loan/')

    if request.method == 'POST':
        # Process your form data here

        # Redirect to /loan after processing the form
        return redirect('/loan')

        # Handle GET requests or render the form
    return render(request, 'your_template_name.html')

    return render(request, thing_id, "index.html")

def home(request):
    return render(request, "home.html")

def logout_view(request):
    logout(request)
    return redirect("")



