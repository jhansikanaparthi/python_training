# ---------
# Creating GIT Version Control System in our laptop
###########
# 1. download and install git software
#   https://git-scm.com/downloads
#
# 2. We create repository using
#   OPTION-1: git UI
#   OPTION-2: Command line
#
#   We are using OPTION-2: Command line
#
#
# 3. making python_training folder as GIT repository
#       Step-1: open command prompt
#       Step-2: cd (Change Directory) to C:\python_training folder
#       Step-3: git init
#       .git folder will create
#       NOW, python_training folder is GIT repository
#
# 4. 'add' and 'commit' all files and folders to newly created repository 'python_training'
#       Step-1: git add bin log practice programs rest_api Readme.txt
#       Step-2: git commit -m "Added all files and folders to local git repository"
#       DONE.. All files are now in git repository
############################
# ----------
# Create Github Repository
# ----------
# 1. create account in https://github.com/
#
# 2. create new repository 'python_training'
#
############################
# ----------
# Link local repository(Laptop) to github repository
# ----------
#
# git remote add origin https://github.com/mahadevaprabhug/python_training_8.git
#// My link//https://github.com/jhansikanaparthi/python_training
############################
# ----------
# PUSH code from local repository(Laptop) to github repository
# ----------
#
# git push -u origin master
#
############################

# ----------
# PULL trainer code
# ----------
# Step-1: create new directory 'trainer_programs'
#
# Step-2: make 'trainer_programs' as git repository
#       git init
#
# Step-3: link local repository to trainer git repository
#       git remote add origin https://github.com/mahadevaprabhug/python_training_8.git
#
# Step-4: git pull origin master
############################
