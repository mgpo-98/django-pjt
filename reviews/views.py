from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review 


# Create your views here.
def index(request):
    reviews = Review.objects.all()
    context ={
        'reviews' : reviews
    }
    return render(request, 'reviews/index.html', context)

def create(request):
    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews:index')
    context = {
        "form" : form,
    }

    return render(request, 'reviews/create.html', context)
def detail(request, pk):
    review = Review.objects.get(pk=pk)
    context ={
        'review' : review
    }
    return render(request, 'reviews/detail.html',context)    
def update(request, pk):
    review = Review.objects.get(pk=pk)
    form = ReviewForm(instance=review)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance= review)
        if form.is_valid():
            form.save()
            return redirect('reviews:detail', review.pk)
    context = {
        'form' : form, 
    }
    return render(request, 'reviews/update.html', context)
def delete(request, pk):
    review = Review.objects.get(pk=pk)
    review.delete()
    return redirect('reviews:index')








