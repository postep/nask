##Detekcja prostych ataków

Celem działania środowiska jest symulacja prostych ataków i obrony skanowania portów TCP


### Uruchamianie

Środowiska maszyn wirtualnych wykonano w Vagrancie. Wszystkie systemy to Debian 9. Uruchomienie sprowadza się do polecenia:
```vagrant up ```
Następnie należy wykonać konfigurację środowisk
```vagrant provision```

### Serwer

Stan obiektu w formacie JSON dostępny pod:
[http://20.0.0.3:80](http://20.0.0.3:80)

Aby wprowadzić sterowanie należy po ukośniku podać wartość sterowania:
[http://20.0.0.3:80/<sterowanie>](http://20.0.0.3:80)

Usługa serwera pisana w python3. Symulacja obiektu o zadanej transmitacji z czasem próbkowania 1/10 s.

### Klient

IP: 10.0.0.5. Usługa klienta pisana w python3. Łączy się z serwerem z częstotliwością 1/10 s. Reguluje na wartość zadaną udostępniony obiekt algorytmem PID.

### Zakłócenie
IP: 10.0.0.1. Symuluje skanowanie portów TCP. Skrypt skanujący jest uruchamiany wraz z poleceniem ```vagrant provision```

### Router
IP: 10.0.0.4, IP:20.0.0.4. Po zablokowaniu ruchu dla konkretnego IP należy ręcznie odblokować ruch.

### Snort
Uruchomiony i śledzony przez skrypt pythona. Rejestruje aktywność klientów. Jeśli zauważy aktywność na porcie innym niż 80 wysyła polecenie blokowania ruchu do komponentu Router (iptables) oraz odpowiedni alert do komponentu DB.

### DB
Serwer bazy danych MongoDB. Przechowuje alerty komponentu Snort.

### Atak i obrona
Atakujący uruchamia parę wątków które skanują porty serwera. W momencie wykrycia ruchu na innym niż 80 porcie sytem obrony  blokuje ruch dla atakującego. 

### Uwagi

* Komponent Snort oraz DB są uruchomione na komponencie Router. TODO: Rozdzielić.

* Instalacja Snorta przez apta odbywa się w trybie graficznym. Jeśli wystąpią problemy z działaniem snorta należy ręcznie ponownie przeprowadzić instalację (wraz z ponowną instalacją plików konfiguracyjnych)

* TODO: Testowanie

* Komponent Zakłócenie zaraz po wykonaniu polecenia provision zaczyna atak i jest on szybko blokowany przez Router. Aby przeprowadzić powtórną symulację ataku należy ręcznie odblokować ruch dla teg urządzenia np: ```sudo iptables -F```



