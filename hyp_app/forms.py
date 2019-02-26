from django import forms
import django_filters
from operator import itemgetter
from .models import Peripheral, Cycle


class PeripheralForm(forms.ModelForm):

    class Meta:
        model = Peripheral
        fields = ('name', 'technical_name', 'topic_base', 'type_peripheral','topic_name', 'specification', 'description', 'is_activated', 'mqtt_topic', 'last_record', 'last_record_state', 'data_metric')

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
        self.fields['data_metric'].widget.attrs.update({'class' : 'form-control'})                 
        #self.fields['sensor_photo'] = widget.attrs.update({'class' : 'form-control'})


class CycleForm(forms.ModelForm):

    class Meta:
        model = Cycle
        fields = ('title', 'actuador_id', 'actuador_record_state', 'is_activated', 'start_cycle', 'end_cycle', 'start_permanence_cycle', 'end_permanence_cycle', 'total_permanence_cycle');

    def __init__(self, *args, **kwargs):
        super(CycleForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class' : 'form-control'})
        result = Peripheral.objects.filter(type_peripheral='atuador').values('peripheral_id','name')
        tuples = list(map(itemgetter('peripheral_id','name'), result))
        self.fields['actuador_id'] = forms.ChoiceField(choices=(tuples))
        self.fields['actuador_id'].widget.attrs.update({'class' : 'form-control'})
        self.fields['actuador_record_state'].widget.attrs.update({'class' : 'form-control'})
        self.fields['is_activated'].widget.attrs.update({'class' : 'form-control'})
        self.fields['start_cycle'].widget.attrs.update({'class' : 'form-control'})
        self.fields['end_cycle'].widget.attrs.update({'class' : 'form-control'})
        self.fields['start_permanence_cycle'].widget.attrs.update({'class' : 'form-control'})
        self.fields['end_permanence_cycle'].widget.attrs.update({'class' : 'form-control'})
        self.fields['total_permanence_cycle'].widget.attrs.update({'class' : 'form-control'})