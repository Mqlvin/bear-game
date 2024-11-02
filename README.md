## Bear game
A mutilplayer, text-based game I made for school.
<br>
### Storyline
It involves a murderer bear, and 3 innocent bears. The innocent bears must search the house for clues
as to whom the murderer is, avoiding the murderer's ability to fake evidence. Finally, the innocent bears
must vote on whom the murderer is.<br><br>
The storyline is procedurally generated each time the game is generated, using a list of facts and dynamically generating the bears characteristics on each game initialisation.
This means each story is relatively unique and makes the game re-playable and engaging.
<br>

### Stack
The general game is text-based, except for being able to view other bear characteristics and having a notebook of evidence collected.
<br>
Hence, I used vanilla HTML/CSS/JS with a text-based system I developed in order to easily provide a bit more functionality than a plain old CLI would.
The backend is written (scruffily) in Python using `flask` and `flask-sock` for serving the web resources and providing the websocket server.
I used this stack as it's once of the easiest and fastest ways to get functionality with as little effort as possible.
<br>

### To play
To play, clone the repository to the host PC. Run `python main.py` in the directory. 4 clients can connect to `http://<hostip>:5000` to play. You can modify `main.py` to change the port as desired.
<br>

### Images
![Example image of game 1](https://github.com/Mqlvin/bear-game/blob/master/repo/game-bear-viewer.png?raw=true)
<br>
![Example image of game 2](https://github.com/Mqlvin/bear-game/blob/master/repo/game-basic.png?raw=true)

