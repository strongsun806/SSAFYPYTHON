from django.forms import ModelForm
from .models import Article

# Model을 이용해서 사용자에게 입력받을 Form을 만들어줌

class ArticleForm(ModelForm):
    #나는 Article 모델을 기준으로 만들어줘~

    class Meta:
        model = Article
        fields = ('title','content',)
        # fields = '__all__'