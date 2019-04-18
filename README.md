# AlfredWorkflows
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Updating](https://img.shields.io/badge/status-updating-lightgreen.svg)

This is a growing repository curates my workflow creations for [Alfred](https://www.alfredapp.com). Most of them are Terminal friendly.  
<sub>For Chinese version of this page, see [漢語版](https://github.com/BaksiLi/AlfredWorkflows/blob/master/README_CN.md).</sub>

# Menu
- [Should-I-do-it](https://github.com/BaksiLi/AlfredWorkflows/tree/master/Index/should_i_do_it): A workflow aimed to solve probably the biggest philosophical question in dailylife: should I do it?  
    Download: [here](https://github.com/BaksiLi/AlfredWorkflows/blob/master/workflows/Should.alfredworkflow?raw=true)
- [Say-command](https://github.com/BaksiLi/AlfredWorkflows/tree/master/Index/say-workflow): A workflow that allows terminal to read out something.  
    Download: [here](https://github.com/BaksiLi/AlfredWorkflows/blob/master/workflows/say_command.alfredworkflow?raw=true)
- [Fast-ascii](https://github.com/BaksiLi/AlfredWorkflows/tree/master/Index/fast-ascii): A workflow that convert and paste ascii fastly.  
    Download: [here](https://github.com/BaksiLi/AlfredWorkflows/blob/master/workflows/Fast_ascii.alfredworkflow?raw=true)

# Other features
## Snippets
I have created a few useful snippets as well. Please have a try.

- [Greek Alphabet](https://github.com/BaksiLi/Greek-Alphabet-Alfred-Snippet)
- [Bopomofo](https://github.com/BaksiLi/Bopomofo-snippet)

## Web Search
**Web Search** (in *Alfred Preferences* -> *Web Search*) enables fast queries from a website by its URL. It is simple but powerful (sorry for the cliché). Then, given its [simplicity](https://www.alfredapp.com/help/features/web-search/custom-searches/), why do I still bother to introduce it here? Because **knowing what it can do is far from know how to do it**. Here I will propose a few webpages to add to Alfred. Click on the link to add them.

- Wolfram|Alpha

<details>

Suppose you are solving a question:
> How many times faster it is to solve TSP (Travelling Salesperson Problem), by using dynamic-programming-based algorithm (![$n!$](features/formula1.png)) than using brute force search algorithm(![$$n^2 2^n$](features/formula2.png)), given that n=100?

The solution is obtained by computing ![$\frac{100!}{100^{2}\times 2^{100}}$](features/formula3.png).
It could be done in just one line, anywhere in your computer.
```
alpha log(100!/(100^2 * 2^100))
```
![illustration](features/alpha1.png)
and you will see the following result in Wolfram|Alpha:
![illustration](features/alpha2.png)
Powerful, innit?

> alfred://customsearch/Compute%20%7Bquery%7D%20in%20Wolfram%20Alpha/alpha/utf8/%2B/https%3A%2F%2Fwww.wolframalpha.com%2Finput%2F%3Fi%3D%7Bquery%7D

</details>
	
- Wolfram MathWorld
<details>

> alfred://customsearch/Search%20%7Bquery%7D%20in%20Wolfram%20MathWorld/math/utf8/%2B/http%3A%2F%2Fmathworld.wolfram.com%2Fsearch%2F%3Fquery%3D%7Bquery%7D</details>
	 
- Standford Encyclopedia of Philosophy
<details>

> alfred://customsearch/Search%20%7Bquery%7D%20in%20Standford%20Encyclopedia%20of%20Philosophy/sep/utf8/nospace/https%3A%2F%2Fplato.stanford.edu%2Fsearch%2Fsearcher.py%3Fquery%3D%7Bquery%7D</details>

# Acknowledgement
This project collection is licenced under the MIT License.  
It is also published on [Packal](http://www.packal.org/users/lisongcheng), please check it if you want to have find out more Alfred widgets written by the author.

Copyright (c) 2018 BaksiLi

