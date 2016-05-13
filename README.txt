This project is a Pokemon Typing Caluclator. This program
is built using the PokeApi.co and Kivy Python Library.
The GUI and all of the widgets are constructed using the 
kv language, a language that is used only with Kivy and is similar
to a sort of simplified HTML. This is actually an app but currently
only work on PC but I have plans to port this to iOS sometime soon.
So after all the widgets are set into a 6x3 grid layout, we make 18 
different screens and set the buttons the call the screens according
to type, and then each screen makes a different API call. It is then
where we decide to parse the data and only bring forward the type names
from the api data. There are also statements where if the dictionary
is empty, then we right a different statment saying that no type
is affected in this category. As part of some asthetics we added
a popular pokemon that associates with their respective types.
We also added a background and to the main screen and all the other
screens. The fonts are colored in and music plays as you make your
selections. This turned out nearly to what I wanted. I am only
missing animated GIFS for the buttons and faster loading times
but I hope to keep working on it and improve these bugs and possibly
submit it as an app.