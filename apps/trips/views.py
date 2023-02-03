from django.shortcuts import render
from .models import Trip , Expense 
from django.views import generic

# Create your views here.
def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    num_trips = Trip.objects.all().count()
    num_expenses = Expense.objects.all().count()
    num_travel_expenses = Expense.objects.filter(type_of_expense__exact='TR').count()


    return render(
        request,
        'index.html',
        context={
            'num_trips': num_trips, 'num_expenses': num_expenses, 'num_travel_expenses': num_travel_expenses
        },
    )
class ExpenseListView(generic.ListView):
    model = Expense

    # def get_queryset(self):
    #     return Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     # Get the blog from id and add it to the context
    #     context['some_data'] = 'This is just some data'
    #     return context
 
class TripListView(generic.ListView):
    model = Trip