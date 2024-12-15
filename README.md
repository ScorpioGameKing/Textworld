# Textworld

#### -Yet another version of Textworld.

## Foreward
  -- Now what do I mean by "another" version? Well scattered arcoss my github are various repos name
  "Textworld" this or "Heartbeat" something. There's even a few generic "Language/Service" name "engine"
  repos around. While most aren't really much and earlier projects are mostly lost at this point you can
  start to paint a picture of my interests.

  ![alt text](./git_dat/images/TextFightRunning.png)

  -- Textworld started as a small Javascript game I made years ago in middle school. It was as simple as
  you could get, Attack, Defend, Run, 3 actions and some pretty cheesy writing but it worked and it was
  a game I made, the beginning of Textworld.

  -- Textworld quickly went from a simple 3 command game to a randomly generated open world dungeon
  crawler. Towns and dungeons would spawn around a grid and you'd spawn somewhere on the map. As you
  traveled the map and slayed monsters you'd gain XP and increase your level. It wasn't much but there was
  the begining to a progression system, having been a Disgaea player most my life I wanted to have
  meaningful big numbers but it never happened.

  -- The idea of Textworld and the many versions of it stayed mostly the same for a while. Most of the major
  changes were starting in new languages and tool sets. I was and still am learning more about programming
  every time I touch the keyboard and this was a large period of trial and error learning.

  -- Then early 2024 I once again sat down and begain work on another version of Textworld. Not this one,
  my other Repo [Godot-Textworld](https://github.com/ScorpioGameKing/Godot-TextWorldRPG) was
  the project. But just before that there was one other project. A theoretical one that gave me a
  new spark and desire to work on Textworld.

  -- I'm a big fan of Rouge-likes and lites as well as old school dungeon crawlers. I'm an avid survial game
  player, randomly generated worlds can have such potential for emergent gameplay with creating bases and
  exploring for new content. I also grew up playing many a classic RPG, Final Fantasy, Dragon Quest, Disgaea,
  The Mana Series and so many more. RPGs and the stories they can tell, the many twists on scaling and
  mechanincs they can have are a huge inspiration in any project I start. Also anime and manga are an addiction

  -- But where does that actually get us? That's just a bunch of good but not immediatly compatable genres.
  What comprimise do I need to make to squeeze them together? What extra little mechanic might just make
  things pop into place? And then it happened. Dwarf Fortress came out on Steam and the idea stuck me.
  Dwarf Fortress simulates the history of it's worlds when you first create one. It places landmarks,
  simulates a few events, makes some changes, skips a few years and repeats so many times. What if I took
  that concept and expanded it into my existing Textworld idea and my personal favorites?

## The Concept

### Intial World

 -- Well I'll say it first, we get one of the most over-scoped projects I've ever managed but we also get
 what I find to be a really interesting concept. That Concept? A randomly generated Rouge-like with meta-
 progression based around the concept of a world history. You fist create a world to play in over multiple
 runs. This world has it's terrain generated, biomes set and any sort of intial terrain effects that are
 needed.

 -- After the inital world has been create we begin to work through the world placing small villages,
 large cities, fortresses and dungeons. We create some logical roads where possible and gather the intial data
 like possible spawn points, enemy lists, item lists, etc. That's the basic world made and ready to go so
 let's move on to character creation.


### Character Creation

  -- Once a world has been made you can begin making a character to use in the world. The first character
  won't have access to anything in terms of meta-progression but there's still plenty of options. You can
  Choose a name, age, race, gender, initial class, starting location amoung other options. The goal is to
  give the player full control and the ability to min-max to break the game in the end. Once we've made the
  first character you can load into the world we made where you chose to spawn.

### Gameplay Loop

  -- The turn to turn gameplay at first is meant to be very explorative. Depending on your start you may have
  different starting quests or even none. You can travel from village to village, buying goods and foraging
  to make money. Maybe you earn enough to buy a home and you choose to settle down, having children. That's a peaceful way of
  playing and is completely valid.

  -- Perhaps instead of peace you want war. You join a local mercenary group and help the local lord win a war.
  Sadly for you after that war the lord was named a traitor by the king and all those who helped him are hunted.
  Desperate you manage to persuade by force some local bandits to be your cover and slowly you come around.
  Being a bandit isn't bad, steady work, good money and no one ever lives to bother you twice.

  -- A few years and some noteriety has a bounty placed on your head. Knights slowly begin to search you out
  and challenge you, those with less honer find you late at night holding their breath you might be asleep.
  It's every second every day, the assualts never end until one day a young mercenary trying to make a name
  for himself gets the lucky blow.

  -- Good, Evil, Neutral. Peace, Chaos or Greed, any playthrough is valid and has an affect on the world.
  Depending on the Types, Number and Scales of the actions you took, the outcomes of quests, personal relationships,
  etc will all have relavent scoring. The man who settled down and raised a family? The village you choose gains
  a unique NPC or boosted population, it's neighbors gain some small boosts. The Bandit before he was labeled
  a traitor helped win a war, that lord had they not been labeld a traitor would've expaneded their territory and
  influence. After becoming a bandit they robbed and killed indiscrimently. The area around their base will
  suffer population, wealth and there will be more bandit activity.

  -- Small or large, every action you take in a run is meant to slowly build and shape a living world over
  many years. You can help raise a family of farmers to the rulers of their lord's lords over generations. You can
  slowly chip away and erase a kingdom from history by always acting against it over the years. That alone has so
  much potential for unique and varied worlds but I did mention Rouge-like, what kind of meta progression is there?

## Let's Get Meta

### The First Meta Story Idea

  -- I've had a few varied ideas for meta progression in different projects. One of my early projects in
  RPG Maker VX Ace was a game about climbing a tower. You created a hunter and entered the Tower. This Tower
  was slowly consuming part of the world, you enter through ruins descend through the mines out into the
  snow covered village in the peaks. You were just another hunter, trying to be the one who might reach
  the top and stop the world from being consumed. And then you die.

  -- Your first death lead you to an astral space, a voice from somewhere reaching out. It explains it can
  give you a boon, a brief exemption from the rules of death. The price would be high but you don't really
  have a choice. You are asked to choose a new life and you wake once more at the base of the tower.

  -- The main Meta Mechanic was the boon. With it you could change your class on death and when you chose it
  again your levels were preserved. That was neat but it meant you palyed the class that was best solo and
  maxed that out. So after a few bosses the option to begin hiring your classes with their levels as party members.
  You could hire a new level 1 or bring your lv 5 healer along with your current lv 10 knight. It was a band-aid
  but it meant you had a reason to experiment with classes again.

### The Evolution

  -- Across the weave there are many realms. Some realms like ours, some just slightly different. Many far more
  ancient or magical and just as many techologically advanced. Just outside these realms are beings of immense
  power. To some Demons, other Gods, regardless they have a will and choose to influence others to follow
  theirs. One of these beings reigns above most, the goddess of Unity. She seeks Unity through true balance.
  Good needs evil for purpose, evil needs good for resistance, she cares not for morals and only seeks to
  observe and maintain this balance.

  -- Eons ago a shadow began to seep into the weave. Unlike most Demons and Gods this wasn't from the usual
  dark corners, it seemed to simply begin to be sometime and has grown since. Realms with favor recived what
  protection their patrons could afford. Some have held to a point, many have cracked and slipped into the
  murky fade. This slow but gradual process has not escaped Unity's notice but with no method to intervene
  directly with balance falling out of order she's helpless but to watch the end.

  -- As she's watched, realms occasionally seemed to linger on, fragmented and doomed to oblivion taking those
  left. Hoping that melding and healing these fractures she begins stitching a new weave, different realms
  blened and stacked, new races and rivaling times lead to their own issues but saving life none the less.

 -- She focused on her work but the Shadow knew, it let those realms linger one, it's grasp was hard to pry.
After she'd stich a realm and place it back the Shadow would creep. Waiting and watching it'd slowly reach
back out, feeling the familiar grip as it pulls on the fragment and fresh realm it belonged to.

-- One of these worlds had a hero's soul by her standards. Not perfect but not inept. At the end of their
realm the chose to stand. Futile as it may be they stood to their last breath. Hearing the cries of this soul
told her she was to late, she'd focused on restoring without noticing what she was really using. She reached
out to this soul, she asked her champion if it would stand once more. The answer need not be heard, objection
or acceptance mattered not as the lack of extremes was what made them her champion.

-- She could not promise the soul the smae frame as it had bt it still did not matter. She gave her champion
a boon, a blessing and a curse to live amoung her falling realms forever. Doomed to forever save or scorn as
her instrument, forever striving to once again attain her true balance.

### So What Does That Mean In Gameplay Terms?

  -- In Terms of gameplay meta progression works in several ways. Every world you make has a main and shard type.
  The main type determins most normal terrain and would encounters while shards add unique spins and content
  from other mains. When a world is first made it get's a countdown clock. That is the number of years before the
  final chance to save a world is. On easier worlds this can be hundreds or even thousands of years, harder worlds
  be the same with higher scaling or have drastically shorter time til destruction. Your goal and main method
  of gaining meta progression aside from world history bonuses is to save these worlds.

  -- The Goal for saving worlds can vary from the cliche slaying a demon king to preventing the collapse of a
  nation. Even something small like raising a family status or surviving special scenarios can count. As you save
  more worlds and restore the weave Unity gains more power and can stengthen your blessings.

  -- More base health, increased damage, Base stat increases are normal choices but you can also rank up
  world and shard difficulties for greater rewards. You can also unlock and upgrade clases through class
  trees for more gameplay options.

  -- The ultimage goal of the game then becomes becoming strong enough to finally take the fight to the Shadow.
  You'll begin invading worlds that are in the fade and completeing high risk missions to pull them back as
  you dig your way down to the source of the shadow and ultimately defat it to restore the weave.
