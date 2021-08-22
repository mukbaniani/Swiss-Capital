from django.core.management import BaseCommand
from faker import Faker
from ...models import Employee, Department, PersonalQuality
import random
from django.utils import timezone


class Command(BaseCommand):
    help = "create employee"

    def handle(self, *args, **options):
        faker = Faker(["ka_GE"])
        timezone_now = timezone.now()
        for _ in range(10):
            em = Employee(
                first_name=faker.unique.first_name(),
                last_name=faker.unique.last_name(),
                citizenship=faker.unique.country(),
                gender="მ",
                person_number=random.randint(11111111111, 999999999999),
                date_of_birth=timezone_now,
                date_expiry=timezone_now,
                card_number=random.randint(11111111111, 999999999999),
                place_of_birth=faker.unique.city(),
                date_of_issue=timezone_now,
                issueing_authority="იუსტიციის სახლი",
                department_id=Department.objects.order_by("?").first(),
            )
            em.save()
            em.personal_quality.add(PersonalQuality.objects.order_by("?").first())
