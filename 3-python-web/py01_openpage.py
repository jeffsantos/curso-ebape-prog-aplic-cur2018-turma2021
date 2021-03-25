import sys, webbrowser, pyperclip

print(sys.argv)

if len(sys.argv) > 1:
    endereco = " ".join(sys.argv[1:])
else:
    endereco = pyperclip.paste()

webbrowser.open(f"https://www.google.com/maps/place/{endereco}")