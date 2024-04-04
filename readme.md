# Ett Skolprojekt; en Flask-applikation.  
## En applikation för anställda på ett företag, byggd med Flask, SQLAlchemy, Flask-Security-too, Flask-Migrate, SQLite, html och CSS. 

# För att köra applikationen;  
I en virtuell miljö; pip install -r requirements.txt.  
Skapa en .env-fil med variablerna; LOCAL_DATABASE_URI, SECRET_KEY och SECURITY_PASSWORD_SALT.

# Om applikationen;  
När applikationen körs seedas data för 500 anställda samt 3 användare.

## Inloggningsuppgifter;  
Användare 1, roller Admin och User;  
Email; admin_user@test.com, Lösenord; adminuserpassword   
Användare 2, roll User;  
Email; user@test.com, Lösenord; userpassword  
Användare 3, roll Admin;  
Email; admin@test.com, Lösenord; adminpassword  


Loggar du in med rollen admin har du åtkomst till samtliga sidor; Hem, Anställda, Personkort, Kontakt och Logga ut. Från sidan anställda kan du klicka på bilderna som är länk för att komma vidare till personkort för respektive person och där få mer info om personen. Klickar du på personkort kommer du till routen employee_card/search och kan söka efter en person på ID.

Loggar du in med enbart rollen User har du åtkomst till Hem, Anställda, Kontakt och Logga ut.
Som User kan du inte klicka på fotona och komma till Personkort.

## Innehåll i applikationen;  
Applikationen består av en förstasida där man kan klicka sig vidare för att logga in.  

Navbar och footer ärvs från base.html och finns på sidorna för Hem, Anställd, Personkort och Kontakt.  

Hem-sidan består av bild och välkomnande text  

Anställda-sidan består av en tabell med Anställda med id, namn, ålder, telefonnummer, land och en bild. Sökfunktion är implementerad för att söka efter något av värdena i tabellen. Sortering är implementerad på id, namn, ålder, telefonnummer och land. Paginering på 30 personer/sida. För inloggad med rollen Admin ligger det en länk på bilden som leder till Personkortet för den anställde.  

Personkort-sidan består av en sökfunktion där användaren kan söka på ID. Finns ID så skickas användaren till sökt persons Personkort. Finns inte ID får användaren återkoppling via ett meddelande och stannar på sidan och kan söka igen.  

Kontakt-sidan består av kontaktuppgifter till företaget samt länkar till Facebook, Instagram och LinkedIn.  

Klickar man på Logga ut så loggas man ut och kommer till sida där man får frågan om man vill logga in igen. Klickar man på Logga in-knappen kommer man direkt till inloggningssidan.
