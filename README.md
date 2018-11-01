# Quick UI

UI to CLI in 1 click
---

![](QuickUI.png)
     
QuickUI is a tool to instantly create a usable UI from any python file which has a CLI created using the `Argument Parser`.  
<img src="https://user-images.githubusercontent.com/7254105/47856409-274b7d80-de0d-11e8-8844-643395054d5e.png">


## Usage

### Step 1: Clone the Repo
`git clone https://github.com/cardwizard/QuickUI`
### Step 2: Install the requirements
`pip install -r requirements.txt`
### Step 3: Run quickUI. Pass path to your python file
`python -m quickui my-awesome-python-file.py`
### Voila! Access the UI
Hit `http://localhost:8765` to access the QuickUI dashboard
 
# Simple, Easy, Quick!
With it, you know exactly what parameters need to be passed to the program while running it.
<img src="https://user-images.githubusercontent.com/7254105/47855319-4ac0f900-de0a-11e8-82ed-f7421383cdb4.png">

## Demo friendly!
Once all the required criterion is met, you can use quickUI to run the program and view the output in a 
friendly `terminal like interface!`. This is great for early internal demos. 
<img src="https://user-images.githubusercontent.com/7254105/47856077-51e90680-de0c-11e8-883e-dc3b8276cfe6.png">

## In-built Static Type Checking
QuickUI adds `static checks on data types` as well. Along with the checks, it
auto-fills the entries with `default values` and can also show `help` fields as a placeholder. 
<img src="https://user-images.githubusercontent.com/7254105/47855736-5eb92a80-de0b-11e8-9195-3665f7d0dd06.png">

## Required*
In case, your parser mentions that a particular field is required, `QuickUI` adds a compulsory check as well.
<img src="https://user-images.githubusercontent.com/7254105/47855858-b22b7880-de0b-11e8-940e-2c6b39efb771.png">

## Error Checking
In case there is an error, it will be shown in the interface itself highlighted in red!
<img src="https://user-images.githubusercontent.com/7254105/47856737-ebfd7e80-de0d-11e8-96a8-d8c50290d18a.png">

**Developer**: [Aadesh M Bagmar](https://github.com/cardwizard)
