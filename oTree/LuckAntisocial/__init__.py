import random
from otree.api import *

doc = """
Part 1: Subjects will receive a lottery ticket with a number between 1 and 180. The number on subjects lottery ticket will decide how much subjects receive.
Part 2: The charity Feed the Children is provided with $3.00 and subjects must decide how much of this you would like to take from the charity.
Part 3: Subjects are asked to assess hypothetical actions that might be completed by other participants in an experiment.
"""


class C(BaseConstants):
    NAME_IN_URL = 'MBE5'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    PROBABILITY = 0.5


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    #modify ticket earnings
    payoffLuck = models.CurrencyField(initial=3.00)

    #modify ticket min and max
    ticket = models.IntegerField(min =152,max= 180)

    prolific_id = models.StringField(default=str(" "))

    payoffCharity = models.CurrencyField()

    orderSNE = models.IntegerField()

    random_value = models.FloatField()

    amount_take = models.CurrencyField(min =0,max=3 , label='')

    #ticket draw
    @staticmethod
    def compute_ticket(player):
        player.ticket = random.randint(152, 180)


    #random order part3(SNE)
    def set_orderSNE(player):
        import random
        player.random_value = random.random()
        player.orderSNE = 1 if player.random_value <= C.PROBABILITY else 2


    def set_payoffCharity(player):
        player.payoffCharity = cu(player.amount_take)

    def set_payoff(player):
        player.payoff = player.payoffCharity + player.payoffLuck

    def make_field(label):
        return models.IntegerField(
            choices=(1,2,3,4,5,6),
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


class Partie1_Instructions(Page):

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.compute_ticket(player),

class Partie1(Page):

    def vars_for_template(player: Player):
        participant = player.participant
        participant.ticket = player.ticket
        participant.payoffLuck = player.payoffLuck

        return dict(draw=participant.ticket,
                    payoffLuck=participant.payoffLuck)


    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.prolific_id = player.participant.label
        player.set_orderSNE(),


class Decision2(Page):

    form_model = 'player'
    form_fields = ['amount_take']

    @staticmethod
    def vars_for_template(player):
        participant = player.participant
        participant.payoffLuck = player.payoffLuck

        return dict(payoffLuck=participant.payoffLuck)

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.set_payoffCharity(),


class SNE(Page):

    form_model = "player"
    form_fields = ['SNE_1', 'SNE_2','SNE_3','SNE_4', 'SNE_5', 'SNE_6', 'SNE_7',
                  'SNE_8', 'SNE_9','SNE_10','SNE_11','SNE_12','SNE_13','SNE_14']

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        participant.payoffCharity = player.payoffCharity
        participant.amount_take = player.amount_take
        participant.payoffLuck = player.payoffLuck

        return dict(payoffCharity=participant.payoffCharity, amount_take=participant.amount_take, payoffLuck=participant.payoffLuck)

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.set_payoff(),


page_sequence = [General_instructions, Partie1_Instructions, Partie1, Decision2, SNE]
