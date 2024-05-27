import json
from pprint import  pprint
import http.client

conn = http.client.HTTPSConnection("moderationapi.com")


def text_analysis(text:str, userId:int, postId:int, metadata:dict, doNotStore:bool ) -> dict:
    """ Explanation:
    This function takes four arguments:
    a. img_url: the url of the image to be analysed, image should be either in .png or .jpg format.
    b. userId: User ID of the user
    c. postId: Post ID of the content
    d. metadata: Any extra information that should be provided. Should be a dictionary.
    e. doNotStore: Whether to store the content.If set to True the content won't enter the review queue.aasa
        """
    payload = {
        "value": text,
        "doNotStore": doNotStore,
        "authorId": f"{userId}",
        "contextId": f"{postId}",
        "metadata": metadata
    }

    headers = {
        "Authorization": "Bearer proj_eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY2NTQxYzBiYjBkY2Q0YmM2NTFjOWY5ZSIsInVzZXJJZCI6IjY2NTQxOTM1ZTViYTAyYjFiZjAyYTgyMiIsInRpbWVzdGFtcCI6MTcxNjc4ODIzNTQ2NCwiaWF0IjoxNzE2Nzg4MjM1fQ.uZ2VQ-D78vb1w506LY_2e78in3sVtk9hoxMqPd2lV48",
        "Content-Type": "application/json"
    }

    data = json.dumps(payload).encode("utf-8")

    conn.request("POST", "/api/v1/moderate/text", data, headers)

    res = conn.getresponse()
    data = res.read()
    data=data.decode("utf-8")
    res=json.loads(data)
    return res


