import os
from datetime import date

from flask import (
    abort,
    Flask,
    render_template,
    request,
    send_from_directory,
)


from sunshine import settings

app = Flask(__name__)
app.config.from_object(settings)


ALL_ITEMS = [
    # (image_url, text)
    # These are in order of reveal.

    (
        1,
        '',
        'Recovering.'
    ),
    (
        2,
        '',
        'Playing some games.'
    ),
    (
        3,
        '',
        'Playing some more games; especially fighting games. LONNEN SMASH!'
    ),
    (
        4,
        '',
        'Surfing the webs looking for animated gifs because that is how I communicate sometimes. Found a cool one.'
    ),
    (
        5,
        '',
        'Hanging with Friday and playing some games.'
    ),
    (
        6,
        '',
        'Feeling a weird scratchy feeling in my jaw.'
    ),
    (
        7,
        '',
        'Looked in the mirror and noticed my jaw was more chiseled looking than it used to be'
    ),
    (
        8,
        '',
        'Noticed I no longer need to shave.'
    ),
    (
        9,
        '',
        'Went to drink a shake and accidentally bit through the glass. Curious. I think about sending an email to remind someone to feed Mike Kelly, but then decide to make this a survival test.'
    ),
    (
        10,
        '',
        'For some reason, I tried to bite some other things. Bit through my front door.'
    ),
    (
        11,
        '',
        'Tried biting harder things: kitchen counter, brick, granite, ti-tan-EE-yum.'
    ),
    (
        12,
        '',
        'Had a silent meeting with myself on vidyo and noticed that my skin is silvery and shiny.'
    ),
    (
        13,
        '',
        'Left the house today and saw a robbery in progress. I bit the robber into submission. What am I turning into?'
    ),
    (
        14,
        '',
        'Continued my biting spree: a jaywalker in front of my skateboard, someone doing graffiti with oxford commas, couple more robbers, some guy selling guns, four gangs involved in a knife fight, disarmed a nuclear missile.'
    ),
    (
        15,
        '',
        'Spent the day thinking about yesterday. The nuclear missile thing kind of spooked me. Maybe I should not try to be a hero?'
    ),
    (
        16,
        '',
        'Gained new resolve: I AM a hero. Traveled the world biting and foiling evil plots in my new biteacopter: bit a snake that was attacking a baby rhino on the African savanna, bit an international arms dealer, bit his brother, bit a warlord who was coming out of retirement, single-handedly ended the war on pugs, chewed up an incoming asteroid, destroyed an alien spaceship hellbent on enslabing the human race, saved a puppy and then saved a second puppy because the experience was enjoyable. Long day.'
    ),
    (
        17,
        '',
        'Continued my biting spree: destroyed a falling building before it crushed an infant in a stroller, bit fifty pounds of heroin in a makeshift submarine coming up the coast, bit a shark with lasers. Accidentally bit my tongue. Nursed my injury with spirits.'
    ),
    (
        18,
        '',
        'Took a bite out of the moon because I could. It tasted terrible, so I spit it out. Foul.'
    ),
    (
        19,
        '',
        'Woman showed up on my doorstep asking if I want to join an elite group. I said, "Lady, I AM an elite group." She left her card.'
    ),
    (
        20,
        '',
        'Bored with biting things. Decided to take a nap and play games today.'
    ),
    (
        21,
        '',
        'Lurked on IRC all day. Tried to bite my way to inbox 0, but couldn\'t. Bug mail is too hard to chew through. I deleted it all.'
    ),
    (
        22,
        '',
        'Emailed Laura telling her I am coming back to work and hell is coming with me. Looking forward to showing Potch how my bark and bite are equal now.'
    )
]


@app.route("/")
def index_view():
    is_all = bool(request.args.get('all', ''))

    items = list(ALL_ITEMS)
    if not is_all:
        days = (date.today() - date(year=2016, month=2, day=1)).days
        items = items[:days+1]

    return render_template(
        'index.html',
        items=items
    )


@app.route('/static/imgs/<img>')
def static_view(img):
    img = ''.join([c for c in img if c.isalnum() or c in "._"])

    path = os.path.join(app.root_path, 'static', 'imgs')
    if not os.path.exists(os.path.join(path, img)):
        print(os.path.join(path, img))
        abort(404)

    return send_from_directory(path, img)
