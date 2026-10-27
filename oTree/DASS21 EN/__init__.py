from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Quiz3'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    def make_field(label):
        return models.IntegerField(
            choices= (1,2,3,4),
            label=label, widget=widgets.RadioSelectHorizontal
        )

    DASS21_1 = make_field(label="")
    DASS21_2 = make_field(label="")
    DASS21_3 = make_field(label="")
    DASS21_4 = make_field(label="")
    DASS21_5 = make_field(label="")
    DASS21_6 = make_field(label="")
    DASS21_7 = make_field(label="")
    DASS21_8 = make_field(label="")
    DASS21_9 = make_field(label="")
    DASS21_10 = make_field(label="")
    DASS21_11 = make_field(label="")
    DASS21_12 = make_field(label="")
    DASS21_13 = make_field(label="")
    DASS21_14 = make_field(label="")
    DASS21_15 = make_field(label="")
    DASS21_16 = make_field(label="")
    DASS21_17 = make_field(label="")
    DASS21_18 = make_field(label="")
    DASS21_19 = make_field(label="")
    DASS21_20 = make_field(label="")
    DASS21_21 = make_field(label="")

    depression = models.StringField()

    anxiety = models.StringField()

    stress = models.StringField()

    def depression_score(player):
        if player.DASS21_3 + player.DASS21_5 + player.DASS21_10 + player.DASS21_13 + player.DASS21_16 + player.DASS21_17 + player.DASS21_21 <= 9 :
            player.depression = 'Normal'

        elif player.DASS21_3 + player.DASS21_5 + player.DASS21_10 + player.DASS21_13 + player.DASS21_16 + player.DASS21_17 + player.DASS21_21 >9 and player.DASS21_3 + player.DASS21_5 + player.DASS21_10 + player.DASS21_13 + player.DASS21_16 + player.DASS21_17 + player.DASS21_21 <14 :
            player.depression = 'Mild'

        elif player.DASS21_3 + player.DASS21_5 + player.DASS21_10 + player.DASS21_13 + player.DASS21_16 + player.DASS21_17 + player.DASS21_21 > 13 and player.DASS21_3 + player.DASS21_5 + player.DASS21_10 + player.DASS21_13 + player.DASS21_16 + player.DASS21_17 + player.DASS21_21 < 20:
            player.depression = 'Moderate'

        elif player.DASS21_3 + player.DASS21_5 + player.DASS21_10 + player.DASS21_13 + player.DASS21_16 + player.DASS21_17 + player.DASS21_21 > 20 and player.DASS21_3 + player.DASS21_5 + player.DASS21_10 + player.DASS21_13 + player.DASS21_16 + player.DASS21_17 + player.DASS21_21 < 28:
            player.depression = 'Severe'

        else:
            player.depression = 'Extremely Severe'

    def anxiety_score(player):
        if player.DASS21_2 + player.DASS21_4 + player.DASS21_7 + player.DASS21_9 + player.DASS21_15 + player.DASS21_19 + player.DASS21_20 <= 7:
            player.anxiety = 'Normal'

        elif player.DASS21_2 + player.DASS21_4 + player.DASS21_7 + player.DASS21_9 + player.DASS21_15 + player.DASS21_19 + player.DASS21_20 > 7 and player.DASS21_2 + player.DASS21_4 + player.DASS21_7 + player.DASS21_9 + player.DASS21_15 + player.DASS21_19 + player.DASS21_20 < 10:
            player.anxiety = 'Mild'

        elif player.DASS21_2 + player.DASS21_4 + player.DASS21_7 + player.DASS21_9 + player.DASS21_15 + player.DASS21_19 + player.DASS21_20 > 9 and player.DASS21_2 + player.DASS21_4 + player.DASS21_7 + player.DASS21_9 + player.DASS21_15 + player.DASS21_19 + player.DASS21_20 < 15:
            player.anxiety = 'Moderate'

        elif player.DASS21_2 + player.DASS21_4 + player.DASS21_7 + player.DASS21_9 + player.DASS21_15 + player.DASS21_19 + player.DASS21_20 > 14 and player.DASS21_2 + player.DASS21_4 + player.DASS21_7 + player.DASS21_9 + player.DASS21_15 + player.DASS21_19 + player.DASS21_20 < 20:
            player.anxiety = 'Severe'

        else:
            player.anxiety = 'Extremely Severe'

    def stress_score(player):
        if player.DASS21_1 + player.DASS21_6 + player.DASS21_8 + player.DASS21_11 + player.DASS21_12 + player.DASS21_14 + player.DASS21_18 <= 14:
            player.stress = 'Normal'

        elif player.DASS21_1 + player.DASS21_6 + player.DASS21_8 + player.DASS21_11 + player.DASS21_12 + player.DASS21_14 + player.DASS21_18 > 14 and player.DASS21_1 + player.DASS21_6 + player.DASS21_8 + player.DASS21_11 + player.DASS21_12 + player.DASS21_14 + player.DASS21_18 < 19:
            player.stress = 'Mild'

        elif player.DASS21_1 + player.DASS21_6 + player.DASS21_8 + player.DASS21_11 + player.DASS21_12 + player.DASS21_14 + player.DASS21_18 > 18 and player.DASS21_1 + player.DASS21_6 + player.DASS21_8 + player.DASS21_11 + player.DASS21_12 + player.DASS21_14 + player.DASS21_18 < 26:
            player.stress = 'Moderate'

        elif player.DASS21_2 + player.DASS21_4 + player.DASS21_7 + player.DASS21_9 + player.DASS21_15 + player.DASS21_19 + player.DASS21_20 > 25 and player.DASS21_1 + player.DASS21_6 + player.DASS21_8 + player.DASS21_11 + player.DASS21_12 + player.DASS21_14 + player.DASS21_18 < 34:
            player.stress = 'Severe'

        else:
            player.stress = 'Extremely Severe'


# PAGES
class Quiz3(Page):

    form_model = "player"
    form_fields = ['DASS21_1','DASS21_2','DASS21_3','DASS21_4','DASS21_5','DASS21_6','DASS21_7',
                   'DASS21_8','DASS21_9','DASS21_10','DASS21_11','DASS21_12','DASS21_13','DASS21_14',
                   'DASS21_15','DASS21_16','DASS21_17','DASS21_18','DASS21_19','DASS21_20','DASS21_21',]


    @staticmethod
    def before_next_page(player, timeout_happened):
        player.depression_score(),
        player.anxiety_score(),
        player.stress_score(),


page_sequence = [Quiz3]
