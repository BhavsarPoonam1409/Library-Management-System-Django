from django.db import models


class Book(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    isbn = models.CharField(max_length=20)
    quantity = models.IntegerField()

    def __str__(self):
        return self.book_name


class Student(models.Model):
    name = models.CharField(max_length=100)
    enrollment_no = models.CharField(max_length=20)
    course = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class IssueBook(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, default='Issued')

    def __str__(self):
        return self.book.book_name