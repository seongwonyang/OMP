from .common import *

@login_required
def BookRegisterView(request):
    if request.method == "GET":
        return render(request, 'book_register.html')

    elif request.method == "POST":
        book_name = request.POST.get('book_name')
        book_isbn = request.POST.get('book_isbn')
        author = request.POST.get('author')
        publisher = request.POST.get('publisher')

        execute("INSERT INTO book(isbn, book_name, author, publisher) "+
                "VALUES ((%s), (%s), (%s), (%s))", (book_isbn, book_name, author, publisher,))

        return redirect('seller:main')