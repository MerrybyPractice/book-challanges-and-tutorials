# Ceasar Cypher by Hand

[Online Cypher Wheel](https://inventwithpython.com/cipherwheel/)

## The Basic Ceasar Cypher

1.1 In this example we are encrypting the string "THE SECRET PASSWORD IS ROSEBUD" using an encryption key of 8, per the book's tutorial.

S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R
A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z
0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12| 13| 14| 15| 16| 17| 18| 19| 20| 21| 22| 23| 24| 25

BPM AMKZMB XSAAEWZV QA ZWAMJCL

1.2 In this example we are decrypting the string "IWT CTL EPHHLDGS XH HLDGSUXHW" using an encryption key of 15, per the book's tutorial.

L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K
A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z
0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12| 13| 14| 15| 16| 17| 18| 19| 20| 21| 22| 23| 24| 25

THE NEW PASSWORD IS SWORDFISH

1.3 In this example we are using basic addition to encrypt "HELLO HOW ARE YOU" using an encryption key of 13, per the book's tutorial.

A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z
0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12| 13| 14| 15| 16| 17| 18| 19| 20| 21| 22| 23| 24| 25

URYYB UBJ NER LBH

H : 7+13 = 20 |           | 20 = U
E : 4+13 = 17 |           | 17 = R
L : 11+13 = 24|           | 24 = Y
O : 14+13 = 27| 27-26 = 1 | 1  = B
W : 22+13 = 35| 35-26 = 9 | 9  = J
A : 0+13 = 13 |           | 13 = N
R : 17+13 = 30| 30-26 = 4 | 4  = E
Y : 24+13 = 37| 37-26 = 11| 11 = L
U : 20+13 = 33| 33-26 = 7 | 7  = H

## 2.0 Practice Problems

2.1 Encrypt entries from Ambrose Bierce's The Devil's Dictionary 

2.1.a AMBIDEXTROUS: Able to pick with equal skill a right- hand pocket or a left. : Key 4

EQFMHIBXVSYW: EFPI XS TMGO AMXL IUYEP WOMPP E VMKLX- LERH TSGOIX SV E PIJX.

A : 0+4 = 4  |           | 4  = E
M : 12+4 = 16|           | 16 = Q
B : 1+4 = 5  |           | 5  = F
I : 8+4 = 12 |           | 12 = M
D : 3+4 = 7  |           | 7  = H
E : 4+4 = 8  |           | 8  = I
X : 23+4 = 27| 27-26 = 1 | 1  = B
T : 19+4 = 23|           | 23 = X
R : 17+4 = 21|           | 21 = V
O : 14+4 = 18|           | 18 = S
U : 20+4 = 24|           | 24 = Y
S : 18+4 = 22|           | 22 = W
L : 11+4 = 15|           | 15 = P
P : 15+4 = 19|           | 19 = T
C : 2+4 = 6  |           | 6  = G
K : 10+4 = 14|           | 14 = O
W : 22+4 = 26| 26-26 = 0 | 0  = A
H : 7+4 = 11 |           | 11 = L
Q : 16+4 = 20|           | 20 = U
G : 6+4 = 10 |           | 10 = K
N : 13+4 = 17|           | 17 = R
F : 5+4 = 9  |           | 9  = J

2.1.b GUILLOTINE: A machine which makes a Frenchman shrug his shoulders with good reason. : Key 17

XLZCCFKZEV: R DRTYZEV NYZTY DRBVJ R WIVETYDRE JYILX YZJ JYFLCUVIJ NZKY XFFU IVRJFE.

G : 6+17 = 23 |           | 23 = X
U : 20+17 = 37| 37-26 = 11| 11 = L
I : 8+17 = 25 |           | 25 = Z
L : 11+17 = 28| 28-26 = 2 | 2  = C
O : 14+17 = 31| 31-26 = 5 | 5  = F
T : 19+17 = 36| 36-26 = 10| 10 = K
I : 8+17 = 25 |           | 25 = Z
N : 13+17 = 30| 30-26 = 4 | 4  = E
E : 4+17 = 21 |           | 21 = V
A : 0+17 = 17 |           | 17 = R
M : 12+17 = 29| 29-26 = 3 | 3  = D
C : 2+17 = 19 |           | 19 = T
H : 7+17 = 24 |           | 24 = Y
W : 22+17 = 39| 39-26 = 13| 13 = N
K : 10+17 = 27| 27-16 = 1 | 1  = B
S : 18+17 = 35| 35-26 = 9 | 9  = J
F : 5+17 = 22 |           | 22 = W
R : 17+17 = 34| 34-26 = 8 | 8  = I
D : 3+17 = 20 |           | 20 = U

2.1.c IMPIETY: Your irreverence toward my deity. : Key 21

DHKDZOT: TJPM DMMZQZMZIXZ OJRVMY HT YZDOT.

I : 8+21 = 29 | 29-26 = 3 | 3  = D
M : 12+21 = 33| 33-26 = 7 | 7  = H
P : 15+21 = 36| 36-26 = 10| 10 = K
E : 4+21 = 25 |           | 25 = Z
T : 19+21 = 40| 40-26 = 14| 14 = O
Y : 24+21 = 45| 45-26 = 19| 19 = T
O : 14+21 = 35| 35-26 = 9 | 9  = J
U : 20+21 = 41| 41-26 = 15| 15 = P
R : 17+21 = 38| 38-26 = 12| 12 = M
V : 21+21 = 42| 42-26 = 16| 16 = Q
N : 13+21 = 34| 34-26 = 8 | 8  = I
C : 2+21 = 23 |           | 23 = X
W : 22+21 = 43| 43-26 = 17| 17 = R
A : 0+21 = 21 |           | 21 = V
D : 3+21 = 24 |           | 24 = Y

2.2 Decrypt entries from Ambrose Bierce's The Devil's Dictionary

2.2.a ZXAI: P RDHIJBT HDBTIXBTH LDGC QN HRDIRWBTC XC PBTGXRP PCS PBTGXRPCH XC HRDIAPCS. : Key 15

KILT: a costume sometimes worn by Scotchmen in America and Americans in Scotland.

Z : 25-15 = 10|           | 10 = K
X : 23-15 = 8 |           | 8  = I
A : 0-15 = -15|-15+26 = 11| 11 = L
I : 8-15 = -7 |-7+26 = 19 | 19 = T
P : 15-15 = 0 |           | 0  = A
R : 17-15 = 2 |           | 2  = C
D : 3-15 = -12|-12+26 = 14| 14 = O
H : 7-15 = -8 |-8+26 = 18 | 18 = S
J : 9-15 = -6 |-6+26 = 20 | 20 = U
B : 1-15 = -14|-14+26 = 12| 12 = M
T : 19-15 = 4 |           | 4  = E
L : 11-15 = -4|-4+26 = 22 | 22 = W
G : 6-15 = -9 |-9+26 = 17 | 17 = R
C : 2-15 = -13|-13+26 = 13| 13 = N
Q : 16-15 = 1 |           | 1  = B
N : 13-15 = -2|-2+26 = 24 | 24 = Y
W : 22-15 = 7 |           | 7  = H
S : 18-15 = 3 |           | 3  = D

2.2.b MQTSWXSV: E VMZEP EWTMVERX XS TYFPMG LSRSVW. : Key 4

IMPOSTOR: a rival aspirant to public honors.

M : 12-4 = 8  |           | 8  = I
Q : 16-4 = 12 |           | 12 = M
T : 19-4 = 15 |           | 15 = P
S : 18-4 = 14 |           | 14 = O
W : 22-4 = 18 |           | 18 = S
X : 23-4 = 19 |           | 19 = T
V : 21-4 = 17 |           | 17 = R
E : 4-4 = 0   |           | 0  = A
Z : 25-4 = 21 |           | 21 = V
P : 15-4 = 11 |           | 11 = L
R : 17-4 = 13 |           | 13 = N
Y : 24-4 = 20 |           | 20 = U
F : 5-4 = 1   |           | 1  = B
G : 6-4 = 2   |           | 2  = C
L : 11-4 = 7  |           | 7  = H

2.3 Encrypt the following sentence with the key 0: This is a silly example.

This is a silly example.

T : 19+0 = 19 |           | 19 = T
H : 7+0 = 7   |           | 7  = H
I : 8+0 = 8   |           | 8  = I
S : 18+0 = 18 |           | 18 = S
A : 0+0 = 0   |           | 0  = A
L : 11+0 = 11 |           | 11 = L
Y : 24+0 = 24 |           | 24 = Y
E : 4+0 = 4   |           | 4  = E
X : 23+0 = 23 |           | 23 = X
M : 12+0 = 12 |           | 12 = M
P : 15+0 = 15 |           | 15 = P

2.4 Determine the key used to encrypt each of the following examples:

2.4.a ROSEBUD – LIMYVOX | 20

2.4.b YAMAMOTO – PRDRDFKF | 17

2.4.c ASTRONOMY – HZAYVUVTF | 7

2.5 What does this sentence encrypted with key 8 decrypt to with key 9? “UMMSVMAA: Cvkwuuwv xibqmvkm qv xtivvqvo i zmdmvom bpib qa ewzbp epqtm.

LDDJMDRR: Tmbnllnm ozshdmbd hm okzmmhmf z qdudmfd sgzs hr znqg zghkd.

U : 20-9 = 11 |           | 11 = L
M : 12-9 = 3  |           | 3  = D
S : 18-9 = 9  |           | 9  = J
V : 21-9 = 12 |           | 12 = M
A : 0-9 = -9  |-9+26 = 17 | 17 = R
C : 2-9 = -7  |-7+26 = 19 | 19 = T
K : 10-9 = 1  |           | 1  = B
W : 22-9 = 13 |           | 13 = N
X : 23-9 = 14 |           | 14 = O
I : 8-9 = -1  |-1+26 = 25 | 25 = Z
B : 1-9 = -8  |-8+26 = 18 | 18 = S
Q : 16-9 = 7  |           | 7  = H
T : 19-9 = 10 |           | 10 = K
O : 14-9 = 5  |           | 5  = F
Z : 25-9 = 16 |           | 16 = Q
D : 3-9 = -6  |-6+26 = 20 | 20 = U
P : 15-9 = 6  |           | 6  = G
E : 4-9 = -1  |-1+26 = 25 | 25 = Z
