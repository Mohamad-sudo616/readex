from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import get_object_or_404


from .models import Book


@login_required
def book_list(request):
    books = Book.objects.all()

    return render(
        request,
        "books/book_list.html",
        {
            "books": books,
        },
    )


@login_required
def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)

    return render(
        request,
        "books/book_detail.html",
        {
            "book": book,
        },
    )