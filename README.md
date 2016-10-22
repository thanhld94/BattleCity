# Battle City
Neural Network and/or Genetic Algorithm Project

## Goals ##
- Create the 'Battle City' game engine
- Agent will use neural network and/or genetic algorithm to learn and play the game

## Discussion
- Environment states
	- Water: can shoot through but cannot go through
	- Brick wall: can break 

## Goal:
	- Defend the homebase and destroy all the enemies

## Game engine design:
	- Environment 
		+ A board matrix contains environment details
	- Player
		+ Hooking up AI: receive environment details and return next action accordingly
	- Enemies
		+ Simple psuedo-random action
	- Main object (contains Environment, Player, Enemies)