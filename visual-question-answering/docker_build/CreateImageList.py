import json
  
# f = open('instances_val2017.json')
# data = json.load(f)
# f.close()
  
# imgaeList=[]
# for i in data['images']:
#     imgaeList.append(i['coco_url'])

# imagejson = {
#     "imageList": imgaeList
# }
# json_string = json.dumps(imagejson)

# with open('sample_images.json', 'w') as outfile:
#     json.dump(imagejson, outfile)

f = open('sample_images.json')
data = json.load(f)
f.close()
imagelist = data["imageList"]

import random, time
seedv = int(time.time())
random.seed(seedv)
sample_list = random.sample(imagelist,3)

print(sample_list)

