# Designs #
 - 5 main objects: Game, GUI, Enemies, Environment, Agent

# Game Object #

## Description ##
-The Game object is the main object. It has all other objects (GUI, Enemies, Environment and Agent) as its attribute.
- Connect all elements together and run the game.
  + Creating a list of enemies objects
  + Creating initial environment
  + Creating agent
  + Controling GUI (draw, redraw ... )
  + Feeding data to each objects (environment and enemies info into Agent, environment and agent info to Enemy, environment, agent, enemies to GUI ...)
  + Checking game status (Gameover, update walls, ... ).
- Each game cycle, update bullet position and environment accordingly
  + If bullet hit brick, remove brick
  + If bullet go out side of board, remove bullet
  + If player's bullet hit enemy, destroy enemy
  + If enemy's bullet hit player, GAMEOVER

## Attributes ##
- Environment environment
- GUI Graphic
- Player agent
- List of Enemy objects

## Methods ##
- initialize(): create initial broard, enemies, agent
- run(): start game

# GUI #

## Description ##
- Create a game UI, drawing environment, players and enemies. Receiving environment, enemies and agent info from Game

## Methods ##
- constructor (Environment env, List<Enemy> enemies, Player player)
- draw(Environment env, List<Enemy> enemies, Player player)
- drawEnvironment(Environment environment)
- drawEnemies(List<Enemy> enemies)
- drawPlayer(Player player)

# Environment #

## Attributes##
- int board[][]: each cell will represent status of each cell
  + 0: empty cell (can move through, can shoot through)
  + 1: wall cell (cannot move through, break if shot)
  + 2: water cell (cannot move through, can shoot through)
  + 3: base

## Methods ##
- update(row, col): changing status of cell (row, col) to destroyed

#Enemy #

## Description ##
- A basic unit with basic pseudeo random movement. Keep moving ahead until it reaches a wall, and fire when Player oobjec the base is insight. 
- When shoot, create a new bullet object and add it to the bullet list
- This bullet list is different from the list in player

## Attributes ##
- contructor (Environment env, Player player, List<Bullet> bullets) 
- Position (row, col)
- moving direction

## Methods ##
- constructor (Environment env, Player player)
- move()

#Player #

## Description ##
- The agent object. controlling the player movement. Receving info of Environment, Enemies from Game.
- When shoot, create a new bullet object and add it to the bullet list

## Attribute ##
- position

## Methods ##
- constructor(Environment env, List<Enemy> enemies, List<Bullet> bullets)
- move()

# Bullet #

## Description ##
- A bullet object fired by a player (both enemies and player)
- Position will be updated by Game object

## Attributes ##
- Direction
- Position

## Methods ##
- move() : update position based on direction
