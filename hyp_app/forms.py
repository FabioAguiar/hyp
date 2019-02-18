from django import forms

from .models import Peripheral


class PeripheralForm(forms.ModelForm):
    

    class Meta:
        model = Peripheral
        fields = ('name', 'technical_name', 'topic_base', 'type_peripheral','topic_name', 'specification', 'description', 'is_activated', 'mqtt_topic', 'last_record', 'last_record_state')

    #Inicia com a classe nos campos do formulário via Django, pois com JQuery há um delay na hora do carregamento da página.
    def __init__(self, *args, **kwargs):
        super(PeripheralForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['technical_name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['topic_base'].widget.attrs.update({'class' : 'form-control'})
        self.fields['type_peripheral'] = forms.ChoiceField(choices=(('sensor', 'Sensor'), ('atuador', 'Atuador')))
        self.fields['type_peripheral'].widget.attrs.update({'class' : 'form-control'})
        self.fields['topic_name'].widget.attrs.update({'class' : 'form-control'})        
        self.fields['specification'].widget.attrs.update({'class' : 'form-control'})
        self.fields['mqtt_topic'].widget.attrs.update({'class' : 'form-control'})
        self.fields['description'].widget.attrs.update({'class' : 'form-control'})
        self.fields['is_activated'].widget.attrs.update({'class' : 'form-control'})
        self.fields['last_record'].widget.attrs.update({'class' : 'form-control'})
        self.fields['last_record_state'].widget.attrs.update({'class' : 'form-control'})        
        #self.fields['sensor_photo'] = widget.attrs.update({'class' : 'form-control'})