## Neural network design

### Game state
A vector of features that determines a state/ positional board

### Values
#### Position
The row and column of the agent's cell

#### Direction
The agent's current direction (0..3)
- 0: up
- 1: down
- 2: left
- 3: right

#### Enemy distance
4 values representing the distance between the agent and enemies in the 4 direction. 
If there is no enemy in a direction, that value will be INF
- e0: distance between the closest enemy above
- e1: distance between the closest enemy below
- e2: distance between the closest enemy on the left
- e3: distance between the closest enemy on the right

#### Bullet distance
4 values representing the distance between the agent and bullets in the 4 direction. 
If there is no bullet in a direction, that value will be INF
- b0: distance between the closest bullet above
- b1: distance between the closest bullet below
- b2: distance between the closest bullet on the left
- b3: distance between the closest bullet on the right

#### Available movement
4 values representing the movement availability in 4 directions
- m0: up
- m1: down
- m2: left
- m3: right
