# Designs#
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
    + Checking game status (Gameover, update walls, ... )
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

# Enemy #
## Description ##
  - A basic unit with basic pseudeo random movement. Keep moving ahead until it reaches a wall, and fire when Player oobjec the base is insight. 
## Attributes ##
  - Position (row, col)
  - moving direction
## Methods ##
  - constructor (Environment env, Player player)
  - move()

# Player #
## Description ##
  - The agent object. controlling the player movement. Receving info of Environment, Enemies from Game.
## Attribute ##
  - position ##
## Methods ##
  - constructor(Environment env, List<Enemy> enemies)
  - move()
