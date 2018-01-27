################  CX1003 Assignment Telegram Bot #################
###########              LinguiBot                     ###########


LinguiBot is a telegram translator bot that is designed to translate foreign text to whatever language the user desires. It also acts as a middleman - translator when having conversations with a foreign acquaintance 


##################     Files & Description     ###################
Python Files .py format
1. GCloudLangList.py

	- A module created that contains all the languages supported by the Google translation API which commands will be translated into ISO-639-1 standard used by Google translation API. 
	  The dictionary contains the 'Key' and 'Value' 'Key' is the commands of the language such as /kor or /eng, while 'Value' is the ISO name google API needs requires an input"

2. LingguiBotDicts.py

	- A python file that contains 2 dictionaries created. The first dictionary "PreviewMessage" contains the messages that to be sent to the user. 
	  It also separates long messages to the user from the main program file.  
 	  The second dictionary, "CallBacklist" is used to compare with the CallBack data returned when the user clicks on the inline button in the language category menu.

3. LinguiBotInLineKeyboard.py

	-  A python file that consists of the inline button functions for the buttons of our telegram bot.

4. project_linguibot.py

	- The main program file that runs our telegram bot. 


.Json File
1. LangBot-141a526bf178.json

	- A file which the Google modules will look for in the environment variable to authenticate service files.
	  It is used to authenticate the service account that was created (gcloud console account)
	  which requires the location of specific files to check for credibility.

Word Document
1. CZ1003 Assignment translation bot documentation
	- A word documentation of our program that describes the various functions used in the program. 

##################     How to run the bot    ####################
1. Unzip the folder
2. Store all the python files and .json 
3. click on project_linguibot.py file
4. Run the main program file on Python



###################    Server Running   #########################
LinguiBot is running on AWS





¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤ Acknowledgements ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤
I would like to thank the following people who have assisted in the preparation of this Project:

•	Bryan, Leader of LoseNChill
•	Hao Jie, Chief Coder of LoseNChill
•	Darren, Assistant Chief Coder of LoseNChill
•	Alex, GrammarNazi of LoseNChill
•	Caroline, the sponsor of LoseNChill


Special thanks to:

Google for providing us with the translation API