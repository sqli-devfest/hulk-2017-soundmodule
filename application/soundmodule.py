import pygame
import paho.mqtt.client as mqtt
import json
import traceback
import os

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("results")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    try:
        parsed_message = json.loads(msg.payload.decode('utf-8'))
        rank = (parsed_message['game'])['rank']
        print("rank "+ str(rank))

        if rank < 4:
            bad_sound.play()
        elif rank < 8:
            average_sound.play()
        else:
            great_sound.play()

    except Exception:
        traceback.print_exc()
        traceback.print_stack()



pygame.mixer.init()
bad_sound = pygame.mixer.Sound("sounds/sad_trombone.ogg")
average_sound = pygame.mixer.Sound("sounds/evil_laugh.ogg")
great_sound = pygame.mixer.Sound("sounds/cheering3.ogg")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt", 1883, 60)
client.loop_forever()
