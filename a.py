import os, platform
os.system("cd $HOME/")
#os.system("termux-setup-storage")
os.system("xdg-open https://www.facebook.com/akash.asif.2")

try:
    import requests
except(ImportError):
    os.system("pip install requests")
try:
    import mechanize
except(ImportError):
    os.system("pip install mechanize")
try:
    import bs4
except(ImportError):
    os.system("pip install bs4")
akash=platform.architecture()[0]
try:
    if akash=="32bit":
        __import__("a32").main_menu()
    elif akash=="64bit":
__import__("a").main_menu()
    else:
        print(" We have issue to launch script")
        exit()
except(AttributeError,OSError,KeyError,IOError):
    if akash == "32bit":
        import a32
        a32.main_menu()
    elif akash == "64bit":
        import a
        a.main_menu()
    else:
        print(" We have issue to launch script")
        exit()
