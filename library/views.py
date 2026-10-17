from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Student, IssueBook
from .forms import BookForm, StudentForm, IssueBookForm
from django.utils import timezone


def home(request):
    return render(request, 'library/home.html')


def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})


def add_book(request):
    form = BookForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('book_list')

    return render(request, 'library/book_form.html', {'form': form})


def edit_book(request, id):
    book = get_object_or_404(Book, id=id)
    form = BookForm(request.POST or None, instance=book)

    if form.is_valid():
        form.save()
        return redirect('book_list')

    return render(request, 'library/book_form.html', {'form': form})


def delete_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book.delete()
        return redirect('book_list')

    return render(request, 'library/delete.html', {'item': book})


def student_list(request):
    students = Student.objects.all()
    return render(request, 'library/student_list.html', {'students': students})


def add_student(request):
    form = StudentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('student_list')

    return render(request, 'library/student_form.html', {'form': form})


def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(request.POST or None, instance=student)

    if form.is_valid():
        form.save()
        return redirect('student_list')

    return render(request, 'library/student_form.html', {'form': form})


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request, 'library/delete.html', {'item': student})

# Issue Book Views

def issue_list(request):
    issues = IssueBook.objects.select_related(
        'book', 'student'
    ).all()

    return render(
        request,
        'library/issue_list.html',
        {'issues': issues}
    )


def issue_book(request):
    form = IssueBookForm(request.POST or None)

    if form.is_valid():
        issue = form.save(commit=False)

        if issue.status == 'Issued':
            if issue.book.quantity > 0:
                issue.book.quantity -= 1
                issue.book.save()
                issue.save()

                return redirect('issue_list')
            else:
                form.add_error('book', 'Book is not available.')

        else:
            issue.save()
            return redirect('issue_list')

    return render(
        request,
        'library/issue_form.html',
        {'form': form}
    )


def return_book(request, id):
    issue = get_object_or_404(IssueBook, id=id)

    if request.method == 'POST':
        if issue.status == 'Issued':
            issue.status = 'Returned'
            issue.return_date = timezone.localdate()
            issue.book.quantity += 1

            issue.book.save()
            issue.save()

        return redirect('issue_list')

    return redirect('issue_list')