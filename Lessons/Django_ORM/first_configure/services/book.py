from typing import List

from db.models import Book


# Retrieve list
def get_books(format_id: int = None,
              authors_ids: List[int] = None
              ):
    queryset = Book.objects.all()
    if format_id is not None:
        queryset = queryset.filter(format_id=format_id)
    if authors_ids is not None:
        queryset = queryset.filter(authors__id__in = authors_ids)
    return queryset


# create
def create_book(
        title: str,
        price: float,
        format_id: int,
        authors_ids: List[int] = None
):
    new_book = Book.objects.create(
        title=title,
        price=price,
        format_id=format_id,
    )
    if authors_ids:
        new_book.authors.set(authors_ids)

    return new_book
