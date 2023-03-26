from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField(max_length=30,
                                label="Your name",
                                error_messages={
                                    "required": "Your name must not be empty!",
                                    "max_length": "Please enter shorter name!",
                                })
    