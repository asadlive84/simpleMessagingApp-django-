from django import forms
from .models import Comment


class CommentReplyForm(forms.Form):
    model=Comment
    filelds = ['comment']

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
