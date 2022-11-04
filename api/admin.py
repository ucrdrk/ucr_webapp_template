from django.contrib import admin
from api.models import Foo
from account.models import User

admin.site.register(Foo)
admin.site.register(User)
