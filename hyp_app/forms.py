from django import forms

from .models import Sensor


class SensorForm(forms.ModelForm):
    

    class Meta:
        model = Sensor
        fields = ('name', 'technical_name', 'type_signal', 'lib_code', 'description', 'is_activated', 'digital_ports_quant', 'analog_ports_quant', 'sensor_photo', 'sensor_document_1', 'sensor_document_2', 'sensor_document_3')  


    def __init__(self, *args, **kwargs):
        super(SensorForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['technical_name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['description'].widget.attrs.update({'class' : 'form-control'})
        self.fields['is_activated'].widget.attrs.update({'class' : 'form-control'})
        self.fields['type_signal'] = forms.ChoiceField(choices=(('DIG', 'Digital'), ('ANAL', 'Analógico'), ('ANALDIG', 'Analógico e Digital')))
        self.fields['type_signal'].widget.attrs.update({'class' : 'form-control'})
        self.fields['lib_code'] = forms.ChoiceField(choices=(('LM35', 'LM35'), ('DHT', 'DHT')))
        self.fields['lib_code'].widget.attrs.update({'class' : 'form-control'})
        self.fields['digital_ports_quant'] = forms.ChoiceField(choices=(('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')), widget=forms.RadioSelect())
        self.fields['analog_ports_quant'] = forms.ChoiceField(choices=(('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')), widget=forms.RadioSelect())
        #self.fields['sensor_photo'] = widget.attrs.update({'class' : 'form-control'})