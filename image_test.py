from image import image_analysis
from pprint import pprint

#Sample content  information
img_url="https://media.istockphoto.com/id/1425167608/photo/a-man-holding-a-gun-in-his-hand-behind-his-back-close-up-view-concepts-crime-attempted-murder.jpg?s=2048x2048&w=is&k=20&c=QME4VQChFChQ7HjeWpympnpqHeZ2kkWFAdcXrkh3tfQ="
doNotStore=False
userId=1
postId=123
metadata={}

#Using the image analyser
res=image_analysis(img_url, userId, postId,metadata,doNotStore)
pprint(res)

"""Sample response =  
{'contentId': '664da2aed30311e865dd58b8',
 'flagged': True,
 'labels': [{'label': 'weapon', 'score': 0.999579},
            {'label': 'violence', 'score': 0.905955},
            {'label': 'gore', 'score': 0.002342},
            {'label': 'suggestive', 'score': 0.000183},
            {'label': 'nudity', 'score': 0.000112},
            {'label': 'drugs', 'score': 3.9e-05},
            {'label': 'smoking', 'score': 2.7e-05},
            {'label': 'hate', 'score': 1.7e-05},
            {'label': 'alcohol', 'score': 5e-06}],
 'request': {'quota_usage': 3, 'timestamp': 1716363950195},
 'status': 'success',
 'texts': []}"""

if res['flagged']==True:
  #Block the content
  print("Inappropriate content")
else:
  #Pass it normally
  print("Content posted to the platform")
  



