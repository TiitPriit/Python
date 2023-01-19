#Turingi test on test, mis on loodud Alan Turingi poolt aastal 1950, et mõõta arvuti "intelligentsust". Testi idee on, et inimene suhtleb tekstipõhise vestlusega arvutiprogrammiga ja arvuti peaks suutma esitada inimesele vastuseid, mis on sarnased inimese poolt esitatud küsimustele. Kui inimene ei suuda kindlaks teha, kas ta suhtleb arvutiga või inimesega, siis võib öelda, et arvuti on õnnestunud Turingi testis.
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('Test')

conversation = [
    "Tere",
    "Tere tulemast!",
    "Kuidas läheb?",
    "Läheb hästi, tänan, kuidas sinuga?",
    "Hästi, tänan",
    "Rõõm kuulda",
    "Mis ilm on täna?",
    "Ma ei tea, ma ei saa ilma jälgida",
    "Mis aeg on?",
    "Ma ei tea, ma ei saa aega jälgida"
]

trainer = ListTrainer(bot)
trainer.train(conversation)

response = bot.get_response("Tere")
print(response)
