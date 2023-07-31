from django.shortcuts import render
from django.utils.timezone import localtime

from datacenter.models import Visit
from .common_functions import get_duration


def format_duration(duration):
    hours, remainder = divmod(duration.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f'{hours:02}:{minutes:02}:{seconds:02}'


def storage_information_view(request):
    unclosed_visits = Visit.objects.filter(leaved_at__isnull=True)

    non_closed_visits = []
    for visit in unclosed_visits:
        duration = get_duration(visit)
        formatted_duration = format_duration(duration)
        visit_info = {
            'who_entered': visit.passcard.owner_name,
            'entered_at': localtime(visit.entered_at),
            'duration': formatted_duration,
        }
        non_closed_visits.append(visit_info)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
