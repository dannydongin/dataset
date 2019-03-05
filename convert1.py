import glob, os
# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)

target_dir = '/content/darknet/dataset/img/'
# Percentage of images to be used for the test set
percentage_test = 10;
# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')  
file_test = open('test.txt', 'w')
# Populate train.txt and test.txt
counter = 1  
index_test = round(100 / percentage_test)  

current_dir += "/img"
dir_list = os.listdir(current_dir)
for directory in dir_list:
	new_current_dir = current_dir+"/"+directory
	new_target_dir = target_dir +directory
	print(new_current_dir)


	for pathAndFilename in glob.iglob(os.path.join(new_current_dir, "*.jpg")):  
	    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
	    if counter == index_test:
	        counter = 1
	        file_test.write(new_target_dir + "/" + title + '.jpg' + "\n")
	    else:
	        file_train.write(new_target_dir + "/" + title + '.jpg' + "\n")
	        counter = counter + 1