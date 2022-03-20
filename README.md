# Smart Cyclette Webcam only Adapter for Gaming

How fun would it be to play a racing game where you need to actually pedal in real life to accelerate in the game? This simple software uses a webcam as a binary sensor to detect the pedal turning to allow a fun cycling/videogaming experience.

## Set-up

A USB webcam should be placed looking at any place in the rotation of the pedal of the cyclette. The webcam will see the change in light level when the pedal passes acting as a binary sensor, at each pass the "energy" will increase. The program will press the left mouse button as long as you have "energy" where energy is recharged while pedalling and also lost over time. This software has been tested emulating the video-game "Mario-Kart" on the Dolphin emulator with costum controls, using an XBOX-one controller for all except accelerating and the left mouse click (simulated by the script while pedalling) for accelerating.
