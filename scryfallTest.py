import scrython

with open("randomMultiIds.txt") as ids:
	content = ids.readlines()
	
content = [x.strip() for x in content]

for c in content:
	card = scrython.cards.Multiverse(id=c)
	print(card.image_uris(1, 'art_crop') + "-" + c)