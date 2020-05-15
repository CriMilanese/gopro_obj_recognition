
# **Real-time GoPro image template matching**
Computer vision python program performing two tasks: the first is a training mode where
the program tries to collect template images from the homonym folder, while the latter is,
thanks to **opencv**, **numpy** and **requests**, making them dependencies, computing a 2D convolution over all the image for different scales, this is technically called our _kernel_. once found the program limitates itself to creating a file showing off its computed rectangle around the object.

### Config:
It is highly suggested to setup a virtual environment with `$> python3 -m venv myEnv`
in the folder where you want this _venv_ to live, I keep them in a folder in the user
home directory and refer to them with **$HOME/..**.
I find useful having an **activate** alias pointing at the correct binary given the
project name in _.bashrc_aliases_.

## Usage:
<center>**make sure your device is connected to the GoPro own wifi**</center>
<center>I experienced unstable connection that would suddently quit</center>

### Train the code:
		open terminal application
		`$> python3 encode.py`
		`$> select mode:" type "sampler"`
		`$> insert photo root...`
it should be standard to 10.5.5.9:8080 so then you only have to point to a
folder, for me it is `/videos/DCIM/105GOPRO/`, mind that the camera firmware updates
might change this address.

once the code is running you can take as many picture
as you need and you will see new files being created in the
'template' folder. Try to find a location at least similar to the one you will deploy at, in order to avoid all the risks that lights and shadows bring about.

### Play the code:
open terminal application \n
type `$> python encode.py` \n
in "select mode:" type "play" \n
This tool saves the kernels in lighter format and different resolution for memory sake, it also download each photo only once before deleting it.
**feature missing**
the possibility to save files locally


##### I read post regarding this technique not working on HERO 7, please let me through the proposed "issues" section
