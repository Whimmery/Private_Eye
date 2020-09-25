# Private_Eye Read Me

Welcome to the Private_Eye Webcrawler ReadMe.

Here is the Set Up and TroubleShooting Section:

************************************************************************************
    Welcome!

    This is the Private_Eye's Help Page.

    ***Commands***

    Type "help" for command details, and bug solutions.    

    Type "scout" for a single keyword search.

    Type "snipe" to look url combined with keyword search.

    Type "heavy" to look for url combined with 2 keyword search.

************************************************************************************
    ***How To Set Up Your Search***

    *(((((UNTIL PACKAGE VERSION IS FINISHED))))* 
    	Add libraries/modules to python using pip
    	-selenium,pandas,time,sys,os, and io
   	-_init__.py currently holds the script to run Private_Eye webcrawler
    -First go into the Private_Eye folder and find the "url-list"
      and add urls in the column "website_link"
    -Do not remove or put urls in the frame that says "website_link"
      the code is reading the name of "website_link" to run the code
    -Close the "url-list" so the program can pull from it without error
    -Open up a terminal and run software as "python private_eye"
    -Type in the command once the software asks for input
    -If selecting one of the 3 search commands,
      wait for program to start search if it delays,
      a Google Chrome window should appear





************************************************************************************
    ___ ____ ____ _  _ ___  _    ____ ____ _  _ ____ ____ ___ _ _  _ ____ 
     |  |__/ |  | |  | |__] |    |___ [__  |__| |  | |  |  |  | |\ | | __ 
     |  |  \ |__| |__| |__] |___ |___ ___] |  | |__| |__|  |  | | \| |__] 

************************************************************************************
~VERSION 0.2.3~

            (  )   (   )  ) 
             ) (   )  (  (  
             ( )  (    ) )  
             _____________  
            <_____________> ___  
            |             |/ _ \  
            |    You're     | | |  
            |    Doing      |_| |  
         ___|    Great!   |\___/  
        /    \___________/    \  
        \_____________________/  

****For troubleshooting errors that is not on this list contact: Rhea Santos ****

***Problem 0: "Nothing is happening when I type a search command"

-Solutions:
    -Go into the folder and check the webbrowser's driver
    -Check to see if the webbrowser's driver is same version
      as the Google Chrome running
    -If you are running a Mac or PC Desktop,
      you will need to probably need a new driver that matches your OS
    -If the version is the same as Google's web browser and OS,
      you will need to delete the driver and reinstall the version as a clean install
       Downlod from here-  https://chromedriver.chromium.org/downloads



***Problem 1: "Nothing is saving in outputted Excel sheet"

-Solutions:
    -Check the keyword is written properly 
    (it does not like \, do not feed keywords with a \ or program won't work at all)
    
    -Make sure in the Excel sheet "url-list" the column "website_link"
     is defined as "website_link" in Name Manager 
    
    -Do the same thing for "Name" column in checking the Excel Sheet-
     for "Name" being in Name Manager
    
    -Delete and rename/readd to Name Manager the columns for a clean retry



***Problem 2: "Typed a new keyword but no new results are saving in outputted Excel sheet"

-Solutions:
    -Go through same troubleshooting steps as of "Problem 1"
    
    -Most often problem is the keyword count is not correct
    
    -Second most reoccuring problem is that the Name Manager 
    "website_link" needs to be renamed again in "url-list" template



***Problem 3: "Keep getting same results for outputted Excel Sheet "

-Solutions:
    -"url-list" Template Sheet needs updated 
     with a new list of urls you are looking for

    -Open url-list to copy and past list of new urls 
     under the frame named "website_link"

    -Do not get rid of frame called "website_link", 
     code is using it to read the urls in that column

    -Make sure every url in list has "https://" infront of the links and a " /", 
     or urls will not be recognized as urls and no search done on them



***Problem 5: "It's taking me forever to make a url list to copy and paste 
                in the "url-list" section of the input Excel Sheet Template! HELP!!!"

-Solutions:

    -No worries, there is an easier way
    -Download Notepad++
    -Paste url list you want to add "https://" and the "/" at the end.

    -Windows: Press Ctrl + H
    -"Replace" box will appear, make sure "Search Mode" is set to "Regular Expression"
    -In the "Find What:", type " ^ ", and in the "Replace with: ", type " https:// "
    -Click "Replace All" and all the urls will have " https:// " infront of the urls
    -Next: In the "Find What:", type " $ ", and in the "Replace with: ", type " / "
    -Click "Replace All" and all the urls will have " / " behind the urls
    -You should have a list ready to copy and paste in the section "website_link" in the "url-list" Excel Sheet Template


    -Mac: Press- 
            There isn't a Mac version of Notepad++
    -Try either finding alternative software 
    -Or use Excel macros to make separate columns to manually make " https:// " and " / " by using =CONCATENATE
    -And copy and Paste Special options that copys all the features, 
    -Keep merging and concatenate-ing till you have the url list set to look like " https://examplewebsite.com/ "

      
************************************************************************************  
    ___ _  _ ____ _  _ _  _    _   _ ____ _  _   /
     |  |__| |__| |\ | |_/      \_/  |  | |  |  / 
     |  |  | |  | | \| | \_      |   |__| |__| .  


************************************************************************************

License Open Source
-------

Have fun!