from django.utils.timezone import localtime, now


def get_duration(visit):
    entered_at = visit.entered_at
    leaved_at = visit.leaved_at if visit.leaved_at else localtime(now())
    duration = leaved_at - entered_at
    return duration
