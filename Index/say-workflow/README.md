<img src="./raw/icon.png" width:auto height=128pt align="right" />

say-workflow
---
Read out something swiftly. [Download](https://github.com/BaksiLi/AlfredWorkflows/blob/master/workflows/say_command.alfredworkflow?raw=true)

Does this ever happens to you?
That you just want to have a *quick check of the pronunciation* of a word/sentence without being distracted too much.
Or you want to *surprise your classmates in a boring lecture* (and no one would realise that's you)?

Now with say-workflow, you can do all of these just with simple clicks on your keyboard.

This workflow is design for [*Alfred3*](http://alfredapp.com), although it might run on other apps as well.

# Installation
Double-click on *say_command.alfredworkflow* or *info.plist* in the folder, then Alfred will start loading it.  
Further configuration is done within Alfred.

# Usage
It reads text swiftly without open terminal or a text file. 
1. Toggle Alfred
  ![1](./pics/1.png)

1. Type in the keyword
  ![2](./pics/2.png)  
  ```say: ``` or simply `say` and return
  
1. Type in either **Language code** or the text directly
  by default, it will speak in the language of your system's preference:  
  ![3](./pics/3.png)  
  this is the same from saying  
  `say: Can't understand at all!` in the Terminal.  
  or you could indicate what language do you want it to speak in:  
  ![4](./pics/4.png)  
  with or without blank space after it:  
  ![5](./pics/5.png)  
  and return, bob's your uncle!

Since ver. 0.4, say-workflow is able to recognise anagrams of the language codes. E.g. `Pj` and `Jp` are valid synonyms for `jp`. 

# Troubleshooting
- If you would like to change the voice or add more languages, just add them in the dictionary called langs in the source code.  
```langs = {'jp':'Kyoko','en':'Daniel'}```  
add it like this:  
```langs = {'jp':'Kyoko','en':'Daniel','ch':'Sinji'}```  
for voices names and their corresponding abbreviations, check [“say” in different language?](https://apple.stackexchange.com/questions/3454/say-in-different-language).
- If you type in a word but nothing has happened.
check if the text you've typed in is valid under the language you chose. If it doesn't help, raise an issue and I will sort it ASAP.
