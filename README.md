# MewgenicsManualArchipelago
A Manual Archipelago implementation for Mewgenics

Current Ideas:
Goal: Specific Bosses or Variable Boss of Area, Depending on setting

Items:
* 3 Progressive Cat: Start with one, get up to 4
* 6 Classes, Collarless excluded, maybe also from further acts (Configurable)
* 5 Item Slots: Weapon, Head, Neck etc...
* 4 Areas: Sewers, Caves, Junk Yard, Bone Yard
* 4 Progressive Skills: Can only use x Skill if you have this unlocked
  - This is meant per Battle: Each battle, you may choose which x Skill(s) you want to use and you may only use those x Skills, where x is the amount of Progressive Skills you have
  - E.g: If you have 2 Progressive Skills, you may opt to use only Skill 2 and 4 for the first Battle, 1 and 2 for the second battle and 3 and 4 for the Boss.

Filler: Meow (Nothing)

Locations: 
* Every fight I guess? Including Hard Path??? Or should that be an extra option?
  - Maybe if you are expected to do multiple runs it would make sense to have more / configurable amount per biome
* Kill X Birds
* Bosses Could give multiple
* Events: Use of specific Stats / Run (No Stat used)
* Achieve a 1 Round win
* Achieve a 3 Round win against a Boss
* ? Revive a Cat
* ? Have 2/4/6 familiars/charmed at the same time
* ? Deal 15/20/25 damage in a single hit
* ? 3/4/5 Crits in a single combat
* ? Heal 10/15/20 hp in a single combat (excludes auto heal at end of combat)
* ? Pick up 3/4/5 items from the ground in a single combat
* ? Stack 2/3/4 different debuffs on a single enemy

Death Link Trigger:
* Cat Down
* Cat Dead
* Game over

Death Link Consequences:
* Game over
* Try to kill one of your cats or just don't use it
* Try to down one or your cats or just don't use it for combat
* Skip a turn with all cats
* Skip a turn with 1 cat

Trap: 
* Skip Turn (Current / Next Cat)
* Unequip an item for next combat 

This manual is mainly focused on Act 1 and not including progression I haven't gotten to yet. It is intended to be played with any mewgenics save, however I would recommend that you play with a copy of your save so you don't have issues with food and lose your op items or a random save (make tool)

This manual is (for now) intended to be only an honor system manual. Everything can be done in an unmodded Mewgenics game with a save file that has the areas unlocked that you define in the yaml. Default this means Up to caves and boneyard, excluding Throbbing Domain.

This also means you will NOT need the debug console / save editing / other complicated stuff.

You can just play normal Mewgenics with self imposed restrictions and external progression.

Since mewgenics is already very random I decided that I want the randomization in this to be restrictions that could make archipelago runs feel different. This is why you have restricted classes / how many cats you can take / which item slots you can fill

House Bosses are also not currently included in this manual.

Checklist when starting a run:
How many Progressive Cats do you have? You can take n+1 Cats per Progressive Cat. E.g. if you have 0, take 1 Cat, if you have 2, take 3 Cats

Which classes do you have unlocked? You can define which classes you have want to play with in the yaml. You can also define which classes you wanna start with with starting_items. It is recommended to only give yourself a max of 1-2 starting classes so each archipelago feels different because you use different class combinations

When choosing items for your cats, take into account which slots you have unlocked. You may take any items from your home, even if you don't have the slots unlocked yet, but you need to unequip them before the first battle. (You might wanna do this if you know that you will get an item slot unlocked during the run). The only exception is that you should not take cursed / items that you cannot unequip into slots you have not unlocked yet.
If you get a slot unlocked during a run, you may equip items into it.

If you are forced to equip a cursed item / parasite through an event, you're in luck, even if you don't have the slot unlocked, you may use the effects of that item .

You may only go to areas you have unlocked. In the beginning this is only The Alley.

Your goal is to beat the bosses you defined in your yaml. By default the goal is to defeat Dybbuk and Spinnerette.


Which checks to send:
* "Area Combat X" 
  - Each time you beat a combat in this area, send a check. This includes Hard combat, but not bosses or mini bosses
* "Area Hard Combat X"
  - Each time you beat a Hard Combat in this area, send a check
* "Area Mini Boss"
  - Send this check when You defeat the Area Mini Boss 
* "Area Boss" 
  - Send this check when You defeat the Area Boss 
* "Kill X Birds"
  - Each time you kill a bird, send one of these checks
* "1 Turn Win X"
  - Each time you win a Combat in Turn 1, send one of these checks
* "3 Turn (Mini-)Boss Win X"
  - Each time you win a Boss or Mini Boss Combat in or before Turn 3, send one of these checks
* "Stat Event X", e.g. Strength Event 2
  - Each time you choose this stat in an event, send one of these checks
