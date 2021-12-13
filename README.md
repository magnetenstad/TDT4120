
# TDT4120 Pensumhefte, 2021

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
- [x] ! [A4] [Kunne definere asymptotisk notasjon, $O$, $\Omega$, $\Theta$, $o$ og $\omega$](#a4-kunne-definere-asymptotisk-notasjon-o-omega-theta-o-og-omega)
- [x] ! [A5] [Kunne definere best-case, average-case og worst-case](#a5-kunne-definere-best-case-average-case-og-worst-case)
- [x] ! [A6] [Forstå løkkeinvarianter og induksjon](#a6-forstå-løkkeinvarianter-og-induksjon)
- [x] ! [A7] [Forstå rekursiv dekomponering og induksjon over delinstanser](#a7-forstå-rekursiv-dekomponering-og-induksjon-over-delinstanser)
- [x] [A8] [Forstå Insertion-Sort](#a8-forstå-insertion-sort)


### Forelesning 2: Datastrukturer
- [x] [B1] [Forstå hvordan stakker og køer fungerer](#b1-forstå-hvordan-stakker-og-køer-fungerer)
- [x] [B2] [Forstå hvordan lenkede lister fungerer](#b2-forstå-hvordan-lenkede-lister-fungerer)
- [x] [B3] [Forstå hvordan pekere og objekter kan implementeres](#b3-forstå-hvordan-pekere-og-objekter-kan-implementeres)
- [x] ! [B4] [Forstå hvordan direkte adressering og hashtabeller fungerer](#b4-forstå-hvordan-direkte-adressering-og-hashtabeller-fungerer)
- [x] [B5] [Forstå konfliktløsing ved kjeding (chaining)](#b5-forstå-konfliktløsing-ved-kjeding-chaining)
- [x] [B6] [Kjenne til grunnleggende hashfunksjoner](#b6-kjenne-til-grunnleggende-hashfunksjoner)
- [x] [B7] [Vite at man for statiske datasett kan ha worst-case O(1) for søk](#b7-vite-at-man-for-statiske-datasett-kan-ha-worst-case-o1-for-søk)
- [x] [B8] [Kunne definere amortisert analyse](#b8-kunne-definere-amortisert-analyse)
- [x] [B9] [Forstå hvordan dynamiske tabeller fungerer](#b8-kunne-definere-amortisert-analyse)


### Forelesning 3: Splitt og hersk
- [x] ! [C1] [Forstå designmetoden divide-and-conquer (splitt og hersk)](#c1-forstå-designmetoden-divide-and-conquer-splitt-og-hersk)
- [x] [C2] [Forstå maximum-subarray-problemet med løsninger](#c2-forstå-maximum-subarray-problemet-med-løsninger)
- [x] [C3] [Forstå Bisect og Bisect'](#c3-forstå-bisect-og-bisect)
- [x] [C4] [Forstå Merge-Sort](#c4-forstå-merge-sort)
- [x] [C5] [Forstå Quicksortog Randomized-Quicksort](#c5-forstå-quicksort-og-randomized-quicksort)
- [ ] ! [C6] [Kunne løse rekurrenser med substitusjon, rekursjonstrær og masterteoremet](#c6-kunne-løse-rekurrenser-med-substitusjon-rekursjonstrær-og-masterteoremet)
- [ ] ! [C7] [Kunne løse rekurrenser med iterasjonsmetoden](#c7-kunne-løse-rekurrenser-med-iterasjonsmetoden)
- [ ] [C8] [Forstå hvordan variabelskifte fungerer](#c8-forstå-hvordan-variabelskifte-fungerer)


### Forelesning 4: Rangering i lineær tid
- [x] ! [D1] [Forstå hvorfor sammenligningsbasert sortering har en worst-case på $\Omega(n \lg n)$](#d1-forstå-hvorfor-sammenligningsbasert-sortering-har-en-worst-case-på-omegan-lg-n)
- [x] [D2] [Vite hva en stabil sorteringsalgoritme er](#d2-vite-hva-en-stabil-sorteringsalgoritme-er)
- [x] [D3] [Forstå Counting-Sort, og hvorfor den er stabil](#d3-forstå-counting-sort-og-hvorfor-den-er-stabil)
- [x] ! [D4] [Forstå Radix-Sort, og hvorfor den trenger en stabil subrutine](#d4-forstå-radix-sort-og-hvorfor-den-trenger-en-stabil-subrutine)
- [x] [D5] [Forstå Bucket-Sort](#d5-forstå-bucket-sort)
- [x] [D6] [Forstå Randomized-Select](#d6-forstå-randomized-select)
- [x] [D7] [Kjenne til Select](#d7-kjenne-til-select)


### Forelesning 5: Rotfaste trestrukturer
- [x] ! [E1] [Forstå hvordan heaps fungerer, og hvordan de kan brukes som prioritetskøer](#e1-forstå-hvordan-heaps-fungerer-og-hvordan-de-kan-brukes-som-prioritetskøer)
- [x] [E2] [Forstå Heapsort](#e2-forstå-heapsort)
- [x] [E3] [Forstå hvordan rotfaste trær kan implementeres](#e3-forstå-hvordan-rotfaste-trær-kan-implementeres)
- [x] ! [E4] [Forstå hvordan binære søketrær fungerer](#e4-forstå-hvordan-binære-søketrær-fungerer)
- [x] [E5] [Vite at forventet høyde for et tilfeldig binært søketre er $\Theta(\lg n)$](#e5-vite-at-forventet-høyde-for-et-tilfeldig-binært-søketre-er-thetalg-n)
- [x] [E6] [Vite at det finnes søketrær med garantert høyde på $\Theta(\lg n)$](#e6-vite-at-det-finnes-søketrær-med-garantert-høyde-på-thetalg-n)


### Forelesning 6: Dynamisk programmering
- [x] ! [F1] [Forstå ideen om en delinstansgraf](#f1-forstå-ideen-om-en-delinstansgraf)
- [x] ! [F2] [Forstå designmetoden dynamisk programmering](#f2-forstå-designmetoden-dynamisk-programmering)
- [x] ! [F3] [Forstå løsning ved memoisering (top-down)](#f3-forstå-løsning-ved-memoisering-top-down)
- [x] [F4] [Forstå løsning ved iterasjon (bottom-up)](#f4-forstå-løsning-ved-iterasjon-bottom-up)
- [x] [F5] [Forstå hvordan man rekonstruerer en løsning fra lagrede beslutninger](#f5-forstå-hvordan-man-rekonstruerer-en-løsning-fra-lagrede-beslutninger)
- [x] [F6] [Forstå hva optimal delstruktur er](#f6-forstå-hva-optimal-delstruktur-er)
- [x] [F7] [Forstå hva overlappende delinstanser er](#f7-forstå-hva-overlappende-delinstanser-er)
- [x] [F8] [Forstå eksemplene stavkutting og LCS](#f8-forstå-eksemplene-stavkutting-og-lcs)
- [ ] [F9] [Forstå løsningen på det binære ryggsekkproblemet](#f9-forstå-løsningen-på-det-binære-ryggsekkproblemet)


### Forelesning 7: Grådige algoritmer
- [x] ! [G1] [Forstå designmetoden grådighet](#g1-forstå-designmetoden-grådighet)
- [x] ! [G2] [Forstå grådighetsegenskapen (the greedy-choice property)](#g2-forstå-grådighetsegenskapen-the-greedy-choice-property)
- [x] [G3] [Forstå eksemplene aktivitet-utvelgelse og det kontinuerlige ryggsekkproblemet](#g3-forstå-eksemplene-aktivitet-utvelgelse-og-det-kontinuerlige-ryggsekkproblemet)
- [x] [G4] [Forstå Huffman og Huffman-koder](#g4-forstå-huffman-og-huffman-koder)


### Forelesning 8: Traversering av grafer
- [x] [H1] [Forstå hvordan grafer kan implementeres](#h1-forstå-hvordan-grafer-kan-implementeres)
- [x] [H2] [Forstå BFS, også for å finne korteste vei uten vekter](#h2-forstå-bfs-også-for-å-finne-korteste-vei-uten-vekter)
- [ ] [H3] [Forstå DFS, parentesteoremet og hvit-sti-teoremet](#h3-forstå-dfs-parentesteoremet-og-hvit-sti-teoremet)
- [ ] [H4] [Forstå hvordan DFS klassifiserer kanter](#h4-forstå-hvordan-dfs-klassifiserer-kanter)
- [x] [H5] [Forstå Topological-Sort](#h5-forstå-topological-sort)
- [x] [H6] [Forstå hvordan DFS kan implementeres med en stakk](#h6-forstå-hvordan-dfs-kan-implementeres-med-en-stakk)
- [x] [H7] [Forstå hva traverseringstrær (som bredde-først- og dybde-først-trær) er](#h7-forstå-hva-traverseringstrær-som-bredde-først--og-dybde-først-trær-er)
- [x] ! [H8] [Forstå traversering med vilkårlig prioritetskø](#h8-forstå-traversering-med-vilkårlig-prioritetskø)


### Forelesning 9: Minimale spenntrær
- [x] [I1] [Forstå skog-implementasjonen av disjunkte mengder](#i1-forstå-skog-implementasjonen-av-disjunkte-mengder)
- [x] [I2] [Vite hva spenntrær og minimale spenntrær er](#i2-vite-hva-spenntrær-og-minimale-spenntrær-er)
- [x] ! [I3] [Forstå Generic-MST](#i3-forstå-generic-mst)
- [x] [I4] [Forstå hvorfor lette kanter er trygge kanter](#i4-forstå-hvorfor-lette-kanter-er-trygge-kanter)
- [x] [I5] [Forstå MST-Kruskal](#i5-forstå-mst-kruskal)
- [x] [I6] [Forstå MST-Prim](#i6-forstå-mst-prim)


### Forelesning 10: Korteste vei fra én til alle
- [ ] [J1] [Forstå ulike varianter av korteste-vei- eller korteste-sti-problemet](#j1-forstå-ulike-varianter-av-korteste-vei--eller-korteste-sti-problemet-single-source-single-destination-single-pair-all-pairs)
- [x] [J2] [Forstå strukturen til korteste-vei-problemet](#j2-forstå-strukturen-til-korteste-vei-problemet)
- [x] [J3] [Forstå at negative sykler gir mening for korteste enkle vei (simple path)](#j3-forstå-at-negative-sykler-gir-mening-for-korteste-enkle-vei-simple-path)
- [x] [J4] [Forstå at korteste enkle vei kan løses vha. lengste enkle vei og omvendt](#j4-forstå-at-korteste-enkle-vei-kan-løses-vha-lengste-enkle-vei-og-omvendt)
- [ ] [J5] [Forstå hvordan man kan representere et korteste-vei-tre](#j5-forstå-hvordan-man-kan-representere-et-korteste-vei-tre)
- [x] ! [J6] [Forstå kant-slakking (edge relaxation) og Relax](#j6-forstå-kant-slakking-edge-relaxation-og-relax)
- [ ] [J7] [Forstå ulike egenskaper ved korteste veier og slakking](#j7-forstå-ulike-egenskaper-ved-korteste-veier-og-slakking)
- [x] [J8] [Forstå Bellman-Ford](#j8-forstå-bellman-ford)
- [x] [J9] [Forstå Dag-Shortest-Paths](#j9-forstå-dag-shortest-paths)
- [ ] ! [J10] [Forstå kobling mellom Dag-Shortest-Paths og dynamisk programmering](#j10-forstå-kobling-mellom-dag-shortest-paths-og-dynamisk-programmering)
- [x] [J11] [Forstå Dijkstra](#j11-forstå-dijkstra)


### Forelesning 11: Korteste vei fra alle til alle
- [ ] [K1] [Forstå forgjengerstrukturen for alle-til-alle-varianten av korteste vei-problemet](#k1-forstå-forgjengerstrukturen-for-alle-til-alle-varianten-av-korteste-vei-problemet-print-all-pairs-shortest-path)
- [x] [K2] [Forstå Floyd-Warshall](#k2-forstå-floyd-warshall)
- [x] [K3] [Forstå Transitive-Closure](#k3-forstå-transitive-closure)
- [x] [K4] [Forstå Johnson](#k4-forstå-johnson)


### Forelesning 12: Maksimal flyt
- [ ] [L1] [Kunne definere flytnett, flyt og maks-flyt-problemet](#l1-kunne-definere-flytnett-flyt-og-maks-flyt-problemet)
- [ ] [L2] [Kunne håndtere antiparallelle kanter og flere kilder og sluk](#l2-kunne-håndtere-antiparallelle-kanter-og-flere-kilder-og-sluk)
- [ ] ! [L3] [Kunne definere restnettet til et flytnett med en gitt flyt](#l3-kunne-definere-restnettet-til-et-flytnett-med-en-gitt-flyt)
- [ ] [L4] [Forstå hvordan man kan oppheve (cancel) flyt](#l4-forstå-hvordan-man-kan-oppheve-cancel-flyt)
- [ ] [L5] [Forstå hva en forøkende sti (augmenting path) er](#l5-forstå-hva-en-forøkende-sti-augmenting-path-er)
- [ ] [L6] [Forstå hva snitt, snitt-kapasitet og minimalt snitt er](#l6-forstå-hva-snitt-snitt-kapasitet-og-minimalt-snitt-er)
- [ ] ! [L7] [Forstå maks-flyt/min-snitt-teoremet](#l7-forstå-maks-flytmin-snitt-teoremet)
- [x] [L8] [Forstå Ford-Fulkerson-Method og Ford-Fulkerson](#l8-forstå-ford-fulkerson-method-og-ford-fulkerson)
- [x] [L9] [Vite at Ford-Fulkerson med BFS kalles Edmonds-Karp-algoritmen](#l9-vite-at-ford-fulkerson-med-bfs-kalles-edmonds-karp-algoritmen)
- [ ] [L10] [Forstå hvordan maks-flyt kan finne en maksimum bipartitt matching](#l10-forstå-hvordan-maks-flyt-kan-finne-en-maksimum-bipartitt-matching)
- [ ] ! [L11] [Forstå heltallsteoremet (integrality theorem)](#l11-forstå-heltallsteoremet-integrality-theorem)


### Forelesning 13: NP-kompletthet
- [x] [M1] [Forstå sammenhengen mellom optimerings- og beslutnings-problemer](#m1-forstå-sammenhengen-mellom-optimerings--og-beslutnings-problemer)
- [ ] [M2] [Forstå koding (encoding) av en instans](#m2-forstå-koding-encoding-av-en-instans)
- [ ] [M3] [Forstå hvorfor løsningen på det binære ryggsekkproblemet ikke er polynomisk](#m3-forstå-hvorfor-løsningen-på-det-binære-ryggsekkproblemet-ikke-er-polynomisk)
- [ ] [M4] [Forstå forskjellen på konkrete og abstrakte problemer](#m4-forstå-forskjellen-på-konkrete-og-abstrakte-problemer)
- [ ] [M5] [Forstå representasjonen av beslutningsproblemer som formelle språk](#m5-forstå-representasjonen-av-beslutningsproblemer-som-formelle-språk)
- [x] [M6] [Forstå definisjonen av klassene P, NP og co-NP](#m6-forstå-definisjonen-av-klassene-p-np-og-co-np)
- [x] [M7] [Forstå redusibilitets-relasjonen $\leq_p$](#m7-forstå-redusibilitets-relasjonen-leq_p)
- [x] ! [M8] [Forstå definisjonen av NP-hardhet og NP-kompletthet](#m8-forstå-definisjonen-av-np-hardhet-og-np-kompletthet)
- [x] [M9] [Forstå den konvensjonelle hypotesen om forholdet mellom P, NP og NPC](#m9-forstå-den-konvensjonelle-hypotesen-om-forholdet-mellom-p-np-og-npc)
- [x] ! [M10] [Forstå hvordan NP-kompletthet kan bevises ved én reduksjon](#m10-forstå-hvordan-np-kompletthet-kan-bevises-ved-én-reduksjon)
- [ ] ! [M11] [Kjenne de NP-komplette problemene CIRCUIT-SAT, SAT, 3-CNF-SAT, CLIQUE, VERTEX-COVER, HAM-CYCLE, TSP og SUBSET-SUM](#m11-kjenne-de-np-komplette-problemene-circuit-sat-sat-3-cnf-sat-clique-vertex-cover-ham-cycle-tsp-og-subset-sum)
- [ ] [M12] [Forstå at det binære ryggsekkproblemet er NP-hardt](#m12-forstå-at-det-binære-ryggsekkproblemet-er-np-hardt)
- [x] [M13] [Forstå at lengste enkle-vei-problemet er NP-hardt](#m13-forstå-at-lengste-enkle-vei-problemet-er-np-hardt)
- [x] [M14] [Være i stand til å konstruere enkle NP-kompletthetsbevis](#m14-være-i-stand-til-å-konstruere-enkle-np-kompletthetsbevis)



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

#### [A4] Kunne definere asymptotisk notasjon, $O$, $\Omega$, $\Theta$, $o$ og $\omega$
Notasjon | Forklaring | Tegn
---|---|---
$\omega$ | streng nedre grense | $>$
$\Omega$ | nedre grense | $\geq$
$\Theta$ | øvre og nedre grense | $=$
$O$ | øvre grense | $\leq$
$o$ | streng øvre grense | $<$

#### [A5] Kunne definere best-case, average-case og worst-case
**Best-case** er den minimale kjøretiden, gitt et optimalt input. **Average-case** er den gjennomsnittlige kjøretiden, over alle mulige inputs. **Worst-case** er den maksimale kjøretiden, gitt verst tenkelig input.

#### [A6] Forstå løkkeinvarianter og induksjon
**Løkkeinvariant**: et krav tilfredsstilles etter hver iterasjon, brukes til bevis.
**Induksjon**: Grunntilfelle + induktivt steg kan gi et bevis for alle n > grunntilfellet.

#### [A7] Forstå rekursiv dekomponering og induksjon over delinstanser
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

#### [B4] Forstå hvordan direkte adressering og hashtabeller fungerer

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
Best case | $\Theta(1)$
Average/worst case | Spørs på hashfunksjonen

Attributt | Hash-Search
---|---
Beskrivelse | Henter et element fra en hashtabell
Input | T: hashtabell, k: nøkkel
Output | Elementet i tabellen med den gitt nøkkelen, eller None
Best case | $\Theta(1)$
Average/worst case | Spørs på hashfunksjonen

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
Best case | $\Theta(1)$
Average/worst case | Spørs på hashfunksjonen

Attributt | Chained-Hash-Search
---|---
Beskrivelse | Henter et element fra en kjedet hashtabell
Input | T: kjedet hashtabell, k: nøkkel
Output | Elementet i tabellen med den gitt nøkkelen, eller None
Best case | $\Theta(1)$
Average/worst case | Spørs på hashfunksjonen

Attributt | Chained-Hash-Delete
---|---
Beskrivelse | Sletter et element i en kjedet hashtabell
Input | T: kjedet hashtabell, x: element
Best case | $\Theta(1)$
Average/worst case | Spørs på hashfunksjonen

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
En god hashfunksjon vil tilnærmet tilfredsstille antagelsen om simpel uniform hashing, altså at hver key er like sannsynlig	å hashe til enhver av de $m$ lukene, uavhengig av hvor andre keys har hashet.
- Divisjonsmetoden, $h(k) = k \mod m$
- Multiplikasjonsmetoden $h(k) = floor(m(ka \mod 1))$

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

#### [C1] Forstå designmetoden divide-and-conquer (splitt og hersk)
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
Input | `A`: sortert liste, `p`: minste indeks, `r`: største indeks, `v`: verdi som søkes etter
Output | Indeksen til verdien det søkes etter
Worst case | $\Theta(\lg n)$
Average case | $\Theta(\lg n)$
Best case | $\Theta(1)$, hvis `v` er i midten

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

#### [C6] Kunne løse rekurrenser med substitusjon, rekursjonstrær og masterteoremet

#### [C7] Kunne løse rekurrenser med iterasjonsmetoden

#### [C8] Forstå hvordan variabelskifte fungerer



### Forelesning 4: Rangering i lineær tid

#### [D1] Forstå hvorfor sammenligningsbasert sortering har en worst-case på $\Omega(n \lg n)$
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

#### [D4] Forstå Radix-Sort, og hvorfor den trenger en stabil subrutine
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
Select løser det samme problemet som Randomized-Select, men prøver å velge en god pivot istedenfor å ta en tilfeldig.
Merk: Det kreves ikke grundig forståelse av virkemåten til Select.

### Forelesning 5: Rotfaste trestrukturer

#### [E1] Forstå hvordan heaps fungerer, og hvordan de kan brukes som prioritetskøer
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

#### [E4] Forstå hvordan binære søketrær fungerer
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

#### [F1] Forstå ideen om en delinstansgraf
En delinstansgraf viser hvordan en probleminstans kan bygges opp av delinstanser.

#### [F2] Forstå designmetoden dynamisk programmering
When developing a dynamic-programming algorithm, we follow a sequence of four steps:
1. Characterize the structure of an optimal solution.
2. Recursively define the value of an optimal solution.
3. Compute the value of an optimal solution, typically in a bottom-up fashion.
4. Construct an optimal solution from computed information.

Dynamisk programmering brukes for problemer som har overlappende delproblemer og optimal delstruktur.

#### [F3] Forstå løsning ved memoisering (top-down)
Ved memoisering løser vi problemet på vanlig rekursiv måte, men lagrer resultatet av hvert delproblem, slik at det kan brukes senere uten ytterligere kjøretid.

#### [F4] Forstå løsning ved iterasjon (bottom-up)
Vi sorterer delproblemene etter størrelse. Vi begynner med det minste og bygger oss opp til en løsning av det større problemet.

#### [F5] Forstå hvordan man rekonstruerer en løsning fra lagrede beslutninger
Sjekke om det er blitt gjort tidligere og hente resultatet istedenfor å kalkulere det på nytt.

#### [F6] Forstå hva optimal delstruktur er
Optimal delstruktur vil si at en løsning av en delinstans inngår i den globale løsningen.

#### [F7] Forstå hva overlappende delinstanser er
Hvis to delinstanser i en delinstans begge avhenger av en tredje delinstans, er den tredje delinstansen en overlappende delinstans.

#### [F8] Forstå eksemplene stavkutting og LCS

##### Stavkutting
Attributt | Cut-Rod
---|---
Beskrivelse | Finner beste pris, gitt en stavlengde og priser på ulike lengder
Input | p: tabell av priser, n: stavlengde
Output | Beste pris
Kjøretid | $O(2^n)$
Minnebruk | $\Theta(1)$

Attributt | Memoized-Cut-Rod
---|---
Beskrivelse | Memoisert (top-down) versjon av Cut-Rod
Input | p: tabell av priser, n: stavlengde
Output | Beste pris
Kjøretid | $O(n^2)$
Minnebruk | $\Theta(n)$

Attributt | Bottom-Up-Cut-Rod
---|---
Beskrivelse | Iterativ (bottom-up) versjon av Cut-Rod
Input | p: tabell av priser, n: stavlengde
Output | Beste pris
Kjøretid | $O(n^2)$
Minnebruk | $\Theta(n)$

````python
def cut_rod(p, n):
    if n == 0:
        return 0
    q = -float('inf')
    for i in range(1, n + 1):
        q = max(q, p[i - 1] + cut_rod(p, n - i))
    return q

def memoized_cut_rod(p, n):
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
    r = [0] * (n + 1)
    for j in range(1, n + 1):
        q = -float('inf')
        for i in range(1, j + 1):
            q = max(q, p[i] + r[j - i])
        r[j] = q
    return r[n]

def extended_bottom_up_cut_rod(p, n):
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
    _, s = extended_bottom_up_cut_rod(p, n)
    while n > 0:
        print(s[n])
        n -= s[n]
````
[Implementasjon av stavkutting](lib/cut_rod.py)

##### Longest common subsequence (LCS)
Attributt | LCS-Length
---|---
Beskrivelse | Sammenligner liste X og Y og finner lengste felles subsekvens
Input | X: liste, Y: liste
Output | To matriser som lengste felles subsekvens kan leses fra (brukes i Print-LCS)
Kjøretid | $\Theta(mn)$
Minnebruk | $\Theta(mn)$

Attributt | Print-LCS
---|---
Beskrivelse | Printer lengste felles subsekvens, gitt b-matrisen fra LCS-Length
Input | b: matrise fra LCS-Length, X: den tilhørende listen som ble brukt i LCS-Length, i: hvilken rad det skal leses fra, j: hvilken kolonne det skal leses fra
Output | Lengste felles subsekvens
Kjøretid | $\Theta(m + n)$
Minnebruk | $\Theta(1)$

````python
def lcs_length(X, Y):
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

#### [G1] Forstå designmetoden grådighet
A greedy algorithm always makes the choice that looks best at the moment. That is, it makes a locally optimal choice in the hope that this choice will lead to a globally optimal solution.

1. Cast the optimization problem as one in which we make a choice and are left
with one subproblem to solve.
2. Prove that there is always an optimal solution to the original problem that makes
the greedy choice, so that the greedy choice is always safe.
3. Demonstrate optimal substructure by showing that, having made the greedy
choice, what remains is a subproblem with the property that if we combine an
optimal solution to the subproblem with the greedy choice we have made, we
arrive at an optimal solution to the original problem.

#### [G2] Forstå grådighetsegenskapen (the greedy-choice property)
**Greedy-choice property**: we can assemble a globally
optimal solution by making locally optimal (greedy) choices. 

#### [G3] Forstå eksemplene aktivitet-utvelgelse og det kontinuerlige ryggsekkproblemet

##### Aktivitet-utvelgelse
Attributt | Recursive-Activity-Selector
---|---
Beskrivelse | Maksimerer antall aktiviterer
Input | `s`: starttider, `f`: sluttider, `k`: tid, `n`: antall aktiviteter å velge mellom
Output | Et sett av de valgte aktivitene
Kjøretid | $\Theta(n)$
Ekstra krav | En fake aktivitet $a_0$ med $f_0 = 0$ må legges til s og f. Input må være sortert etter sluttider.

Attributt | Greedy-Activity-Selector
---|---
Beskrivelse | Maksimerer antall aktiviterer
Input | `s`: starttider, `f`: sluttider
Output | Et sett av de valgte aktivitene
Kjøretid | $\Theta(n)$
Ekstra krav | En fake aktivitet $a_0$ med $f_0 = 0$ må legges til s og f. Input må være sortert etter sluttider.

````python
def recursive_activity_selector(s, f, k, n):
    m = k + 1
    while m <= n and s[m] < f[k]:
        m += 1
    if m <= n:
        return {m}.union(recursive_activity_selector(s, f, m, n)) # a[m]
    else:
        return set()

def greedy_activity_selector(s, f):
    n = len(s)
    A = set(s[0])
    k = 0
    for m in range(1, n):
        if s[m] >= f[k]:
            A.add(m) # a[m]
            k = m
    return A
````

##### Det kontinuerlige ryggsekkproblemet
I motsetning til det binære ryggsekkproblemet, er det kontinuerlige ryggsekkproblemet enkelt å løse med en grådig algoritme. Vi kan alltid fylle ryggsekken med det mest verdifulle, helt til ryggsekken er full.

#### [G4] Forstå Huffman og Huffman-koder
Attributt | Huffman
---|---
Beskrivelse | Bygger et Huffman-tre (vha. min-haug)
Input | `C`: et sett av $n$ karakterer, hver med en bestemt frekvens $c.freq$.
Output | Roten til Huffman-treet
Kjøretid | $O(n \lg n)$

````python
def huffman(C):
    n = len(C)
    Q = build_min_heap(C)
    for _ in range(n - 1):
        z = Node()
        x = heap_extract_min(Q)
        y = heap_extract_min(Q)
        z.left = x
        z.right = y
        z.freq = x.freq + y.freq
        min_heap_insert(Q, z)
    return heap_extract_min(Q)
````
[Implementasjon av Huffman](lib/huffman.py)



### Forelesning 8: Traversering av grafer

#### [H1] Forstå hvordan grafer kan implementeres
To vanlige implementasjoner av grafer er 1. å bruke nabolister, eller 2. en nabomatrise. Nabolister er effektive for grafer med få kanter, mens nabomatriser er effektive for grafer med mange kanter.

#### [H2] Forstå BFS, også for å finne korteste vei uten vekter
Attributt | BFS
---|---
Beskrivelse | Bredde først søk, kan finne korteste vei uten vekter
Input | `G`: en graf, `s` startnode
Output | Markerer alle noder med avstand $d$ fra startnoden, og forgjenger $pi$
Kjøretid | $O(V + E)$

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
Attributt | DFS
---|---
Beskrivelse | Dybde først søk, kan brukes til å klassifisere kanter
Input | `G`: en graf
Output | Markerer alle noder med tid $time$, og forgjenger $pi$
Kjøretid | $\Theta(V + E)$

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
TODO: parentesteoremet og hvit-sti-teoremet

#### [H4] Forstå hvordan DFS klassifiserer kanter

#### [H5] Forstå Topological-Sort
Attributt | Topological-Sort
---|---
Beskrivelse | Sorterer en graf topologisk, vha. DFS
Input | `G`: en graf
Output | En topologisk sortert lenket liste over nodene
Kjøretid | $\Theta(V + E)$

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
Hvis du bytter ut køen i implementasjonen av BFS med en stakk, vil det bli DFS.

#### [H7] Forstå hva traverseringstrær (som bredde-først- og dybde-først-trær) er
Trær som er resultater av henholdsvis BFS og DFS.

#### [H8] Forstå traversering med vilkårlig prioritetskø
Se implementasjon av BFS, denne har FIFO-kø men virker annerledes ved bruk av annen kø.



### Forelesning 9: Minimale spenntrær
The inverse Ackermann function $\alpha(n)$ grows extraordinarily slowly, so this factor is 4 or less for any $n$ that can actually be written in the physical universe. This makes disjoint-set operations practically amortized constant time.

#### [I1] Forstå skog-implementasjonen av disjunkte mengder
Attributt | Connected-Components
---|---
Beskrivelse | Forbereder bruk av Same-Component
Input | `G`: en graf
Kjøretid | $\Theta(E\alpha(n))$

Attributt | Same-Component
---|---
Beskrivelse | Avgjør om to noder er i den samme komponenten
Input | 
Output | True hvis nodene er i samme komponent, False ellers
Kjøretid | $\Theta(\alpha(n))$

Attributt | Make-Set
---|---
Beskrivelse | Lager et nytt sett bestående av den gitte noden
Input | `x`: en node
Kjøretid | $\Theta(1)$

Attributt | Link
---|---
Beskrivelse | Kobler sammen to noder, basert på rank
Input | `x`: en node, `y`: en node
Kjøretid | $\Theta(1)$

Attributt | Link
---|---
Beskrivelse | Linker settet til `x` med settet til `y`
Input | `x`: en node, `y`: en node
Kjøretid | $\Theta(\alpha(n))$

Attributt | Find-Set
---|---
Beskrivelse | Returner den øverste forfederen til noden, og setter den som direkte forelder
Input | `x`: en node
Output | Den øverste forfederen til noden (representerer settet)
Kjøretid | $\Theta(\alpha(n))$

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
Et **tre** er en urettet graf der alle noder er koblet med nøyaktig én sti. Dette er ekvivalent med å si at den er asyklisk. Et **spenntre** av en urettet graf $G$ er en delgraf som er et tre og inneholder alle nodene i $G$. Et **minimalt spenntre** er et spenntre hvor summen av kantvektene er minst mulig.

#### [I3] Forstå Generic-MST
````
GENERIC-MST(G, w):
    A = Ø
    while A does not form a spanning tree
        find an edge (u, v) that is safe for A
        A = A U {(u, v)}
    return A
````

#### [I4] Forstå hvorfor lette kanter er trygge kanter
Invariant: Kantmengden utgjør en del av et minimalt spenntre.
En *trygg kant* er en kant som bevarer invarianten.

Den letteste kanten (som ikke danner en sykel) er trygg fordi vi må uansett på et tidspunkt koble sammen snittet og det finnes ingen billigere måte å gjøre det lettere på. Kan illustreres med vei over bro https://algdat.idi.ntnu.no/lysark/forelesn09_kort.pdf

#### [I5] Forstå MST-Kruskal
Attributt | MST-Kruskal
---|---
Beskrivelse | Bygger et minimalt spenntre ved å sortere kantene
Input | `G`: en graf, `w`: kantvektene
Output | Kantene som danner et minimalt spenntre
Kjøretid | $O(E \lg V)$

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
    return A
````
[Implementasjon av MST-Kruskal](lib/minimal_spanning_tree.py)

#### [I6] Forstå MST-Prim
Attributt | MST-Prim
---|---
Beskrivelse | Bygger ett tre gradvis; en lett kant over snittet rundt treet er alltid trygg
Input | `G`: en graf, `w`: kantvektene, `r`: rotnode
Output | Nodene sine forgjengerverdier $pi$ danner et minimalt spenntre
Kjøretid | $O(E \lg V)$, eller $O(E + V \lg V)$ ved bruk av Fibonacci-haug

````python
def mst_prim(G, w, r):
    for u in G.V:
        u.key = float('inf')
        u.pi = None
    r.key = 0
    Q = build_min_heap(G.V)
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
Single Source Shortest Paths (SSSP): en til alle. ?

#### [J2] Forstå strukturen til korteste-vei-problemet
Man skal finne korteste vei.

#### [J3] Forstå at negative sykler gir mening for korteste enkle vei (simple path)
For korteste enkle vei må man unngå syklene (for at den skal være enkel) så det tillatter at de kan eksistere i grafen.

#### [J4] Forstå at korteste enkle vei kan løses vha. lengste enkle vei og omvendt
Kan gå fra den ene til den andre ved å negere kantvektene.

#### [J5] Forstå hvordan man kan representere et korteste-vei-tre


#### [J6] Forstå kant-slakking (edge relaxation) og Relax
Attributt | Relax
---|---
Beskrivelse | $v$ lar $u$ være sin forelder, om det er gunstig
Input | `u`: en node, `v`: en node, `w`: kantvektene
Kjøretid | $\Theta(1)$

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
TODO

#### [J8] Forstå Bellman-Ford
Attributt | Bellman-Ford
---|---
Beskrivelse | Finner korteste vei fra én til alle
Input | `G`: en graf, `w`: kantvektene, `s`: startnode
Output | Nodene sine $d$- og $pi$-verdier antyder lengden fra start og forelder. Algoritmen returnerer False dersom det finnes en negativ sykel og True ellers 
Kjøretid | $O(VE)$

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

#### [J9] Forstå Dag-Shortest-Paths
Attributt | DAG-Shortest-Paths
---|---
Beskrivelse | Finner korteste vei fra én til alle i en rettet asyklisk graf
Input | `G`: en graf, `w`: kantvektene, `s`: startnode
Output | Nodene sine $d$- og $pi$-verdier antyder lengden fra start og forelder 
Kjøretid | $O(V + E)$
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

#### [J10] Forstå kobling mellom Dag-Shortest-Paths og dynamisk programmering

#### [J11] Forstå Dijkstra
Attributt | Dijkstra
---|---
Beskrivelse | Finner korteste vei fra én til alle i en graf med ikke-negative kantvekter
Input | `G`: en graf, `w`: kantvektene, `s`: startnode
Output | Nodene sine $d$- og $pi$-verdier antyder lengden fra start og forelder 
Kjøretid | $O(E \lg V)$, eller $O(V \lg V + E)$ ved bruk av Fibonacci-haug
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
Attributt | Print-All-Pairs-Shortest-Path
---|---
Beskrivelse | Printer korteste vei fra `i` til `j`
Input | `Pi` forgjengermatrise, `i`: nodeindeks, `j`; nodeindeks
Kjøretid | $O(V)$
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
Attributt | Floyd-Warshall
---|---
Beskrivelse | Finner korteste vei fra alle til alle
Input | `W`: nabomatrise
Output | Avstandsmatrise
Kjøretid | $\Theta(V^3)$
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
Attributt | Transitive-Closure
---|---
Beskrivelse | Finner transitiv lukning. Dvs. oversikt over hvilke noder som har stier til andre noder
Input | `W`: nabomatrise
Output | Matrise som beskriver den transitive lukningen ("binær avstandsmatrise")
Kjøretid | $\Theta(n^3)$
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
Se boka s. 700.
Attributt | Johnson
---|---
Beskrivelse | Finner korteste vei fra alle til alle ved hjelp av *reweighting*, *Bellman-Ford* og *Dijkstra*.
Input | `G`: en graf, `w`: kantvektene
Output | Avstandsmatrise
Kjøretid | $O(VE \lg V)$, eller $O(V^2 \lg V + VE)$ ved bruk av fibonacci-haug
````
JOHNSON(G, w)
    compute G'
    if Bellman-Ford(G', w, s) == False
        print "the input graph contains a negative-weight cycle"
    else
        for each vertex v in G'.V
            set h(v) to the value of d(s, v) computed by Bellman-Ford
        for each edge (u, v) in G'.E
            w*(u, v) = w(u, v) + h(u) - h(v)
        let D = (d_uv) be a new n*n matrix
        for each vertex u in G.V
            run Dijkstra(G, w*, u) to compute d*(u, v) for all v in G.V
            for each vertex v in G.V
                d_uv = d*(u, v) + h(v) - h(u)
        return D
````

### Forelesning 12: Maksimal flyt

#### [L1] Kunne definere flytnett, flyt og maks-flyt-problemet

#### [L2] Kunne håndtere antiparallelle kanter og flere kilder og sluk

#### [L3] Kunne definere restnettet til et flytnett med en gitt flyt

#### [L4] Forstå hvordan man kan oppheve (cancel) flyt

#### [L5] Forstå hva en forøkende sti (augmenting path) er

#### [L6] Forstå hva snitt, snitt-kapasitet og minimalt snitt er

#### [L7] Forstå maks-flyt/min-snitt-teoremet

#### [L8] Forstå Ford-Fulkerson-Method og Ford-Fulkerson
Attributt | Ford-Fulkerson
---|---
Beskrivelse | Implementasjon av Ford-Fulkerson-Method, finner maks flyt
Input | `G`: en graf, `s`: kilde, `t`: sluk
Output | Kantene sine $f$-verdier indikerer maks-flyten
Kjøretid | $O(E \| f^*\|)$
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
Attributt | Edmonds-Karp
---|---
Beskrivelse | Ford-Fulkerson med BFS, finner maks flyt
Input | `G`: en graf, `s`: kilde, `t`: sluk
Output | kantene sine $f$-verdier indikerer maks-flyten
Kjøretid | $O(VE^2)$

#### [L10] Forstå hvordan maks-flyt kan finne en maksimum bipartitt matching

#### [L11] Forstå heltallsteoremet (integrality theorem)



### Forelesning 13: NP-kompletthet

#### [M1] Forstå sammenhengen mellom optimerings- og beslutnings-problemer
Optimeringsproblemer har gjerne tilhørende beslutningsproblemer og omvendt. For eksempel kan optimeringsproblemet *å finne korteste vei* knyttes til beslutningsproblemet *finnes det en vei med avstand $\leq k$?*.

#### [M2] Forstå koding (encoding) av en instans

#### [M3] Forstå hvorfor løsningen på det binære ryggsekkproblemet ikke er polynomisk

#### [M4] Forstå forskjellen på konkrete og abstrakte problemer
Men hovedpoenget er altså at konkrete problemer er, på sett og vis, konkrete representasjoner av de abstrakte problemene, der instansene er kodet som strenger (f.eks. serier med bits), akkurat som i en datamaskin, mens abstrakte problemer bare er abstrakte, matematiske problemer (relasjoner mellom input/output). Se mer på side 1054-1055.

#### [M5] Forstå representasjonen av beslutningsproblemer som formelle språk

#### [M6] Forstå definisjonen av klassene P, NP og co-NP
NP er beslutningsproblemer der ja-svar kan verifiseres i polynomisk tid. co-NP er beslutninger der nei-svar kan verifiseres i polynomisk tid. P er problemene i NP som kan løses i polynomisk tid. 

#### [M7] Forstå redusibilitets-relasjonen $\leq_p$
Dersom vi reduserer $A$ til $B$ skriver vi $A \leq_p B$. Det vil si at $B$ er minst like vanskelig som $A$.

#### [M8] Forstå definisjonen av NP-hardhet og NP-kompletthet
At et problem er NP-hardt vil si at det er minst like vanskelig som de vanskeligste problemene i NP. Hvis et problem er i NP og er NP-hardt, så er det NP-komplett.

#### [M9] Forstå den konvensjonelle hypotesen om forholdet mellom P, NP og NPC
Den konvensjonelle hypotesen går ut på at
- P $\subset$ NP
- P $\neq$ NP
- P $\cap$ NPC $= \emptyset$

#### [M10] Forstå hvordan NP-kompletthet kan bevises ved én reduksjon
Dersom vi reduserer et problem som er bevist NP-komplett $A$, til et problem $B$ i NP, $A \leq_p B$, vet vi at $B$ er minst like vanskelig som $A$ og derfor også NP-komplett. 

#### [M11] Kjenne de NP-komplette problemene CIRCUIT-SAT, SAT, 3-CNF-SAT, CLIQUE, VERTEX-COVER, HAM-CYCLE, TSP og SUBSET-SUM

#### [M12] Forstå at det binære ryggsekkproblemet er NP-hardt

#### [M13] Forstå at lengste enkle-vei-problemet er NP-hardt
Hamiltonvei-problemet kan reduseres til lengste enkle-vei-problemet, derfor er lengste enkle-vei-problemet NP-hardt.

#### [M14] Være i stand til å konstruere enkle NP-kompletthetsbevis
Ved reduksjon fra NP-komplette problemer.