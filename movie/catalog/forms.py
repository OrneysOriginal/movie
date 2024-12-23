from django import forms
from catalog.validators import (
    validate_space_len_comment,
    validate_length_comment,
)


class CommentForm(forms.Form):
    comment = forms.CharField(
        widget=forms.TextInput(),
        max_length=1023,
        validators=[validate_space_len_comment, validate_length_comment],
    )
