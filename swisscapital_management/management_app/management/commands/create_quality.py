from django.core.management import BaseCommand
from ...models import PersonalQuality


class Command(BaseCommand):
    help = "create personal quality"

    def handle(self, *args, **options):
        personal_quality = [
            "კომუნიკაბელური",
            "პუნქტუალური",
            "ზარმაცი",
            "პასუხისმგებლიანი",
        ]
        for quality in personal_quality:
            PersonalQuality.objects.create(quality=quality)
