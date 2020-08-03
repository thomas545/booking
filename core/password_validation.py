import re
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class UpperCaseValidatior:
    def validate(self, password, user=None):
        if not re.search("[A-Z]", password):
            raise ValidationError(
                _("The password must contain at least 1 uppercase letter, A-Z."),
                code="No Upper",
            )

    def get_help_text(self):
        return _("Your password must contain at least 1 uppercase letter, A-Z.")


class LowerCaseValidation:
    def validate(self, password, user=None):
        if re.search("[a-z]", password) is None:
            raise ValidationError(
                _("The password must contain at least 1 lowercase letter, a-z."),
                code="No Lower",
            )

    def get_help_text(self):
        return _("Your password must contain at least 1 lowercase letter, a-z.")

