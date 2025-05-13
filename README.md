# project.py


# PROJECT TITLE
"Python Pixel Art Application"
## Demo
Demo Video: https://youtu.be/VljludoVmX0

## GitHub Repository
GitHub Repo: (https://github.com/L-a-e/finalQuiz.py)

## Description

Use different colors and pen shapes to create a drawing of your choice. 
This drawing application should give the user the freedom to create unique, pixelated illustrations tailored to their tastes. 

Try six different colors using pygame to create a blank canvas that reads the users mouse imputs
while simultaneously implementing the color they chose.
This program calculates the position of the user's mouse and fills the desired area on a drawn grid. 
This grid rounds the position to the nearest integer, that way the drawing is crisp and pixel perfect. 

Main file: Draws each button created, refrencing each file below for variable information. 
Runs the main game loop at 60FPS and draws the specified rows and columns to create  grid. 
Updates the main program to draw a white background for a cleaar canvas. 
Initializes the grid and appends each "square" or pixel to the canvas

Init file: stores information from seetings and button file and used as reference in main file.

Settings file: Stores variables like RGB values of each color, fonts and size, 
rows and columns and much more for the main function to call upon.

Button file: Draws each button using an outline in black, which is divided 
by 2, so that only the outline is visible, and a black, fuilled in square is not present. Draws the buttons
at the bottom clearly and returns the users pos of the mouse to false if they happened to click on anything that isnt a button.


A future area this project could iprove on is the ability to change the size of the canvas on a whim, 
that way teh user may create pixel art in smaller or larger canvases. I would also liek to add more colors in the future, 
or a color picker for a more specific look.