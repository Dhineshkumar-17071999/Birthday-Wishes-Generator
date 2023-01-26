from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

Funny = ["May your Facebook wall be filled with messages from people you never talk to.",
         "You’re older today than yesterday but younger than tomorrow, again happy birthday!",
         "Forget about the past, you can’t change it. Forget about the future, you can’t predict it. And forget about the present, I didn’t get you one.",
         "Cheers on your birthday. One step closer to adult underpants.",
         "You know, you don’t look that old. But then, you don’t look that young, either.",
         "Don’t get all weird about getting older! Our age is merely the number of years the world has been enjoying us!",
         "As you get older three things happen. The first is your memory goes, and I can’t remember the other two.",
         "You are only young once, but you can be immature for a lifetime.",
         "On your birthday, I thought of giving you the cutest gift in the world. But then I realized that is not possible because you yourself are the cutest gift in the world.",
         "It’s birthday time again, and wow! You’re a whole year older now! So clown around and have some fun to make this birthday your best one.",
         "Just wanted to be the first one to wish you happy birthday so I can feel superior to your other well-wishers.",
         "Congratulations on being even more experienced. I’m not sure what you learned this year, but every experience transforms us into the people we are today.",
         "When the little kids ask how old you are at your party, you should go ahead and tell them. While they’re distracted trying to count that high, you can steal a bite of their cake!"]
Inspirational = ["Count your life by smiles, not tears. Count your age by friends, not years.",
                 "I hope all your birthday wishes and dreams come true.",
                 "A wish for you on your birthday, whatever you ask may you receive, whatever you seek may you find, whatever you wish may it be fulfilled on your birthday and always.",
                 "Another adventure filled year awaits you. Welcome it by celebrating your birthday with pomp and splendor. Wishing you a very happy and fun-filled birthday!",
                 "May the joy that you have spread in the past come back to you on this day.",
                 "Your life is just about to pick up speed and blast off into the stratosphere. Wear a seat belt and be sure to enjoy the journey.",
                 "This birthday, I wish you abundant happiness and love. May all your dreams turn into reality and may lady luck visit your home today.",
                 "May you be gifted with life’s biggest joys and never-ending bliss. After all, you yourself are a gift to earth, so you deserve the best.",
                 "Count not the candles…see the lights they give. Count not the years, but the life you live. Wishing you a wonderful time ahead.",
                 "Forget the past; look forward to the future, for the best things are yet to come.",
                 "Birthdays are a new start, a fresh beginning and a time to pursue new endeavors with new goals. Move forward with confidence and courage. You are a very special person. May today and all of your days be amazing!",
                 "Your birthday is the first day of another 365-day journey. Be the shining thread in the beautiful tapestry of the world to make this year the best ever. Enjoy the ride.",
                 "Be happy! Today is the day you were brought into this world to be a blessing and inspiration to the people around you! You are a wonderful person! May you be given more birthdays to fulfill all of your dreams!"]
Cute = ["Wishing you a day filled with happiness and a year filled with joy.",
        "Sending you smiles for every moment of your special day…Have a wonderful time and a very happy birthday!",
        "Hope your special day brings you all that your heart desires! Here’s wishing you a day full of pleasant surprises!",
        "On your birthday we wish for you that whatever you want most in life it comes to you just the way you imagined it or better.",
        "Wishing you a beautiful day with good health and happiness forever.",
        "It’s a smile from me… To wish you a day that brings the same kind of happiness and joy that you bring to me.",
        "On this wonderful day, I wish you the best that life has to offer!",
        "I may not be by your side celebrating your special day with you, but I want you to know that I’m thinking of you and wishing you a wonderful birthday.",
        "I wish for all of your wishes to come true.",
        "Many years ago on this day, God decided to send an angel to earth. The angel was meant to touch lives and that happened! Happy birthday my sweet angel!",
        "Sending you a birthday wish wrapped with all my love.",
        "From good friends and true, from old friends and new, may good luck go with you and happiness too!",
        "A simple celebration, a gathering of friends; here wishing you great happiness and a joy that never ends.",
        "It’s always a treat to wish happy birthday to someone so sweet.",
        " Here’s to another year of laughing at our own jokes and keeping each other sane! Love you and happy birthday!",
        "Words alone are not enough to express how happy I am you are celebrating another year of your life! My wish for you on your birthday is that you are, and will always be, happy and healthy.",
        "I hope that today, at your party, you dance and others sing as you celebrate with joy your best birthday."]
Sweet = ["Hope all your birthday wishes come true!",
         "It’s your special day — get out there and celebrate!",
         "Wishing you the biggest slice of happy today.",
         "I hope your celebration gives you many happy memories!",
         "Our age is merely the number of years the world has been enjoying us!",
         "Enjoy your special day.",
         "Have the best birthday ever!",
         "Wherever the year ahead takes you, I hope it’s happy.",
         "The day is all yours — have fun!",
         "Cheers to you for another trip around the sun!",
         "Today is about you. I can’t wait to celebrate you all day long!",
         "Here’s to more life, love, and adventures with you to come!"]

# general = ["May this special day bring you endless joy and tons of precious memories!",
#            "Joy is in the air because your special day is here!",
#            "Your birthday only comes once a year, so make sure this is the most memorable one.",
#            "When you were young you were only attractive. Now you are attractive and wise.",
#            "Wishing you a wonderful Birthday and all the most amazing things on your Big Day!",
#            "You know all about me, I know all about you. Since we can read each other’s minds I don’t need a creative message.",
#            "he years fly by. You’ve been blessed with another one. Make it count!",
#            "Hope your birthday is as wonderful and extraordinary as you are.",
#            "You’re one of the hardest-working people I know. Relax a little and enjoy your Birthday.",
#            "May this birthday be the beginning of a wonderful period in your life!",
#            "Wishing you a birthday full of love and joy from the moment you open your eyes ’til the second you fall asleep.",
#            "Another adventure-filled year awaits you. Work hard, play hard, and love passionately."]

@app.route('/', methods = ['GET','POST'])
def index():
    return render_template('index.html')


@app.route('/submit', methods = ['POST','GET'])
def submit():
    if request.method == 'POST':
        global temp_name, temp_val, command, comma, temp_wish
        wish_list = []
        name = request.form['name']
        if len(name) != 0:
            temp_name = name
        if len(name) == 0:
            temp_name = temp_name
        selected_value = request.form['my_dropdown']
        if len(selected_value) != 0:
            temp_val = selected_value
        if len(selected_value) == 0:
            temp_val = temp_val
        wish_type = request.form['wish_type']
        if len(wish_type) != 0:
            temp_wish = wish_type
        if len(wish_type) == 0:
            temp_wish = temp_wish
        if temp_wish == 'Funny':
            wish_list = Funny
        elif temp_wish == 'Sweet':
            wish_list = Sweet
        elif temp_wish == 'Cute':
            wish_list = Cute
        elif temp_wish == 'Inspirational':
            wish_list = Inspirational
            
        wish = random.choice(wish_list)
        return render_template('index.html',command = 'Happy Birthday My', name = temp_name, selected_value = temp_val,comma = ',', wish = wish)


if __name__ == '__main__':
    app.run(debug=True)