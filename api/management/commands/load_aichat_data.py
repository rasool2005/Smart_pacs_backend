from django.core.management.base import BaseCommand
from api.models import AIChat
from api.data import qa_data


class Command(BaseCommand):
    help = 'Load initial AI chat data from data.py'

    def handle(self, *args, **options):
        # Clear existing data if needed
        AIChat.objects.all().delete()

        # Load data from qa_data
        for item in qa_data:
            AIChat.objects.create(
                question=item["question"],
                answer=item["answer"]
            )
            self.stdout.write(
                self.style.SUCCESS(f'Added: {item["question"]}')
            )

        self.stdout.write(
            self.style.SUCCESS('✓ AI Chat data loaded successfully!')
        )
