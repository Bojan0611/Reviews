from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from .forms import ReviewForm
from .models import Review

# Create your views here.

class ReviewView(CreateView):
    
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"

class ThankYouView(TemplateView):
    
    template_name = "reviews/thank_you.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works" 
        return context
    
    
class ReviewListView(ListView):
     
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"
    
    def get_queryset(self):
        base_query = super().get_queryset()
        return base_query.filter(rating__gte=1).order_by("rating")
    
class SingleReviewView(DetailView):
    
    template_name = "reviews/single_review.html"
    model = Review
    
class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        request.session["review_id"] = review_id
        return HttpResponseRedirect("/reviews/"+review_id)
        