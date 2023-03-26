from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField(max_length=30,
                                label="Your name",
                                error_messages={
                                    "required": "Your name must not be empty!",
                                    "max_length": "Please enter shorter name!",
                                })
    review_text = forms.CharField(label="Your Feedback",
                                  max_length=250,
                                  widget=forms.Textarea)
    rating = forms.IntegerField(label="Your rating",
                                min_value=1,
                                max_value=5)
    