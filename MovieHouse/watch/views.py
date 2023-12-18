from django.shortcuts import render,redirect
from series.models import Series
from movie.models import Movie
from django.contrib import messages
from watch.models import Mwatchlist,Swatchlist,Freetrial,Account,Annual,Month,Freetriallist
from django.contrib.auth.decorators import login_required
from datetime import date,timedelta
# Create your views here.
@login_required
def add_to_watchlist(request,pk):
    m=Movie.objects.get(pk=pk)
    user=request.user
    try:
        w=Mwatchlist.objects.filter(user=user,movie=m)
        w.delete()
        w = Mwatchlist.objects.create(movie=m, user=user)
        w.save()
    except:
        w=Mwatchlist.objects.create(movie=m,user=user)
        w.save()
    return redirect('watch:Mwatchlist')
@login_required
def viewwatchlist(request):
    user = request.user
    s = Swatchlist.objects.filter(user=user)
    return render(request, 'watchlist.html', {'s':s})
@login_required
def viewMwatchlist(request):
    user=request.user
    m= Mwatchlist.objects.filter(user=user)
    return render(request,'Mwatchlist.html', {'m': m})
@login_required
def add_to_Swatchlist(request,pk):
    m = Series.objects.get(pk=pk)
    user = request.user
    try:
        w = Swatchlist.objects.get(user=user, series=m)
        w.delete()
        w = Swatchlist.objects.create(series=m, user=user)
        w.save()
    except:
        w = Swatchlist.objects.create(series=m, user=user)
        w.save()
    return redirect('watch:watchlist_view')
@login_required
def mremove(request,pk):
    m=Mwatchlist.objects.get(pk=pk)
    m.delete()
    return viewMwatchlist(request)
@login_required
def sremove(request,pk):
    s=Swatchlist.objects.get(pk=pk)
    s.delete()
    return viewwatchlist(request)
@login_required
def subscribe(request):
    user=request.user
    try:
        try:
            f = Freetrial.objects.get(user=user)
            if (f):
                try:
                    s = Month.objects.get(user=user)
                    if(s):
                        try:
                            a = Annual.objects.get(user=user)
                            if (a):
                                return render(request, 'subscribe.html', {'s': s,'a':a,'f':f})
                        except:
                            return render(request, 'subscribe.html', {'s': s,'f':f})
                except:
                    try:
                        a = Annual.objects.get(user=user)
                        if (a):
                            return render(request, 'subscribe.html', {'a': a, 'f': f})
                    except:
                      return render(request, 'subscribe.html',{'f': f})
        except:
            list = Freetriallist.objects.get(user=user)
            if (list):
                try:
                    s = Month.objects.get(user=user)
                    if (s):
                        try:
                            a = Annual.objects.get(user=user)
                            if (a):
                                return render(request, 'subscribe.html', {'s': s, 'a': a, 'e':list})
                        except:
                            return render(request, 'subscribe.html', {'s': s, 'e':list})
                except:
                    try:
                        a = Annual.objects.get(user=user)
                        if (a):
                            return render(request, 'subscribe.html', {'a': a, 'e':list})
                    except:
                        return render(request, 'subscribe.html',{'e':list})
    except:
        try:
            s = Month.objects.get(user=user)
            if (s):
                return render(request, 'subscribe.html', {'s': s})
        except:
            try:
                a = Annual.objects.get(user=user)
                if (a):
                    return render(request, 'subscribe.html', {'a': a})
            except:
                return render(request, 'subscribe.html')
@login_required
def freetrial(request):
    user=request.user
    current_date=date.today().isoformat()
    expdate=(date.today()+timedelta(days=20)).isoformat()
    f = Freetrial.objects.create(user=user,date1=current_date,exp_date=expdate)
    f.save()
    p=Freetriallist.objects.create(user=user)
    p.save()
    return redirect('movie:homeall')
@login_required
def subscription(request):
    if(request.method=="POST"):
        n=request.POST['n']
        user=request.user
        current_date = date.today().isoformat()
        expdate=(date.today()+timedelta(days=28)).isoformat()
        amount=49
        try:
            try:
                u=Month.objects.get(user=user)
                if(u):
                    a="Subscription validity is not expired"
                    return render(request, 'subscribeconfirm.html', {'a': a})
            except:
                acct = Account.objects.get(acctnumber=n)
                if (acct.balance >= amount):
                    acct.balance -= amount
                    acct.save()
                    s = Month.objects.create(user=user, amount=amount,date1=current_date,exp_date=expdate)
                    s.save()
                    msg = "subscribed successfully"
                    return render(request, 'subscribeconfirm.html', {'msg': msg})
                else:
                    msg = "Insufficient Balance.You Cant Place Order"
                    return render(request, 'subscribeconfirm.html', {'msg': msg})
        except:
            messages.error(request, "Invalid accountnumber ")
            return render(request,'subscription.html')
    return render(request,'subscription.html')
@login_required
def subscription2(request):
    if (request.method == "POST"):
        n = request.POST['n']
        user = request.user
        current_date = date.today().isoformat()
        #expdate = date.today().isoformat()
        expdate=(date.today()+timedelta(days=365)).isoformat()
        amount = 500
        try:
            try:
                u=Annual.objects.get(user=user)
                if (u):
                    a = "Subscription validity is not expired"
                    return render(request, 'subscribeconfirm.html', {'a': a})
            except:
                acct = Account.objects.get(acctnumber=n)
                if (acct.balance >= amount):
                    acct.balance -= amount
                    acct.save()
                    s = Annual.objects.create(user=user, amount=amount,date1=current_date,exp_date=expdate)
                    s.save()
                    msg = "subscribed successfully"
                    return render(request, 'subscribeconfirm.html', {'msg': msg})
                else:
                    msg = "Insufficient Balance.You Cant Subscribe"
                    return render(request, 'subscribeconfirm.html', {'msg': msg})
        except:
            messages.error(request, "Invalid accountnumber ")
            return render(request, 'subscription2.html')
    return render(request,'subscription2.html')

