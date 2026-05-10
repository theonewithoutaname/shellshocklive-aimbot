#Persistent
#NoEnv
SetTitleMatchMode, 2  ; Match partial window titles
DetectHiddenWindows, On

windowTitle := "Aimbot"

WinSet, AlwaysOnTop, On, %windowTitle%

^t::
    WinGet, style, Style, %windowTitle%
    WinSet, AlwaysOnTop, Toggle, %windowTitle%
    return

^q::
    ExitApp