from datetime import datetime


def do_conversion(term, func, *args, **kwargs):
    try:
        return func(term, *args, **kwargs)
    except:
        return None

def get_filter_method(queryset, model):
    return model.objects.filter if (queryset.count() == 0 and model) else queryset.filter

def search_by_int(queryset, search_term, get_filter, model=None):
    cleaned_term = do_conversion(search_term, int)
    if cleaned_term:
        queryset |= get_filter_method(queryset, model)(**get_filter(cleaned_term))

    return queryset


def search_by_date(queryset, search_term, get_filter, model=None, date_format='%b %Y'):
    cleaned_term = do_conversion(search_term, datetime.strptime, date_format)
    if cleaned_term:
        queryset |= get_filter_method(queryset, model)(**get_filter(cleaned_term))

    return queryset