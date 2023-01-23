from django import forms
from django.contrib import admin

class MyModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        status = request.GET.get('status')
        if status == 'active':
            return MyModel.objects.filter(is_active=True)
        elif status == 'inactive':
            return MyModel.objects.filter(is_active=False)
        else:
            return MyModel.objects.all()

    class StatusFilterForm(forms.Form):
        status = forms.ChoiceField(choices=[('', 'All'), ('active', 'Active'), ('inactive', 'Inactive')])
    
    def changelist_view(self, request, extra_context=None):
        form = self.StatusFilterForm(request.GET)
        extra_context = extra_context or {}
        extra_context['form'] = form
        return super().changelist_view(request, extra_context=extra_context)

