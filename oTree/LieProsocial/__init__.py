from otree.api import *


doc = """
Part 1: Subjects are allocated one of six possible endowments based on a privately rolled six-sided dice.
Part 2: Subjects are provided with $3.00 and must decide how much of this you would like to give to the charity Feed the Children
Part 3: Subjects are asked to assess hypothetical actions that might be completed by other participants in an experiment.
"""


class C(BaseConstants):
    NAME_IN_URL = 'MBE3'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    PROBABILITY = 0.5


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    prolific_id = models.StringField(default=str(" "))

    FirstDice = models.IntegerField(min=1, max=6)

    SecondDice = models.IntegerField(min=1, max=6)

    SumDice = models.IntegerField()

    payoffDice = models.CurrencyField()
    payoffCharity = models.CurrencyField()

    random_value = models.FloatField()

    orderSNE = models.IntegerField()

    amount_give = models.CurrencyField(min =0,max=3 , label='')

    def set_orderSNE(player):
        import random
        player.random_value = random.random()
        player.orderSNE = 1 if player.random_value <= C.PROBABILITY else 2

    @staticmethod
    def compute_payoffDice(player):
        if player.SumDice == 7:
            player.payoffDice = 0.50
        elif player.SumDice == 6 or player.SumDice == 8:
            player.payoffDice = 1
        elif player.SumDice == 5 or player.SumDice == 9:
            player.payoffDice = 1.50
        elif player.SumDice == 4 or player.SumDice == 10:
            player.payoffDice = 2
        elif player.SumDice == 3 or player.SumDice == 11:
            player.payoffDice = 2.50
        elif player.SumDice == 2 or player.SumDice == 12:
            player.payoffDice = 3

    def compute_sumDice(player):
        player.SumDice = player.FirstDice + player.SecondDice

    def set_payoffCharity(player):
        player.payoffCharity = cu(3 - player.amount_give)

    def set_payoff(player):
        player.payoff = player.payoffCharity + player.payoffDice

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


class Decision(Page):

    form_model = 'player'
    form_fields = ['FirstDice','SecondDice']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.compute_sumDice(),
        player.compute_payoffDice(player),
        player.prolific_id = player.participant.label
        player.set_orderSNE(),


class Decision2(Page):

    form_model = 'player'
    form_fields = ['amount_give']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.set_payoffCharity(),


    @staticmethod
    def vars_for_template(player):
        participant = player.participant
        participant.FirstDice = player.FirstDice
        participant.SecondDice = player.SecondDice
        participant.SumDice = player.SumDice
        participant.payoffDice = player.payoffDice

        return dict(FirstDice=participant.FirstDice,
                    SecondDice=participant.SecondDice,
                    SumDice=participant.SumDice,
                    payoffDice=participant.payoffDice)

class SNE(Page):

    form_model = "player"
    form_fields = ['SNE_1', 'SNE_2','SNE_3','SNE_4', 'SNE_5', 'SNE_6', 'SNE_7',
                  'SNE_8', 'SNE_9','SNE_10','SNE_11','SNE_12','SNE_13','SNE_14']


    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        participant.payoffCharity = player.payoffCharity
        participant.amount_give = player.amount_give

        return dict(payoffCharity=participant.payoffCharity, amount_give=participant.amount_give)

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.set_payoff(),


page_sequence = [General_instructions, Decision, Decision2, SNE]
