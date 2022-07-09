
import json

from django.core.management.base import BaseCommand, CommandError
from card_database.models import Card



class Command(BaseCommand):
    help = 'Add cards to DB from a json file.'

    def add_arguments(self, parser):
        parser.add_argument('json_file', nargs='+', type=str)

    def handle(self, *args, **options):
        with open(options['json_file'][0]) as f:
            data = json.load(f)
            try:
                for card in data:
                    Card.objects.create(
                        card_number=card['cardNumber'],
                        card_name=card['cardName'],
                        card_text=card['cardText'],
                        thumbnail=card['thumbnail'],
                        color=card['color'].replace(';',' '),
                        card_type=card['cardType'],
                        energy_cost=card['energyCost'],
                        special_trait=card['specialTrait'],
                        power_card=card['power'],
                        combo_power=card['comboPower'],
                        combo_energy=card['comboEnergy'],
                        era=card['era'],
                        card_character=card['cardCharacter'],
                        card_url=card['url'],
                        card_limit=card['cardLimit'],
                        is_ultimate=card['isUltimate'],
                        is_super_combo=card['isSuperCombo'],
                        is_dragon_ball=card['isDragonBall']
                    )
            except Exception as err:
                raise CommandError(f'ERR: {err}')

            self.stdout.write(self.style.SUCCESS('Successfully Added CARDS!'))