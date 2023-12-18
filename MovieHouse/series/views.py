from django.shortcuts import render,redirect
from series.models import Series,Episode,Scategory
from watch.models import Freetrial,Annual,Month
from django.contrib.auth.decorators import login_required
from datetime import date
# Create your views here.
@login_required
def series_home(request):
    s = Scategory.objects.all()
    return render(request,'shome.html',{'s':s})
@login_required
def series_details(request,pk):
    s=Series.objects.get(pk=pk)
    return render(request,'sdetails.html',{'s':s})
@login_required
def series_view(request,pk):
    m = Episode.objects.get(pk=pk)
    c = date.today().isoformat()
    user=request.user
    try:
        try:
            f = Freetrial.objects.get(user=user)
            if (f):
                if (c==str(f.exp_date)):
                    f.delete()
                    return redirect('watch:subscribe')
                else:
                   return render(request, 'movie.html', {'m': m})
        except:
            s = Month.objects.get(user=user)
            if (s):
                if (c==str(s.exp_date)):
                    s.delete()
                    return redirect('watch:subscribe')
                else:
                    return render(request, 'movie.html', {'m': m})
    except:
        try:
            a = Annual.objects.get(user=user)
            if (a):
                if (c==str(a.exp_date)):
                    a.delete()
                    return redirect('watch:subscribe')
                else:
                  return render(request, 'movie.html', {'m': m})
        except:
            return redirect('watch:subscribe')
    else:
        return redirect('watch:subscribe')


@login_required
def series_episodes(request,p):
    s=Episode.objects.filter(esname__sname=p)
    m=Series.objects.get(sname=p)
    l=m.no_of_episodes
    return render(request, 'episodes.html', {'s': s, 'range': range(1, l + 1)})

@login_required
def series_category(request,p):
    s=Series.objects.filter(category__scname=p)
    return render(request,'scategory.html',{'p':s})
