'''
Local Settings for a heroku_ebooks account. #fill in the name of the account you're tweeting from here.
'''

#configuration
MY_CONSUMER_KEY = 'wl94ulmntw1hnSdcZr4XWWAdk'
MY_CONSUMER_SECRET = 'dEBIo4WDBLVb1NeorNk79ENXghCxJ1gwrtcU24qiClNwHvpZ7h'
MY_ACCESS_TOKEN_KEY = '4904962708-LD7HGcm0F3wVDkbdzYYJUVK31fqyDiuySksBqCI'
MY_ACCESS_TOKEN_SECRET = 'TZ4pyMzowpGRcNEfNvASIFIDcGULo38LpE3T50jpyRDbi'

SOURCE_ACCOUNTS = ["richggall"] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
ODDS = 8 #How often do you want this to run? 1/8 times?
ORDER = 2 #how closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = False #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = ".txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API.
TWEET_ACCOUNT = "gall_ebooks" #The name of the account you're tweeting to.

