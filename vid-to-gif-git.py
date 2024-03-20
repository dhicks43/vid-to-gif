import os

# Put the location of the folder full of videos here
filepath = ""

# This will put the final converted gifs into a folder called "Final" inside your folder
final_location = '{}Final/'.format(filepath)

try:
	os.makedirs(final_location)
except:
	pass

filelist = [_ for _ in os.listdir(filepath) if os.path.isfile(filepath + _)]

for file in filelist:
	# gifski uses regex to match, webm maker often uses brackets to denote timestamp, this fixes it
	workingdir = '{}temp/{}/'.format(filepath, file.rsplit(".", 1)[0].replace("[", "(").replace("]", ")"))
	try:
		os.makedirs(workingdir)	
	except FileExistsError:
		pass
	
	# Converts the video file into frames
	os.system('ffmpeg -i "{}" "{}frame%04d.png"'.format(filepath + file, workingdir))
	
	# Turns the frames into the final gif
	os.system('gifski -o "{}.gif" "{}frame*.png"'.format(final_location + file, workingdir))