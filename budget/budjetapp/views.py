from datetime import datetime, date
from django.shortcuts import render, redirect
from dateutil import parser
from .models import Budget

def main(request):
    if request.method == 'GET':
        records = Budget.objects.all()
        return render(request, 'budjetapp/index.html', {"records": records})

    if request.method == 'POST':
        coming = 0
        spending = 0
        sorted_records = []
        start_date_raw = int(request.POST["start_date"])
        start_date= datetime(year=int(start_date_raw/10000), month=int(start_date_raw % 10000/100), day=int(start_date_raw %100 ))
        end_date_raw = int(request.POST["end_date"])
        end_date= datetime(year=int(end_date_raw/10000), month=int(end_date_raw % 10000/100), day=int(end_date_raw %100 ))

        if start_date and end_date:
            records = Budget.objects.all()
            for record in records:
                if record.created.timestamp() >= start_date.timestamp() and record.created.timestamp() <= end_date.timestamp():
                    sorted_records.append(record)
                    if record.coming_or_spending == True:
                        coming+=record.money
                        
                    else:
                        spending+=record.money    

        
        return render(request, 'budjetapp/details.html', {"sorted_records" : sorted_records, "spending" : spending, "coming" : coming}) 


def records(request):
    if request.method == 'POST':
        name = request.POST['name']
        coming_or_spending = request.POST.get('checks')
        print(coming_or_spending)
        category= request.POST["category"]
        money = request.POST["money"]
        if name:
            new_record = Budget(name = name, category = category, coming_or_spending = bool(coming_or_spending),  money = money)
            new_record.save()
        return redirect(to='/')
    return render(request, 'budjetapp/records.html', {})


def delete_record(request, id):
    record = Budget.objects.get(id=id)
    print(record)
    record.delete()
    return redirect(to='/') 

  
