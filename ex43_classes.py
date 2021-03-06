from sys import exit
from random import randint

class Scene(object):

	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."
		exit(1)

class Engine(object):
	def __init__(self,scene_map):
		self.scene_map = scene_map

	def play(self):
		currnet_scene = self.scene_map.opening_scene()
		while currnet_scene != None:
			print "\n_________"
			next_scene_name = currnet_scene.enter()
			current_scene =  self.scene_map.next_scene(next_scene_name)

class Death(Scene):

	quips = [ "You died.You kinda suck at this.",
					"Your mom would be proud... if she were smater.",
					"Such a lusr.",
					"I have a small puppy that's better at this."
			]

	def enter(self):
		print Death.quips[randint(0,len(self.quips)-1)]
		exit(1)

class CentralCorridor(Scene):

	def enter(self):
		print "The Gothons of planet #25 have invaded your ship and destroyed"
		print "you entire crew.you are the last surviving member and your last"
		print "Missition is to get the neutron destrut bomb from the weapons armory,"
		print "put it in the bridge ,and blow the ship up after getting into an "
		print "escape pod."
		print "\n"
		print "You're running down the central corrider to Weapons Armory when"
		print "a Gothon jumps out,red scaly skin ,dark grimy teeth,and evil clown costure"
		print "flowing around his hate filled body.He's blocking the door t the"
		print "Armory and about to pull a weapon to blast you."

		action = raw_input(">")
		
		if  action == "shoot":
			print "Quick on the draw you yank out your blaster and fire it at the Gothon."
			print "His clown costume is flowing and moving around his body,which throws"
			print "off your aim.Your laser hits his costume but misses him entirely .This"
			print "completely ruins his brand new costume his mother bought him,which"
			print "makes him fly into a rage and blast you repeatdly in the face untill"
			print "You are dead.Then he eats you"
			return "death"

		elif action == "dodge!":
			print "Like a world class boxer you dodge weave slip and slide right"
			print "as the Gothon's blaster crnaks a laser past your head."
			print "In the middle of your head on the metal wall and pass out."
			print "bang your head on the metal wall and pass out."
			print "you wake up shortly after only to die as the Gothon stomps on"
			print "your head and eats you."
			return "death"

		elif action == "tell a joke":
			print "Lucky for you they made you learn Gothon insults in the academy."
			print "You tell the one Gothon joke you know:"
			print "Lbhe zbgure vf fb sng,jura fur fvgf nebhaq gur ubhfr,fur fvgf nebhaq gur ubhfr."
			print "The Gothon stops ,tries not to laugh ,then busts out laughing and can't move."
			print "While he's laghing you run up and shoor him square in the head"
			print "putting him down ,then jump through the Weapon Armory."
			return "laser_weapon_armory"
		else:
			print "DOES NOT COMPUTE!"
			return 'cetral_corridor'

class LaserWeaponArmory(Scene):
	
	def enter(self):
		print "you do a dive roll into weapon Armory,crouch and scan the room"
		print "for more Gothons that might be hding.It's dead quiet."
		print "You stand up and run to the far side of the room "
		print "get the bomb. The code is 3 digits."
		code = "%d%d%d" % (randint(1,9) ,randint(1,9),randint(1,9))
		guess = raw_input("[keypad>")
		guesses = 0

		while guess != code and guesses < 10:
			print "BZZZZEDDDD!"
			guesses += 1
			guess = raw_input("[keypad]>")

		if guess == code:
			print "The container clicks open the seal breaks,letting gas out."
			print "You grab the neutron bomb and run as fast as you can to be"
			print "bridge where you must place it in the right spot."
			return 'the_bridge'
		else:
			print "The lock buzzes one last time and then you hear a sickening"
			print "melting sound as the mechanism is fused together."
			print "You decide to sit there,and fianlly the Githins blow up the"
			print "ship from their ship and you die ."
			return 'death'



class TheBridge(Scene):
	
	def enter(self):
		print "You burst onto the bridge with the neutron destruct bomb"
		print "under your arm and surprise 5 Gothons who are trying to"
		print "take control of the ship .Each of them has an even uglier"
		print "clown costume than the last.They haven't pulled their"
		print "weapons out yet, as they see the active bomb under your"
		print "arm and don't want to set it off."


		action = raw_input(">")
		if action == "throw the bomb":
			print "In a panic you throw the bomb at the group of Gothons"
			print "and make a leap for the door .Right as you drop it a"
			print "Gothon shoots you right in the back killing you."
			print "As you die you see another Gothon frantically try to disarm"
			print "the bomb.You die knowing they will probably blow up when"
			return 'death'

		elif action == "slowly place the bomb":
			print "You point your blaster at the bomb under arm"
			print "and the Gothons put their hands up and start to sweat."
			print "get off this tin can."
			return 'escape_pod'
		else:
			print "DOES NOT COMPUTE!"
			return 'the_bridge'	

class EscapePod(Scene):
		
	def enter(self):
		print "You rush through the ship desperately trying to  make it to"
		print "the escape pod before the whole ship explodes.It seems like"
		print "hardly any Githins are in the ship,so your run is clear of"
		print "iterference .You get to the chamber with the escape pods, and"
		print "now need to pick one to take.Some of them could be damaged"
		print "do you take?"

		good_pod = randint(1,5)
		guess = raw_input("[pod #]>")
	
		if int(guess) != good_pod:
			print "You jump into pod %s and hit the eject button ." % guess
			print "The pod escapes out into the void of psace then"
			print "implodes as the hull ruptures,crushing your body"
			return 'death'
		else:
			print "You jump into pod %s and hit the eject button." % guess
			print "The pod easily slides out into space heading to"
			print "the planet below.As it flies to the planet ,you look"
			print "back and see your ship implode then explode like a"
			print "bright star,taking out the Gothon ship at the same"
			print "time.You won!"
			
			return 'finished'

class Map(object):
	
	scenes = { 
				'central_corridor': CentralCorridor(),
				'laser_weapon_armory': LaserWeaponArmory(),
				'the_bridge': TheBridge(),
				'escape_pod': EscapePod(),
				'death': Death()
	}

	def __init__(self,start_scene):
		self.start_scene = start_scene

	def next_scene(self,scene_name):
		return Map.scenes.get(scene_name)
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
