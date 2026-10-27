from otree.api import *


doc = """
Payoff
"""


class C(BaseConstants):
    NAME_IN_URL = 'payoff8'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    prolific_id = models.StringField(default=str(" "))


# PAGES
class Results(Page):

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.prolific_id = player.participant.label


class ResultsWaitPage(WaitPage):
    pass


class Prolific(Page):

    @staticmethod
    def js_vars(player):
        return dict(
            completionlink=
            player.subsession.session.config['completionlink']
        )


page_sequence = [Results, Prolific]
