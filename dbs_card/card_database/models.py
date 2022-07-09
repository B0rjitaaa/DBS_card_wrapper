from django.db import models

COLORS = [
    ('Red', 'Red'),
    ('Blue', 'Blue'),
    ('Green', 'Green'),
    ('Black', 'Black'),
    ('Yellow', 'Yellow'),
    ('Green/Yellow', 'Green and Yellow'),
    ('Green/Red', 'Green and Red'),
    ('GreenYellow', 'Green and Yellow'),
    ('Blue/Yellow', 'Blue and Yellow'),
    ('Blue/Green', 'Blue and Green'),
    ('Red/Yellow', 'Red and Yellow'),
    ('Red/Blue', 'Red and Blue'),
]

CARD_TYPES = [
    ('Battle', 'Battle Card'),
    ('Unison', 'Unison Card'),
    ('Extra', 'Extra Card'),
    ('Leader', 'Leader Card'),
]


class Card(models.Model):
    card_number = models.CharField(max_length=20)
    card_name = models.CharField(max_length=50)
    card_text = models.TextField()
    thumbnail =  models.URLField()
    color =  models.CharField(max_length=50, choices=COLORS)
    card_type = models.CharField(max_length=50, choices=CARD_TYPES)
    energy_cost =  models.CharField(max_length=50)
    special_trait =  models.CharField(max_length=50)
    power_card =  models.CharField(max_length=50)
    combo_power =  models.IntegerField()
    combo_energy =  models.IntegerField()
    era =  models.CharField(max_length=50)
    card_character =  models.CharField(max_length=50)
    card_url =  models.URLField()
    card_limit =  models.IntegerField()
    is_ultimate = models.IntegerField(default=0)
    is_super_combo = models.IntegerField(default=0)
    is_dragon_ball = models.IntegerField(default=0)
    card_limit = models.IntegerField()

    class Meta:
        ordering = ['card_number']

    def __str__(self):
        return f"{self.card_number}: {self.card_name}"