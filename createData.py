from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog
import random

kevArray = []
peteArray = []
johnArray = []
christopherArray = []
gregArray = []
ronArray = []
markArray = []
carlArray = []
heatherArray = []
robArray = []

cardNames = []

kevcards = Card.where(artist='Kev Walker').all()
for card in kevcards:
	if(card.multiverse_id != None and card.cmc != 0 and card.name not in cardNames):
		cardNames.append(card.name)
		kevArray.append(card.multiverse_id)

print("Kev array count : " + str(len(kevArray)))
cardNames.clear()

petecards = Card.where(artist='Pete Venters').all()
for card in petecards:
	if(card.multiverse_id != None and card.cmc != 0 and card.name not in cardNames):
		cardNames.append(card.name)
		peteArray.append(card.multiverse_id)

print("Pete array count : " + str(len(peteArray)))
cardNames.clear()

johncards = Card.where(artist='John Avon').all()
for card in johncards:
	if(card.multiverse_id != None and card.cmc != 0 and card.name not in cardNames):
		cardNames.append(card.name)
		johnArray.append(card.multiverse_id)

print("John array count : " + str(len(johnArray)))
cardNames.clear()

christophercards = Card.where(artist='Christopher Moeller').all()
for card in christophercards:
	if(card.multiverse_id != None and card.cmc != 0 and card.name not in cardNames):
		cardNames.append(card.name)
		christopherArray.append(card.multiverse_id)

print("Christopher array count : " + str(len(christopherArray)))
cardNames.clear()

gregcards = Card.where(artist='Greg Staples').all()
for card in gregcards:
	if(card.multiverse_id != None and card.cmc != 0 and card.name not in cardNames):
		cardNames.append(card.name)
		gregArray.append(card.multiverse_id)

print("Greg array count : " + str(len(gregArray)))
cardNames.clear()

roncards = Card.where(artist='Ron Spencer').all()
for card in roncards:
	if(card.multiverse_id != None and card.cmc != 0 and card.name not in cardNames):
		cardNames.append(card.name)
		ronArray.append(card.multiverse_id)

print("Ron array count : " + str(len(ronArray)))
cardNames.clear()

markcards = Card.where(artist='Mark Tedin').all()
for card in markcards:
	if(card.multiverse_id != None and card.cmc != 0 and card.name not in cardNames):
		cardNames.append(card.name)
		markArray.append(card.multiverse_id)

print("Mark array count : " + str(len(markArray)))
cardNames.clear()

carlcards = Card.where(artist='Carl Critchlow').all()
for card in carlcards:
	if(card.multiverse_id != None and card.cmc != 0 and card.name not in cardNames):
		cardNames.append(card.name)
		carlArray.append(card.multiverse_id)

print("Carl array count : " + str(len(carlArray)))
cardNames.clear()

heathercards = Card.where(artist='Heather Hudson').all()
for card in heathercards:
	if(card.multiverse_id != None and card.cmc != 0 and card.name not in cardNames):
		cardNames.append(card.name)
		heatherArray.append(card.multiverse_id)

print("Heather array count : " + str(len(heatherArray)))
cardNames.clear()

robcards = Card.where(artist='Rob Alexander').all()
for card in robcards:
	if(card.multiverse_id != None and card.type != "" and card.name not in cardNames):
		cardNames.append(card.name)
		robArray.append(card.multiverse_id)

print("Rob array count : " + str(len(robArray)))
cardNames.clear()

numToSelect = 125

allCards = []
kevRandom = random.sample(kevArray, numToSelect)
peteRandom = random.sample(peteArray, numToSelect)
johnRandom = random.sample(johnArray, numToSelect)
christopherRandom = random.sample(christopherArray, numToSelect)
gregRandom = random.sample(gregArray, numToSelect)
ronRandom = random.sample(ronArray, numToSelect)
markRandom = random.sample(markArray, numToSelect)
carlRandom = random.sample(carlArray, numToSelect)
heatherRandom = random.sample(heatherArray, numToSelect)
robRandom = random.sample(robArray, numToSelect)

allCards = kevRandom + peteRandom + johnRandom + christopherRandom + gregRandom + ronRandom + markRandom + carlRandom + heatherRandom + robRandom

file = open("randomMultiIds.txt","w")
for line in allCards:
	file.write(str(line) + "\n")
file.close()