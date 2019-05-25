# AlfredWorkflows
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Updating](https://img.shields.io/badge/status-updating-lightgreen.svg)
[![Contribute](https://img.shields.io/badge/contribute-gray.svg?style=flat)](https://github.com/BaksiLi/AlfredWorkflows/blob/master/CONTRIBUTE.md)

本倉庫儲存了我為 Alfred 寫的部分流程插件（workflow）。 部分插件可直接用於 Terminal 中。
 
一些特定的功能需要用戶購買 [Powerpack](https://www.alfredapp.com/powerpack/) 。
 
<sub>本文內容請以[英文版](https://github.com/BaksiLi/AlfredWorkflows/blob/master/README.md)為準。</sub>

## 目錄
- [Should-I-do-it](https://github.com/BaksiLi/AlfredWorkflows/tree/master/Index/should_i_do_it): 即「**我該咋辦**」，用於解決日常最為棘手的哲學問題。當你面對這個充滿灰度認知的世界時，或許你會想問一下：我該咋辦？   
    [下載](https://github.com/BaksiLi/AlfredWorkflows/blob/master/workflows/Should.alfredworkflow?raw=true)
- [Say-command](https://github.com/BaksiLi/AlfredWorkflows/tree/master/Index/say-workflow): 即「**嘮嘮唄**」，用於使終端大聲讀出你的想法。辦公室裡，所有人都在低頭開小差時的突然覺醒！   
    [下載](https://github.com/BaksiLi/AlfredWorkflows/blob/master/workflows/say_command.alfredworkflow?raw=true)
- [Fast-ascii](https://github.com/BaksiLi/AlfredWorkflows/tree/master/Index/fast-ascii): 即「**超凡ASCII**」，用於快速轉換文字於ASCII碼。剩下來的時間，終於可以好好讀書啦！   
	[下載](https://github.com/BaksiLi/AlfredWorkflows/blob/master/workflows/Fast_ascii.alfredworkflow?raw=true)

# 其他功能
## Snippets（案頭紙）
[Snippets](https://www.alfredapp.com/help/features/snippets/) 是 Alfred 提供的另一生產利器。它允許快捷輸入各種符號、字段甚至是經過處理的信息。以下是我寫的一些 snippets。請移步 [AlfredSnippets](https://github.com/BaksiLi/AlfredSnippets)。

## Web Search （快速檢索）
**Web Search** (於 *Alfred Preferences* -> *Web Search*) 可使您快速遊走於知識的海洋中：簡單而強大（sorry for the cliché）。 然既說其[簡](https://www.alfredapp.com/help/features/web-search/custom-searches/)，又何必專門於此介紹它呢？因**人無完人，而知行之不一** （knowing what it can do is far from know how to do it）也。故茲推薦幾個「必備」網站及它們的設置，以承君便。

安裝方法即是去往下面的網址，然後 Alfred 會自動加載它。圖標的加載需要手動拖拽。

<table>
<tr>
  <th><img src="features/wa.png" alt="Wolfram|Alpha Logo" width="50" height="50"></th>
  <th><img src="features/wm.png" alt="MathWorld Logo" width="50" height="50"></th>
  <th><img src="features/sep_man_r.png" alt="SEP Logo red" width="25" height="25">/<img src="features/sep_man_w.png" alt="SEP Logo white" width="25" height="25">/<img src="features/sep_man_k.png" alt="SEP Logo black" width="25" height="25"></th>
</tr>
<tr>
  <td>Wolfram&#124;Alpha</td>
  <td>Wolfram MathWorld</td>
  <td>Standford Encyclopedia of Philosophy*</td>
</tr>
</table>

<details>
<summary>Wolfram|Alpha：知識引擎加快速檢索，爽歪歪！</summary>

> alfred://customsearch/Compute%20%7Bquery%7D%20in%20Wolfram%20Alpha/alpha/utf8/%2B/https%3A%2F%2Fwww.wolframalpha.com%2Finput%2F%3Fi%3D%7Bquery%7D

默認關鍵詞 `alpha`。
</details>

<details>
<summary>Wolfram MathWorld：方便查詢數學、計算機科學及統計的資料</summary>


> alfred://customsearch/Search%20%7Bquery%7D%20in%20Wolfram%20MathWorld/math/utf8/%2B/http%3A%2F%2Fmathworld.wolfram.com%2Fsearch%2F%3Fquery%3D%7Bquery%7D

默認關鍵詞 `math`。
</details>

<details>
<summary>Standford Encyclopaedia of Philosophy：著名哲學百科，時刻待機。</summary>

![SEP illustration](features/sep1.png)

> alfred://customsearch/Search%20%7Bquery%7D%20in%20Standford%20Encyclopedia%20of%20Philosophy/sep/utf8/nospace/https%3A%2F%2Fplato.stanford.edu%2Fsearch%2Fsearcher.py%3Fquery%3D%7Bquery%7D

默認關鍵詞 `sep`。

\* 如果你是 [*Friend of SEP*](https://plato.stanford.edu/support/friends.html)，可以嘗試下面的版本直接檢索百科目錄。 
> alfred://customsearch/Search%20%7Bquery%7D%20in%20SEP%27s%20catalogue/sepf/utf8/%2B/https%3A%2F%2Fleibniz.stanford.edu%2Ffriends%2Fsearch_title%2F%3Fquery%3D%7Bquery%7D

默認關鍵詞 `sepf`。

</details>

# 承知
本項目採以 MIT Licence。

It is also published on [Packal](http://www.packal.org/users/lisongcheng), please check it if you want to have find out more Alfred widgets written by the author.

Copyright (c) 2018 BaksiLi
