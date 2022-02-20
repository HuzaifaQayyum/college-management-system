from datetime import datetime


def do_conversion(term, func, *args, **kwargs):
    try:
        return func(term, *args, **kwargs)
    except:
        return None

def search_by_int(queryset, search_term, get_filter):
    cleaned_term = do_conversion(search_term, int)
    if cleaned_term:
        queryset |= queryset.filter(**get_filter(cleaned_term))

    return queryset


def search_by_date(queryset, search_term, get_filter, date_format='%b %Y'):
    cleaned_term = do_conversion(search_term, datetime.strptime, date_format)
    if cleaned_term:
        queryset |= queryset.filter(**get_filter(cleaned_term))

    return queryset