# 🍁 Autumn (Not the season)
Autumn, in a nutshell, it's a Textual WM. It's not a fork of twin (another Textual WM), but i made this because twin is pretty outdated. Btw, sorry for my bad english.
## ⚖️ License
It's released under the CC0 1.0 (Creative Commons 1.0 Universal) license, meaning idc if someone uses my code in any way.
## Model
Autumn follows a rolling-release model.
## ❗ Requirements
Autumn requires Python 3.10≥ and Unicode support in order to draw loading screens or separators. In future it will also need TrueColor (24-bit color), and Autumn hasn't snapshot, so use modern terminals like xterm or gnome terminal to make sure your terminal will be capable to execute autumn in the future. If you currently use autumn standard on tty, when truecolor appears on autumn, make sure to download autumnvt. With autumnvt animations will still play but they lowkey suck.
## ➡️ Installation Guide
### 🐧 Debian or Debian-based
Open a terminal, like GNOME Terminal or xterm.
type:
`sudo apt install python3`
## 📰 News
Autumn Koala, on 18 May 2026, dropped sysresl on the Koala Terminal Emulator (KTE). Also dropped a new shortcut (^A ENTER) to close the window without typing. The sysresl command internally calls the resl() python function, and ^A ENTER is basically \x01 (the terminal, when you press ^A, makes this sequence) and ENTER (send input). It means that \x01 (^A) is just an alias for sysresl.
