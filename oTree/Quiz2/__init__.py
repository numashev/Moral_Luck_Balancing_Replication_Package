from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Quiz2'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    def make_field(label):
        return models.IntegerField(
            choices=(1,2,3,4,5),
            label=label, widget=widgets.RadioSelectHorizontal
        )

    Quiz2_1 = make_field(label="")
    Quiz2_2 = make_field(label="")
    Quiz2_3 = make_field(label="")
    Quiz2_4 = make_field(label="")
    Quiz2_5 = make_field(label="")
    Quiz2_6 = make_field(label="")
    Quiz2_7 = make_field(label="")
    Quiz2_8 = make_field(label="")
    Quiz2_9 = make_field(label="")
    Quiz2_10 = make_field(label="")




# PAGES
class Quiz2(Page):

    form_model = "player"
    form_fields = ['Quiz2_1', 'Quiz2_2','Quiz2_3','Quiz2_4', 'Quiz2_5', 'Quiz2_6', 'Quiz2_7', 'Quiz2_8', 'Quiz2_9','Quiz2_10']


page_sequence = [Quiz2]
