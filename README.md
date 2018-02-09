#Title  

##Purpose  
The purpose of the project is to make tabletop rpg sessions more immersive.  
The goal of the project then is to give a DM the ability to easily set the scene
and mood of a room easily. This project aims to link together various things to help achieve
this.

##Integrations  
The project should be able to do the following:  
 - Show a background image  
 - Change room light color  
 - Change room music  
The current plan is for backgrounds to be implemented by displaying them through pygame, lights
to be done through the LIFX api, and music to be done through mps-youtube.

##Scenes  
A scene is a background image along with one or more moods.  
A DM can choose a scene from the list to be brought to that scene's mood page.
Once there, the background will change to that scene's image, and the DM can
choose a mood from the list of moods associated with the scene.

##Moods  
A mood consists of background music and lighting information. A mood can have
a number of audio tracks associated with it, which loop while that mood is enabled.
Moods also have lighting affects.
