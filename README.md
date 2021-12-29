# URLShorten
URL shortener written in python
Used a dictionary to store key-value pairs
Stored the Dictionary as a JSON file to save entries between sessions

## How to Use:
Once the program is running, there will be several commands you can use:
 - Store
   - Syntax:  'store' [URL]
   - generates and displays a keyword/shortened url
 - Key
   - Syntax:  'key' [key]
   - opens the website pointed to by the key
 - Keys
   - Syntax:  'keys'
   - displays all the key-value pairs available at the moment
 - Browse
   - Syntax:  'browse' [URL]
   - opens the website
 - Exit
   - closes the program

## Libraries used:
  - webbrowser
  - random + string
  - json

## Webbrowser
  allowed me to open up url's in my web browser

## Random + String
  allowed me to generate random strings to use as my dictionary keys/shortened URL's
  
## Json
  gave me easy to use file I/O to store my dictionary as a JSON file in between sessions

### Pylint.jpeg
  pylint evaluation of my source code
  
### PythonProject.jpeg
  example of program opening up a shortened URL in my webbrowser
  browser pointed to by 'path' variable
