from django.forms import ModelForm
from .models import Url

URL_VALID_CHARS = list(r"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~:/?#[]@!$&'()*+,;=%")


class UrlForm(ModelForm):
    class Meta:
        model = Url
        fields = ['url']

    def clean(self):
        url = self.cleaned_data.get('url')
        if url == '' or url is None:
            self.add_error('url', 'Invalid URL')
        else:
            for ch in url:
                if ch not in URL_VALID_CHARS:
                    self.add_error('url', 'Invalid URL')
                    break

        return self.cleaned_data
