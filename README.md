# Quick UI
<img src="https://user-images.githubusercontent.com/7254105/47854958-2dd7f600-de09-11e8-9e23-3f2dd7d172f5.png" align="center">
     
QuickUI is a tool to instantly create a usable UI from any python file which has a CLI created using the `Argument Parser`.  
<img src="https://user-images.githubusercontent.com/7254105/47856409-274b7d80-de0d-11e8-8844-643395054d5e.png">
 
With it, you know exactly what parameters need to be passed to the program while running it.
<img src="https://user-images.githubusercontent.com/7254105/47855319-4ac0f900-de0a-11e8-82ed-f7421383cdb4.png">

It not only creates a beautiful UI, but adds `static checks on data types` as well. Along with the checks, it
auto-fills the entries with `default values` and can also show `help` fields as a placeholder. 
<img src="https://user-images.githubusercontent.com/7254105/47855736-5eb92a80-de0b-11e8-9195-3665f7d0dd06.png">

In case, your parser mentions that a particular field is required, `QuickUI` adds a compulsory check as well.
<img src="https://user-images.githubusercontent.com/7254105/47855858-b22b7880-de0b-11e8-940e-2c6b39efb771.png">

Once all the required criterion is met, you can use quickUI to run the program and view the output in a 
friendly `terminal like interface!` 
<img src="https://user-images.githubusercontent.com/7254105/47856077-51e90680-de0c-11e8-883e-dc3b8276cfe6.png">

A user can run the code multiple times (ofcourse, by changing the arguments). QuickUI maintains a `history` so that it is easy for a user to distinguish 
between runs. Every run also contains the command that was finally run on your system as a separate thread.
<img src="https://user-images.githubusercontent.com/7254105/47856152-82c93b80-de0c-11e8-976b-601a8aa61099.png">

In case there is an error, it will be shown in the interface itself highlighted in red!
<img src="https://user-images.githubusercontent.com/7254105/47856737-ebfd7e80-de0d-11e8-96a8-d8c50290d18a.png">

Another cool thing that you can do with this tool is, since it exposes a server, you can instantly `ngrok` it.
So, in case there is a python file which you need to run on your system, you can run the server and host it over the internet.
The QuickUI dashboard is `Mobile Friendly` which will make it possible for you to run your scripts from your phone!  
<img src="https://user-images.githubusercontent.com/7254105/47857353-67136480-de0f-11e8-83f3-fc0f7332f6c2.png" width="200">

## How does it work?
QuickUI statically traverses your code to find out code segments where `Argument Parser` is being used. 
We perform a Breadth First Search on its `Abstract Syntax Tree`.

It records data types, help boxes, required fields, choices, etc. It can handle all data types supported by Argument Parser.

Once the parameters are finalized, they are rendered using a Flask Server. The user can fill in the form and run the code in the browser itself
`jquery-terminal.js` is being used to render the output. 


## Usage
Till it is pushed onto pypi, you can use it by following these steps -
### Step 1: Clone the Repo
`git clone https://github.com/cardwizard/QuickUI`
### Step 2: Install the requirements
`pip install -r requirements.txt`
### Step 3: Run quickUI. Pass path to your python file
`python -m quickui my-awesome-python-file.py`
### Step 4: Access the UI
Hit `http://localhost:8765` to access the QuickUI dashboard


## Developer
[Aadesh M Bagmar](https://github.com/cardwizard)
 