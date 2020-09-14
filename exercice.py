#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

def square_root(a: float) -> float:
    return math.sqrt(a)


def square(a: float) -> float:
    return a ** 2


def average(a: float, b: float, c: float) -> float:
    return sum([a, b, c]) / 3


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    return math.radians(angle_degs + (angle_mins + (angle_secs / 60)) / 60)


def to_degrees(angle_rads: float) -> tuple:
    degrees = math.degrees(angle_rads)
    minutes = (degrees % 1) * 60
    seconds = (minutes % 1) * 60

    return degrees - minutes, minutes - seconds, seconds


def to_celsius(temperature: float) -> float:
    return (temperature - 32) / 1.8


def to_farenheit(temperature: float) -> float:
    return temperature * 1.8 + 32

def puissance(V, R):
    P = V**2 / R
    return P

def orthogonalité(X1, Y1, X2, Y2):
    O = X1*X2 + Y1*Y2
    if 0 ==0:
        return True
    else:
        return False

def moyenne_positive(liste):
    m = 0
    for i in range(0, len(liste)):
        m = m + liste[i]
    m = m / len(liste)
    return m

def décomp_prix(cout):
    centaine = cout // 100
    reste1 = cout % 100
    vingtaine = reste1 // 20
    reste2 = reste1 % 20
    dizaine = reste2 // 10
    reste3 = reste2 % 10
    cinq = reste3 // 5
    unités = reste3 % 5
    décompo = [centaine, vingtaine, dizaine, cinq, unités]
    return décompo


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
