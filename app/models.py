from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


# Create your models here.

def validate_file_size(file):
    size = file.size
    if size < 3000:
        raise ValidationError(
            ("The %(name)s file size must be greater than 3000 Bytes. But your file size is %(size)s Bytes."),
                params={"name": file.name, 'size': size}
        )
    else:
        return file

def fnc(value):
    if len(value) <= 5:
        raise ValidationError(
            _("The %(value)s length must be greater than 5!"),
            params={"value": value},
        )
    else:
        return value


class UserFile(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False, validators=[fnc])
    file = models.FileField(upload_to='files', validators=[validate_file_size])

    def __str__(self):
        return self.name.title()
    
    # def clean(self):
    #     super(UserFile, self).clean()

    #     if len(self.name) < 10:
    #         raise ValidationError(
    #             _("%(value)s length must be greater than 10!"),
    #             params={"value": self.name},
    #         )
    #     size = self.file.size
    #     if size < 3000:
    #         raise ValidationError(
    #             _("%(value)s file size must be greater than 3000 Bytes. But your file size is %(size)s Bytes."),
    #             params={"value": self.file.name, 'size': size},
    #         )

        

