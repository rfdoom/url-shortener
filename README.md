# Name of Project:

- Unique Resource Length Adjuster


## Important Use Information

- This application is used to get a short URL from a long URL and vice versa.

- I use a postgresql database here called 'all_urls', that can be changed to whatever you want as long as it's updated in the 'settings.py' under the 'proj' folder.

- This application features three pages for the user, as well as an error page:
  - HOME: This is my homepage. It features an input field to search the current database by nickname for whatever URL you want. It will return the long URL, short URL, and nickname if it is located within this database. If not, it will inform the user that that name is not in the database.

  - ENCODE: This is where you get a shortened URL. Enter the URL, including the 'https://', and a nickname you would like that URL to have once it's entered into the database. This page will throw up a warning if an entry in the database already has that nickname. It will also throw an error if the external API does not send a status code of '7'. It will give you the status code and an option to go to the API's page to find out what that status code means. If all goes well, it'll return a JSON format of your shortened URL from the external API. This page uses 'Cutt.ly' API.

  - DECODE: This is where you can expand shortened URLs. It returns a JSON format of the long URL from the external API. This page uses 'One Simple API' API.

  - ERROR: If an error occurs that I didn't plan for, it'll redirect you to the error page. This page has a three second countdown where it will send the user back to the homepage.

- I have included the keys for each external API in the 'views.py' file under the 'app' folder. I know this is a security risk, but since I don't know how this will be checked I'm leaving it there. It is a free API so I don't mind it.

- I chose not to include the CSS here. I plan to do it later on.


### TO RUN THIS PROJECT:

- First, start a virtual environment to download the dependencies.

- Next, download the 'requirements.txt' file using 'pip install -r requirements.txt'

- Finally, use the command 'python manage.py runserver' to start the Django server. It should link to your localhost. ALT + click the link in your terminal to open it.

- Use the app as you please.