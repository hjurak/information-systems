from django.shortcuts import render, get_object_or_404, redirect
from .models import Conference, Presentation, Participant, ScientificWork
from .forms import ParticipantForm, ScientificWorkForm

def index(request):
    conferences = Conference.objects.all()
    return render(request, 'index.html', {'conferences': conferences})

def conference_detail(request, conference_id):
    conference = get_object_or_404(Conference, pk=conference_id)
    presentations = Presentation.objects.filter(conference=conference)
    return render(request, 'conference_detail.html', {'conference': conference, 'presentations': presentations})

def participant_detail(request, participant_id):
    participant = get_object_or_404(Participant, pk=participant_id)
    works = participant.works.all()
    return render(request, 'participant_detail.html', {'participant': participant, 'works': works})

def scientific_work_detail(request, work_id):
    work = get_object_or_404(ScientificWork, pk=work_id)
    return render(request, 'scientific_work_detail.html', {'work': work})

def work_list(request):
    works = ScientificWork.objects.all()
    return render(request, 'work_list.html', {'works': works})

# Searches
def search(request):
    author_lastname = request.GET.get('author_lastname')

    if author_lastname is not None:
        works = ScientificWork.objects.filter(authors__contains=author_lastname)
    else:
        works = ScientificWork.objects.all()  

    return render(request, 'work_list.html', {'works': works})

def search_by_title(request):
    work_title = request.GET.get('work_title')

    if work_title:
        works = ScientificWork.objects.filter(title__icontains=work_title)
    else:
        works = ScientificWork.objects.all()

    return render(request, 'work_list.html', {'works': works})

def search_by_participant(request):
    participant_name = request.GET.get('participant_name')

    if participant_name:
        participants = Participant.objects.filter(
            first_name__icontains=participant_name
        ) | Participant.objects.filter(
            last_name__icontains=participant_name
        )
        works = ScientificWork.objects.filter(participants__in=participants).distinct()
    else:
        works = ScientificWork.objects.all()

    return render(request, 'work_list.html', {'works': works})

# Participant views
def participant_list(request):
    participants = Participant.objects.all()
    return render(request, 'participant_list.html', {'participants': participants})

def participants_detail(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    return render(request, 'participants_detail.html', {'participant': participant})

def participant_create(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('participant_list')
    else:
        form = ParticipantForm()
    return render(request, 'participant_form.html', {'form': form})

def participant_update(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    if request.method == 'POST':
        form = ParticipantForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            return redirect('participant_list')
    else:
        form = ParticipantForm(instance=participant)
    return render(request, 'participant_form.html', {'form': form})

def participant_delete(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    if request.method == 'POST':
        participant.delete()
        return redirect('participant_list')
    return render(request, 'participant_confirm_delete.html', {'participant': participant})


# ScientificWork views
def scientificwork_list(request):
    scientificworks = ScientificWork.objects.all()
    return render(request, 'scientificwork_list.html', {'scientificworks': scientificworks})

def scientificwork_detail(request, pk):
    scientificwork = get_object_or_404(ScientificWork, pk=pk)
    return render(request, 'scientificwork_detail.html', {'scientificwork': scientificwork})

def scientificwork_create(request):
    if request.method == 'POST':
        form = ScientificWorkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('scientificwork_list')
    else:
        form = ScientificWorkForm()
    return render(request, 'scientificwork_form.html', {'form': form})

def scientificwork_update(request, pk):
    scientificwork = get_object_or_404(ScientificWork, pk=pk)
    if request.method == 'POST':
        form = ScientificWorkForm(request.POST, instance=scientificwork)
        if form.is_valid():
            form.save()
            return redirect('scientificwork_list')
    else:
        form = ScientificWorkForm(instance=scientificwork)
    return render(request, 'scientificwork_form.html', {'form': form})

def scientificwork_delete(request, pk):
    scientificwork = get_object_or_404(ScientificWork, pk=pk)
    if request.method == 'POST':
        scientificwork.delete()
        return redirect('scientificwork_list')
    return render(request, 'scientificwork_confirm_delete.html', {'scientificwork': scientificwork})
