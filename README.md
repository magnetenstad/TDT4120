
# Pensumhefte, 2021, realisert.

## Overordnede læringsmål
De overordnede læringsmålene for emnet er som følger.

**Dere skal ha kunnskap om:**
- [ ] [X1] Et bredt spekter av etablerte algoritmer og datastrukturer
- [ ] [X2] Klassiske algoritmiske problemer med kjente effektive løsninger
- [ ] [X3] Komplekse problemer uten kjente effektive løsninger

**Dere skal kunne:**
- [ ] [X4] Analysere algoritmers korrekthet og effektivitet
- [ ] [X5] Formulere problemer så de kan løses av algoritmer
- [ ] ! [X6] Konstruere nye effektive algoritmer

**Dere skal være i stand til:**
- [ ] [X7] Å bruke eksisterende algoritmer og programvare på nye problemer
- [ ] [X8] Å utvikle nye løsninger på praktiske algoritmiske problemstillinger

## Gjennom semesteret

**Læringsmål for hver algoritme:**
- [ ] [Z1] Kjenne den formelle definisjonen av det generelle problemet den løser
- [ ] [Z2] Kjenne til eventuelle tilleggskrav den stiller for å være korrekt
- [ ] [Z3] Vite hvordan den oppfører seg; kunne utføre algoritmen, trinn for trinn
- [ ] ! [Z4] Forstå korrekthetsbeviset; hvordan og hvorfor virker algoritmen egentlig?
- [ ] [Z5] Kjenne til eventuelle styrker eller svakheter, sammenlignet med andre
- [ ] [Z6] Kjenne kjøretidene under ulike omstendigheter, og forstå utregningen

**Læringsmål for hver datastruktur:**
- [ ] [Z7] Forstå algoritmene (jf. mål Z01–Z06) for de ulike operasjonene på strukturen
- [ ] [Z8] Forstå hvordan strukturen representeres i minnet

**Læringsmål for hvert problem:**
- [ ] [Z9] Kunne angi presist hva input er
- [ ] [Z10] Kunne angi presist hva output er og hvilke egenskaper det må ha

## Forelesning 1: Problemer og algoritmer
- [ ] [A1] Forstå bokas pseudokode-konvensjoner
- [ ] [A2] Kjenne egenskapene til random-access machine-modellen (RAM)
- [ ] [A3] Kunne definere problem, instans og problemstørrelse
- [ ] ! [A4] Kunne definere asymptotisk notasjon, O, Ω, Θ, o og ω.
- [ ] ! [A5] Kunne definere best-case, average-case og worst-case
- [ ] ! [A6] Forstå løkkeinvarianter og induksjon
- [ ] ! [A7] Forstå rekursiv dekomponering og induksjon over delinstanser
- [x] [A8] Forstå [Insertion-Sort](/lib/insertion_sort.py)

## Forelesning 2: Datastrukturer
- [x] [B1] Forstå hvordan [stakker](lib/structures/stack.py) og [køer](lib/structures/queue.py) fungerer (Stack-Empty, Push, Pop, Enqueue, Dequeue)
- [x] [B2] Forstå hvordan [lenkede lister](lib/structures/linked_list.py) fungerer (List-Search, List-Insert, List-Delete, List-Delete', List-Search', List-Insert')
- [ ] [B3] Forstå hvordan pekere og objekter kan implementeres
- [ ] ! [B4] Forstå hvordan direkte adressering og hashtabeller fungerer
- [x] [B5] Forstå konfliktløsing ved [kjeding](lib/structures/hash_table_chained.py) (chaining) (Chained-Hash-Insert, Chained-Hash-Search, Chained-Hash-Delete)
- [ ] [B6] Kjenne til grunnleggende hashfunksjoner
- [ ] [B7] Vite at man for statiske datasett kan ha worst-case O(1) for søk
- [ ] [B8] Kunne definere amortisert analyse
- [x] [B9] Forstå hvordan [dynamiske tabeller](lib/structures/table.py) fungerer (Table-Insert)

## Forelesning 3: Splitt og hersk
- [ ] ! [C1] Forstå designmetoden divide-and-conquer (splitt og hersk)
- [x] [C2] Forstå [maximum-subarray-problemet](lib/find_maximum_subarray.py) med løsninger
- [x] [C3] Forstå [Bisect og Bisect'](lib/bisect.py)
- [x] [C4] Forstå [Merge-Sort](lib/merge_sort.py)
- [x] [C5] Forstå [Quicksort](lib/quicksort.py) og [Randomized-Quicksort](lib/randomized_select.py)
- [ ] ! [C6] Kunne løse rekurrenser med substitusjon, rekursjonstrær og masterteoremet
- [ ] ! [C7] Kunne løse rekurrenser med iterasjonsmetoden
- [ ] [C8] Forstå hvordan variabelskifte fungerer

## Forelesning 4: Rangering i lineær tid
- [ ] ! [D1] Forstå hvorfor sammenligningsbasert sortering har en worst-case på Ω(n lg n)
- [ ] [D2] Vite hva en stabil sorteringsalgoritme er
- [x] [D3] Forstå [Counting-Sort](lib/counting_sort.py), og hvorfor den er stabil
- [x] ! [D4] Forstå [Radix-Sort](lib/radix_sort.py), og hvorfor den trenger en stabil subrutine
- [x] [D5] Forstå [Bucket-Sort](lib/bucket_sort.py)
- [x] [D6] Forstå [Randomized-Select](lib/randomized_select.py)
- [ ] [D7] Kjenne til Select
Merk: Det kreves ikke grundig forståelse av virkemåten til Select.

## Forelesning 5: Rotfaste trestrukturer
- [x] ! [E1] Forstå hvordan [heaps](lib/structures/binary_heap.py) fungerer, og hvordan de kan brukes som
prioritetskøer (Parent, Left, Right, Max-Heapify, Build-Max-Heap, Heapsort,
Max-Heap-Insert, Heap-Extract-Max, Heap-Increase-Key, Heap-Maximum. Også
tilsvarende for min-heaps, f.eks., Build-Min-Heap og Heap-Extract-Min.)
- [x] [E2] Forstå [Heapsort](lib/heapsort.py)
- [ ] [E3] Forstå hvordan rotfaste trær kan implementeres
- [x] ! [E4] Forstå hvordan [binære søketrær](lib/structures/binary_tree.py) fungerer (Inorder-Tree-Walk, Tree-Search, Iterative-Tree-Search, Tree-Minimum, Tree-Maximum, Tree-Successor, Tree-Predecessor, Tree-Insert, Transplant, Tree-Delete)
- [ ] [E5] Vite at forventet høyde for et tilfeldig binært søketre er Θ(lg n)
- [ ] [E6] Vite at det finnes søketrær med garantert høyde på Θ(lg n)
Merk: Det kreves ikke grundig forståelse av Transplant og Tree-Delete.

## Forelesning 6: Dynamisk programmering
- [ ] ! [F1] Forstå ideen om en delinstansgraf
- [ ] ! [F2] Forstå designmetoden dynamisk programmering
- [ ] ! [F3] Forstå løsning ved memoisering (top-down)
- [ ] [F4] Forstå løsning ved iterasjon (bottom-up)
- [ ] [F5] Forstå hvordan man rekonstruerer en løsning fra lagrede beslutninger
- [ ] [F6] Forstå hva optimal delstruktur er
- [ ] [F7] Forstå hva overlappende delinstanser er
- [x] [F8] Forstå eksemplene [stavkutting](lib/cut_rod.py) og [LCS](lib/longest_common_subsequence.py)
- [x] [F9] Forstå løsningen på [det binære ryggsekkproblemet](lib/knapsack.py) (Knapsack, Knapsack')

## Forelesning 7: Grådige algoritmer
- [ ] ! [G1] Forstå designmetoden grådighet
- [ ] ! [G2] Forstå grådighetsegenskapen (the greedy-choice property)
- [ ] [G3] Forstå eksemplene aktivitet-utvelgelse og det kontinuerlige
  ryggsekkproblemet
- [x] [G4] Forstå [Huffman](lib/huffman.py) og Huffman-koder

## Forelesning 8: Traversering av grafer
- [ ] [H1] Forstå hvordan grafer kan implementeres
- [x] [H2] Forstå [BFS](lib/bfs.py), også for å finne korteste vei uten vekter
- [x] [H3] Forstå [DFS](lib/dfs.py), parentesteoremet og hvit-sti-teoremet
- [ ] [H4] Forstå hvordan DFS klassifiserer kanter
- [x] [H5] Forstå [Topological-Sort](lib/topological_sort.py)
- [ ] [H6] Forstå hvordan DFS kan implementeres med en stakk
- [ ] [H7] Forstå hva traverseringstrær (som bredde-først- og dybde-først-trær) er
- [ ] ! [H8] Forstå traversering med vilkårlig prioritetskø

## Forelesning 9: Minimale spenntrær
- [x] [I1] Forstå skog-implementasjonen av [disjunkte mengder](lib/structures/disjunct_set.py) (Connected-Components, Same-Component, Make-Set, Union, Link, Find-Set)
- [ ] [I2] Vite hva spenntrær og minimale spenntrær er
- [x] ! [I3] Forstå [Generic-MST](lib/minimal_spanning_tree.py)
- [ ] [I4] Forstå hvorfor lette kanter er trygge kanter
- [x] [I5] Forstå [MST-Kruskal](lib/minimal_spanning_tree.py)
- [x] [I6] Forstå [MST-Prim](lib/minimal_spanning_tree.py)

## Forelesning 10: Korteste vei fra én til alle
- [ ] [J1] Forstå ulike varianter av korteste-vei- eller korteste-sti-problemet (Single-source, single-destination, single-pair, all-pairs)
- [ ] [J2] Forstå strukturen til korteste-vei-problemet
- [ ] [J3] Forstå at negative sykler gir mening for korteste enkle vei (simple path)
- [ ] [J4] Forstå at korteste enkle vei kan løses vha. lengste enkle vei og omvendt
- [ ] [J5] Forstå hvordan man kan representere et korteste-vei-tre
- [x] ! [J6] Forstå kant-slakking (edge relaxation) og [Relax](lib/single_source_shortest_path.py)
- [ ] [J7] Forstå ulike egenskaper ved korteste veier og slakking (Triangle
  inequality, upper-bound property, no-path property, convergence property,
  path-relaxation property, predecessor-subgraph property)
- [x] [J8] Forstå [Bellman-Ford](lib/single_source_shortest_path.py)
- [x] [J9] Forstå [Dag-Shortest-Paths](lib/single_source_shortest_path.py)
- [ ] ! [J10] Forstå kobling mellom Dag-Shortest-Paths og dynamisk programmering
- [x] [J11] Forstå [Dijkstra](lib/single_source_shortest_path.py)

## Forelesning 11: Korteste vei fra alle til alle
- [ ] [K1] Forstå forgjengerstrukturen for alle-til-alle-varianten av korteste vei-problemet ([Print-All-Pairs-Shortest-Path](lib/all_pairs_shortest_paths.py))
- [x] [K2] Forstå [Floyd-Warshall](lib/all_pairs_shortest_paths.py)
- [x] [K3] Forstå [Transitive-Closure](lib/transitive_closure.py)
- [ ] [K4] Forstå [Johnson](lib/all_pairs_shortest_paths.py)

## Forelesning 12: Maksimal flyt
- [ ] [L1] Kunne definere flytnett, flyt og maks-flyt-problemet
- [ ] [L2] Kunne håndtere antiparallelle kanter og flere kilder og sluk
- [ ] ! [L3] Kunne definere restnettet til et flytnett med en gitt flyt
- [ ] [L4] Forstå hvordan man kan oppheve (cancel) flyt
- [ ] [L5] Forstå hva en forøkende sti (augmenting path) er
- [ ] [L6] Forstå hva snitt, snitt-kapasitet og minimalt snitt er
- [ ] ! [L7] Forstå maks-flyt/min-snitt-teoremet
- [x] [L8] Forstå Ford-Fulkerson-Method og [Ford-Fulkerson](lib/ford_fulkerson.py)
- [ ] [L9] Vite at Ford-Fulkerson med BFS kalles [Edmonds-Karp-algoritmen](lib/ford_fulkerson.py)
- [ ] [L10] Forstå hvordan maks-flyt kan finne en maksimum bipartitt matching
- [ ] ! [L11] Forstå heltallsteoremet (integrality theorem)

## Forelesning 13: NP-kompletthet
- [ ] [M1] Forstå sammenhengen mellom optimerings- og beslutnings-problemer
- [ ] [M2] Forstå koding (encoding) av en instans
- [ ] [M3] Forstå hvorfor løsningen på det binære ryggsekkproblemet ikke er polynomisk
- [ ] [M4] Forstå forskjellen på konkrete og abstrakte problemer
- [ ] [M5] Forstå representasjonen av beslutningsproblemer som formelle språk
- [ ] [M6] Forstå definisjonen av klassene P, NP og co-NP
- [ ] [M7] Forstå redusibilitets-relasjonen $\leq_p$
- [ ] ! [M8] Forstå definisjonen av NP-hardhet og NP-kompletthet
- [ ] [M9] Forstå den konvensjonelle hypotesen om forholdet mellom P, NP og NPC
- [ ] ! [M10] Forstå hvordan NP-kompletthet kan bevises ved én reduksjon
- [ ] ! [M11] Kjenne de NP-komplette problemene CIRCUIT-SAT, SAT, 3-CNF-SAT, CLIQUE, VERTEX-COVER, HAM-CYCLE, TSP og SUBSET-SUM
- [ ] [M12] Forstå at det binære ryggsekkproblemet er NP-hardt
- [ ] [M13] Forstå at lengste enkle-vei-problemet er NP-hardt
- [ ] [M14] Være i stand til å konstruere enkle NP-kompletthetsbevis