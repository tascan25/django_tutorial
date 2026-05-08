from django import forms
from .models import Reviews

# class ReviewForms(forms.Form):
#     user_name = forms.CharField(
#         label="Your Name",
#         required=True, 
#         max_length=50,
#         error_messages={
#             "required":'Your name is required, you cannot leave it empty',
#             "max_length":"please enter the shorter name"
#         }
#     )

#     review_text = forms.CharField(
#         label="Your Feedback", 
#         required=True,
#         max_length=200,
#         error_messages={
#             "required":"this field, is requried",
#             "max_length":"please donot enter the more than 200 characters"
#         },
#         widget=forms.Textarea
#     )

#     rating = forms.IntegerField(min_value=1, max_value=5)

class ReviewForms(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = "__all__"
        labels = {
            "user_name":"Your Name",
            "review_text": "Your Feedback", 
            "rating":"Your Rating",
        }
        error_messages = {
            "user_name":{
                "required":"this field is requried your feedback is valued here",
                "max_length":"this field should not exceed the max length"
            }, 
            "review_text":{
                "required":"This field is required, your feedback is valued here",
                "max_length":"this field should not exceed the max length"
            },
            "rating":{
                "required":"This field is required",
            }
        }