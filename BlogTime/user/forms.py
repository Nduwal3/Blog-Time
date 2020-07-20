from django.forms import ModelForm


class MODELNAMEForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = MODELNAME
        fields = ('',)
