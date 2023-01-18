from django.shortcuts import render, redirect
from journey.models import Turn, City, Country,Reservation
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.db.models import F,Count
from django.db.models import Count
from .filters import TurnFilter

# Create your views here.
def index(request):
    turn = Turn.objects.filter(country__name__startswith="Azerbaycan").annotate(
        width_percent=Count('persons')*500/F('max_person')).annotate(num_people=Count('persons')).annotate(join_percent=Count('persons')*100/F('max_person'))
    # perc =turn[id].percentage/turn[id].max_person
    
    
   
    # print(turn[0].percentage/turn[0].max_person)  
    # people_count = Turn.objects.annotate(num_people=Count('persons'))
    print(turn[1].join_percent)
    context = {
        'turn': turn,
        # 'people_count': people_count
    }
    return render(request, "index.html", context)

def about(request):
    turn = Turn.objects.exclude(country__name__startswith="Azerbaycan").annotate(
        num_people=Count('persons'))
    context = {
        'turn': turn
    }
    return render(request, "about.html", context)

def deals(request):
    people_count = Turn.objects.annotate(num_people=Count('persons'))
    pfilter = TurnFilter()
    properties_filter = TurnFilter(request.GET,queryset=Turn.objects.all().annotate(
        num_people=Count('persons')))
    # participant_percentage= (people_count*500)/properties_filter.max_person
    # print("ddddddddddddddddddddddddddddddddddddddddddddp",properties_filter.__dict__)
    properties = properties_filter.qs
    # participant_percentage= int((people_count*500)/properties.max_person)
    page_number = int(request.GET.get('page',1))
    paginator = Paginator(properties,2)
    page = paginator.page(page_number)

    return render(request,'deals.html',{
        'pfilter':pfilter,        
        'properties': page.object_list, 
        'paginator': paginator,
        'page_object': page,
        'filter': TurnFilter,
        'properties': page.object_list,
        'paginator': paginator,
        'people_count': people_count
})




def enroll_the_course(request):
    turn_id = request.POST['turn_id']
    turn_name = request.POST['turn_name']
    user_id = request.POST['user_id']
    user_email = request.POST['user_email']
    rezerv = Reservation.objects.create(user=user_id,turn=turn_id,name=turn_name,mail=user_email)
    return redirect('index')
def travel_detail(request, id):
    turn = get_object_or_404(Turn, id=id)
    count_person = turn.persons.count()
    persons = turn.persons.filter(id=request.user.id)

    context = {
        'turn': turn,
        'persons':persons,
        'count_person': count_person
    }
    return render(request, 'travel_details.html', context)

def travel_register(request):
    turn_id = request.POST['turn_id']
    user_id = request.POST['user_id']
    turn= Turn.objects.get(id=turn_id)
    persons_count=turn.persons.count()
    if turn.persons.filter(id=user_id):
     turn.persons.remove(user_id)
    else:
        turn.persons.add(user_id)
    return redirect('index')





# def travel_reserv(request):
#     # turn = get_object_or_404(Turn, id=id)
#     ty = Turn.objects.all()
#     # form = ResevForm()
#     # if request.method == "POST":
        
#     #     form = ResevForm(request.POST)
       
#     #     if form.is_valid():
#     #         print("ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff")

           
#     #         form.save()
#     #         return redirect('index')
   
#     return render(request, 'reservation.html', context = {
#         # 'turn': turn,
#         'ty': ty,
#         # 'form': form,
#     } )
