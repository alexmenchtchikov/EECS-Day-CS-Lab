"""Setup for the EECS Day Wordle lab: creates wordbank.txt and defines the helper tools.

Run it from the notebook with `%run -i wordle_setup.py`. Students don't need to read
or change this file, but they're welcome to peek!
"""
import html, json, math, random, time, uuid
from IPython.display import HTML, display

_RAW_WORDS = """
aback abase abate abbey abbot abhor abide abled abode abort about above abuse abyss
acorn acrid actor acute adage adapt adept admin admit adobe adopt adore adorn adult
affix afire afoot afoul after again agape agate agent agile aging aglow agony agora
agree ahead aider aisle alarm album alert algae alibi alien align alike alive allay
alley allot allow alloy aloft alone along aloof aloud alpha altar alter amass amaze
amber amble amend amiss amity among ample amply amuse angel anger angle angry angst
anime ankle annex annoy annul anode antic anvil aorta apart aphid aping apnea apple
apply apron aptly arbor ardor arena argue arise armor aroma arose array arrow arson
artsy ascot ashen aside askew assay asset atoll atone attic audio audit augur aunty
avail avert avian avoid await awake award aware awash awful awoke axial axiom axion
azure bacon badge badly bagel baggy baker baler balmy banal banjo barge baron basal
basic basil basin basis baste batch bathe baton batty bawdy bayou beach beady beard
beast beech beefy befit began begat beget begin begun being belch belie belle belly
below bench beret berry berth beset betel bevel bezel bible bicep biddy bigot bilge
billy binge bingo biome birch birth bison bitty black blade blame bland blank blare
blast blaze bleak bleat bleed bleep blend bless blimp blind blink bliss blitz bloat
block bloke blond blood bloom blown bluer bluff blunt blurb blurt blush board boast
bobby boney bongo bonus booby boost booth booty booze boozy borax borne bosom bossy
botch bough boule bound bowel boxer brace braid brain brake brand brash brass brave
bravo brawl brawn bread break breed briar bribe brick bride brief brine bring brink
briny brisk broad broil broke brood brook broom broth brown brunt brush brute buddy
budge buggy bugle build built bulge bulky bully bunch bunny burly burnt burst bused
bushy butch butte buxom buyer bylaw cabal cabby cabin cable cacao cache cacti caddy
cadet cagey cairn camel cameo canal candy canny canoe canon caper caput carat cargo
carol carry carve caste catch cater catty caulk cause cavil cease cedar cello chafe
chaff chain chair chalk champ chant chaos chard charm chart chase chasm cheap cheat
check cheek cheer chess chest chick chide chief child chili chill chime china chirp
chock choir choke chord chore chose chuck chump chunk churn chute cider cigar cinch
circa civic civil clack claim clamp clang clank clash clasp class clean clear cleat
cleft clerk click cliff climb cling clink cloak clock clone close cloth cloud clout
clove clown cluck clued clump clung coach coast cobra cocoa colon color comet comfy
comic comma conch condo conic copse coral corer corny couch cough could count coupe
court coven cover covet covey cower coyly crack craft cramp crane crank crash crass
crate crave crawl craze crazy creak cream credo creed creek creep creme crepe crept
cress crest crick cried crier crime crimp crisp croak crock crone crony crook cross
croup crowd crown crude cruel crumb crump crush crust crypt cubic cumin curio curly
curry curse curve curvy cutie cyber cycle cynic daddy daily dairy daisy dally dance
dandy datum daunt dealt death debar debit debug debut decal decay decor decoy decry
defer deign deity delay delta delve demon demur denim dense depot depth derby deter
detox deuce devil diary dicey digit dilly dimly diner dingo dingy diode dirge dirty
disco ditch ditto ditty diver dizzy dodge dodgy dogma doing dolly donor donut dopey
doubt dough dowdy dowel downy dowry dozen draft drain drake drama drank drape drawl
drawn dread dream dress dried drier drift drill drink drive droit droll drone drool
droop dross drove drown druid drunk dryer dryly duchy dully dummy dumpy dunce dusky
dusty dutch duvet dwarf dwell dwelt dying eager eagle early earth easel eaten eater
ebony eclat edict edify eerie egret eight eject eking elate elbow elder elect elegy
elfin elide elite elope elude email embed ember emcee empty enact endow enema enemy
enjoy ennui ensue enter entry envoy epoch epoxy equal equip erase erect erode error
erupt essay ester ether ethic ethos etude evade event every evict evoke exact exalt
excel exert exile exist expel extol extra exult eying fable facet faint fairy faith
false fancy fanny farce fatal fatty fault fauna favor feast fecal feign fella felon
femme femur fence feral ferry fetal fetch fetid fetus fever fewer fiber fibre ficus
field fiend fiery fifth fifty fight filer filet filly filmy filth final finch finer
first fishy fixer fizzy fjord flack flail flair flake flaky flame flank flare flash
flask fleck fleet flesh flick flier fling flint flirt float flock flood floor flora
floss flour flout flown fluff fluid fluke flume flung flunk flush flute flyer foamy
focal focus foggy foist folio folly foray force forge forgo forte forth forty forum
found foyer frail frame frank fraud freak freed freer fresh friar fried frill frisk
fritz frock frond front frost froth frown froze fruit fudge fugue fully fungi funky
funny furor furry fussy fuzzy gaffe gaily gamer gamma gamut gassy gaudy gauge gaunt
gauze gavel gawky gayer gayly gazer gecko geeky geese genie genre ghost ghoul giant
giddy gipsy girly girth given giver glade gland glare glass glaze gleam glean glide
glint gloat globe gloom glory gloss glove glyph gnash gnome godly going golem golly
gonad goner goody gooey goofy goose gorge gouge gourd grace grade graft grail grain
grand grant grape graph grasp grass grate grave gravy graze great greed green greet
grief grill grime grimy grind gripe groan groin groom grope gross group grout grove
growl grown gruel gruff grunt guard guava guess guest guide guild guile guilt guise
gulch gully gumbo gummy guppy gusto gusty gypsy habit hairy halve handy happy hardy
harem harpy harry harsh haste hasty hatch hater haunt haute haven havoc hazel heady
heard heart heath heave heavy hedge hefty heist helix hello hence heron hilly hinge
hippo hippy hitch hoard hobby hoist holly homer honey honor horde horny horse hotel
hotly hound house hovel hover howdy human humid humor humph humus hunch hunky hurry
husky hussy hutch hydro hyena hymen hyper icily icing ideal idiom idiot idler idyll
igloo iliac image imbue impel imply inane inbox incur index inept inert infer ingot
inlay inlet inner input inter intro ionic irate irony islet issue itchy ivory jaunt
jazzy jelly jerky jetty jewel jiffy joint joist joker jolly joust judge juice juicy
jumbo jumpy junta junto juror kappa karma kayak kebab khaki kinky kiosk kitty knack
knave knead kneed kneel knelt knife knock knoll known koala krill label labor laden
ladle lager lance lanky lapel lapse large larva lasso latch later lathe latte laugh
layer leach leafy leaky leant leapt learn lease leash least leave ledge leech leery
lefty legal leggy lemon lemur leper level lever libel liege light liken lilac limbo
limit linen liner lingo lipid lithe liver livid llama loamy loath lobby local locus
lodge lofty logic login loopy loose lorry loser louse lousy lover lower lowly loyal
lucid lucky lumen lumpy lunar lunch lunge lupus lurch lurid lusty lying lymph lynch
lyric macaw macho macro madam madly mafia magic magma maize major maker mambo mamma
mammy manga mange mango mangy mania manic manly manor maple march marry marsh mason
masse match matey mauve maxim maybe mayor mealy meant meaty mecca medal media medic
melee melon mercy merge merit merry metal meter metro micro midge midst might milky
mimic mince miner minim minor minty minus mirth miser missy mocha modal model modem
mogul moist molar moldy money month moody moose moral moron morph mossy motel motif
motor motto moult mound mount mourn mouse mouth mover movie mower mucky mucus muddy
mulch mummy munch mural murky mushy music musky musty myrrh nadir naive nanny nasal
nasty natal naval navel needy neigh nerdy nerve never newer newly nicer niche niece
night ninja ninny ninth noble nobly noise noisy nomad noose north nosey notch novel
nudge nurse nutty nylon nymph oaken obese occur ocean octal octet odder oddly offal
offer often olden older olive ombre omega onion onset opera opine opium optic orbit
order organ other otter ought ounce outdo outer outgo ovary ovate overt ovine ovoid
owing owner oxide ozone paddy pagan paint paler palsy panel panic pansy papal paper
parer parka parry parse party pasta paste pasty patch patio patsy patty pause payee
payer peace peach pearl pecan pedal penal pence penne penny perch peril perky pesky
pesto petal petty phase phone phony photo piano picky piece piety piggy pilot pinch
piney pinky pinto piper pique pitch pithy pivot pixel pixie pizza place plaid plain
plait plane plank plant plate plaza plead pleat plied plier pluck plumb plume plump
plunk plush poesy point poise poker polar polka polyp pooch poppy porch poser posit
posse pouch pound pouty power prank prawn preen press price prick pride pried prime
primo print prior prism privy prize probe prone prong proof prose proud prove prowl
proxy prude prune psalm pubic pudgy puffy pulpy pulse punch pupal pupil puppy puree
purer purge purse pushy putty pygmy quack quail quake qualm quark quart quash quasi
queen queer quell query quest queue quick quiet quill quilt quirk quite quota quote
quoth rabbi rabid racer radar radii radio rainy raise rajah rally ralph ramen ranch
randy range rapid rarer raspy ratio ratty raven rayon razor reach react ready realm
rearm rebar rebel rebus rebut recap recur recut reedy refer refit regal rehab reign
relax relay relic remit renal renew repay repel reply rerun reset resin retch retro
retry reuse revel revue rhino rhyme rider ridge rifle right rigid rigor rinse ripen
riper risen riser risky rival river rivet roach roast robin robot rocky rodeo roger
rogue roomy roost rotor rouge rough round rouse route rover rowdy rower royal ruddy
ruder rugby ruler rumba rumor rupee rural rusty sadly safer saint salad sally salon
salsa salty salve salvo sandy saner sappy sassy satin satyr sauce saucy sauna saute
savor savoy savvy scald scale scalp scaly scamp scant scare scarf scary scene scent
scion scoff scold scone scoop scope score scorn scour scout scowl scram scrap scree
screw scrub scrum scuba sedan seedy segue seize semen sense sepia serif serum serve
setup seven sever sewer shack shade shady shaft shake shaky shale shall shalt shame
shank shape shard share shark sharp shave shawl shear sheen sheep sheer sheet sheik
shelf shell shied shift shine shiny shire shirk shirt shoal shock shone shook shoot
shore shorn short shout shove shown showy shrew shrub shrug shuck shunt shush shyly
siege sieve sight sigma silky silly since sinew singe siren sissy sixth sixty skate
skier skiff skill skimp skirt skulk skull skunk slack slain slang slant slash slate
slave sleek sleep sleet slept slice slick slide slime slimy sling slink sloop slope
slosh sloth slump slung slunk slurp slush slyly smack small smart smash smear smell
smelt smile smirk smite smith smock smoke smoky smote snack snail snake snaky snare
snarl sneak sneer snide sniff snipe snoop snore snort snout snowy snuck snuff soapy
sober soggy solar solid solve sonar sonic sooth sooty sorry sound south sower space
spade spank spare spark spasm spawn speak spear speck speed spell spelt spend spent
sperm spice spicy spied spiel spike spiky spill spilt spine spiny spire spite splat
split spoil spoke spoof spook spool spoon spore sport spout spray spree sprig spunk
spurn spurt squad squat squib stack staff stage staid stain stair stake stale stalk
stall stamp stand stank stare stark start stash state stave stead steak steal steam
steed steel steep steer stein stern stick stiff still stilt sting stink stint stock
stoic stoke stole stomp stone stony stood stool stoop store stork storm story stout
stove strap straw stray strip strut stuck study stuff stump stung stunk stunt style
suave sugar suing suite sulky sully sumac sunny super surer surge surly sushi swami
swamp swarm swash swath swear sweat sweep sweet swell swept swift swill swine swing
swirl swish swoon swoop sword swore sworn swung synod syrup tabby table taboo tacit
tacky taffy taint taken taker tally talon tamer tango tangy taper tapir tardy tarot
taste tasty tatty taunt tawny teach teary tease teddy teeth tempo tenet tenor tense
tenth tepee tepid terra terse testy thank theft their theme there these theta thick
thief thigh thing think third thong thorn those three threw throb throw thrum thumb
thump thyme tiara tibia tidal tiger tight tilde timer timid tipsy titan tithe title
toast today toddy token tonal tonga tonic tooth topaz topic torch torso torus total
totem touch tough towel tower toxic toxin trace track tract trade trail train trait
tramp trash trawl tread treat trend triad trial tribe trice trick tried tripe trite
troll troop trope trout trove truce truck truer truly trump trunk truss trust truth
tryst tubal tuber tulip tulle tumor tunic turbo tutor twang tweak tweed tweet twice
twine twirl twist twixt tying udder ulcer ultra umbra uncle uncut under undid undue
unfed unfit unify union unite unity unlit unmet unset untie until unwed unzip upper
upset urban urine usage usher using usual usurp utile utter vague valet valid valor
value valve vapid vapor vault vaunt vegan venom venue verge verse verso verve vicar
video vigil vigor villa vinyl viola viper viral virus visit visor vista vital vivid
vixen vocal vodka vogue voice voila vomit voter vouch vowel vying wacky wafer wager
wagon waist waive waltz warty waste watch water waver waxen weary weave wedge weedy
weigh weird welch welsh wench whack whale wharf wheat wheel whelp where which whiff
while whine whiny whirl whisk white whole whoop whose widen wider widow width wield
wight willy wimpy wince winch windy wiser wispy witch witty woken woman women woody
wooer wooly woozy wordy world worry worse worst worth would wound woven wrack wrath
wreak wreck wrest wring wrist write wrong wrote wrung wryly yacht yearn yeast yield
young youth zebra zesty zonal
"""
_WORDS = sorted(_RAW_WORDS.split())
_WORD_SET = set(_WORDS)

# Save the word bank as a text file (one UPPERCASE word per line), like a real dataset.
with open("wordbank.txt", "w") as _f:
    for _w in _WORDS:
        _f.write(_w.upper() + "\n")


# ---------- Reference Wordle rules (used by the game, the tests, and the competition) ----------
def _feedback(guess, secret):
    result = ["-"] * 5
    leftover = {}
    for i in range(5):
        if guess[i] == secret[i]:
            result[i] = "G"
        else:
            leftover[secret[i]] = leftover.get(secret[i], 0) + 1
    for i in range(5):
        if result[i] != "G" and leftover.get(guess[i], 0) > 0:
            result[i] = "Y"
            leftover[guess[i]] -= 1
    return "".join(result)


def _filter(candidates, guess, feedback):
    return [w for w in candidates if _feedback(guess, w) == feedback]


# ---------- Display helpers ----------
_COLORS = {"G": "#6aaa64", "Y": "#c9b458", "-": "#787c7e"}


def emoji(feedback):
    """Turn a feedback string like 'GY--G' into colored squares."""
    return "".join({"G": "🟩", "Y": "🟨"}.get(c, "⬛") for c in feedback)


def show_board(history, title=None):
    """Draw a Wordle board from a list of (guess, feedback) pairs."""
    rows = []
    for guess, feedback in history:
        tiles = "".join(
            f'<div style="width:42px;height:42px;display:flex;align-items:center;justify-content:center;'
            f'background:{_COLORS.get(c, "#787c7e")};color:#fff;font:bold 24px Arial,sans-serif;'
            f'border-radius:3px">{html.escape(ch.upper())}</div>'
            for ch, c in zip(guess, feedback)
        )
        rows.append(f'<div style="display:flex;gap:5px;margin-bottom:5px">{tiles}</div>')
    head = (f'<div style="font:bold 15px Arial,sans-serif;margin-bottom:8px">{html.escape(title)}</div>'
            if title else "")
    display(HTML(f'<div style="display:inline-block;padding:12px 12px 7px;background:#fff;color:#1a1a1b;'
                 f'border-radius:10px;border:1px solid #d3d6da">{head}{"".join(rows)}</div>'))


# ---------- Friendly checkers for the exercises ----------
def _is_blank_error(e):
    return isinstance(e, NameError) and "___" in str(e)


def _blank_msg():
    print("There's still a blank (___) to fill in! Replace every ___ with code, then run the cell again.")


def _args(args):
    return ", ".join(repr(a) for a in args)


def _run_cases(fn, cases):
    name = getattr(fn, "__name__", "your function")
    try:
        for args, expected in cases:
            got = fn(*args)
            if got != expected:
                print(f"❌ {name}({_args(args)}) returned {got!r}, but it should return {expected!r}. Take another look!")
                return False
    except Exception as e:
        if _is_blank_error(e):
            _blank_msg()
            return False
        raise
    print(f"✅ {name} passed all the tests. Nice work!")
    return True


def check_wordbank(words):
    if len(words) != len(_WORDS):
        print(f"❌ Expected {len(_WORDS)} words, but your list has {len(words)}.")
        return False
    messy = [w for w in words if not isinstance(w, str) or w != w.strip().lower()]
    if messy:
        print(f"❌ Some words still need cleaning up, like {messy[0]!r}. Hint: .strip() and .lower()")
        return False
    if sorted(words) != _WORDS:
        print("❌ Hmm, the words don't match the word bank. Make sure you append each cleaned word.")
        return False
    print(f"✅ Loaded {len(words):,} clean words. The dataset is ready!")
    return True


def check_count_vowels(fn):
    return _run_cases(fn, [(("crane",), 2), (("audio",), 4), (("lymph",), 0), (("eerie",), 4), (("queue",), 4)])


def check_count_same_position(fn):
    return _run_cases(fn, [(("crane", "trace"), 3), (("crane", "crane"), 5),
                           (("speed", "abide"), 0), (("crane", "nacre"), 1)])


def check_words_without(fn):
    small = ["crane", "bloom", "fizzy", "eerie"]
    return _run_cases(fn, [((small, "e"), ["bloom", "fizzy"]), ((small, "z"), ["crane", "bloom", "eerie"]),
                           ((small, "q"), small), (([], "a"), [])])


def check_letter_counts(fn):
    return _run_cases(fn, [(("speed",), {"s": 1, "p": 1, "e": 2, "d": 1}),
                           (("crane",), {"c": 1, "r": 1, "a": 1, "n": 1, "e": 1}),
                           (("eerie",), {"e": 3, "r": 1, "i": 1})])


def check_feedback(fn):
    tricky = [("crane", "trace"), ("speed", "abide"), ("crane", "crane"), ("eerie", "there"),
              ("geese", "these"), ("allay", "algae"), ("robot", "otter"), ("lolly", "alloy"), ("abbey", "kebab")]
    rng = random.Random(0)
    pairs = tricky + [(rng.choice(_WORDS), rng.choice(_WORDS)) for _ in range(3000)]
    try:
        for guess, secret in pairs:
            got, want = fn(guess, secret), _feedback(guess, secret)
            if got != want:
                if isinstance(got, list):
                    print("❌ get_feedback returned a list. Make sure you return \"\".join(feedback).")
                    return False
                shown = emoji(got) if isinstance(got, str) and len(got) == 5 else ""
                print(f"❌ get_feedback({guess!r}, {secret!r}) returned {got!r} {shown}\n"
                      f"   but it should be {want!r} {emoji(want)}. Take another look!")
                return False
    except Exception as e:
        if _is_blank_error(e):
            _blank_msg()
            return False
        raise
    print(f"✅ get_feedback matches real Wordle on {len(pairs):,} test games, including the tricky repeated letters!")
    return True


def check_filter_words(fn):
    try:
        for guess, secret in [("raise", "pinky"), ("crane", "watch"), ("speed", "abide"), ("pinky", "pinky")]:
            fb = _feedback(guess, secret)
            got, want = fn(list(_WORDS), guess, fb), _filter(_WORDS, guess, fb)
            if got != want:
                print(f"❌ After guessing {guess!r} and getting {fb!r} {emoji(fb)}, there should be "
                      f"{len(want)} words left, but filter_words kept {len(got) if isinstance(got, list) else got}.")
                return False
    except Exception as e:
        if _is_blank_error(e):
            _blank_msg()
            return False
        raise
    print("✅ filter_words works! You can now narrow down 2,315 words in a flash.")
    return True


def check_first_word_solver(fn):
    return _run_cases(fn, [((["crane", "slate", "trace"], []), "crane"), ((["pinky"], [("raise", "--Y--")]), "pinky")])


def check_play_game(fn):
    first = lambda candidates, history: candidates[0]
    try:
        for secret in ["pinky", "fuzzy", "aback", "zonal"]:
            want = len(_play(first, secret, 20)[0])
            got = fn(first, secret, show=False)
            if got != want:
                print(f"❌ Playing the secret word {secret!r} took {got} guesses, but it should take {want}.")
                return False
    except Exception as e:
        if _is_blank_error(e):
            _blank_msg()
            return False
        raise
    print("✅ play_game works! Your computer can play Wordle all by itself.")
    return True


def _ref_frequency(candidates, history):
    counts = {}
    for word in candidates:
        for letter in set(word):
            counts[letter] = counts.get(letter, 0) + 1
    best_word, best_score = None, -1
    for word in candidates:
        score = sum(counts[letter] for letter in set(word))
        if score > best_score:
            best_word, best_score = word, score
    return best_word


def check_frequency_solver(fn):
    rng = random.Random(1)
    cases = [((list(_WORDS), []), _ref_frequency(_WORDS, []))]
    for _ in range(5):
        c = sorted(rng.sample(_WORDS, rng.randint(3, 40)))
        cases.append(((c, []), _ref_frequency(c, [])))
    return _run_cases(fn, cases)


def _ref_average_remaining(guess, candidates):
    groups = {}
    for s in candidates:
        p = _feedback(guess, s)
        groups[p] = groups.get(p, 0) + 1
    return sum(k * k for k in groups.values()) / len(candidates)


def check_average_remaining(fn):
    try:
        for guess in ["crane", "pizza", "audio"]:
            got, want = fn(guess, _WORDS), _ref_average_remaining(guess, _WORDS)
            if not isinstance(got, (int, float)) or abs(got - want) > 1e-6:
                print(f"❌ average_remaining({guess!r}, WORDS) returned {got!r}, but it should be about {want:.2f}.")
                return False
    except Exception as e:
        if _is_blank_error(e):
            _blank_msg()
            return False
        raise
    print("✅ average_remaining works!")
    return True


# ---------- Running solvers (tests + competition) ----------
def _play(solver, secret, max_guesses=10):
    """Play one game with the official rules. Returns (history, solved)."""
    candidates, history = list(_WORDS), []
    while len(history) < max_guesses:
        guess = solver(list(candidates), list(history))
        if not isinstance(guess, str):
            raise TypeError(f"Your solver returned {guess!r}, but it should return a word (a string) like 'crane'.")
        guess = guess.strip().lower()
        if guess not in _WORD_SET:
            raise ValueError(f"Your solver guessed {guess!r}, which isn't in the word bank. Every guess must be "
                             f"one of the 5-letter words in WORDS (heads up: some popular words like 'adieu' aren't!)")
        fb = _feedback(guess, secret)
        history.append((guess, fb))
        if fb == "GGGGG":
            return history, True
        candidates = _filter(candidates, guess, fb)
    return history, False


MAX_GUESSES = 10      # a game that isn't solved in 10 guesses...
FAIL_SCORE = 12       # ...counts as 12 guesses


def _score(history, solved):
    return len(history) if solved else FAIL_SCORE


def test_solver(solver, num_games=100, seed=2026):
    """Play `num_games` random secret words and report the average number of guesses."""
    name = getattr(solver, "__name__", "your solver")
    secrets = random.Random(seed).sample(_WORDS, num_games)
    print(f"Testing {name} on {num_games} secret words...")
    start, scores = time.time(), []
    try:
        for secret in secrets:
            scores.append(_score(*_play(solver, secret, MAX_GUESSES)))
    except Exception as e:
        if _is_blank_error(e):
            _blank_msg()
            return None
        raise
    avg = sum(scores) / len(scores)
    print(f"\n   Average: {avg:.3f} guesses per word")
    print(f"   Solved within 6 guesses (real Wordle rules): {sum(s <= 6 for s in scores)} / {num_games}\n")
    biggest = max(scores.count(n) for n in set(scores))
    for n in range(1, MAX_GUESSES + 1):
        k = scores.count(n)
        if k or n <= 6:
            print(f"   {n:>2} {'guess  ' if n == 1 else 'guesses'} | {'█' * round(30 * k / biggest)} {k}")
    if FAIL_SCORE in scores:
        print(f"   not solved | {'█' * round(30 * scores.count(FAIL_SCORE) / biggest)} {scores.count(FAIL_SCORE)}")
    print(f"\n   Time: {time.time() - start:.1f} seconds")
    return avg


def _berkeley_solver(candidates, history):
    """The Berkeley student's solver: a carefully chosen opener, then common letters."""
    if not history:
        return "slate"
    return _ref_frequency(candidates, history)


def competition(solver, code=90, num_words=20, reveal=False):
    """Play 20 secret words and compare against the Berkeley student's solver."""
    secrets = random.Random(f"eecs-day-{code}").sample(_WORDS, num_words)
    name = getattr(solver, "__name__", "your solver")
    print(f"Competition code {code}: {name} vs. the Berkeley student on {num_words} secret words...")
    start, games = time.time(), []
    for i, secret in enumerate(secrets, 1):
        try:
            games.append(_play(solver, secret, MAX_GUESSES))
        except Exception as e:
            if _is_blank_error(e):
                _blank_msg()
                return None
            print(f"Your solver crashed on secret word #{i}.")
            raise
    elapsed = time.time() - start
    bot_games = [_play(_berkeley_solver, s, MAX_GUESSES) for s in secrets]

    you = [_score(*g) for g in games]
    bot = [_score(*g) for g in bot_games]
    you_avg, bot_avg = sum(you) / num_words, sum(bot) / num_words
    wins = sum(a < b for a, b in zip(you, bot))
    ties = sum(a == b for a, b in zip(you, bot))

    rows = []
    for i, ((hist, solved), y, b) in enumerate(zip(games, you, bot)):
        label = secrets[i].upper() if reveal else f"Secret #{i + 1}"
        squares = " ".join(emoji(fb) for _, fb in hist) + ("" if solved else " ❌")
        mark = "🟢" if y < b else ("⚪" if y == b else "🔴")
        rows.append(f"<tr><td style='white-space:nowrap;padding-right:8px'>{label}</td><td style='font-size:13px;letter-spacing:-1px'>{squares}</td>"
                    f"<td style='text-align:center'><b>{y}</b></td><td style='text-align:center'>{b}</td>"
                    f"<td style='text-align:center'>{mark}</td></tr>")
    if you_avg < bot_avg - 1e-9:
        verdict = "You outperformed the Berkeley student! Show a TA!"
        color = "#538d4e"
    elif abs(you_avg - bot_avg) < 1e-9:
        verdict = "Dead even! Can you squeeze out one more guess?"
        color = "#b59f3b"
    else:
        verdict = "The Berkeley student wins this round. Try a bonus idea and run it again!"
        color = "#787c7e"
    th = "style='text-align:left;padding:4px 8px;border-bottom:2px solid #d3d6da'"
    display(HTML(f"""
<div style="font-family:Arial,sans-serif;background:#fff;color:#1a1a1b;border:1px solid #d3d6da;
            border-radius:12px;padding:16px 20px;max-width:640px">
  <div style="display:flex;gap:16px;flex-wrap:wrap;margin-bottom:12px">
    <div style="flex:1;min-width:180px;background:#f6f7f8;border-radius:10px;padding:12px;text-align:center">
      <div style="font-size:13px;color:#555">You ({html.escape(name)})</div>
      <div style="font-size:40px;font-weight:800">{you_avg:.2f}</div>
      <div style="font-size:12px;color:#555">average guesses</div></div>
    <div style="flex:1;min-width:180px;background:#f6f7f8;border-radius:10px;padding:12px;text-align:center">
      <div style="font-size:13px;color:#555">Berkeley student</div>
      <div style="font-size:40px;font-weight:800">{bot_avg:.2f}</div>
      <div style="font-size:12px;color:#555">average guesses</div></div>
  </div>
  <div style="background:{color};color:#fff;font-weight:700;border-radius:8px;padding:10px;text-align:center;
              margin-bottom:12px">{verdict}</div>
  <div style="font-size:13px;margin-bottom:8px">Word by word: you won <b>{wins}</b>, tied <b>{ties}</b>,
    lost <b>{num_words - wins - ties}</b> · solved within 6 guesses: <b>{sum(s <= 6 for s in you)}/{num_words}</b>
    · your solver took {elapsed:.1f}s</div>
  <table style="border-collapse:collapse;font-size:14px;width:100%">
    <tr><th {th}>Word</th><th {th}>Your game</th><th {th}>You</th><th {th}>Berkeley</th><th {th}></th></tr>
    {''.join(rows)}
  </table>
</div>"""))
    return you_avg


# ---------- The playable Wordle game ----------
_GAME_TEMPLATE = r"""
<div id="__UID__" class="wdl-root" tabindex="0">
<style>
#__UID__ { --g:#6aaa64; --y:#c9b458; --x:#787c7e; --bd:#d3d6da; --ink:#1a1a1b;
  font-family:"Helvetica Neue",Arial,sans-serif; background:#fff; color:var(--ink);
  max-width:500px; margin:0 auto; padding:14px 8px 18px; box-sizing:border-box;
  border-radius:14px; border:2px solid var(--bd); outline:none; user-select:none; -webkit-user-select:none; }
#__UID__:focus { border-color:#7aa7e9; }
#__UID__ .hdr { text-align:center; font-weight:800; font-size:30px; letter-spacing:3px; }
#__UID__ .sub { text-align:center; font-size:12px; color:#787c7e; margin-top:2px; }
#__UID__ .msg { height:36px; display:flex; align-items:center; justify-content:center; }
#__UID__ .msg span { background:var(--ink); color:#fff; padding:7px 14px; border-radius:6px; font-weight:700; font-size:14px; }
#__UID__ .board { display:flex; flex-direction:column; gap:5px; width:290px; margin:0 auto 14px; }
#__UID__ .row { display:flex; gap:5px; }
#__UID__ .tile { width:54px; height:54px; border:2px solid var(--bd); display:flex; align-items:center;
  justify-content:center; font-size:30px; font-weight:800; text-transform:uppercase; box-sizing:border-box; color:var(--ink); }
#__UID__ .tile.filled { border-color:#878a8c; animation:pop___UID__ .1s ease-in-out; }
#__UID__ .tile.g { background:var(--g); border-color:var(--g); color:#fff; }
#__UID__ .tile.y { background:var(--y); border-color:var(--y); color:#fff; }
#__UID__ .tile.x { background:var(--x); border-color:var(--x); color:#fff; }
#__UID__ .tile.flip { animation:flip___UID__ .5s ease-in-out; }
#__UID__ .row.shake { animation:shake___UID__ .4s; }
#__UID__ .row.win .tile { animation:bounce___UID__ .5s ease; }
@keyframes pop___UID__ { 50% { transform:scale(1.1); } }
@keyframes flip___UID__ { 0% { transform:rotateX(0); } 50% { transform:rotateX(90deg); } 100% { transform:rotateX(0); } }
@keyframes shake___UID__ { 20%,60% { transform:translateX(-6px); } 40%,80% { transform:translateX(6px); } }
@keyframes bounce___UID__ { 40% { transform:translateY(-14px); } 80% { transform:translateY(2px); } }
#__UID__ .kb { display:flex; flex-direction:column; gap:7px; padding:0 4px; }
#__UID__ .kbrow { display:flex; gap:5px; justify-content:center; }
#__UID__ .key { flex:1; max-width:43px; height:54px; border:0; border-radius:4px; background:var(--bd);
  color:var(--ink); font-weight:700; font-size:14px; text-transform:uppercase; cursor:pointer; padding:0;
  font-family:inherit; }
#__UID__ .key.wide { max-width:66px; flex:1.5; font-size:12px; }
#__UID__ .key.g { background:var(--g); color:#fff; }
#__UID__ .key.y { background:var(--y); color:#fff; }
#__UID__ .key.x { background:var(--x); color:#fff; }
#__UID__ .foot { display:flex; align-items:center; justify-content:center; gap:12px; margin-top:14px; flex-wrap:wrap; }
#__UID__ .newbtn { background:var(--g); color:#fff; border:0; border-radius:20px; padding:9px 20px;
  font-weight:700; font-size:14px; cursor:pointer; font-family:inherit; }
#__UID__ .hint { font-size:12px; color:#787c7e; }
#__UID__ .share { text-align:center; font-size:18px; line-height:1.25; margin-top:10px; white-space:pre; min-height:0; }
</style>
<div class="hdr">WORDLE</div>
<div class="sub">UC Berkeley EECS Day edition</div>
<div class="msg"></div>
<div class="board"></div>
<div class="kb"></div>
<div class="foot">
  <button class="newbtn" tabindex="-1">New game</button>
  <span class="hint">Click the game, then type on your keyboard (or tap the keys)</span>
</div>
<div class="share"></div>
</div>
<script>
(function () {
  var WORDS = __WORDS_JSON__;
  var VALID = new Set(WORDS);
  var ROWS = 6, COLS = 5;
  var CLASS = { G: "g", Y: "y", "-": "x" };
  var RANK = { x: 1, y: 2, g: 3 };
  var PRAISE = ["Genius!", "Magnificent!", "Impressive!", "Splendid!", "Great!", "Phew!"];
  var root = document.getElementById("__UID__");
  var boardEl = root.querySelector(".board"), msgEl = root.querySelector(".msg");
  var kbEl = root.querySelector(".kb"), shareEl = root.querySelector(".share");
  var secret, row, cur, over, busy, keyState, results, msgTimer;

  // Same rules as get_feedback in Python: greens first, then yellows from the leftover letters.
  function feedback(guess, secret) {
    var res = ["-", "-", "-", "-", "-"], left = {};
    for (var i = 0; i < COLS; i++) {
      if (guess[i] === secret[i]) res[i] = "G";
      else left[secret[i]] = (left[secret[i]] || 0) + 1;
    }
    for (var j = 0; j < COLS; j++) {
      if (res[j] !== "G" && left[guess[j]] > 0) { res[j] = "Y"; left[guess[j]]--; }
    }
    return res.join("");
  }

  var tiles = [], rowEls = [];
  for (var r = 0; r < ROWS; r++) {
    var rowEl = document.createElement("div");
    rowEl.className = "row";
    tiles.push([]);
    for (var c = 0; c < COLS; c++) {
      var t = document.createElement("div");
      t.className = "tile";
      rowEl.appendChild(t);
      tiles[r].push(t);
    }
    boardEl.appendChild(rowEl);
    rowEls.push(rowEl);
  }

  var keyEls = {};
  ["qwertyuiop", "asdfghjkl", "<zxcvbnm>"].forEach(function (letters) {
    var kr = document.createElement("div");
    kr.className = "kbrow";
    letters.split("").forEach(function (ch) {
      var b = document.createElement("button");
      b.tabIndex = -1;
      var k = ch === "<" ? "enter" : ch === ">" ? "back" : ch;
      b.className = "key" + (k.length > 1 ? " wide" : "");
      b.textContent = k === "enter" ? "Enter" : k === "back" ? "⌫" : ch;
      b.addEventListener("mousedown", function (e) { e.preventDefault(); });
      b.addEventListener("click", function () { root.focus({ preventScroll: true }); press(k); });
      kr.appendChild(b);
      if (k.length === 1) keyEls[k] = b;
    });
    kbEl.appendChild(kr);
  });

  function showMsg(text, ms) {
    clearTimeout(msgTimer);
    msgEl.innerHTML = "";
    var s = document.createElement("span");
    s.textContent = text;
    msgEl.appendChild(s);
    if (ms) msgTimer = setTimeout(function () { msgEl.innerHTML = ""; }, ms);
  }

  function paint() {
    for (var c = 0; c < COLS; c++) {
      var t = tiles[row][c];
      t.textContent = cur[c] || "";
      t.className = "tile" + (cur[c] ? " filled" : "");
    }
  }

  function shake() {
    var el = rowEls[row];
    el.classList.remove("shake");
    void el.offsetWidth;
    el.classList.add("shake");
  }

  function newGame() {
    secret = WORDS[Math.floor(Math.random() * WORDS.length)];
    row = 0; cur = ""; over = false; busy = false; keyState = {}; results = [];
    for (var r = 0; r < ROWS; r++) {
      rowEls[r].className = "row";
      for (var c = 0; c < COLS; c++) { tiles[r][c].textContent = ""; tiles[r][c].className = "tile"; }
    }
    Object.keys(keyEls).forEach(function (k) { keyEls[k].className = "key"; });
    clearTimeout(msgTimer);
    msgEl.innerHTML = "";
    shareEl.textContent = "";
    root.focus({ preventScroll: true });
  }

  function finish(text) {
    over = true;
    showMsg(text);
    var lines = results.map(function (fb) {
      return fb.split("").map(function (ch) { return ch === "G" ? "🟩" : ch === "Y" ? "🟨" : "⬛"; }).join("");
    });
    var won = results[results.length - 1] === "GGGGG";
    shareEl.textContent = "EECS Day Wordle " + (won ? results.length : "X") + "/6\n" + lines.join("\n");
  }

  function submit() {
    if (cur.length < COLS) { shake(); showMsg("Not enough letters", 1200); return; }
    if (!VALID.has(cur)) { shake(); showMsg("Not in word list", 1200); return; }
    var guess = cur, r = row, fb = feedback(guess, secret);
    busy = true;
    tiles[r].forEach(function (t, c) {
      setTimeout(function () {
        t.classList.add("flip");
        setTimeout(function () { t.classList.add(CLASS[fb[c]]); }, 250);
      }, c * 300);
    });
    setTimeout(function () {
      for (var c = 0; c < COLS; c++) {
        var L = guess[c], cls = CLASS[fb[c]];
        if (!keyState[L] || RANK[cls] > RANK[keyState[L]]) {
          keyState[L] = cls;
          keyEls[L].className = "key " + cls;
        }
      }
      results.push(fb);
      row++; cur = ""; busy = false;
      if (fb === "GGGGG") { rowEls[r].classList.add("win"); finish(PRAISE[r]); }
      else if (row === ROWS) { finish("The word was " + secret.toUpperCase()); }
    }, COLS * 300 + 250);
  }

  function press(k) {
    if (over || busy) return;
    if (k === "enter") submit();
    else if (k === "back") { cur = cur.slice(0, -1); paint(); }
    else if (/^[a-z]$/.test(k) && cur.length < COLS) { cur += k; paint(); }
  }

  root.addEventListener("keydown", function (e) {
    if (e.ctrlKey || e.metaKey || e.altKey) return;
    var k = e.key === "Enter" ? "enter" : e.key === "Backspace" ? "back" : (e.key || "").toLowerCase();
    if (k === "enter" || k === "back" || /^[a-z]$/.test(k)) {
      e.preventDefault();
      e.stopPropagation();
      press(k);
    }
  });
  var newBtn = root.querySelector(".newbtn");
  newBtn.addEventListener("mousedown", function (e) { e.preventDefault(); });
  newBtn.addEventListener("click", newGame);
  newGame();
})();
</script>
"""


def play_wordle():
    """Start a game of Wordle with a random secret word from the word bank."""
    uid = "wdl" + uuid.uuid4().hex[:8]
    page = _GAME_TEMPLATE.replace("__UID__", uid).replace("__WORDS_JSON__", json.dumps(_WORDS))
    display(HTML(page))


print(f"✅ Setup complete! Saved {len(_WORDS):,} words to wordbank.txt")
