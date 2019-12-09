from omxplayer import OMXPlayer 

def play(path, stop):
    player = OMXPlayer('fromYoutube.mp4') 
    player.play()
    while player.is_playing:
        if stop == True:
            break
    player.quit()
def stop():
    global player
    player.stop()

class player(threading.Thread):
    def __init__(self, path, stop):
        threading.Thread.__init__(self)
        self.path = path
        self.stop = stop
    
    def run(self):
        play(self.path, self.stop)