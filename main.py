import webbrowser
for z in range(100):
    a = input("Search for a Website :")
    if a == "google search":
        for y in range(100):
            b = input("Search Google:")
            if b != "":
                webbrowser.open("https://www.google.com/search?q=" + b)
            else:
                break
    else:
        webbrowser.open("https://" + a + "/")
