from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator, RegexValidator
from PIL import Image


GENDER_CHOICE = (("მ", "კაცი"), ("ქ", "ქალი"))
INCORRECT_PASSPORT_LENGTH = _("პირადობა უნდა შეიცავდეს მხოლოდ 11 ციფრს")
PERSON_NUMBER_LENGTH = 11
INCORRECT_CARD_NUMBER_LENGTH = _("ბარათის ნომერი უნდა შეიცავდეს 9 სიმბოლოს")
REGEX_RULE = "^[0-9]*$"
REGEX_CARD_NUMBER = "^[0-9]{2}[A-Z]{2}[0-9]{5}$"
CARD_NUMBER_LENGTH = 9
INCORRECT_CARD_NUMBER_FORMAT = _(
    "არასწორი ფორმატი ბარათი უნდა შეიცავდეს 2 ციფრს შემდეგ 2 დიდ ლათინურ ასოს და ბოლოს 5 ციფრს"
)


class Department(models.Model):
    department_name = models.CharField(
        max_length=25, verbose_name=_("დეპარტამენტის სახელი")
    )

    class Meta:
        ordering = ["-id"]
        verbose_name = _("დეპარტამენტები")

    def __str__(self):
        return f"{self.department_name}"


class PersonalQuality(models.Model):
    quality = models.CharField(max_length=25, verbose_name=_("პიროვნული თვისებები"))

    class Meta:
        ordering = ["-id"]
        verbose_name = _("პიროვნული თვისებები")

    def __str__(self):
        return f"{self.quality}"


class Employee(models.Model):
    first_name = models.CharField(max_length=15, verbose_name=_("სახელი"))
    last_name = models.CharField(max_length=20, verbose_name=_("გვარი"))
    citizenship = models.CharField(max_length=20, verbose_name=_("მოქალაქეობა"))
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICE, verbose_name=_("სქესი")
    )
    person_number = models.CharField(
        max_length=11,
        validators=[
            MinLengthValidator(
                limit_value=PERSON_NUMBER_LENGTH, message=INCORRECT_PASSPORT_LENGTH
            ),
            RegexValidator(regex=REGEX_RULE, message=INCORRECT_PASSPORT_LENGTH),
        ],
        unique=True,
        help_text=_("შეიყვანეთ მცოლოდ 11 ციფრი"),
        verbose_name=_("პირადი ნომერი"),
    )
    date_of_birth = models.DateField(
        verbose_name=_("დაბადების თარიღი"),
    )
    date_expiry = models.DateField(
        verbose_name=_("მოქმედების ვადა"),
    )
    card_number = models.CharField(
        max_length=9,
        validators=[
            MinLengthValidator(
                limit_value=CARD_NUMBER_LENGTH, message=INCORRECT_CARD_NUMBER_LENGTH
            ),
            RegexValidator(
                regex=REGEX_CARD_NUMBER, message=INCORRECT_CARD_NUMBER_FORMAT
            ),
        ],
        unique=True,
        help_text=_("2 ციფრი -> 2 დიდი ლათინური ასო -> 5 ციფრი მაგ. 11AB11111"),
        verbose_name=_("ბარათის ნომერი"),
    )
    image = models.ImageField(
        verbose_name=_("სურათი"), upload_to="images", default="default.jpg"
    )
    place_of_birth = models.CharField(max_length=15, verbose_name=_("დაბადების ადგილი"))
    date_of_issue = models.DateField(
        verbose_name=_("გაცემის თარიღი"),
    )
    issueing_authority = models.CharField(
        max_length=20, verbose_name=_("გამცემი ორგანი")
    )
    department_id = models.ForeignKey(
        Department, on_delete=models.CASCADE, verbose_name=_("დეპარტამენტი")
    )
    personal_quality = models.ManyToManyField(
        PersonalQuality, verbose_name=_("პიროვნული თვისებები")
    )

    class Meta:
        ordering = ["-id"]
        verbose_name = _("თანამშრომლები")

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 100 or img.width > 100:
            output_size = (100, 100)
            img.thumbnail(output_size)
            img.save(self.image.path)
