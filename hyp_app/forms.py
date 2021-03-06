from django import forms
from .models import User, Login, Peripheral, Cycle, Broker


class LoginForm(forms.ModelForm):

    class Meta:
        model = Login
        fields = ('email', 'passwd')


    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class' : 'form-control'})
        self.fields['passwd'].widget.attrs.update({'class' : 'form-control'})


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('name','email', 'passwd')


    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class' : 'form-control'})        
        self.fields['email'].widget.attrs.update({'class' : 'form-control'})
        self.fields['passwd'].widget.attrs.update({'class' : 'form-control'})

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
        self.fields['description'].widget.attrs.update({'rows' : '5'})        
        self.fields['is_activated'].widget.attrs.update({'class' : 'form-control'})
        self.fields['last_record'].widget.attrs.update({'class' : 'form-control'})
        self.fields['last_record_state'].widget.attrs.update({'class' : 'form-control'})
        self.fields['data_metric'].widget.attrs.update({'class' : 'form-control'})
        #self.fields['sensor_photo'] = widget.attrs.update({'class' : 'form-control'})


class CycleForm(forms.ModelForm):

    class Meta:
        model = Cycle
        fields = ('title', 'actuador_id', 'is_activated', 'start_time', 'end_time', 'start_cycle', 'end_cycle');

    def __init__(self, *args, **kwargs):
        super(CycleForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class' : 'form-control'})
        result = Peripheral.objects.filter(type_peripheral='atuador').values_list('peripheral_id','name')
        self.fields['actuador_id'].widget.choices = result
        self.fields['actuador_id'].widget.attrs.update({'class' : 'form-control'})
        self.fields['is_activated'].widget.attrs.update({'class' : 'form-control'})
        self.fields['start_time'].widget.attrs.update({'class' : 'form-control'})
        self.fields['end_time'].widget.attrs.update({'class' : 'form-control'})
        self.fields['start_cycle'].widget.attrs.update({'class' : 'form-control'})
        self.fields['end_cycle'].widget.attrs.update({'class' : 'form-control'})


class BrokerForm(forms.ModelForm):

    class Meta:
        model = Broker
        fields = ('name', 'port', 'keep_alive', 'user_name', 'passwd', 'is_activated');

    def __init__(self, *args, **kwargs):
        super(BrokerForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['port'].widget.attrs.update({'class' : 'form-control'})
        self.fields['keep_alive'].widget.attrs.update({'class' : 'form-control'})
        self.fields['user_name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['passwd'].widget.attrs.update({'class' : 'form-control'})
        self.fields['is_activated'].widget.attrs.update({'class' : 'form-control'}) 