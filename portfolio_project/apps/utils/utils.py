from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def paginator_use(request, list, num=3):
    page = request.GET.get('page', 1)

    paginator = Paginator(list, num)
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return list
