from django import forms
from .models import Task, Tag
from datetime import datetime, date


class TaskForm(forms.ModelForm):
    time_created = forms.TimeField(
        label="Time created",
        required=True,
        widget=forms.TimeInput(format="%H:%M", attrs={"type": "time"}),
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "tags", "is_done"]
        widgets = {
            "deadline": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "tags": forms.CheckboxSelectMultiple(),
        }

    def save(self, commit=True):
        task = super().save(commit=False)
        entered_time = self.cleaned_data["time_created"]
        today = date.today()
        created_dt = datetime.combine(today, entered_time)

        task.created_at = created_dt

        if commit:
            task.save()
            self.save_m2m()
        return task


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
