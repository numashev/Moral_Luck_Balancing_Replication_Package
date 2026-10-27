from otree.api import *
import datetime
doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Consent'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    refus, accept = 0,1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    participate = models.IntegerField(
        choices=[(0, 'I agree'), (1, 'I desagree')]
        , widget=widgets.RadioSelectHorizontal)

# PAGES
class Welcome(Page):
    form_model = 'player'
    form_fields = ['participate']


class End(Page):
    def is_displayed(player: Player):
        return player.participate == 0


page_sequence = [Welcome, End]
