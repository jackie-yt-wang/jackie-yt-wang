##########################################################
# SET DEFAUL VARIABLES

filenametime=$(date +"%m%d%Y%H%M%S")

#########################################################
# SET VARIABLES 
export BASE_FOLDER=$GITHUB_WORKSPACE
# export BASE_FOLDER='/Users/apple/Desktop/DataEngineeringBootCamp/GithubProfile/jackie-yt-wang'
export SCRIPTS_FOLDER=${BASE_FOLDER}'/scripts'
export LOGDIR=${BASE_FOLDER}'/logs'
export SHELL_SCRIPT_NAME='update_github_readme'
export LOG_FILE=${LOGDIR}/${SHELL_SCRIPT_NAME}_${filenametime}.log
export PYTHON_SCRIPT='update_weather.py'
#########################################################

# SET LOG RULES
exec > >(tee ${LOG_FILE})
exec 2> >(tee ${LOG_FILE})

#########################################################
# RUN PYTHON
echo 'Install necessary Python Libraries'
pipenv install
echo "Start to run Python Script and Update ReadMe"
pipenv run python3 ${SCRIPTS_FOLDER}/${PYTHON_SCRIPT}

RC1=$?
if [ ${RC1} != 0 ];
then
	echo "PYTHON RUNNING FAILED"
	echo "[ERROR:] RETURN CODE:  ${RC1}"
	echo "[ERROR:] REFER TO THE LOG FOR THE REASON FOR THE FAILURE."
	exit 1
fi

echo "PROGRAM SUCCEEDED"

exit 0 