﻿
# **Real-time GoPro image template matching**
Computer vision python program performing two tasks: the first is a training mode where
the program tries to collect template images from the homonym folder, the second is,
thanks to opencv, numpy and requests, therefore


## USAGE:
<center>*make sure your device is connected to the GoPro own wifi*</center>

### Config:
It is highly suggested to setup a virtual environment with `$> python3 -m venv myEnv`
in the folder where you want this ~~venv~~ to live, I keep them in a folder in the user
home directory and refer to them with **$HOME/..**   
### Train the code:
		open terminal application
		type "$> python3 encode.py"
		in "$> select mode:" type "sampler"
		in "$> insert photo root" type ""

	once the code is running you can take as many picture
	as you need and you will see new files being created in the
	'template' folder

	PLAY THE CODE:
		open terminal application
		type "python encode.py"
		in "select mode:" type "play"

##### I read post regarding this technique not working on HERO 7, please let me through the proposed "issues" section