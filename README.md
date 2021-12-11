
# Pensumhefte, 2021, realisert.

Dette dokumentet ligger ute på https://magne.dev/TDT4120/.
Dersom du ønsker å kjøre algoritmene, kan du klone prosjektet fra https://github.com/magnetenstad/TDT4120.



## Læringsmål

### Overordnede læringsmål
De overordnede læringsmålene for emnet er som følger.

**Dere skal ha kunnskap om:**
- [x] [X1] Et bredt spekter av etablerte algoritmer og datastrukturer
- [x] [X2] Klassiske algoritmiske problemer med kjente effektive løsninger
- [ ] [X3] Komplekse problemer uten kjente effektive løsninger

**Dere skal kunne:**
- [ ] [X4] Analysere algoritmers korrekthet og effektivitet
- [ ] [X5] Formulere problemer så de kan løses av algoritmer
- [ ] ! [X6] Konstruere nye effektive algoritmer

**Dere skal være i stand til:**
- [ ] [X7] Å bruke eksisterende algoritmer og programvare på nye problemer
- [ ] [X8] Å utvikle nye løsninger på praktiske algoritmiske problemstillinger


### Gjennom semesteret

**Læringsmål for hver algoritme:**
- [x] [Z1] Kjenne den formelle definisjonen av det generelle problemet den løser
- [x] [Z2] Kjenne til eventuelle tilleggskrav den stiller for å være korrekt
- [x] [Z3] Vite hvordan den oppfører seg; kunne utføre algoritmen, trinn for trinn
- [ ] ! [Z4] Forstå korrekthetsbeviset; hvordan og hvorfor virker algoritmen egentlig?
- [ ] [Z5] Kjenne til eventuelle styrker eller svakheter, sammenlignet med andre
- [x] [Z6] Kjenne kjøretidene under ulike omstendigheter, og forstå utregningen

**Læringsmål for hver datastruktur:**
- [x] [Z7] Forstå algoritmene (jf. mål Z01–Z06) for de ulike operasjonene på strukturen
- [x] [Z8] Forstå hvordan strukturen representeres i minnet

**Læringsmål for hvert problem:**
- [x] [Z9] Kunne angi presist hva input er
- [x] [Z10] Kunne angi presist hva output er og hvilke egenskaper det må ha


### Forelesning 1: Problemer og algoritmer
- [x] [A1] [Forstå bokas pseudokode-konvensjoner](#a1-forstå-bokas-pseudokode-konvensjoner)
- [x] [A2] [Kjenne egenskapene til random-access machine-modellen (RAM)](#a2-kjenne-egenskapene-til-random-access-machine-modellen-ram)
- [x] [A3] [Kunne definere problem, instans og problemstørrelse](#a3-kunne-definere-problem-instans-og-problemstørrelse)
- [x] ! [A4] [Kunne definere asymptotisk notasjon, $O$, $\Omega$, $\Theta$, $o$ og $\omega$](#-a4-kunne-definere-asymptotisk-notasjon-o-omega-theta-o-og-omega)
- [x] ! [A5] [Kunne definere best-case, average-case og worst-case](#-a5-kunne-definere-best-case-average-case-og-worst-case)
- [x] ! [A6] [Forstå løkkeinvarianter og induksjon](#-a6-forstå-løkkeinvarianter-og-induksjon)
- [x] ! [A7] [Forstå rekursiv dekomponering og induksjon over delinstanser](#-a7-forstå-rekursiv-dekomponering-og-induksjon-over-delinstanser)
- [x] [A8] [Forstå Insertion-Sort](#a8-forstå-insertion-sort)


### Forelesning 2: Datastrukturer
- [x] [B1] [Forstå hvordan stakker og køer fungerer](#b1-forstå-hvordan-stakker-og-køer-fungerer)
- [x] [B2] [Forstå hvordan lenkede lister fungerer](#b2-forstå-hvordan-lenkede-lister-fungerer)
- [x] [B3] [Forstå hvordan pekere og objekter kan implementeres](#b3-forstå-hvordan-pekere-og-objekter-kan-implementeres)
- [x] ! [B4] [Forstå hvordan direkte adressering og hashtabeller fungerer](#-b4-forstå-hvordan-direkte-adressering-og-hashtabeller-fungerer)
- [x] [B5] [Forstå konfliktløsing ved kjeding (chaining)](#b5-forstå-konfliktløsing-ved-kjeding-chaining)
- [ ] [B6] [Kjenne til grunnleggende hashfunksjoner](#b6-kjenne-til-grunnleggende-hashfunksjoner)
- [x] [B7] [Vite at man for statiske datasett kan ha worst-case O(1) for søk](#b7-vite-at-man-for-statiske-datasett-kan-ha-worst-case-o1-for-søk)
- [x] [B8] [Kunne definere amortisert analyse](#b8-kunne-definere-amortisert-analyse)
- [x] [B9] [Forstå hvordan dynamiske tabeller fungerer](#b8-kunne-definere-amortisert-analyse)


### Forelesning 3: Splitt og hersk
- [x] ! [C1] [Forstå designmetoden divide-and-conquer (splitt og hersk)](#-c1-forstå-designmetoden-divide-and-conquer-splitt-og-hersk)
- [x] [C2] [Forstå maximum-subarray-problemet med løsninger](#c2-forstå-maximum-subarray-problemet-med-løsninger)
- [x] [C3] [Forstå Bisect og Bisect'](#c3-forstå-bisect-og-bisect)
- [x] [C4] [Forstå Merge-Sort](#c4-forstå-merge-sort)
- [x] [C5] [Forstå Quicksortog Randomized-Quicksort](#c5-forstå-quicksort-og-randomized-quicksort)
- [ ] ! [C6] [Kunne løse rekurrenser med substitusjon, rekursjonstrær og masterteoremet](#-c6-kunne-løse-rekurrenser-med-substitusjon-rekursjonstrær-og-masterteoremet)
- [ ] ! [C7] [Kunne løse rekurrenser med iterasjonsmetoden](#-c7-kunne-løse-rekurrenser-med-iterasjonsmetoden)
- [ ] [C8] [Forstå hvordan variabelskifte fungerer](#c8-forstå-hvordan-variabelskifte-fungerer)


### Forelesning 4: Rangering i lineær tid
- [x] ! [D1] [Forstå hvorfor sammenligningsbasert sortering har en worst-case på $\Omega(n \lg n)$](#-d1-forstå-hvorfor-sammenligningsbasert-sortering-har-en-worst-case-på-omegan-lg-n)
- [x] [D2] [Vite hva en stabil sorteringsalgoritme er](#d2-vite-hva-en-stabil-sorteringsalgoritme-er)
- [x] [D3] [Forstå Counting-Sort, og hvorfor den er stabil](#d3-forstå-counting-sort-og-hvorfor-den-er-stabil)
- [x] ! [D4] [Forstå Radix-Sort, og hvorfor den trenger en stabil subrutine](#-d4-forstå-radix-sort-og-hvorfor-den-trenger-en-stabil-subrutine)
- [x] [D5] [Forstå Bucket-Sort](#d5-forstå-bucket-sort)
- [x] [D6] [Forstå Randomized-Select](#d6-forstå-randomized-select)
- [ ] [D7] [Kjenne til Select](#d7-kjenne-til-select)


### Forelesning 5: Rotfaste trestrukturer
- [x] ! [E1] [Forstå hvordan heaps fungerer, og hvordan de kan brukes som prioritetskøer](#-e1-forstå-hvordan-heaps-fungerer-og-hvordan-de-kan-brukes-som-prioritetskøer)
- [x] [E2] [Forstå Heapsort](#e2-forstå-heapsort)
- [x] [E3] [Forstå hvordan rotfaste trær kan implementeres](#e3-forstå-hvordan-rotfaste-trær-kan-implementeres)
- [x] ! [E4] [Forstå hvordan binære søketrær fungerer](#-e4-forstå-hvordan-binære-søketrær-fungerer)
- [x] [E5] [Vite at forventet høyde for et tilfeldig binært søketre er $\Theta(\lg n)$](#e5-vite-at-forventet-høyde-for-et-tilfeldig-binært-søketre-er-thetalg-n)
- [x] [E6] [Vite at det finnes søketrær med garantert høyde på $\Theta(\lg n)$](#e6-vite-at-det-finnes-søketrær-med-garantert-høyde-på-thetalg-n)


### Forelesning 6: Dynamisk programmering
- [ ] ! [F1] [Forstå ideen om en delinstansgraf](#-f1-forstå-ideen-om-en-delinstansgraf)
- [ ] ! [F2] [Forstå designmetoden dynamisk programmering](#-f2-forstå-designmetoden-dynamisk-programmering)
- [ ] ! [F3] [Forstå løsning ved memoisering (top-down)](#-f3-forstå-løsning-ved-memoisering-top-down)
- [ ] [F4] [Forstå løsning ved iterasjon (bottom-up)](#f4-forstå-løsning-ved-iterasjon-bottom-up)
- [ ] [F5] [Forstå hvordan man rekonstruerer en løsning fra lagrede beslutninger](#f5-forstå-hvordan-man-rekonstruerer-en-løsning-fra-lagrede-beslutninger)
- [ ] [F6] [Forstå hva optimal delstruktur er](#f6-forstå-hva-optimal-delstruktur-er)
- [ ] [F7] [Forstå hva overlappende delinstanser er](#f7-forstå-hva-overlappende-delinstanser-er)
- [x] [F8] [Forstå eksemplene stavkutting og LCS](#f8-forstå-eksemplene-stavkutting-og-lcs)
- [x] [F9] [Forstå løsningen på det binære ryggsekkproblemet](#f9-forstå-løsningen-på-det-binære-ryggsekkproblemet)


### Forelesning 7: Grådige algoritmer
- [ ] ! [G1] [Forstå designmetoden grådighet](#-g1-forstå-designmetoden-grådighet)
- [ ] ! [G2] [Forstå grådighetsegenskapen (the greedy-choice property)](#-g2-forstå-grådighetsegenskapen-the-greedy-choice-property)
- [ ] [G3] [Forstå eksemplene aktivitet-utvelgelse og det kontinuerlige ryggsekkproblemet](#g3-forstå-eksemplene-aktivitet-utvelgelse-og-det-kontinuerlige-ryggsekkproblemet)
- [x] [G4] [Forstå Huffman og Huffman-koder](#g4-forstå-huffman-og-huffman-koder)


### Forelesning 8: Traversering av grafer
- [ ] [H1] [Forstå hvordan grafer kan implementeres](#h1-forstå-hvordan-grafer-kan-implementeres)
- [x] [H2] [Forstå BFS, også for å finne korteste vei uten vekter](#h2-forstå-bfs-også-for-å-finne-korteste-vei-uten-vekter)
- [x] [H3] [Forstå DFS, parentesteoremet og hvit-sti-teoremet](#h3-forstå-dfs-parentesteoremet-og-hvit-sti-teoremet)
- [ ] [H4] [Forstå hvordan DFS klassifiserer kanter](#h4-forstå-hvordan-dfs-klassifiserer-kanter)
- [x] [H5] [Forstå Topological-Sort](#h5-forstå-topological-sort)
- [ ] [H6] [Forstå hvordan DFS kan implementeres med en stakk](#h6-forstå-hvordan-dfs-kan-implementeres-med-en-stakk)
- [ ] [H7] [Forstå hva traverseringstrær (som bredde-først- og dybde-først-trær) er](#h7-forstå-hva-traverseringstrær-som-bredde-først--og-dybde-først-trær-er)
- [ ] ! [H8] [Forstå traversering med vilkårlig prioritetskø](#-h8-forstå-traversering-med-vilkårlig-prioritetskø)


### Forelesning 9: Minimale spenntrær
- [x] [I1] [Forstå skog-implementasjonen av disjunkte mengder](#i1-forstå-skog-implementasjonen-av-disjunkte-mengder)
- [ ] [I2] [Vite hva spenntrær og minimale spenntrær er](#i2-vite-hva-spenntrær-og-minimale-spenntrær-er)
- [x] ! [I3] [Forstå Generic-MST](#-i3-forstå-generic-mst)
- [ ] [I4] [Forstå hvorfor lette kanter er trygge kanter](#i4-forstå-hvorfor-lette-kanter-er-trygge-kanter)
- [x] [I5] [Forstå MST-Kruskal](#i5-forstå-mst-kruskal)
- [x] [I6] [Forstå MST-Prim](#i6-forstå-mst-prim)


### Forelesning 10: Korteste vei fra én til alle
- [ ] [J1] [Forstå ulike varianter av korteste-vei- eller korteste-sti-problemet](#j1-forstå-ulike-varianter-av-korteste-vei--eller-korteste-sti-problemet-single-source-single-destination-single-pair-all-pairs)
- [ ] [J2] [Forstå strukturen til korteste-vei-problemet](#j2-forstå-strukturen-til-korteste-vei-problemet)
- [ ] [J3] [Forstå at negative sykler gir mening for korteste enkle vei (simple path)](#j3-forstå-at-negative-sykler-gir-mening-for-korteste-enkle-vei-simple-path)
- [ ] [J4] [Forstå at korteste enkle vei kan løses vha. lengste enkle vei og omvendt](#j4-forstå-at-korteste-enkle-vei-kan-løses-vha-lengste-enkle-vei-og-omvendt)
- [ ] [J5] [Forstå hvordan man kan representere et korteste-vei-tre](#j5-forstå-hvordan-man-kan-representere-et-korteste-vei-tre)
- [x] ! [J6] [Forstå kant-slakking (edge relaxation) og Relax](#-j6-forstå-kant-slakking-edge-relaxation-og-relax)
- [ ] [J7] [Forstå ulike egenskaper ved korteste veier og slakking](#j7-forstå-ulike-egenskaper-ved-korteste-veier-og-slakking)
- [x] [J8] [Forstå Bellman-Ford](#j8-forstå-bellman-ford)
- [x] [J9] [Forstå Dag-Shortest-Paths](#j9-forstå-dag-shortest-paths)
- [ ] ! [J10] [Forstå kobling mellom Dag-Shortest-Paths og dynamisk programmering](#-j10-forstå-kobling-mellom-dag-shortest-paths-og-dynamisk-programmering)
- [x] [J11] [Forstå Dijkstra](#j11-forstå-dijkstra)


### Forelesning 11: Korteste vei fra alle til alle
- [ ] [K1] [Forstå forgjengerstrukturen for alle-til-alle-varianten av korteste vei-problemet](#k1-forstå-forgjengerstrukturen-for-alle-til-alle-varianten-av-korteste-vei-problemet-print-all-pairs-shortest-path)
- [x] [K2] [Forstå Floyd-Warshall](#k2-forstå-floyd-warshall)
- [x] [K3] [Forstå Transitive-Closure](#k3-forstå-transitive-closure)
- [ ] [K4] [Forstå Johnson](#k4-forstå-johnson)


### Forelesning 12: Maksimal flyt
- [ ] [L1] [Kunne definere flytnett, flyt og maks-flyt-problemet](#l1-kunne-definere-flytnett-flyt-og-maks-flyt-problemet)
- [ ] [L2] [Kunne håndtere antiparallelle kanter og flere kilder og sluk](#l2-kunne-håndtere-antiparallelle-kanter-og-flere-kilder-og-sluk)
- [ ] ! [L3] [Kunne definere restnettet til et flytnett med en gitt flyt](#-l3-kunne-definere-restnettet-til-et-flytnett-med-en-gitt-flyt)
- [ ] [L4] [Forstå hvordan man kan oppheve (cancel) flyt](#l4-forstå-hvordan-man-kan-oppheve-cancel-flyt)
- [ ] [L5] [Forstå hva en forøkende sti (augmenting path) er](#l5-forstå-hva-en-forøkende-sti-augmenting-path-er)
- [ ] [L6] [Forstå hva snitt, snitt-kapasitet og minimalt snitt er](#l6-forstå-hva-snitt-snitt-kapasitet-og-minimalt-snitt-er)
- [ ] ! [L7] [Forstå maks-flyt/min-snitt-teoremet](#-l7-forstå-maks-flytmin-snitt-teoremet)
- [x] [L8] [Forstå Ford-Fulkerson-Method og Ford-Fulkerson](#l8-forstå-ford-fulkerson-method-og-ford-fulkerson)
- [ ] [L9] [Vite at Ford-Fulkerson med BFS kalles Edmonds-Karp-algoritmen](#l9-vite-at-ford-fulkerson-med-bfs-kalles-edmonds-karp-algoritmen)
- [ ] [L10] [Forstå hvordan maks-flyt kan finne en maksimum bipartitt matching](#l10-forstå-hvordan-maks-flyt-kan-finne-en-maksimum-bipartitt-matching)
- [ ] ! [L11] [Forstå heltallsteoremet (integrality theorem)](#-l11-forstå-heltallsteoremet-integrality-theorem)


### Forelesning 13: NP-kompletthet
- [x] [M1] [Forstå sammenhengen mellom optimerings- og beslutnings-problemer](#m1-forstå-sammenhengen-mellom-optimerings--og-beslutnings-problemer)
- [ ] [M2] [Forstå koding (encoding) av en instans](#m2-forstå-koding-encoding-av-en-instans)
- [ ] [M3] [Forstå hvorfor løsningen på det binære ryggsekkproblemet ikke er polynomisk](#m3-forstå-hvorfor-løsningen-på-det-binære-ryggsekkproblemet-ikke-er-polynomisk)
- [ ] [M4] [Forstå forskjellen på konkrete og abstrakte problemer](#m4-forstå-forskjellen-på-konkrete-og-abstrakte-problemer)
- [ ] [M5] [Forstå representasjonen av beslutningsproblemer som formelle språk](#m5-forstå-representasjonen-av-beslutningsproblemer-som-formelle-språk)
- [x] [M6] [Forstå definisjonen av klassene P, NP og co-NP](#m6-forstå-definisjonen-av-klassene-p-np-og-co-np)
- [x] [M7] [Forstå redusibilitets-relasjonen $\leq_p$](#m7-forstå-redusibilitets-relasjonen-leq_p)
- [x] ! [M8] [Forstå definisjonen av NP-hardhet og NP-kompletthet](#-m8-forstå-definisjonen-av-np-hardhet-og-np-kompletthet)
- [x] [M9] [Forstå den konvensjonelle hypotesen om forholdet mellom P, NP og NPC](#m9-forstå-den-konvensjonelle-hypotesen-om-forholdet-mellom-p-np-og-npc)
- [x] ! [M10] [Forstå hvordan NP-kompletthet kan bevises ved én reduksjon](#-m10-forstå-hvordan-np-kompletthet-kan-bevises-ved-én-reduksjon)
- [ ] ! [M11] [Kjenne de NP-komplette problemene CIRCUIT-SAT, SAT, 3-CNF-SAT, CLIQUE, VERTEX-COVER, HAM-CYCLE, TSP og SUBSET-SUM](#-m11-kjenne-de-np-komplette-problemene-circuit-sat-sat-3-cnf-sat-clique-vertex-cover-ham-cycle-tsp-og-subset-sum)
- [ ] [M12] [Forstå at det binære ryggsekkproblemet er NP-hardt](#m12-forstå-at-det-binære-ryggsekkproblemet-er-np-hardt)
- [x] [M13] [Forstå at lengste enkle-vei-problemet er NP-hardt](#m13-forstå-at-lengste-enkle-vei-problemet-er-np-hardt)
- [x] [M14] [Være i stand til å konstruere enkle NP-kompletthetsbevis](#m14-være-i-stand-til-å-konstruere-enkle-np-kompletthetsbevis)




## Realisert

### Forelesning 1: Problemer og algoritmer
#### [A1] Forstå bokas pseudokode-konvensjoner
Bokas pseudokode-konvensjoner er generelt enkle å forstå. Det er likevel verdt å merke seg at det som regel brukes 1-indeksering, mens koden i dette dokumentet vil bruke 0-indeksering, fordi det her er implementert i Python.

#### [A2] Kjenne egenskapene til random-access machine-modellen (RAM)
Before we can analyze an algorithm, we must have a model of the implementation technology that we will use. The RAM model contains instructions commonly found in real computers: arithmetic (such as add, subtract, multiply, divide, remainder, floor, ceiling), data movement (load, store, copy), and control (conditional and unconditional branch, subroutine call and return). Each such instruction takes a constant amount of time. What if a RAM had an instruction that sorts? Then we could sort in just one instruction. Such a RAM would be unrealistic, since real computers do not have such instructions.

#### [A3] Kunne definere problem, instans og problemstørrelse
- Algoritme: Informally, an algorithm is any well-defined computational procedure that takes some value, or set of values, as input and produces some value, or set of values, as output. An algorithm is thus a sequence of computational steps that transform the input into the output.
- Problem: The statement of the problem specifies in general terms the desired input/output relationship.
- Probleminstans: In general, an instance of a problem consists of the input (satisfying whatever constraints are imposed in the problem statement) needed to compute a solution to the problem.
- Problemstørrelse: Størrelse på input tilhørende en probleminstans, f.eks. antall tall som skal sorteres i et sorteringsproblem. 

#### ! [A4] Kunne definere asymptotisk notasjon, $O$, $\Omega$, $\Theta$, $o$ og $\omega$
Notasjon | Forklaring | Tegn
---|---|---
$\omega$ | streng nedre grense | $>$
$\Omega$ | nedre grense | $\geq$
$\Theta$ | øvre og nedre grense | $=$
$O$ | øvre grense | $\leq$
$o$ | streng øvre grense | $<$

#### ! [A5] Kunne definere best-case, average-case og worst-case
**Best-case** er den minimale kjøretiden, gitt et optimalt input. **Average-case** er den gjennomsnittlige kjøretiden, over alle mulige inputs. **Worst-case** er den maksimale kjøretiden, gitt verst tenkelig input.

#### ! [A6] Forstå løkkeinvarianter og induksjon
**Løkkeinvariant**: et krav tilfredsstilles etter hver iterasjon, brukes til bevis.
**Induksjon**: Grunntilfelle + induktivt steg kan gi et bevis for alle n > grunntilfellet.

#### ! [A7] Forstå rekursiv dekomponering og induksjon over delinstanser
**Rekursiv dekomponering**:  Del instansen i mindre biter, løs problemet rekursivt for disse, og kombinér løsningene.

#### [A8] Forstå Insertion-Sort
Attributt | Insertion-Sort
---|---
Beskrivelse | Sorteringsalgoritme
Input | A: vilkårlig liste av tall
Output | Sortert liste (in place)
Worst case | $\Theta(n^2)$, hvis input er omvendt sortert
Average case | $\Theta(n^2)$
Best case | $\Theta(n)$, hvis input allerede er sortert
Minnebruk | $\Theta(1)$
In place | True
Stabil | True
Løkkeinvariant | For hver iterasjon er delarrayet $A[1 \dots j - 1]$ sortert, og element $j$ plasseres slik at $A[1 \dots j]$ blir sortert.

````python
def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        # Insert A[j] into the sorted sequence A[0 .. j - 1]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
````
[Implementasjon av Insertion-Sort](/lib/insertion_sort.py)



### Forelesning 2: Datastrukturer

#### [B1] Forstå hvordan stakker og køer fungerer

##### Stakker
Attributt | Stack-Empty
---|---
Beskrivelse | Sjekker om stakken er tom
Input | S: stakk
Output | True hvis stakken er tom, False ellers
Kjøretid | $\Theta(1)$

Attributt | Push
---|---
Beskrivelse | Legger til et element på stakken
Input | S: stakk, x: element
Kjøretid | $\Theta(1)$

Attributt | Pop
---|---
Beskrivelse | Fjerner og returnerer øverste element av stakken
Input | S: stakk
Output | Elementet på toppen av stakken
Kjøretid | $\Theta(1)$

````python
def stack_empty(S):
    return S.top == 0

def push(S, x):
    S.top += 1
    S[S.top] = x

def pop(S):
    if stack_empty(S):
        print("ERROR: underflow")
    else:
        S.top -= 1
        return S[S.top + 1]
````
[Implementasjon av stakker](lib/structures/stack.py)

##### Køer
Attributt | Enqueue
---|---
Beskrivelse | Legger til et element på halen til køen
Input | Q: kø
Kjøretid | $\Theta(1)$

Attributt | Dequeue
---|---
Beskrivelse | Fjerner og returnerer elementet som står først i køen
Input | Q: kø
Output | Det første elementet i køen
Kjøretid | $\Theta(1)$

````python
def enqueue(Q, x):
    Q[Q.tail] = x
    if Q.tail == Q.length:
        Q.tail = 0
    else:
        Q.tail += 1

def dequeue(Q):
    x = Q[Q.head]
    if Q.head == Q.length:
        Q.head = 0
    else:
        Q.head += 1
    return x
````
[Implementasjon av køer](lib/structures/queue.py)

#### [B2] Forstå hvordan lenkede lister fungerer
TODO: List-Delete', List-Search', List-Insert'

Attributt | List-Search
---|---
Beskrivelse | Søker etter et element med en spesifikk nøkkel
Input | L: lenket liste, k: nøkkel
Output | Elementet med nøkkelen, eller NIL
Kjøretid | $\Theta(n)$

Attributt | List-Insert
---|---
Beskrivelse | Legger et element til starten av en lenket liste
Input | L: lenket liste, x: element
Kjøretid | $\Theta(1)$

Attributt | List-Delete
---|---
Beskrivelse | Fjernet et element fra en dobbeltlenket liste
Input | L: dobbeltlenket liste, x: element
Kjøretid | $\Theta(1)$

````python
def list_search(L, k):
    x = L.head
    while x != None and x.key != k:
        x = x.next
    return x

def list_insert(L, x):
    x.next = L.head
    if L.head != None:
        L.head.prev = x
    L.head = x
    x.prev = None

def list_delete(L, x):
    if x.prev != None:
        x.prev.next = x.next
    else:
        L.head = x.next
    if x.next != None:
        x.next.prev = x.prev
````
[Implementasjon av lenkede lister](lib/structures/linked_list.py)

#### [B3] Forstå hvordan pekere og objekter kan implementeres
Pekere og objekter kan implementeres ved lister og indekser. Indeksene fungerer som pekere. Det er to måter å gjøre dette på:
1. Feltene/attributtene i objektet plassereres i separate lister
2. Én liste holder av en viss lengde til hvert objekt slik at det får plass til attributtene

#### ! [B4] Forstå hvordan direkte adressering og hashtabeller fungerer

##### Direkte adressering
Attributt | Direct-Address-Search
---|---
Beskrivelse | Henter et element fra en direct-access-tabell
Input | T: direct-access-tabell, k: nøkkel
Output | Elementet i tabellen med den gitt nøkkelen, eller None
Kjøretid | $\Theta(1)$

Attributt | Direct-Address-Insert
---|---
Beskrivelse | Setter et element inn i en direct-access-tabell
Input | T: direct-access-tabell, x: element
Kjøretid | $\Theta(1)$

Attributt | Direct-Address-Delete
---|---
Beskrivelse | Sletter et element i en direct-access-tabell
Input | T: direct-access-tabell, x: element
Kjøretid | $\Theta(1)$

````python
def direct_address_search(T, k):
    return T[k]

def direct_address_insert(T, x):
    T[x.key] = x
    
def direct_address_delete(T, x):
    T[x.key] = None
````

##### Hashtabeller
Attributt | Hash-Insert
---|---
Beskrivelse | Setter et element inn i en hashtabell
Input | T: hashtabell, x: element
Kjøretid | ?

Attributt | Hash-Search
---|---
Beskrivelse | Henter et element fra en hashtabell
Input | T: hashtabell, k: nøkkel
Output | Elementet i tabellen med den gitt nøkkelen, eller None
Kjøretid | ?

````python
def hash_insert(T, k):
    i = 0
    j = h(k, i)
    if T[j] == None:
        T[j] = k
        return j
    i += 1
    while i != T.m:
        j = h(k, i)
        if T[j] == None:
            T[j] = k
            return j
        i += 1

def hash_search(T, k):
    i = 0
    j = h(k, i)
    if T[j] == k:
        return j
    i += 1
    while T[j] != None and i != T.m:
        j = h(k, i)
        if T[j] == k:
            return j
        i += 1
    return None
````
[Implementasjon av hashtabeller](lib/structures/hash_table_open_address.py)

#### [B5] Forstå konfliktløsing ved kjeding (chaining)
Attributt | Chained-Hash-Insert
---|---
Beskrivelse | Setter et element inn i en kjedet hashtabell
Input | T: kjedet hashtabell, x: element
Kjøretid | ?

Attributt | Chained-Hash-Search
---|---
Beskrivelse | Henter et element fra en kjedet hashtabell
Input | T: kjedet hashtabell, k: nøkkel
Output | Elementet i tabellen med den gitt nøkkelen, eller None
Kjøretid | ?

Attributt | Chained-Hash-Delete
---|---
Beskrivelse | Sletter et element i en kjedet hashtabell
Input | T: kjedet hashtabell, x: element
Kjøretid | ?

````python
def chained_hash_insert(T, x):
    T[h(x.key)].append(x)

def chained_hash_search(T, k):
    for x in T[h(k)]:
        if x.key == k:
            return x
    return None

def chained_hash_delete(T, x):
    T[h(x.key)].remove(x)
````
[Implementasjon av kjeding](lib/structures/hash_table_chained.py)

#### [B6] Kjenne til grunnleggende hashfunksjoner
TODO

#### [B7] Vite at man for statiske datasett kan ha worst-case $O(1)$ for søk
For statiske datasett kan vi konstruere *perfekte* hashfunksjoner, og dermed oppnå $O(1)$ for søk.

#### [B8] Kunne definere amortisert analyse
Average case og amortisert kjøretid kan fremstå som litt like til å starte med, siden de begge ser på et gjennomsnitt. Men, mens average case ser på gjennomsnitt på tvers av alle mulige individuelle instanser, så handler amortisert kjøretid om å se på gjennomsnitt på tvers av en rekke av etterfølgende verste-tilfelle invokasjoner. Altså, handler gjennomsnittet i amortisert kjøretid om invokasjoner som ikke utføres uavhengig av hverandre.

Ta for eksempel det typiske eksempelet med en dynamisk tabell. Når vi ser på amortisert kjøretid i dette tilfellet, så ser vi på den gjennomsnittlige kjøretiden for en innsettelse, i verste tilfelle, når vi setter inn $n$ elementer etter hverandre i samme instans av datastrukturen.

#### [B9] Forstå hvordan dynamiske tabeller fungerer
Attributt | Table-Insert
---|---
Beskrivelse | Legger til et element i en dynamisk tabell, dobler størrelsen dersom full
Input | T: dynamisk tabell, x: element
Kjøretid | $O(1)$, amortisert

Attributt | Table-Delete
---|---
Beskrivelse | Fjerner et element fra en dynamisk tabell, halverer størrelsen dersom kun $\frac{1}{4}$ er i bruk
Input | T: dynamisk tabell, x: element
Kjøretid | $O(1)$, amortisert

````python
def table_insert(T, x):
    if T.size == 0:
        T.table = [None]
        T.size = 1
    if T.num == T.size:
        new_table = [None] * (T.size * 2)
        for i in range(len(T.table)):
            new_table[i] = T.table[i]
        T.table = new_table
        T.size *= 2
    T.table[T.num] = x
    T.num += 1

def table_delete(T, x):
    T.table[T.table.index(x)] = None
    T.num -= 1
    if T.num < T.size//4:
        new_table = [None] * (T.size//2)
        j = 0
        for i in range(len(T.table)):
            if T.table[i] != None:
                new_table[j] = T.table[i]
                j += 1
        T.table = new_table
        T.size //= 2
````
[Implementasjon av dynamiske tabeller](lib/structures/table.py)



### Forelesning 3: Splitt og hersk

#### ! [C1] Forstå designmetoden divide-and-conquer (splitt og hersk)
1. Divide: Dele opp i subproblemer
2. Conquer: Løse subproblemene
3. Combine: Kombinere løsningene til en større løsning

#### [C2] Forstå maximum-subarray-problemet med løsninger

##### Find-Maximum-Subarray
Attributt | Find-Maximum-Subarray
---|---
Beskrivelse | Finner subarrayet i et array med størst sum av elementer
Input | A: array, low: laveste indeks, high: største indeks
Kjøretid | $\Theta(n \lg n)$

````python
def find_max_crossing_subarray(A, low, mid, high):
    left_sum = -float('inf')
    _sum = 0
    for i in range(mid, low - 1, -1):
        _sum += A[i]
        if _sum > left_sum:
            left_sum = _sum
            max_left = i
    right_sum = -float('inf')
    _sum = 0
    for j in range(mid + 1, high + 1):
        _sum += A[j]
        if _sum > right_sum:
            right_sum = _sum
            max_right = j
    return max_left, max_right, left_sum + right_sum

def find_maximum_subarray(A, low, high):
    if high == low:
        return (low, high, A[low])
    else:
        mid = floor((low + high) / 2)
        left_low, left_high, left_sum = find_maximum_subarray(A, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray(A, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum
````
[Implementasjon maximum-subarray-problemet](lib/find_maximum_subarray.py)

#### [C3] Forstå Bisect og Bisect'
Attributt | Bisect
---|---
Beskrivelse | Binærsøk, søker i en sortert liste
Input | A: sortert liste, p: minste indeks, r: største indeks, v: verdi som søkes etter
Output | Indeksen til verdien det søkes etter
Worst case | $\Theta(\lg n)$
Average case | $\Theta(\lg n)$
Best case | $\Theta(1)$ if v is in the middle

````python
def bisect(A, p, r, v):
    if p <= r:
        q = floor((p + r) / 2)
        if v == A[q]:
            return q
        elif v < A[q]:
            return bisect(A, p, q - 1, v)
        else:
            return bisect(A, q + 1, r, v)
    else:
        return None

def iterative_bisect(A, p, r, v):
    while p <= r:
        q = floor((p + r) / 2)
        if v == A[q]:
            return q
        elif v < A[q]:
            r = q - 1
        else:
            p = q + 1
    return None
````
[Implementasjon av Bisect](lib/bisect.py)

#### [C4] Forstå Merge-Sort
Attributt | Merge-Sort
---|---
Beskrivelse | Sorteringsalgoritme
Input | A: vilkårlig liste av tall, p: minste indeks, r: største indeks
Output | Sortert liste
Worst case | $\Theta(n \lg n)$
Average case | $\Theta(n \lg n)$
Best case | $\Theta(n \lg n)$
Minnebruk | $\Theta(n)$
In place | False
Stabil | True

Attributt | Merge
---|---
Beskrivelse | Setter sammen to sorterte dellister til en sortert liste
Input | A: liste med to sorterte dellister, p: minste indeks, q: indeksen som splitter listene r: største indeks
Output | Sortert liste
Kjøretid | $\Theta(n)$
Minnebruk | $\Theta(n)$
In place | False
Stabil | True

````python
def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)
    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + j + 1]
    L[n1] = float('inf')
    R[n2] = float('inf')
    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def merge_sort(A, p, r):
    if p < r:
        q = floor((p + r) / 2)
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)
````
[Implementasjon Merge-Sort](lib/merge_sort.py)

#### [C5] Forstå Quicksort og Randomized-Quicksort

##### Quicksort
Attributt | Quicksort
---|---
Beskrivelse | Sorteringsalgoritme
Input | A: vilkårlig liste av tall, p: minste indeks, r: største indeks
Output | Sortert liste
Worst case | $\Theta(n^2)$, hvis input er sortert
Average case | $\Theta(n \lg n)$
Best case | $\Theta(n \lg n)$
Minnebruk | $\Theta(1)$
In place | True
Stabil | False

````python
def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)
````
[Implementasjon av Quicksort](lib/quicksort.py)

##### Randomized-Quicksort
Attributt | Quicksort
---|---
Beskrivelse | Sorteringsalgoritme
Input | A: vilkårlig liste av tall, p: minste indeks, r: største indeks
Output | Sortert liste
*Forventet* worst case | $\Theta(n \lg n)$ 
Average case | $\Theta(n \lg n)$
Best case | $\Theta(n \lg n)$
Minnebruk | $\Theta(1)$
In place | True
Stabil | False

````python
def randomized_partition(A, p, r):
    i = randint(p, r)
    A[i], A[r] = A[r], A[i]
    return partition(A, p, r)

def randomized_quicksort(A, p, r):
    if p < r:
        q = randomized_partition(A, p, r)
        randomized_quicksort(A, p, q - 1)
        randomized_quicksort(A, q + 1, r)
````
[Implementasjon av Randomized-Quicksort](lib/randomized_select.py)

#### ! [C6] Kunne løse rekurrenser med substitusjon, rekursjonstrær og masterteoremet

#### ! [C7] Kunne løse rekurrenser med iterasjonsmetoden

#### [C8] Forstå hvordan variabelskifte fungerer



### Forelesning 4: Rangering i lineær tid

#### ! [D1] Forstå hvorfor sammenligningsbasert sortering har en worst-case på $\Omega(n \lg n)$
En liste med $n$ elementer har $n!$ permutasjoner, som vi ved å sortere skal finne én bestemt av. Vi kan modellere problemet som et binært beslutningstre, med $n!$ løvnoder. Høyden på treet blir antall beslutninger vi må gjøre, altså antall sammenligninger, for å komme til en løsning. Det totale antall noder i et komplett binærtre med $n!$ løvnoder er $2n!-1$. Det maksimale antall løvnoder i et binærtre er $2^h$. Vi har da $2^h \geq n! \implies h \geq \lg{n!} \implies h = \Omega(n \lg n)$

#### [D2] Vite hva en stabil sorteringsalgoritme er
En sorteringsalgoritme sies å være stabil dersom rekkefølgen av like elementer i listen som sorteres blir bevart.

#### [D3] Forstå Counting-Sort, og hvorfor den er stabil
Attributt | Counting-Sort
---|---
Beskrivelse | Sorteringsalgoritme for heltall mellom $0$ og $k$
Input | A: liste av heltall mellom 0 og k, B: liste for resultatet, k: det høyeste tallet
Output | Sortert liste
Kjøretid | $\Theta(n + k)$ 
Minnebruk | $\Theta(k)$
In place | False
Stabil | True

````python
def counting_sort(A, B, k):
    C = [0] * k
    for i in A:
        C[i] += 1
    for i in range(1, k):
        C[i] += C[i-1]
    for i in range(len(A) - 1, -1, -1):
        v = A[i]
        B[C[v]-1] = v
        C[v] -= 1
````
[Implementasjon av Counting-Sort](lib/counting_sort.py)

#### ! [D4] Forstå Radix-Sort, og hvorfor den trenger en stabil subrutine
Attributt | Radix-Sort (using Counting-Sort)
---|---
Beskrivelse | Sorteringsalgoritme for elementer med $d$ siffer, der hvert siffer er mellom $0$ og $k$
Input | A: liste som skal sorteres, B: liste for resultatet, k: det høyeste sifferet, d: antall siffer i hvert element
Output | Sortert liste
Kjøretid | $\Theta(d(n + k))$ 
Minnebruk | $\Theta(n + k)$
In place | False
Stabil | True

Merk: følgende implementasjon sorterer strenger. 
````python
def counting_sort(A, B, k, d):
    C = [0] * k
    for v in A:
        C[ord(v[d])] += 1
    for i in range(1, k):
        C[i] += C[i-1]
    for i in range(len(A) - 1, -1, -1):
        v = A[i]
        B[C[ord(v[d])]-1] = v
        C[ord(v[d])] -= 1

def radix_sort(A, d):
    B = [None] * len(A)
    k = (ord(max(c for word in A for c in word)) + 1) \
        if len(A) and d else 0
    for i in range(d-1,-1,-1):
        counting_sort(A, B, k, i)
        A, B = B, A
    return A
````
[Implementasjon av Radix-Sort](lib/radix_sort.py)

#### [D5] Forstå Bucket-Sort
Attributt | Bucket-Sort
---|---
Beskrivelse | Sorteringsalgoritme for tall mellom 0 og 1
Input | A: liste av tall mellom 0 og 1
Output | Sortert liste
Worst case | $\Theta(n^2)$, hvis mange elementer havner i samme bøtte
Average case | $\Theta(n)$
Best case | $\Theta(n)$
Minnebruk | $\Theta(n)$
In place | False
Stabil | True

````python
def bucket_sort(A):
    n = len(A)
    B = [[] for _ in range(n)]
    for i in range(n):
        B[floor(n * A[i])].append(A[i])
    for j in range(n):
        insertion_sort(B[j])
    return [value for bucket in B for value in bucket]
````
[Implementasjon av Bucket-Sort](lib/bucket_sort.py)

#### [D6] Forstå Randomized-Select
Attributt | Randomized-Select
---|---
Beskrivelse | Finner det $i$-te minste elementet i arrayet $A[p \dots r]$
Input | A: liste av tall, p: minste indeks, r: største indeks, i: ordningstallet
Output | Det $i$-te minste elementet
Worst case | $\Theta(n^2)$
Average case | $\Theta(n)$
Best case | $\Theta(n)$
In place | True

````python
def randomized_select(A, p, r, i):
    if p == r:
        return A[p]
    q = randomized_partition(A,p,r)
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return randomized_select(A, p, q - 1, i)
    else:
        return randomized_select(A, q + 1, r, i - k)
````
[Implementasjon av Randomized-Select](lib/randomized_select.py)

#### [D7] Kjenne til Select
Merk: Det kreves ikke grundig forståelse av virkemåten til Select.



### Forelesning 5: Rotfaste trestrukturer

#### ! [E1] Forstå hvordan heaps fungerer, og hvordan de kan brukes som prioritetskøer
Max-Heap kan brukes som en prioritetskø som prioriterer de største elementene, Min-Heap kan brukes som en prioritetskø som prioriterer de minste elementene.

Attributt | Parent
---|---
Beskrivelse | Finner indeksen til forelderen til en node i en binærhaug
Input | i: indeksen til en node
Output | Indeksen til forelderen
Kjøretid | $\Theta(1)$

Attributt | Left
---|---
Beskrivelse | Finner det venstre barnet til en node i en binærhaug
Input | i: indeksen til en node
Output | Indeksen til det venstre barnet
Kjøretid | $\Theta(1)$

Attributt | Right
---|---
Beskrivelse | Finner det høyre barnet til en node i en binærhaug
Input | i: indeksen til en node
Output | Indeksen til det høyre barnet
Kjøretid | $\Theta(1)$

##### Heap

````python
def parent(i):
    return floor(i / 2)

def left(i):
    return 2 * i + 1 # 2 * i, if 1-indexed

def right(i):
    return 2 * i + 2  # 2 * i + 1, if 1-indexed
````

##### Max-Heap
Attributt | Max-Heapify
---|---
Beskrivelse | Realiserer maks-haug-egenskapen for en gitt node i en maks-haug
Input | A: maks-haug i: indeksen til en node
Kjøretid | $O(\lg n)$

Attributt | Build-Max-Heap
---|---
Beskrivelse | Bygger en maks-haug
Input | A: array
Kjøretid | $O(n)$

Attributt | Heap-Maximum
---|---
Beskrivelse | Returnerer det maksimale elementet i en maks-haug
Input | A: maks-haug
Output | Det maksimale elementet
Kjøretid | $\Theta(1)$

Attributt | Heap-Extract-Maximum
---|---
Beskrivelse | Fjerner og returnerer det maksimale elementet i en maks-haug
Input | A: maks-haug
Output | Det maksimale elementet
Kjøretid | $O(\lg n)$

Attributt | Heap-Increase-Key
---|---
Beskrivelse | Setter nøkkelen til en node til en ny (høyere) verdi
Input | A: maks-haug, i: indeks, key: den nye nøkkelen
Kjøretid | $O(\lg n)$

Attributt | Max-Heap-Insert
---|---
Beskrivelse | Setter inn et nytt element i en maks-haug
Input | A: maks-haug, x: element
Kjøretid | $O(\lg n)$

````python
def max_heapify(A, i):
    l = left(i)
    r = right(i)
    if l < A.heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < A.heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)

def build_max_heap(A):
    A.heap_size = len(A)
    for i in range(floor(len(A) / 2), -1, -1):
        max_heapify(A, i)

def heap_maximum(A):
    return A[0]

def heap_extract_max(A):
    if A.heap_size < 0:
        print("ERROR: heap underflow")
    max_ = A[0]
    A[0] = A[A.heap_size - 1]
    A.heap_size -= 1
    max_heapify(A, 0)
    return max_

def heap_increase_key(A, i, key):
    if key < A[i]:
        print("ERROR: new key is smaller than current key")
    A[i] = key
    while i > 0 and A[parent(i)] < A[i]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)

def max_heap_insert(A, key):
    A.heap_size += 1
    A[A.heap_size - 1] = -float('inf')
    heap_increase_key(A, A.heap_size - 1, key)
````

##### Min-Heap
Attributt | Min-Heapify
---|---
Beskrivelse | Realiserer min-haug-egenskapen for en gitt node i en min-haug
Input | A: min-haug i: indeksen til en node
Kjøretid | $O(\lg n)$

Attributt | Build-Min-Heap
---|---
Beskrivelse | Bygger en min-haug
Input | A: array
Kjøretid | $O(n)$

Attributt | Heap-Minimum
---|---
Beskrivelse | Returnerer det minimale elementet i en min-haug
Input | A: min-haug
Output | Det minimale elementet
Kjøretid | $\Theta(1)$

Attributt | Heap-Extract-Minimum
---|---
Beskrivelse | Fjerner og returnerer det minimale elementet i en min-haug
Input | A: min-haug
Output | Det minimale elementet
Kjøretid | $O(\lg n)$

Attributt | Heap-Increase-Key
---|---
Beskrivelse | Setter nøkkelen til en node til en ny (høyere) verdi
Input | A: min-haug, i: indeks, key: den nye nøkkelen
Kjøretid | $O(\lg n)$

Attributt | Min-Heap-Insert
---|---
Beskrivelse | Setter inn et nytt element i en min-haug
Input | A: min-haug, x: element
Kjøretid | $O(\lg n)$

````python
def min_heapify(A, i):
    l = left(i)
    r = right(i)
    if l < A.heap_size and A[l] < A[i]:
        smallest = l
    else:
        smallest = i
    if r < A.heap_size and A[r] < A[smallest]:
        smallest = r
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        min_heapify(A, smallest)

def build_min_heap(A):
    A.heap_size = len(A)
    for i in range(floor(len(A) / 2), -1, -1):
        min_heapify(A, i)

def heap_minimum(A):
    return A[0]

def heap_extract_min(A):
    if A.heap_size < 0:
        print("ERROR: heap underflow")
    min_ = A[0]
    A[0] = A[A.heap_size - 1]
    A.heap_size -= 1
    min_heapify(A, 0)
    return min_

def heap_decrease_key(A, i, key):
    if A[i] < key:
        print("ERROR: new key is larger than current key")
    A[i] = key
    while i > 0 and A[i] < A[parent(i)]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)

def min_heap_insert(A, key):
    A.heap_size += 1
    A[A.heap_size - 1] = float('inf')
    heap_decrease_key(A, A.heap_size - 1, key)
````
[Implementasjon av heaps](lib/structures/binary_heap.py)

#### [E2] Forstå Heapsort
Attributt | Heapsort
---|---
Beskrivelse | Sorteringsalgoritme
Input | A: vilkårlig liste av tall
Output | Sortert liste (in place)
Kjøretid| $O(n \lg n)$
Minnebruk | $\Theta(1)$
In place | True
Stabil | False

````python
def heapsort(A):
    build_max_heap(A)
    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        A.heap_size -= 1
        max_heapify(A, 0)
````
[Implementasjon av Heapsort](lib/heapsort.py)

#### [E3] Forstå hvordan rotfaste trær kan implementeres
Binærtrær kan representeres ved at hver node har tre pekere: p (parent), left og right.
For trær hvor node kan ha flere barn, kan man også representere det ved tre pekere: p, left-child og right-sibling.

#### ! [E4] Forstå hvordan binære søketrær fungerer
Attributt | Inorder-Tree-Walk
---|---
Beskrivelse | Printer et binærsøketre *inorder*
Input | x: noden å begynne på (gjerne rotnoden)
Output | Utskrift av nodene i rekkefølge
Kjøretid | $\Theta(n)$

Attributt | Tree-Search
---|---
Beskrivelse | Søker etter et node med en gitt nøkkel
Input | x: noden å begynne på (gjerne rotnoden), k: nøkkelen det søkes etter
Output | Noden med nøkkelen, eller NIL
Kjøretid | $O(\lg n)$

Attributt | Tree-Minimum
---|---
Beskrivelse | Returnerer den minste noden i binærsøketreet
Input | x: noden å begynne på (gjerne rotnoden)
Output | Den minste noden
Kjøretid | $O(\lg n)$

Attributt | Tree-Maximum
---|---
Beskrivelse | Returnerer den største noden i binærsøketreet
Input | x: noden å begynne på (gjerne rotnoden)
Output | Den største noden
Kjøretid | $O(\lg n)$

Attributt | Tree-Successor
---|---
Beskrivelse | Returnerer noden som er etter den gitt noden, når de er i *inorder* rekkefølge
Input | x: en node
Output | *Successor*-en til den gitte noden
Kjøretid | $O(\lg n)$

Attributt | Tree-Insert
---|---
Beskrivelse | Legger til en node til treet, på en gyldig plass
Input | T: treet (rotnoden), z: noden som legges til
Kjøretid | $O(\lg n)$

Attributt | Transplant
---|---
Beskrivelse | Erstatter en node i treet med en annen
Input | T: treet (rotnoden), u: noden som skal erstattes, v: noden som erstatter
Kjøretid | $\Theta(1)$

Attributt | Tree-Delete
---|---
Beskrivelse | Sletter den gitte noden fra treet
Input | x: en node
Kjøretid | $O(\lg n)$


````python
def inorder_tree_walk(x):
    if x != None:
        inorder_tree_walk(x.left)
        print(x.key)
        inorder_tree_walk(x.right)

def tree_search(x, k):
    if x == None or k == x.key:
        return x
    if k < x.key:
        return tree_search(x.left, k)
    else:
        return tree_search(x.right, k)

def iterative_tree_search(x, k):
    while x != None and k != x.key:
        if k < x.key:
            x = x.left
        else:
            x = x.right
    return x

def tree_minimum(x):
    while x.left != None:
        x = x.left
    return x

def tree_maximum(x):
    while x.right != None:
        x = x.right
    return x

def tree_successor(x):
    if x.right != None:
        return tree_minimum(x.right)
    y = x.p
    while y != None and x == y.right:
        x = y
        y = y.p
    return y

def tree_insert(T, z):
    y = None
    x = T.root
    while x != None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y == None:
        T.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z

def transplant(T, u, v):
    if u.p == None:
        T.root = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v
    if v != None:
        v.p = u.p

def tree_delete(T, z):
    if z.left == None:
        transplant(T, z, z.right)
    elif z.right == None:
        transplant(T, z, z.left)
    else:
        y = tree_minimum(z.right)
        if y.p != z:
            transplant(T, y, y.right)
            y.right = z.right
            y.right.p = y
        transplant(T, z, y)
        y.left = z.left
        y.left.p = y
````
[Implementasjon av binære søketrær](lib/structures/binary_tree.py)

#### [E5] Vite at forventet høyde for et tilfeldig binært søketre er $\Theta(\lg n)$
Dette er bevist i boka på side 300, men det er ikke nødvendig å forstå beviset.

#### [E6] Vite at det finnes søketrær med garantert høyde på $\Theta(\lg n)$
Trivielt?


### Forelesning 6: Dynamisk programmering
#### ! [F1] Forstå ideen om en delinstansgraf
#### ! [F2] Forstå designmetoden dynamisk programmering
#### ! [F3] Forstå løsning ved memoisering (top-down)
#### [F4] Forstå løsning ved iterasjon (bottom-up)
#### [F5] Forstå hvordan man rekonstruerer en løsning fra lagrede beslutninger
#### [F6] Forstå hva optimal delstruktur er
#### [F7] Forstå hva overlappende delinstanser er
#### [F8] Forstå eksemplene stavkutting og LCS
##### Stavkutting
````python
def cut_rod(p, n):
    """
    CUT-ROD

    Time Complexity: O(2^n)
    """
    if n == 0:
        return 0
    q = -float('inf')
    for i in range(1, n + 1):
        q = max(q, p[i - 1] + cut_rod(p, n - i))
    return q

def memoized_cut_rod(p, n):
    """
    MEMOIZED-CUT-ROD

    Time Complexity: O(n^2)
    """
    r = [-float('inf')] * (n + 1)
    return memoized_cut_rod_aux(p, n, r)

def memoized_cut_rod_aux(p, n, r):
    if r[n - 1] >= 0:
        return r[n - 1]
    if n == 0:
        q = 0
    else:
        q = -float('inf')
        for i in range(1, n + 1):
            q = max(q, p[i - 1] + memoized_cut_rod_aux(p, n - i))
    r[n] = q
    return q

def bottom_up_cut_rod(p, n):
    """
    BOTTOM-UP-CUT-ROD

    Time Complexity: O(n^2)
    """
    r = [0] * (n + 1)
    for j in range(1, n + 1):
        q = -float('inf')
        for i in range(1, j + 1):
            q = max(q, p[i] + r[j - i])
        r[j] = q
    return r[n]

def extended_bottom_up_cut_rod(p, n):
    """
    EXTENDED-BOTTOM-UP-CUT-ROD

    Time Complexity: O(n^2)
    """
    r = [0] * (n + 1)
    s = [0] * (n + 1)
    for j in range(1, n + 1):
        q = -float('inf')
        for i in range(1, j + 1):
            if q < p[i] + r[j - i]:
                q = p[i] + r[j - i]
                s[j] = i
        r[j] = q
    return r, s

def print_cut_rod_solution(p, n):
    """
    PRINT-CUT-ROD-SOLUTION

    Time Complexity: O(n^2)
    """
    _, s = extended_bottom_up_cut_rod(p, n)
    while n > 0:
        print(s[n])
        n -= s[n]
````
[Implementasjon av stavkutting](lib/cut_rod.py)

##### Longest common subsequence (LCS)
````python
def lcs_length(X, Y):
    """
    LCS-LENGTH

    Time Complexity: Theta(m*n)
    Space Complexity: Theta(m*n)
    """
    m = len(X)
    n = len(Y)
    b = [[0] * n for _ in range(m)]
    c = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i - 1][j - 1] = '↖'
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i - 1][j - 1] = '↑'
            else:
                c[i][j] = c[i][j - 1]
                b[i - 1][j - 1] = '←'
    return c, b

def print_lcs(b, X, i, j):
    """
    PRINT-LCS

    Time Complexity: Theta(m + n)
    Space Complexity: Theta(1)
    """
    if i == -1 or j == -1:
        return
    if b[i][j] == '↖':
        print_lcs(b, X, i - 1, j - 1)
        print(X[i], end=" ")
    elif b[i][j] == '↑':
        print_lcs(b, X, i - 1, j)
    else:
        print_lcs(b, X, i, j - 1)
````
[Implementasjon av LCS](lib/longest_common_subsequence.py)

#### [F9] Forstå løsningen på det binære ryggsekkproblemet
````python
def knapsack(n, W, w, v):
    """
    KNAPSACK

    Time Complexity: Theta(nW) = Theta(n2^m)
    """
    if n == 0:
        return 0
    x = knapsack(n - 1, W)
    if w[n] > W:
        return x
    else:
        y = knapsack(n - 1, W - w[n]) + v[n]
        return max(x, y)

def bottom_up_knapsack(n, W, w, v):
    """
    KNAPSACK'

    Time Complexity: Theta(nW) = Theta(n2^m)
    """
    K = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(W + 1):
            x = K[i - 1][j]
            if j < w[i]:
                K[i][j] = x
            else:
                y = K[i - 1][j - w[i]] + v[i]
                K[i][j] = max(x, y)
````
[Implementasjon av det binære ryggsekkproblemet](lib/knapsack.py)



### Forelesning 7: Grådige algoritmer

#### ! [G1] Forstå designmetoden grådighet

#### ! [G2] Forstå grådighetsegenskapen (the greedy-choice property)

#### [G3] Forstå eksemplene aktivitet-utvelgelse og det kontinuerlige ryggsekkproblemet

##### Aktivitet-utvelgelse

##### Det kontinuerlige ryggsekkproblemet

#### [G4] Forstå Huffman og Huffman-koder
````python
def huffman(C):
    n = len(C)
    Q = build_min_heap(C.copy())
    for _ in range(n - 1):
        z = Node()
        x = heap_extract_min(Q)
        y = heap_extract_min(Q)
        z.freq = x.freq + y.freq
        min_heap_insert(Q, z)
    return heap_extract_min(Q)
````
[Implementasjon av Huffman](lib/huffman.py)



### Forelesning 8: Traversering av grafer

#### [H1] Forstå hvordan grafer kan implementeres
To vanlige implementasjoner av grafer er å bruke nabolister, eller en nabomatrise. Nabolister er effektive for grafer med få kanter, mens nabomatriser er effektive for grafer med mange kanter.

#### [H2] Forstå BFS, også for å finne korteste vei uten vekter
````python
def bfs(G, s):
    for u in G.V - set(s):
        u.color = "white"
        u.d = float('inf')
        u.pi = None
    s.color = "gray"
    s.d = 0
    s.pi = None
    Q = Queue()
    enqueue(Q, s)
    while Q:
        u = dequeue(Q)
        for v in G.Adj[u]:
            if v.color == "white":
                v.color = "gray"
                v.d = u.d + 1
                v.pi = u
                enqueue(Q, v)
        u.color = "black"
````
[Implementasjon av BFS](lib/bfs.py)

#### [H3] Forstå DFS, parentesteoremet og hvit-sti-teoremet
````python
def dfs(G):
    global time
    for u in G.V:
        u.color == "white"
        u.pi = None
    time = 0
    for u in G.V:
        if u.color == "white":
            dfs_visit(G, u)
    
def dfs_visit(G, u):
    global time
    time += 1
    u.d = time
    u.color = "gray"
    for v in G.Adj[u]:
        if v.color == "white":
            v.pi = u
            dfs_visit(G, v)
    u.color = "black"
    time += 1
    u.f = time
````
[Implementasjon av DFS](lib/dfs.py)

#### [H4] Forstå hvordan DFS klassifiserer kanter

#### [H5] Forstå Topological-Sort
````python
def topological_sort(G):
    global L
    L = LinkedList()
    ts_dfs(G)
    return L

def ts_dfs(G):
    global time
    for u in G.V:
        u.color == "white"
        u.pi = None
    time = 0
    for u in G.V:
        if u.color == "white":
            ts_dfs_visit(G, u)
    
def ts_dfs_visit(G, u):
    global time, L
    time += 1
    u.d = time
    u.color = "gray"
    for v in G.Adj[u]:
        if v.color == "white":
            v.pi = u
            ts_dfs_visit(G, v)
    u.color = "black"
    time += 1
    u.f = time
    list_insert(L, LinkedListElement(u))
````
[Implementasjon av Topological-Sort](lib/topological_sort.py)

#### [H6] Forstå hvordan DFS kan implementeres med en stakk

#### [H7] Forstå hva traverseringstrær (som bredde-først- og dybde-først-trær) er

#### ! [H8] Forstå traversering med vilkårlig prioritetskø



### Forelesning 9: Minimale spenntrær

#### [I1] Forstå skog-implementasjonen av disjunkte mengder
````python
def connected_components(G):
    for v in G.V:
        make_set(v)
    for u, v in G.E:
        if find_set(u) != find_set(v):
            union(u, v)

def same_component(u, v):
    return find_set(u) == find_set(v)
    
def make_set(x):
    x.p = x
    x.rank = 0

def union(x, y):
    link(find_set(x), find_set(y))

def link(x, y):
    if x.rank > y.rank:
        y.p = x
    else:
        x.p = y
        if x.rank == y.rank:
            y.rank += 1

def find_set(x):
    if x != x.p:
        x.p = find_set(x.p)
    return x.p
````
[Implementasjon av disjunkte mengder](lib/structures/disjunct_set.py) 

#### [I2] Vite hva spenntrær og minimale spenntrær er

#### ! [I3] Forstå Generic-MST
````
GENERIC-MST(G, w):
    A = Ø
    while A does not form a spanning tree
        find an edge (u, v) that is safe for A
        A = A U {(u, v)}
    return A
````

#### [I4] Forstå hvorfor lette kanter er trygge kanter

#### [I5] Forstå MST-Kruskal
````python
def mst_kruskal(G, w):
    A = set()
    for v in G.V:
        make_set(v)
    edges = sorted(G.E, key=lambda edge: w[edge[0]][edge[1]])
    for u, v in edges:
        if find_set(u) != find_set(v):
            A.add((u, v))
            union(u, v)
````
[Implementasjon av MST-Kruskal](lib/minimal_spanning_tree.py)

#### [I6] Forstå MST-Prim
````python
def mst_prim(G, w, r):
    for u in G.V:
        u.key = float('inf')
        u.pi = None
    r.key = 0
    Q = build_min_heap(G.V.copy())
    while Q:
        u = heap_extract_min(Q)
        for v in G.Adj[u]:
            if v in Q and w[u][v] < v.key:
                v.pi = u
                v.key = w[u][v]
````
[Implementasjon av MST-Prim](lib/minimal_spanning_tree.py)



### Forelesning 10: Korteste vei fra én til alle

#### [J1] Forstå ulike varianter av korteste-vei- eller korteste-sti-problemet (Single-source, single-destination, single-pair, all-pairs)

#### [J2] Forstå strukturen til korteste-vei-problemet

#### [J3] Forstå at negative sykler gir mening for korteste enkle vei (simple path)

#### [J4] Forstå at korteste enkle vei kan løses vha. lengste enkle vei og omvendt

#### [J5] Forstå hvordan man kan representere et korteste-vei-tre

#### ! [J6] Forstå kant-slakking (edge relaxation) og Relax
````python
def relax(u, v, w):
    if v.d > u.d + w[u][v]:
        v.d = u.d + w[u][v]
        v.pi = u
````
[Implementasjon av Relax](lib/single_source_shortest_path.py)

#### [J7] Forstå ulike egenskaper ved korteste veier og slakking
(Triangle inequality, upper-bound property, no-path property, convergence property,
path-relaxation property, predecessor-subgraph property)

#### [J8] Forstå Bellman-Ford
<details>
    <summary>Kode</summary>
    
````python
def bellman_ford(G, w, s):
    initialize_single_source(G, s)
    for _ in range(len(G.V) - 1):
        for u, v in G.E:
            relax(u, v, w)
    for u, v in G.E:
        if v.d > u.d + w[u][v]:
            return False
    return True
````
[Implementasjon av Bellman-Ford](lib/single_source_shortest_path.py)
</details>

#### [J9] Forstå Dag-Shortest-Paths
````python
def dag_shortest_paths(G, w, s):
    initialize_single_source(G, s)
    u = topological_sort(G)
    while u != None:
        for v in G.Adj[u.key]:
            relax(u, v, w)
        u = u.next
````
[Implementasjon av Dag-Shortest-Paths](lib/single_source_shortest_path.py)

#### ! [J10] Forstå kobling mellom Dag-Shortest-Paths og dynamisk programmering

#### [J11] Forstå Dijkstra
````python
def dijkstra(G, w, s):
    initialize_single_source(G, s)
    S = set()
    Q = build_min_heap(G.V.copy())
    while Q:
        u = heap_extract_min(Q)
        S.add(u)
        for v in G.Adj[u]:
            relax(u, v, w)
````
[Implementasjon av Dijkstra](lib/single_source_shortest_path.py)



### Forelesning 11: Korteste vei fra alle til alle

#### [K1] Forstå forgjengerstrukturen for alle-til-alle-varianten av korteste vei-problemet
````python
def print_all_pairs_shortest_path(Pi, i, j):
    if i == j:
        print(i)
    elif Pi[i][j] == None:
        print(f"No path from {i} to {j} exists.")
    else:
        print_all_pairs_shortest_path(Pi, i, Pi[i][j])
        print(j)
````
[Implementasjon av Print-All-Pairs-Shortest-Path](lib/all_pairs_shortest_paths.py)

#### [K2] Forstå Floyd-Warshall
````python
def floyd_warshall(W):
    n = len(W)
    D = [None] * (n + 1)
    D[0] = W
    for k in range(1, n + 1):
        D[k] = [[None] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                D[k][i][j] = min(D[k - 1][i][j], \
                    D[k - 1][i][k] + D[k - 1][k][j])
    return D[n]
````
[Implementasjon av Floyd-Warshall](lib/all_pairs_shortest_paths.py)

#### [K3] Forstå Transitive-Closure
````python
def transitive_closure(G):
    n = len(G.V)
    T = [None] * (n + 1)
    T[0] = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j or (i, j) in G.E:
                T[0][i][j] = 1
            else:
                T[0][i][j] = 0
    for k in range(1, n + 1):
        T[k] = [[None] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                T[k][i][j] = T[k - 1][i][j] or T[k - 1][i][k] and T[k - 1][k][j]
    return T[n]

def transitive_closure_optimized(G):
    n = len(G.V)
    T = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j or (i, j) in G.E:
                T[i][j] = 1
            else:
                T[i][j] = 0
    for k in range(1, n + 1):
        for i in range(n):
            for j in range(n):
                T[i][j] = T[i][j] or T[i][k] and T[k][j]
    return T
````
[Implementasjon av Transitive-Closure](lib/transitive_closure.py)

#### [K4] Forstå Johnson
````python
def johnson(G, w):
    pass # TODO: implement johnson
````
[Implementasjon av Johnson](lib/all_pairs_shortest_paths.py)



### Forelesning 12: Maksimal flyt

#### [L1] Kunne definere flytnett, flyt og maks-flyt-problemet

#### [L2] Kunne håndtere antiparallelle kanter og flere kilder og sluk

#### ! [L3] Kunne definere restnettet til et flytnett med en gitt flyt

#### [L4] Forstå hvordan man kan oppheve (cancel) flyt

#### [L5] Forstå hva en forøkende sti (augmenting path) er

#### [L6] Forstå hva snitt, snitt-kapasitet og minimalt snitt er

#### ! [L7] Forstå maks-flyt/min-snitt-teoremet

#### [L8] Forstå Ford-Fulkerson-Method og Ford-Fulkerson
````
FORD-FULKERSON-METHOD(G, s, t)
    initialize flow f to 0
    while there exists an augmenting path p in the residual network Gf
        augment flow f along p
    return f

FORD-FULKERSON(G, s, t)
    for each edge (u, v) in G.E
        (u, v).f = 0
    while there exists a path p from s to t in the residual network Gf
        cf(p) = min{cf(u, v) : (u, v) is in p}
        for each edge (u, v) in p
            if (u, v) in E
                (u, v).f = (u, v).f + cf(p)
            else (u, v).f = (u, v).f - cf(p)
````

#### [L9] Vite at Ford-Fulkerson med BFS kalles Edmonds-Karp-algoritmen
````python
# TODO: Implement Edmonds-Karp
````
[Implementasjon av Edmonds-Karp](lib/ford_fulkerson.py)

#### [L10] Forstå hvordan maks-flyt kan finne en maksimum bipartitt matching

#### ! [L11] Forstå heltallsteoremet (integrality theorem)



### Forelesning 13: NP-kompletthet

#### [M1] Forstå sammenhengen mellom optimerings- og beslutnings-problemer
Optimeringsproblemer har gjerne tilhørende beslutningsproblemer og omvendt. For eksempel kan optimeringsproblemet *å finne korteste vei* knyttes til beslutningsproblemet *finnes det en vei med avstand $\leq k$?*.

#### [M2] Forstå koding (encoding) av en instans

#### [M3] Forstå hvorfor løsningen på det binære ryggsekkproblemet ikke er polynomisk

#### [M4] Forstå forskjellen på konkrete og abstrakte problemer

#### [M5] Forstå representasjonen av beslutningsproblemer som formelle språk

#### [M6] Forstå definisjonen av klassene P, NP og co-NP
NP er beslutningsproblemer der ja-svar kan verifiseres i polynomisk tid. co-NP er beslutninger der nei-svar kan verifiseres i polynomisk tid. P er problemene i NP som kan løses i polynomisk tid. 

#### [M7] Forstå redusibilitets-relasjonen $\leq_p$
Dersom vi reduserer $A$ til $B$ skriver vi $A \leq_p B$. Det vil si at $B$ er minst like vanskelig som $A$.

#### ! [M8] Forstå definisjonen av NP-hardhet og NP-kompletthet
At et problem er NP-hardt vil si at det er minst like vanskelig som de vanskeligste problemene i NP. Hvis et problem er i NP og er NP-hardt, så er det NP-komplett.

#### [M9] Forstå den konvensjonelle hypotesen om forholdet mellom P, NP og NPC
Den konvensjonelle hypotesen går ut på at
- P $\subset$ NP
- P $\neq$ NP
- P $\cap$ NPC $= \emptyset$

#### ! [M10] Forstå hvordan NP-kompletthet kan bevises ved én reduksjon
Dersom vi reduserer et problem som er bevist NP-komplett $A$, til et problem $B$ i NP, $A \leq_p B$, vet vi at $B$ er minst like vanskelig som $A$ og derfor også NP-komplett. 

#### ! [M11] Kjenne de NP-komplette problemene CIRCUIT-SAT, SAT, 3-CNF-SAT, CLIQUE, VERTEX-COVER, HAM-CYCLE, TSP og SUBSET-SUM

#### [M12] Forstå at det binære ryggsekkproblemet er NP-hardt

#### [M13] Forstå at lengste enkle-vei-problemet er NP-hardt
Hamiltonvei-problemet kan reduseres til lengste enkle-vei-problemet, derfor er lengste enkle-vei-problemet NP-hardt.

#### [M14] Være i stand til å konstruere enkle NP-kompletthetsbevis
Ved reduksjon fra NP-komplette problemer.