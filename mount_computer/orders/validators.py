from django.core.exceptions import ValidationError

def validate_cpu(value):
    if value.objects.get():
        print(value)
        raise ValidationError("error")
    else:
        return value