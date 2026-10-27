from otree.api import *

doc = """
"""


class C(BaseConstants):
    NAME_IN_URL = 'MBE1'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    PROBABILITY = 0.5


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    payoffBsl = models.CurrencyField(initial=2.00)

    prolific_id = models.StringField(default=str(" "))

    payoffCharity = models.CurrencyField()

    orderSNE = models.IntegerField()

    random_value = models.FloatField()

    amount_give = models.CurrencyField(min=0, max=3, label='')


    def set_orderSNE(player):
        import random
        player.random_value = random.random()
        player.orderSNE = 1 if player.random_value <= C.PROBABILITY else 2


    def set_payoffCharity(player):
        player.payoffCharity = cu(3 - player.amount_give)

    def set_payoff(player):
        player.payoff = player.payoffCharity + player.payoffBsl

    def make_field(label):
        return models.IntegerField(
            choices=(1, 2, 3, 4, 5, 6),
            label=label, widget=widgets.RadioSelectHorizontal
        )

    SNE_1 = make_field(label="")
    SNE_2 = make_field(label="")
    SNE_3 = make_field(label="")
    SNE_4 = make_field(label="")
    SNE_5 = make_field(label="")
    SNE_6 = make_field(label="")
    SNE_7 = make_field(label="")

    SNE_8 = make_field(label="")
    SNE_9 = make_field(label="")
    SNE_10 = make_field(label="")
    SNE_11 = make_field(label="")
    SNE_12 = make_field(label="")
    SNE_13 = make_field(label="")
    SNE_14 = make_field(label="")


# PAGES
class General_instructions(Page):
    pass


class Decision1(Page):

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.prolific_id = player.participant.label
        player.set_orderSNE(),


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


class Decision2(Page):

    form_model = 'player'
    form_fields = ['amount_give']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.set_payoffCharity(),


class SNE(Page):

    form_model="player"
    form_fields =['SNE_1', 'SNE_2','SNE_3','SNE_4', 'SNE_5', 'SNE_6', 'SNE_7',
                  'SNE_8', 'SNE_9','SNE_10','SNE_11','SNE_12','SNE_13','SNE_14']

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        participant.payoffCharity = player.payoffCharity
        participant.amount_give = player.amount_give
        participant.payoffBsl = player.payoffBsl

        return dict(payoffCharity=participant.payoffCharity,
                    amount_give=participant.amount_give,
                    payoffBsl=participant.payoffBsl)

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.set_payoff(),


page_sequence = [General_instructions, Decision1, Decision2, SNE]
