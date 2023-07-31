from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime

from datetime import timedelta
from datacenter.models import Visit, Passcard
from .common_functions import get_duration


def is_visit_long(visit):
    duration = get_duration(visit)
    one_hour = timedelta(hours=1)
    return duration > one_hour


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    this_passcard_visits = Visit.objects.filter(passcard=passcard)

    for visit in this_passcard_visits:
        visit.entered_at = localtime(visit.entered_at)
        visit.duration = get_duration(visit)
        visit.is_strange = is_visit_long(visit)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits,
    }
    return render(request, 'passcard_info.html', context)
