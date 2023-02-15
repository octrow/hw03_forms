from django.core.paginator import Paginator


def paginate_posts(post_list, request):
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get("page")
    return paginator.get_page(page_number)
