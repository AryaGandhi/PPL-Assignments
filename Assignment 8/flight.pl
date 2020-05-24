flight(toronto,aircanada , london,500, 360).
flight(toronto,united , london,650, 420 ).
flight(toronto,aircanada , madrid,900, 480 ).
flight(toronto,united , madrid,950, 540 ).
flight(toronto,iberia, madrid,800, 480 ).

flight(madrid, aircanada, barcelona, 100, 60).
flight(madrid, iberia, barcelona, 120, 65).
flight(madrid, iberia, valencia, 40, 50).
flight(madrid, iberia, malaga, 50, 60).

flight(barcelona, iberia, valencia, 110, 75).
flight(barcelona, iberia, london , 220, 240).

flight(malaga, iberia, valencia, 80, 120).
flight(paris, united, toulouse, 35, 120).

%query to check if a flight exists between any two cities
doesFlightExist(A, B):-
    flight(A, C, B, D, E);
    flight(B, C, A, D, E).

airport(toronto, 50, 60).
airport(london, 75, 80).
airport(madrid, 75, 45).
airport(barcelona, 40, 30).
airport(valencia , 40, 20).
airport(malaga, 50 , 30).
airport(paris, 50, 60).
airport(toulouse, 40, 30).

%query to produce all the cities with the airport tax in dollars and the minimum security delay in minutes. 
airport(C,T,D) :- airport(C,T,D).

%query to check if flight is cheap
isFlightCheap(A,C,B):- flight(A,C,B,P,D),
                        P<400.

%query to check if it is possible to go from one city to another in two flights
areTwoFlights(A, B):- doesFlightExist(A, X), doesFlightExist(X,B).

%query to check if a flight is preferred(it is preferred if the flight is cheap and the flight is of air canada)
isFlightPreferred(A, C, B):- C == aircanada;
                        isFlightCheap(A, C, B).

%If there is a flight from city A to city B with United, then there is a flight from city A to city B with Air Canada. 
checkExistence(A,B,C,D) :- flight(A,C,B,E,F)  -> flight(A,D,B,G,H) ; flight(B,C,A,E,F)  -> flight(B,D,A,G,H).

%query to produce all the possible flights in both directions with the price in dollars and the duration in minutes.
fly(A, C, B, P, D) :-
    flight(A, C, B, P, D),
    write(A),
    write(' '),
    write(C),
    write(' '),
    write(B),
    write(' '),
    write(P),
    write($),
    write(' '),
    write(D),
    write(m),
    nl,
    write(B),
    write(' '),
    write(C),
    write(' '),
    write(A),
    write(' '),
    write(P),
    write($),
    write(' '),
    write(D),
    write(m),
    nl.
