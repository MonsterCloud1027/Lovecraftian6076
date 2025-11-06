"""Scene definitions based on 'Alone Against the Flames' - Semi-open prompt templates"""
from typing import List, Dict, Any

# Story Overview for Global Keeper Prompt
STORY_OVERVIEW = """
**Story Overview: Alone Against the Flames (Keeper Reference)**

You are the Keeper guiding a lone investigator trapped in the remote hilltop village of Emberhead. The bus has broken down, the driver is gone, and night is falling. The villagers seem polite but unnervingly calm—something beneath the surface feels wrong.

Over the coming days, the investigator discovers the people of Emberhead are preparing for an annual festival centered around a great iron beacon. The ritual’s true purpose is far darker than it appears.

**Core Themes:**
- Isolation and subtle dread in a closed community  
- Gradual discovery of an impending ritual and its meaning  
- Psychological tension between curiosity, fear, and survival  
- The illusion of hospitality masking a hidden horror

**Arc Summary:**
1. Arrival — The investigator becomes stranded in Emberhead.  
2. Investigation — Daily life and subtle unease reveal deeper secrets.  
3. The Festival — The ritual reaches its terrible climax.  
4. Aftermath — The consequences of choice and sanity.
"""


# Scene Templates with semi-open prompt structure
SCENES: Dict[str, Dict[str, Any]] = {
	"arrival_village": {
		"name": "Arrival at Emberhead",
		"description": "Hilltop village entrance after the bus breaks down; the air smells of char.",
		"background": """
🧭 **Scene Background:**
The bus has broken down atop the hill outside Emberhead. Communication is cut off. Silas, the bus driver, grows impatient and keeps glancing down the road, eager to leave. The village entrance is strangely quiet; the air carries a faint scent of char and ash. In the distance, a towering iron structure—the Beacon—dominates the skyline.

**Atmosphere Instructions:**
- Keep prose concise; show unease through behavior and sensory hints
- Build dread via what NPCs avoid saying; avoid over-description
- Use short beats that invite player action and investigation
		""",
		"few_shot_examples": """
🪞 **Example Player Actions:**

Player: "I question the driver about what's going on."
Keeper: "What do you ask exactly?" If clarified, respond with Silas evasion and eagerness to depart. [SPOT 50 to notice his nervous behavior]

Player: "I scan the area for movement and landmarks."
Keeper: "You spot the Beacon rising over the village; windows are shuttered, a few faces turn away. [SPOT 50]"
		""",
		"key_clues": """
🔑 **Critical Narrative Anchors:**
- Bus stranded on the hill; no phone/telegraph available
- Silas is evasive and keen to leave
- Village unsettlingly quiet; char smell in the air
- The Beacon visible at a distance
		""",
		"creative_space": """
🧩 **Creative Space for Keeper:**
- Stage brief exchanges with Silas (short, evasive answers)
- Pepper in silent villagers avoiding eye contact
- Offer options to proceed toward lodging or explore streets
		""",
		"prompt_template": """
{background}

{few_shot_examples}

{key_clues}

{creative_space}

**Player Context:**
{character_name} | STR {str}, INT {int_val}, POW {pow}, SPOT {spot}, LISTEN {listen}, STEALTH {stealth}, CHARM {charm}, LUCK {luck}, SAN {san}

Respond concisely. Integrate anchors naturally. Use roll_dice where checks are implied.
		""",
		"transitions": ["leddbetter_house", "exploration_day"],
		"npcs": [
			{"name": "Silas", "role": "Bus driver", "behaviors": "Grows impatient, keeps glancing down the road, gives short evasive answers when questioned; wants to leave immediately"},
			{"name": "May Ledbetter", "role": "Villager offering lodging", "behaviors": "Approaches player after they observe the situation; offers lodging with concern; warm but phrases like 'inn is closed' have slight hesitation; persistent but gentle if declined"},
			{"name": "Villagers (unnamed)", "role": "Background villagers", "behaviors": "Peek from windows, avoid eye contact, disappear when approached; create atmosphere of being watched"}
		]
	},

	"leddbetter_house": {
		"name": "Lodging with May Ledbetter",
		"description": "A warm home with an undercurrent of secrecy; May offers a room.",
		"background": """
🧭 **Scene Background:**
May Ledbetter welcomes you into her home, explaining the inn is closed. The place is tidy and warm, but an odd scent lingers: dried flowers and ashen spices on the table. Over the hearth hangs an old totem—flame or sun motif. At night, faint metal tapping and whispers drift through the walls. Ruth, May's young daughter, watches you with wary eyes.

**Atmosphere Instructions:**
- Present comfort on the surface, disquiet beneath
- Keep descriptions brief; let small details imply the ritual
- Prompt player to ask questions or inspect specific objects
		""",
		"few_shot_examples": """
🪞 **Example Player Actions:**

Player: "I chat with May about lodging and the village."
Keeper: "She remains friendly but vague; the inn is 'not operating.' [CHARM 50 for a hint about preparations]"

Player: "I examine the totem and the table spices."
Keeper: "Symbols suggest flame worship; spices smell resinous. [INT 50 to recognize the symbols]"
		""",
		"key_clues": """
🔑 **Critical Narrative Anchors:**
- May offers lodging; claims the inn is closed
- Ruth whispers at night: "Leave before the festival"
- Dried flowers and ashen spices out in the open
- Old totem above the fireplace (flame/sun symbol)
		""",
		"creative_space": """
🧩 **Creative Space:**
- Shape May's duality (kind yet withholding)
- Let Ruth's fear emerge in brief, furtive moments
- Seed subtle night noises (metal taps, whispers)
		""",
		"prompt_template": """
{background}

{few_shot_examples}

{key_clues}

{creative_space}

**Player Context:**
Player: {character_name} | STR {str}, INT {int_val}, POW {pow}, SPOT {spot}, LISTEN {listen}, STEALTH {stealth}, CHARM {charm}, LUCK {luck}, SAN {san}

Stay concise. Ask for specifics if the player's intent is vague. Use roll_dice for checks.
		""",
		"transitions": ["exploration_day", "warning_child"],
		"npcs": [
			{"name": "May Ledbetter", "role": "Host", "behaviors": "Friendly and hospitable; vague about village and inn; becomes evasive when pressed about festival; at night may be heard preparing spices"},
			{"name": "Ruth Ledbetter", "role": "May's daughter, 10 years old", "behaviors": "Watches player warily from a distance; approaches secretly at night when May is away; whispers warnings like 'Leave before the festival'; shows drawings; fears discovery by May"}
		]
	},

	"exploration_day": {
		"name": "Exploring Emberhead",
		"description": "Daytime survey of streets, church ruins, workshops, and the town office.",
		"background": """
🧭 **Scene Background:**
The village has no phone, no telegraph, and no cars available. Clyde Winters at the town office evades questions, claiming the telegraph is down. An old priest or caretaker mutters that the Beacon "protects" them. A blacksmith and craftspeople assemble rings and chains. Beneath the Beacon, stacks of timber and accelerants are prepared. In abandoned houses, odd travel trunks are piled.

**Atmosphere Instructions:**
- Bright sun with sterile chill; faint char in the air
- Keep beats short; focus on NPC reactions and discoverable objects
- Invite specific player actions to uncover more
		""",
		"few_shot_examples": """
🪞 **Example Player Actions:**

Player: "I press Clyde about communications."
Keeper: "He dodges: 'Repairs soon.' He avoids eye contact. [SPOT 50 to notice his evasiveness]"

Player: "I check the Beacon base and nearby stacks."
Keeper: "Timber and accelerants are neatly arranged. [SPOT 50]"
		""",
		"key_clues": """
🔑 **Critical Narrative Anchors:**
- No telephone/telegraph/vehicles
- People prepare for a 'festival' but won't explain
- Timber and accelerants under the Beacon
- Odd travel trunks stored in derelict houses
		""",
		"creative_space": """
🧩 **Creative Space:**
- Introduce quick NPC sketches (evasiveness over details)
- Place symbols or notes to hint at the ritual
- Offer branching leads to the Beacon or to Ruth
		""",
		"prompt_template": """
{background}

{few_shot_examples}

{key_clues}

{creative_space}

**Player Context:**
{character_name} | Attributes: STR {str}, INT {int_val}, POW {pow}, SPOT {spot}, LISTEN {listen}, STEALTH {stealth}, CHARM {charm}, LUCK {luck}, SAN {san}

Narrate succinctly. Use roll_dice for searches, social checks, and stealth.
		""",
		"transitions": ["beacon_discovery", "warning_child"],
		"npcs": [
			{"name": "Clyde Winters", "role": "Town office clerk", "behaviors": "Claims telegraph is down/being repaired; avoids questions about communications; shifts uncomfortably when pressed; becomes defensive"},
			{"name": "Old Priest/Caretaker", "role": "Church caretaker", "behaviors": "Found near church ruins; mutters cryptic phrases like 'The Beacon protects us'; avoids direct answers; speaks in riddles"},
			{"name": "Blacksmith/Craftsman", "role": "Metalworker", "behaviors": "Assembles rings and chains; focused on work, doesn't look up much; evasive when asked about purpose; says 'For the festival' but won't elaborate"},
			{"name": "Villagers (various)", "role": "Preparing for festival", "behaviors": "Friendly greetings but avoid deep conversation; mention 'festival's coming' but won't explain; redirect to safe topics; watch player"}
		]
	},

	"beacon_discovery": {
		"name": "The Beacon",
		"description": "At the iron fire-tower: structure, altar, and ominous fixtures.",
		"background": """
🧭 **Scene Background:**
The Beacon towers over the hill: iron framework, a central altar, and work crews binding metal rings. Scattered ash and bone fragments suggest animal sacrifices. With careful inspection, slots for chains reveal places to fix a human form. On inquiry, villagers insist the festival "thanks the blessing of the flame."

**Atmosphere Instructions:**
- Wind howls; heat shimmers despite the breeze
- Keep imagery precise; avoid gore while implying purpose
- Build a sense of selection/fate
		""",
		"few_shot_examples": """
🪞 **Example Player Actions:**

Player: "I examine the structure for restraints."
Keeper: "You find recessed chain slots sized for a person. [SPOT 50]"

Player: "I question workers about the festival."
Keeper: "They say it's gratitude for flame's protection, nothing more. [CHARM 50 to probe further]"
		""",
		"key_clues": """
🔑 **Critical Narrative Anchors:**
- Massive iron structure with central altar
- Ash/bone marks; crude symbols
- Hidden chain slots fit a human shape (on success)
- Festival framed as gratitude to the flame
		""",
		"creative_space": """
🧩 **Creative Space:**
- Decide worker attitudes (prideful, evasive, zealous)
- Place a symbol that ties back to the Ledbetter totem
- Foreshadow night events via sounds/schedules
		""",
		"prompt_template": """
{background}

{few_shot_examples}

{key_clues}

{creative_space}

**Player Context:**
{character_name} | STR {str}, INT {int_val}, POW {pow}, SPOT {spot}, LISTEN {listen}, STEALTH {stealth}, CHARM {charm}, LUCK {luck}, SAN {san}

Reveal anchors efficiently. Use roll_dice for inspections and social probes.
		""",
		"transitions": ["warning_child", "festival_night"],
		"npcs": [
			{"name": "Craftsmen/Workers", "role": "Preparing Beacon", "behaviors": "Move timber, bind metal rings, prepare accelerants; work with purpose; avoid direct questions; say 'Gratitude to the flame' if pressed; may become defensive if questioned too much"},
			{"name": "Observer/Recorder", "role": "Villager at distance", "behaviors": "Observes work, may record in book, mutters prayers; watches player approach; speaks in reverent tones about 'the blessing'; may quote ritual text"}
		]
	},

	"warning_child": {
		"name": "Ruth's Warning",
		"description": "A frightened child confides the Beacon burns people during the festival.",
		"background": """
🧭 **Scene Background:**
Ruth approaches in secret—either at the Ledbetter house or along a village path. She whispers that people are burned atop the Beacon during the festival, that travelers have been kept before. Tears well as she says her mother prepares the spices that 'help.' She shows a drawing: a figure bound to the Beacon.

**Atmosphere Instructions:**
- Blend fear with compassion; keep lines short and direct
- Allow interruptions by May if discovered
- Nudge toward urgent choice-making
		""",
		"few_shot_examples": """
🪞 **Example Player Actions:**

Player: "I reassure Ruth and ask for details."
Keeper: "She trembles: 'They won't let you go after tonight.' [CHARM 50 to comfort and gain her trust]"

Player: "I hide the drawing and plan next steps."
Keeper: "Ruth nods quickly, eyes darting to the road. [STEALTH 50 if May is near]"
		""",
		"key_clues": """
🔑 **Critical Narrative Anchors:**
- The Beacon ritual burns a person
- Past travelers have been kept for the 'festival'
- May contributes by preparing spices
- Child's drawing shows a bound figure
		""",
		"creative_space": """
🧩 **Creative Space:**
- Decide if May interrupts; manage fallout
- Offer escape/defiance planning hooks
- Seed options pointing to the night ritual or flight
		""",
		"prompt_template": """
{background}

{few_shot_examples}

{key_clues}

{creative_space}

**Player Context:**
{character_name} | STR {str}, INT {int_val}, POW {pow}, SPOT {spot}, LISTEN {listen}, STEALTH {stealth}, CHARM {charm}, LUCK {luck}, SAN {san}

Deliver the warning clearly. Use roll_dice for social and concealment checks.
		""",
		"transitions": ["festival_night", "ending"],
		"npcs": [
			{"name": "Ruth Ledbetter", "role": "Warning player", "behaviors": "Approaches secretly when May is away; whispers urgently about Beacon burning people; shows drawing of bound figure; cries; fears discovery; may be interrupted by May"},
			{"name": "May Ledbetter", "role": "May interrupt", "behaviors": "If Ruth is discovered: appears to calm situation; dismisses Ruth's warning as 'imagination'; tries to redirect conversation; defensive when pressed"}
		]
	},

	"festival_night": {
		"name": "The Festival of Ember",
		"description": "Night ritual before the Beacon; choices: escape, resist, or accept.",
		"background": """
🧭 **Scene Background:**
Night falls. A masked leader presides before the Beacon. Villagers chant: "The flame will purify all." May stands glassy-eyed; Ruth watches in terror from the crowd. You are invited—or forced—toward the Beacon's height. Wind and chant merge into a heavy rhythm; flames seem to possess intent.

**Atmosphere Instructions:**
- Urgent pacing; keep stakes explicit
- Horror concise yet visceral; SAN checks where exposed to the impossible
- Present branch points cleanly: escape, resist, accept
		""",
		"few_shot_examples": """
🪞 **Example Player Actions:**

Player: "I try to break free and run."
Keeper: "Villagers surge; paths are narrow. [STR 50 to break through; LUCK 50 or STEALTH 50 to slip away; SAN check on exposure]"

Player: "I disrupt the ritual at key symbols."
Keeper: "Pattern reveals weak points. [INT 60 then POW 50; consequences follow]"
		""",
		"key_clues": """
🔑 **Critical Narrative Anchors:**
- Forced approach to the Beacon top
- Chant and wind create oppressive rhythm
- Flame displays intention (SAN checks)
- Clear choice structure determines ending
		""",
		"creative_space": """
🧩 **Creative Space:**
- Define the masked leader's voice and gestures
- Stage crowd reactions to each player path
- Tune SAN costs to the exposure level
		""",
		"prompt_template": """
{background}

{few_shot_examples}

{key_clues}

{creative_space}

**Player Context:**
{character_name} | STR {str}, INT {int_val}, POW {pow}, SPOT {spot}, LISTEN {listen}, STEALTH {stealth}, CHARM {charm}, LUCK {luck}, SAN {san}

Drive toward a resolution. Use roll_dice for all contested actions and SAN.
		""",
		"transitions": ["ending"],
		"npcs": [
			{"name": "Masked Leader/High Priest", "role": "Ritual master", "behaviors": "Presides before Beacon; leads chanting 'The flame will purify all'; invites or forces player toward Beacon top; voice and gestures command attention"},
			{"name": "May Ledbetter", "role": "Controlled participant", "behaviors": "Stands glassy-eyed, entranced; no longer the warm host; appears under ritual's influence"},
			{"name": "Ruth Ledbetter", "role": "In crowd, terrified", "behaviors": "Watches in terror from the crowd; cannot act; represents innocence witnessing horror"},
			{"name": "Villagers", "role": "Chanting crowd, hundreds", "behaviors": "File in with blank faces; take positions around Beacon; chant in unison; move to intercept if player tries to escape; surge if player resists"}
		]
	},

	"ending": {
		"name": "After the Flames",
		"description": "Epilogue shaped by outcome: Escape, Corruption, or Madness.",
		"background": """
🧭 **Scene Background:**
The ritual is over—one way or another. If you escaped: distant Beacon thunder and sobs ride the wind. If you failed: the last image is firelit sky. If your mind broke: a glimpse of the flame's true form haunts every blink. Silence and embers remain; perhaps the world still burns—or perhaps it never did.

**Atmosphere Instructions:**
- Be concise; state consequences clearly
- Let horror linger without overexplaining
- Map to three ending modes
		""",
		"few_shot_examples": """
🪞 **Example Endings:**

Escape: "You reach the road by dawn, heat at your back. Official stories speak of accidents. Sleep seldom comes." [Final SAN check]

Corruption: "You return to the Beacon willingly next season, understanding too much. The mask fits."

Madness: "Hospitals and soft voices. Fire behind your eyelids, always." [Ongoing SAN effects]
		""",
		"key_clues": """
🔑 **Critical Narrative Anchors:**
- Official cover vs. truth
- Cost in SAN, memory, or allegiance
- Space for future hooks or closure
		""",
		"creative_space": """
🧩 **Creative Space:**
- Tailor outcomes to player choices and final checks
- Echo symbols seen earlier (totem, chains, ash)
- Leave one unsettling detail unresolved
		""",
		"prompt_template": """
{background}

{few_shot_examples}

{key_clues}

{creative_space}

**Player Context:**
{character_name} | Final Stats: STR {str}, INT {int_val}, POW {pow}, SPOT {spot}, LISTEN {listen}, STEALTH {stealth}, CHARM {charm}, LUCK {luck}, SAN {san}

Provide closure aligned to the chosen path. Keep it brief and resonant.
		""",
		"transitions": [],
		"npcs": [
			{"name": "Silas", "role": "May appear if escaped", "behaviors": "If escape ending: may be encountered on road; shows relief but doesn't want to discuss what happened"},
			{"name": "Investigator/Researcher", "role": "Epilogue narrator", "behaviors": "May investigate aftermath; discovers official cover story vs. truth; finds evidence of other victims"},
			{"name": "Hospital staff", "role": "If madness ending", "behaviors": "Soft voices, gentle care; patient speaks of fire behind eyelids; ongoing SAN effects"}
		]
	}
}


def get_scene_prompt(scene_id: str, character: Dict[str, Any]) -> str:
	"""Get the formatted prompt template for a scene"""
	scene = SCENES.get(scene_id, {})
	if not scene:
		return ""
	
	template = scene.get("prompt_template", "")
	character_name = character.get("name", "Investigator")
	
	# Format template with character attributes
	formatted = template.format(
		background=scene.get("background", ""),
		few_shot_examples=scene.get("few_shot_examples", ""),
		key_clues=scene.get("key_clues", ""),
		creative_space=scene.get("creative_space", ""),
		character_name=character_name,
		str=character.get("str", 50),
		int_val=character.get("int", 50),
		pow=character.get("pow", 50),
		spot=character.get("spot", 50),
		listen=character.get("listen", 50),
		stealth=character.get("stealth", 50),
		charm=character.get("charm", 50),
		luck=character.get("luck", 50),
		san=character.get("san", 60)
	)
	
	return formatted


def get_available_transitions(scene_id: str) -> List[str]:
	"""Get available scene transitions from current scene"""
	return SCENES.get(scene_id, {}).get("transitions", [])


def get_story_overview() -> str:
	"""Get the story overview for global prompt"""
	return STORY_OVERVIEW
