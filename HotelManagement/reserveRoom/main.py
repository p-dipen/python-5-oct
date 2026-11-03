import constant
currentRevereRoom = 4

def reserveRoom(rooms):
    if rooms + currentRevereRoom > constant.ANNUAL_ROOM:
        return "Cannot reverse the room we dont have that much availability"
