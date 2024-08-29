from django import forms


class CheckoutForm(forms.Form):
    payment_method_nonce = forms.CharField(max_length=1000,
                                           widget=forms.widgets.HiddenInput,
                                           required=False)

    def clean(self):
        self.cleaned_data = super().clean()
        # se estiver faltando o Braintree nonce
        if not self.cleaned_data.get('payment_method_nonce'):
            raise forms.ValidationError('Não foi possível verificar o pagamento')
        return self.cleaned_data
