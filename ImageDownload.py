import requests
import scrython

with open("randomMultiIds.txt") as ids:
	content = ids.readlines()

content = [x.strip() for x in content]

with open("artistNames.txt") as names:
	name_array = names.readlines()

name_array = [x.strip() for x in name_array]

count = 1
for c,name in zip(content,name_array):
	card = scrython.cards.Multiverse(id=c)
	img_data = requests.get(card.image_uris(1, 'art_crop')).content
	img_name = 'Dataset/' + name +'.'+ c.strip() + '.' + str(count )+'.jpg'
	with open(img_name, 'wb') as handler:
		handler.write(img_data)
	print(name +'.'+ c.strip() + '.' + str(count) +'.jpg')
	count += 1
