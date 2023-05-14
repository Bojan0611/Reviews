from django import forms

from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(max_length=30,
#                                 label="Your Name",
#                                 error_messages={
#                                     "required": "Your name must not be empty!",
#                                     "max_length": "Please enter shorter name!",
#                                 })
#     review_text = forms.CharField(label="Your Feedback",
#                                   max_length=250,
#                                   widget=forms.Textarea)
#     rating = forms.IntegerField(label="Your Rating",
#                                 min_value=1,
#                                 max_value=5)
    
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        # exclude - i tu lista tego oprócz czego wszystko powinno byc
        labels = {
            "user_name": "Your Name",
            "review_text": "Your Feedback",
            "rating": "Your Rating" 
        }
        error_messages = {
            "user_name": {
                            "required": "Your name must not be empty!",
                            "max_length": "Please enter shorter name!",
                        },
        }