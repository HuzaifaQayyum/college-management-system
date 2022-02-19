from django.core.validators import MinValueValidator, MaxValueValidator

CONSTANCE_IGNORE_ADMIN_VERSION_CHECK = True
CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'


CONSTANCE_ADDITIONAL_FIELDS = {
    'passing_percentage': ['django.forms.fields.IntegerField', {
        'validators': [ MinValueValidator(1, 'percentage must be minimun 1.'), MaxValueValidator(100, 'percentage can be upto 100.') ]
    }],
}

CONSTANCE_CONFIG = {
    'PASSING_PERCENTAGE': (25, 'Minimum percentage to pass the quiz', 'passing_percentage'),
}

CONSTANCE_CONFIG_FIELDSETS = {
    'Quiz': [ 'PASSING_PERCENTAGE' ]
}