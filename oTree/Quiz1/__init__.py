from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Quiz1'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    def make_field(label):
        return models.IntegerField(
            choices=(1,2,3,4,5)
                    ,
            label=label, widget=widgets.RadioSelectHorizontal
        )

    Quiz1_1 = make_field(label="")
    Quiz1_2 = make_field(label="")
    Quiz1_3 = make_field(label="")
    Quiz1_4 = make_field(label="")
    Quiz1_5 = make_field(label="")
    Quiz1_6 = make_field(label="")
    Quiz1_7 = make_field(label="")
    Quiz1_8 = make_field(label="")
    Quiz1_9 = make_field(label="")

    Quiz1_10 = make_field(label="")
    Quiz1_11 = make_field(label="")
    Quiz1_12 = make_field(label="")
    Quiz1_13 = make_field(label="")
    Quiz1_14 = make_field(label="")
    Quiz1_15 = make_field(label="")
    Quiz1_16 = make_field(label="")
    Quiz1_17 = make_field(label="")
    Quiz1_18 = make_field(label="")

    Quiz1_19 = make_field(label="")
    Quiz1_20 = make_field(label="")
    Quiz1_21 = make_field(label="")
    Quiz1_22 = make_field(label="")
    Quiz1_23 = make_field(label="")
    Quiz1_24 = make_field(label="")
    Quiz1_25 = make_field(label="")
    Quiz1_26 = make_field(label="")
    Quiz1_27 = make_field(label="")


# PAGES
class Quiz1(Page):

    form_model = "player"
    form_fields = ['Quiz1_1', 'Quiz1_2','Quiz1_3','Quiz1_4', 'Quiz1_5', 'Quiz1_6', 'Quiz1_7', 'Quiz1_8',
                   'Quiz1_9','Quiz1_10','Quiz1_11','Quiz1_12','Quiz1_13','Quiz1_14','Quiz1_15','Quiz1_16',
                   'Quiz1_17','Quiz1_18','Quiz1_19','Quiz1_20','Quiz1_21','Quiz1_22','Quiz1_23','Quiz1_24','Quiz1_25','Quiz1_26','Quiz1_27']


class Instructions(Page):
    pass




page_sequence = [Instructions, Quiz1]
