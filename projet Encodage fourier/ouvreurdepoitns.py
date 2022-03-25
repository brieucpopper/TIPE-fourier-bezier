#Imports
import json


points = open('coeffs.json')
donnéesjson = json.load(points)
print(donnéesjson)
points.close()
