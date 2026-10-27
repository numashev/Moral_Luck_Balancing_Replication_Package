from os import environ

SESSION_CONFIGS = [

dict(name='Bsl_Prosocial',
     display_name='Bsl_Prosocial',
     app_sequence=['Consent', 'BslProsocial', 'Quiz1',
                   'Quiz2', 'DASS21_EN','DemographicMBE', 'payoff_MBE'],
     num_demo_participants=1,
     completionlink='https://app.prolific.co/submissions/complete?cc=C1MZARSO',

     ),

dict(name='Luck_Prosocial',
     display_name='Luck_Prosocial',
     app_sequence=['Consent', 'LuckProsocial', 'Quiz1',
                   'Quiz2', 'DASS21_EN', 'DemographicMBE', 'payoff_MBE2'],
     num_demo_participants=1,
     completionlink='https://app.prolific.co/submissions/complete?cc=C1MZARSO',
     ),

dict(name='Lie_Prosocial',
     display_name='LieProsocial',
     app_sequence=['Consent', 'LieProsocial', 'Quiz1',
                   'Quiz2', 'DASS21_EN', 'DemographicMBE', 'payoff_MBE3'],
     num_demo_participants=1,
     completionlink='https://app.prolific.co/submissions/complete?cc=C1MZARSO',
     ),


dict(name='Bsl_Antisocial',
     display_name='Bsl_Antisocial',
     app_sequence=['Consent', 'BslAntisocial', 'Quiz1',
                   'Quiz2', 'DASS21_EN','DemographicMBE', 'payoff_MBE4'],
     num_demo_participants=1,
     completionlink='https://app.prolific.co/submissions/complete?cc=C1MZARSO',

     ),

dict(name='Luck_Antisocial',
     display_name='Luck_Antisocial',
     app_sequence=['Consent', 'LuckAntisocial', 'Quiz1',
                   'Quiz2', 'DASS21_EN','DemographicMBE', 'payoff_MBE5'],
     num_demo_participants=1,
     completionlink='https://app.prolific.co/submissions/complete?cc=C1MZARSO',

     ),

dict(name='Lie_Antisocial',
     display_name='Lie_Antisocial',
     app_sequence=['Consent', 'LieAntisocial', 'Quiz1',
                   'Quiz2', 'DASS21_EN','DemographicMBE', 'payoff_MBE6'],
     num_demo_participants=1,
     completionlink='https://app.prolific.co/submissions/complete?cc=C1MZARSO',

     ),

dict(name='Antisocial_Lie',
 display_name='Antisocial_Lie',
 app_sequence=['Consent', 'Antisocial_Lie', 'Quiz1',
               'Quiz2', 'DASS21_EN','DemographicMBE', 'payoff_MBE7'],
 num_demo_participants=1,
 completionlink='https://app.prolific.co/submissions/complete?cc=C1MZARSO',

 ),

dict(name='Prosocial_Lie',
     display_name='Prosocial_Lie',
     app_sequence=['Consent', 'Prosocial_Lie', 'Quiz1', 'Quiz2',
                   'DASS21_EN','DemographicMBE', 'payoff_MBE8'],
     num_demo_participants=1,
     completionlink='https://app.prolific.co/submissions/complete?cc=C1MZARSO',

     ),

]


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']


SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.10,
    participation_fee=0.00,
    doc="",
)

# define here the models for your exported data
PARTICIPANT_FIELDS = [
    'ticket',
    'payoffLuck',
    'payoffBsl',
    'FirstDice',
    'SecondDice',
    'SumDice',
    'payoffDice',
    'amount_give',
    'amount_take',
    'payoffCharity',
]
SESSION_FIELDS = ['prolific_completion_url']

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False
REAL_WORLD_CURRENCY_DECIMAL_PLACES = 1

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

# Set OTREE_SECRET_KEY in your environment. The fallback is for local testing only.
SECRET_KEY = environ.get('OTREE_SECRET_KEY', 'local-development-secret-change-me')

