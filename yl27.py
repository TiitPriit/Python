#API (Application Programming Interface) on spetsiifiline protokoll või meetod, millega erinevad rakendused suhtlevad üksteisega. See võimaldab erinevatel rakendustel andmeid vahetada ja teineteise funktsioone kasutada.
#pip on Pythoni paigaldusprogramm, mis võimaldab teil Pythoni raamatukogusid paigaldada ja haldada. See on tavaliselt Pythoni arendajatele kättesaadav tööriist, mis võimaldab teil oma rakendustes kasutada teiste arendajate poolt loodud raamatukogusid.
#PRAW (Python Reddit API Wrapper) on Pythoni raamatukogu, mis võimaldab teil lihtsalt ja efektiivselt kasutada Redditi API-d. See võimaldab teil luua rakendusi, mis kasutavad Redditi andmeid, näiteks automaatset postituste ja kommentaaride lisamist, andmete kraapimist jne.

"""import praw

reddit = praw.Reddit(client_id='YOUR_CLIENT_ID', 
                     client_secret='YOUR_CLIENT_SECRET', 
                     username='YOUR_USERNAME', 
                     password='YOUR_PASSWORD', 
                     user_agent='YOUR_USER_AGENT')

for submission in reddit.user.me().submissions.new(limit=10):
    print(submission.title)"""


import praw

reddit = praw.Reddit(
    client_id="my client id",
    client_secret="my client secret",
    user_agent="my user agent",
)