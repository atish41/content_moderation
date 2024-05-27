import http.client
import json
from pprint import pprint 
conn=http.client.HTTPSConnection("moderationapi.com")


def image_analysis(img_url:str, userId:int, postId:int, metadata:dict, doNotStore:bool ) -> dict:
    """ Explanation:
    This function takes four arguments:
    a. img_url: the url of the image to be analysed, image should be either in .png or .jpg format.
    b. userId: User ID of the user
    c. postId: Post ID of the content
    d. metadata: Any extra information that should be provided. Should be a dictionary.
    e. doNotStore: Whether to store the content.If set to True the content won't enter the review queue.
        """
    payload = {
        "doNotStore": doNotStore,
        "authorId": f"{userId}",
        "contextId": f"{postId}",
        "metadata": metadata,
        "url": f"{img_url}"
    }

    data=json.dumps(payload).encode('utf-8')
    headers = {
        "Authorization": "Bearer proj_eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY2NTQyY2YzMTVjNjNjZTc5ODEzY2MzMCIsInVzZXJJZCI6IjY2NTQxOTM1ZTViYTAyYjFiZjAyYTgyMiIsInRpbWVzdGFtcCI6MTcxNjc5MjU2MzIzNSwiaWF0IjoxNzE2NzkyNTYzfQ.89E9NWBfkI-MyPKW3VB4tC4-wAcC5AQpYvWm7lrhQrU",
        "Content-Type": "application/json"
    }
    conn.request("POST","/api/v1/moderate/image",data,headers)
    res=conn.getresponse()
    data=res.read()
    data=data.decode("utf-8")
    data=json.loads(data)
   # pprint(data)
    return data


