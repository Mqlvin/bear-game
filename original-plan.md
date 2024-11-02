## Bear game

Bear cluedo

Multiple rooms.. in text based game.

Multiplayer. Procedurally generated rooms or story ? but no graphics

You collect items to solve a murder.. could be multiplayer?

Turn based game.. items are procedurally placed around the map. You must take it in turns to move around the map and make queries.
Inventory based items can be collected and shared between players.

Turn can consist of:
- Sharing information (or inventory)
- As for the murderer, he can fake information and plant it in the house
- Moving between rooms / searching
- Making an accusation

The murderer or players can make accusations.
Per accusations, players must vote on whether they believe the murderer is the accused person or not. The vote decides. The muderer wins if the players vote wrong. The murderer loses if the players vote write.


Websocket server handles all controls. It parses and dispatches messages. The client should have as little functionality as possible to couple the important things together.
<br>
<br>
<br>
On screen, text should be on the left and the right will be filled with notes.
I'll start on the back end today. And decide whether the frontend should be HTML / CSS or cli. (maybe a cool terminal cli with graphics on the right?)

Only 1 active game. Socket servers gets 4 people the ignores all incoming connections.
Game starts by assigning 4 people their names / murdererorinnocent.
The murderer can make fake items to share with the innocents..

