from UI import Label, Card, Center, SoftButton, Button, Raw
from ENV import APP_NAME, FAVICON

def CompHero():
    with Card("w-full h-fit"):
        with Center("w-full h-full gap-2"):
            Label(APP_NAME + FAVICON, "text-5xl md:text-7xl lg:text-9xl font-extrabold w-full text-center")
            Label("The thing that makes sense!", "text-xl w-3xl text-right border-b-2")