"""
Biografieën van de filosofen.
Elke filosoof heeft: wanneer geleefd, stroming, bekende boeken,
bekende uitspraken, en een beschrijving van de filosofische visie.
"""

BIOGRAFIEEN = {
    "socrates": {
        "naam": "Socrates",
        "leefde": "469–399 v.Chr.",
        "stroming": "Klassieke Griekse filosofie / Socratische methode",
        "boeken": [
            "Socrates heeft zelf nooit iets geschreven.",
            "Belangrijkste bronnen: Plato (Apologie, Crito, Phaedo, Symposium, Euthyphro), Xenophon (Memorabilia), Aristophanes (De Wolken).",
        ],
        "uitspraken": [
            "Ik weet dat ik niets weet.",
            "Het ongeëxamineerde leven is niet waard geleefd te worden.",
            "Het is nooit juist om kwaad te doen, ook niet als je kwaad is aangedaan.",
            "We zijn een haan schuldig aan Asclepius; betaal die schuld en vergeet het niet.",
            "Ik ben geen Athener of Griek, maar een burger van de wereld.",
        ],
        "visie": (
            "Socrates' filosofie draait om één kernvraag: hoe moet je leven? "
            "Hij liep rond op de markt van Athene en klampte mensen aan met vragen als: "
            "Wat is rechtvaardigheid? Wat is deugd? Wat is liefde? "
            "Zijn methode – de socratische methode of elenchus – werkte als volgt: "
            "Socrates deed alsof hij niets wist, stelde vragen, en dreef zijn gesprekspartner "
            "langzaam naar een innerlijke tegenstrijdigheid. Het doel was niet om de ander te vernederen, "
            "maar om hem te laten inzien dat wat hij zeker dacht te weten, eigenlijk niet klopte. "
            "Zo ontstond ruimte voor echte waarheid. Een van zijn meest radicale stellingen was: "
            "deugd is kennis. Wie werkelijk weet wat goed is, doet ook het goede. "
            "Niemand doet willens en wetens kwaad. Kennis en moraliteit waren voor Socrates onlosmakelijk verbonden. "
            "Hij zag zichzelf als een horzel – een lastige prikkel die Athene wakker hield. "
            "Hij was geen leraar in de gewone zin, maar een ondervrager. "
            "In 399 v.Chr. werd hij aangeklaagd voor goddeloosheid en het bederven van de jeugd. "
            "Hij werd schuldig bevonden en ter dood veroordeeld. Zijn vrienden regelden een ontsnapping, "
            "maar Socrates weigerde te vluchten. Hij vond dat je de wetten van je stad moet gehoorzamen, "
            "zelfs als ze onrechtvaardig zijn. Hij dronk de gifbeker met een rust die zijn vrienden verbijsterde."
        ),
    },

    "plato": {
        "naam": "Plato",
        "leefde": "428/427–348/347 v.Chr.",
        "stroming": "Idealisme / Platonisme",
        "boeken": [
            "Apologie, Crito, Phaedo, Symposium, Politeia (De Staat), Phaedrus, Timaeus, Theaetetus.",
            "De meeste werken zijn geschreven in dialoogvorm, met Socrates als hoofdpersoon.",
        ],
        "uitspraken": [
            "Het goede is het hoogste voorwerp van kennis.",
            "De mens is een tweevoetig dier zonder veren.",
            "Wie niet weet wat hij niet weet, weet niets.",
            "De tijd is een beweeglijk beeld van de eeuwigheid.",
        ],
        "visie": (
            "Plato's filosofie draait om de vraag naar de ware werkelijkheid achter de verschijnselen. "
            "Hij stelde dat er naast de zichtbare wereld een onzichtbare wereld van eeuwige, "
            "onveranderlijke Vormen of Ideeën bestaat. Het hoogste daarvan is het Goede. "
            "Alles wat we zien is slechts een afspiegeling van die hogere werkelijkheid. "
            "Zijn beroemdste beeld hiervoor is de allegorie van de grot: mensen zitten vastgeketend "
            "in een grot en zien alleen schaduwen op de wand, die ze voor de werkelijkheid aanzien. "
            "De filosoof is degene die zich losmaakt en het licht van de echte wereld ziet. "
            "Plato geloofde ook dat de ziel onsterfelijk is en dat leren in feite een herinneren is "
            "van wat de ziel al wist. In De Staat schetste hij een ideale samenleving, "
            "geleid door filosoof-koningen, omdat alleen zij de ware kennis van het Goede bezitten."
        ),
    },

    "marcus_aurelius": {
        "naam": "Marcus Aurelius",
        "leefde": "121–180 n.Chr.",
        "stroming": "Stoïcisme",
        "boeken": [
            "Ta eis heauton (Overpeinzingen / Meditations), geschreven in het Grieks tijdens zijn veldtochten.",
            "Het werk is nooit bedoeld voor publicatie; het zijn persoonlijke notities aan zichzelf.",
        ],
        "uitspraken": [
            "Je hebt macht over je geest, niet over de gebeurtenissen. Besef dat, en je zult kracht vinden.",
            "Het geluk van je leven hangt af van de kwaliteit van je gedachten.",
            "Accepteer wat je niet kunt veranderen, verander wat je kunt, en heb de wijsheid om het verschil te zien.",
            "De beste wraak is niet gelijk te zijn aan wie je kwaad deed.",
        ],
        "visie": (
            "Marcus Aurelius was keizer van Rome, maar bovenal stoïcijn. "
            "Zijn filosofie draait om één kernidee: je hebt geen controle over wat er gebeurt, "
            "maar wel over hoe je erop reageert. Alles buiten je eigen wil – rijkdom, roem, ziekte, dood – "
            "is uiteindelijk onverschillig. Het enige dat echt van jou is, is je innerlijke houding. "
            "Hij zag het universum als een redelijk geheel, doordrongen van een goddelijke Logos. "
            "De mens moet zich daarin voegen en zijn plicht doen, zonder klagen. "
            "De dood is onvermijdelijk en natuurlijk; er is geen reden om er bang voor te zijn. "
            "Zijn Overpeinzingen zijn geen theoretisch systeem, maar een dagelijkse oefening in zelfbeheersing, "
            "nederigheid en acceptatie. Hij schreef ze voor zichzelf, als herinnering om kalm te blijven "
            "te midden van oorlog, pest en verraad."
        ),
    },

    "boeddha": {
        "naam": "Boeddha (Siddhartha Gautama)",
        "leefde": "ca. 563–483 v.Chr. (of ca. 480–400 v.Chr., exacte data onzeker)",
        "stroming": "Boeddhisme",
        "boeken": [
            "De Pali Canon (Tripitaka), met de toespraken van de Boeddha.",
            "Dhammapada, een verzameling verzen toegeschreven aan de Boeddha.",
            "Belangrijke leerredes: Dhammacakkappavattana Sutta (het in beweging zetten van het wiel van de leer), Anattalakkhana Sutta, Satipatthana Sutta.",
        ],
        "uitspraken": [
            "Het leven is lijden.",
            "De oorzaak van lijden is verlangen.",
            "Het einde van lijden is mogelijk.",
            "Het achtvoudige pad leidt tot het einde van lijden.",
            "Wees je eigen lamp.",
            "Haar noch vlees kan een mens bevrijden; alleen inzicht bevrijdt.",
        ],
        "visie": (
            "De Boeddha's filosofie begint bij de erkenning dat het leven doordrenkt is van lijden (dukkha). "
            "Dat lijden komt voort uit verlangen en gehechtheid. Als je dat verlangen loslaat, verdwijnt het lijden. "
            "Het achtvoudige pad – juist inzicht, juiste intentie, juiste spraak, juist handelen, "
            "juiste levensonderhoud, juiste inspanning, juiste aandacht, juiste concentratie – "
            "is de weg daarnaartoe. Centraal staat het inzicht in de drie kenmerken van alle bestaan: "
            "onbestendigheid (anicca), lijden (dukkha) en niet-zelf (anatta). "
            "Er is geen vast, eeuwig ik; alles is in beweging en met elkaar verbonden. "
            "Het doel is nirvana: het uitdoven van het vuur van verlangen, haat en onwetendheid. "
            "De Boeddha was geen god en wilde ook niet als zodanig worden vereerd. "
            "Hij was een mens die ontwaakte en anderen de weg wees. "
            "Zijn leer is eerder een praktische therapie dan een metafysisch systeem: "
            "onderzoek zelf, ervaar zelf, en laat je niet leiden door blind geloof."
        ),
    },

    "maria_montessori": {
        "naam": "Maria Montessori",
        "leefde": "1870–1952",
        "stroming": "Reformpedagogiek",
        "boeken": [
            "Il metodo della pedagogia scientifica (De methode Montessori, 1909).",
            "The Absorbent Mind (De absorberende geest, 1949).",
            "The Discovery of the Child (De ontdekking van het kind, 1948).",
        ],
        "uitspraken": [
            "Het kind is de vader van de mens.",
            "Help mij het zelf te doen.",
            "De eerste taak van de opvoeding is het kind wakker maken voor het leven.",
            "Speel is het werk van het kind.",
        ],
        "visie": (
            "Maria Montessori was arts en pedagogen. Ze geloofde dat kinderen van nature leergierig zijn "
            "en zichzelf kunnen ontwikkelen als ze de juiste omgeving en vrijheid krijgen. "
            "Ze ontwierp materialen en een methode waarin het kind zelfstandig ontdekt, "
            "in plaats van passief te luisteren naar een leraar. De leraar is een begeleider, "
            "geen instructeur. Kernbegrippen zijn voorbereide omgeving, vrijheid binnen grenzen, "
            "en gevoelige periodes – fasen waarin een kind extra ontvankelijk is voor bepaalde vaardigheden. "
            "Montessori zag het kind als de bouwer van de volwassene: wie het kind goed begeleidt, "
            "bouwt aan een betere samenleving. Haar methode wordt wereldwijd toegepast, "
            "van peuteropvang tot middelbaar onderwijs."
        ),
    },

    "aristoteles": {
        "naam": "Aristoteles",
        "leefde": "384–322 v.Chr.",
        "stroming": "Deugdethiek / Peripatetische school",
        "boeken": [
            "Ethica Nicomachea (Nicomachische ethiek).",
            "Politica (Politiek).",
            "Metaphysica (Metafysica).",
            "De Anima (Over de ziel).",
            "Poetica (Poëtica).",
            "Organon (logische werken).",
        ],
        "uitspraken": [
            "Wij zijn wat we herhaaldelijk doen. Uitmuntendheid is dus geen daad, maar een gewoonte.",
            "Het geheel is meer dan de som der delen.",
            "De mens is van nature een politiek dier.",
            "Het goede is datgene waarnaar alles streeft.",
            "Een vriend is een tweede zelf.",
        ],
        "visie": (
            "Aristoteles was een leerling van Plato, maar zijn filosofie is aardser en empirischer. "
            "Hij geloofde niet in een aparte wereld van Vormen, maar zag de vormen in de dingen zelf. "
            "Kennis begint bij waarneming en ervaring. Zijn ethiek draait om het gulden middenpad: "
            "deugd is het juiste midden tussen twee uitersten. Moed is bijvoorbeeld het midden "
            "tussen lafheid en roekeloosheid. Het doel van het leven is eudaimonia – geluk of flourishing – "
            "en dat bereik je door je karakter te vormen via gewoonten. "
            "Aristoteles was ook de eerste die de logica systematiseerde, de biologie bestudeerde, "
            "en de politiek als wetenschap benaderde. Hij zag de mens als een sociaal wezen "
            "dat alleen in gemeenschap tot bloei komt."
        ),
    },

    "spinoza": {
        "naam": "Baruch Spinoza",
        "leefde": "1632–1677",
        "stroming": "Rationalisme / Monisme",
        "boeken": [
            "Ethica, ordine geometrico demonstrata (Ethiek, uiteengezet volgens de geometrische methode, 1677).",
            "Tractatus theologico-politicus (Theologisch-politiek traktaat, 1670).",
            "Tractatus de intellectus emendatione (Verhandeling over de verbetering van het verstand).",
        ],
        "uitspraken": [
            "God, ofwel de Natuur.",
            "Vrijheid is het inzicht in de noodzakelijkheid.",
            "De hoogste activiteit van de geest is God kennen.",
            "Haed en verdriet zijn tekenen van onwetendheid.",
        ],
        "visie": (
            "Spinoza's filosofie is een van de meest radicale en samenhangende systemen uit de westerse traditie. "
            "Hij stelde dat er maar één substantie bestaat: God, ofwel de Natuur. "
            "Alles wat bestaat is een verschijningsvorm van die ene substantie. "
            "Geest en lichaam zijn niet twee aparte dingen, maar twee aspecten van hetzelfde. "
            "Hij schreef zijn Ethica in de vorm van wiskundige bewijzen: definities, axioma's, stellingen. "
            "Volgens Spinoza is alles noodzakelijk zoals het is; er is geen vrije wil in de gewone zin. "
            "Echte vrijheid is het begrijpen van die noodzakelijkheid. "
            "Emoties zijn niet slecht, maar ze moeten worden begrepen; wie zijn emoties begrijpt, "
            "wordt er minder door meegesleept. Het hoogste geluk is de intellectuele liefde tot God, "
            "ofwel het begrijpen van de natuur als geheel."
        ),
    },

    "confucius": {
        "naam": "Confucius (Kong Fuzi)",
        "leefde": "551–479 v.Chr.",
        "stroming": "Confucianisme",
        "boeken": [
            "De Analecten (Lunyu), een verzameling uitspraken van Confucius, door leerlingen opgetekend.",
            "De Vijf Klassieken worden aan hem toegeschreven of door hem bewerkt: Lente- en Herfstannalen, Boek der Veranderingen, Boek der Liederen, Boek der Riten, Boek der Geschiedenis.",
        ],
        "uitspraken": [
            "Wat je niet wilt dat anderen jou aandoen, doe dat ook hen niet aan.",
            "De mens die niet nadenkt over wat ver weg is, zal ellende dichtbij vinden.",
            "Het is beter een lamp aan te steken dan de duisternis te vervloeken.",
            "Wie leert zonder na te denken, verdwaalt. Wie nadenkt zonder te leren, raakt in gevaar.",
            "Een reis van duizend mijl begint met één stap.",
        ],
        "visie": (
            "Confucius' filosofie is geen metafysisch systeem, maar een leer van juiste verhoudingen. "
            "Centraal staat ren: menselijkheid, medemenselijkheid, warmte. "
            "Daarnaast li: de juiste vormen, rituelen en gewoonten die het sociale leven ordenen. "
            "Hij geloofde dat een samenleving in harmonie is als mensen hun rol goed vervullen: "
            "vorst als vorst, vader als vader, zoon als zoon. "
            "Zelfverbetering is een levenslange taak. De edele mens (junzi) is niet iemand van hoge geboorte, "
            "maar iemand van karakter. Confucius was geen revolutionair; hij wilde de wijsheid van de oudheid herstellen. "
            "Zijn leer werd eeuwenlang de basis van het Chinese onderwijs en bestuur."
        ),
    },

    "lao_tze": {
        "naam": "Lao Tze (Laozi)",
        "leefde": "ca. 6e–4e eeuw v.Chr. (exacte data onzeker; mogelijk een legendarische figuur)",
        "stroming": "Taoïsme",
        "boeken": [
            "Tao Te Ching (Daodejing), het kernwerk van het taoïsme, toegeschreven aan Lao Tze.",
            "Het boek bestaat uit 81 korte hoofdstukken van poëtische wijsheid.",
        ],
        "uitspraken": [
            "De tao die genoemd kan worden is niet de eeuwige tao.",
            "Zachtheid overwint hardheid; het zwakke overwint het sterke.",
            "Wie niets doet, laat niets ongedaan.",
            "Een reis van duizend mijl begint met één stap.",
            "Water is zacht en toch overwint het de rots.",
        ],
        "visie": (
            "Lao Tze's filosofie draait om de tao: de weg, de natuurlijke orde der dingen. "
            "De tao is onnoembaar, ongrijpbaar, en toch de bron van alles. "
            "De mens moet niet tegen de stroom in zwemmen, maar meebewegen met de natuurlijke gang van zaken. "
            "Dat is wu wei: niet-doen, of beter: handelen zonder geforceerd te handelen. "
            "Lao Tze wantrouwt regels, wetten en moralisme. Hoe meer verboden, hoe meer dieven. "
            "Hij prijst eenvoud, zachtheid, en het vermogen om terug te treden. "
            "Het taoïsme is geen pessimisme, maar een diep vertrouwen in de natuurlijke orde. "
            "Zijn invloed op de Chinese cultuur, kunst, geneeskunde en vechtsport is enorm geweest."
        ),
    },

    "camus": {
        "naam": "Albert Camus",
        "leefde": "1913–1960",
        "stroming": "Absurdisme / Existentialisme",
        "boeken": [
            "L'Étranger (De vreemdeling, 1942).",
            "Le Mythe de Sisyphe (De mythe van Sisyphus, 1942).",
            "La Peste (De pest, 1947).",
            "L'Homme révolté (De mens in opstand, 1951).",
            "La Chute (De val, 1956).",
        ],
        "uitspraken": [
            "Er is maar één werkelijk serieus filosofisch probleem: de zelfmoord.",
            "We moeten ons Sisyphus gelukkig voorstellen.",
            "In het midden van de winter ontdekte ik eindelijk dat er in mij een onoverwinnelijke zomer was.",
            "Ik kom tot opstand, dus wij zijn.",
            "De absurde mens zegt ja en zijn inspanning is nooit voorbij.",
        ],
        "visie": (
            "Camus' filosofie begint bij het absurde: de botsing tussen het menselijke verlangen naar betekenis "
            "en de stomme stilte van het universum. Het leven heeft geen voorgegeven zin. "
            "De vraag is niet of we zelfmoord moeten plegen, maar of we kunnen leven zonder zin. "
            "Camus' antwoord is ja: we moeten de absurditeit omarmen en toch doorgaan. "
            "Dat is de opstand. Sisyphus, die eeuwig een rotsblok de berg op duwt, is het beeld van de mens. "
            "Maar Sisyphus is gelukkig, omdat hij zijn lot aanvaardt en er waardigheid aan ontleent. "
            "Camus was ook een man van solidariteit. In De pest laat hij zien hoe mensen in tijden van crisis "
            "samenkomen en hun plicht doen, zonder heldhaftigheid, maar met gewone moed. "
            "Zijn filosofie is geen pessimisme, maar een nuchter humanisme."
        ),
    },
    
    "nietzsche": {
        "naam": "Friedrich Nietzsche",
        "leefde": "1844–1900",
        "stroming": "Existentialisme / Lebensphilosophie",
        "boeken": [
            "Die Geburt der Tragödie (De geboorte van de tragedie, 1872).",
            "Also sprach Zarathustra (Aldus sprak Zarathustra, 1883–1885).",
            "Jenseits von Gut und Böse (Voorbij goed en kwaad, 1886).",
            "Zur Genealogie der Moral (De genealogie van de moraal, 1887).",
            "Der Antichrist (De antichrist, 1888).",
            "Ecce Homo (1888).",
        ],
        "uitspraken": [
            "God is dood.",
            "Wat mij niet doodt, maakt mij sterker.",
            "Wie een waarom heeft om te leven, verdraagt bijna elke hoe.",
            "De mens is een touw gespannen tussen dier en Übermensch.",
            "Je moet chaos in je hebben om een dansende ster te baren.",
            "Er zijn geen feiten, alleen interpretaties.",
        ],
        "visie": (
            "Nietzsche is een van de meest misverstane filosofen uit de westerse traditie. "
            "Zijn kernboodschap is niet dat geweld goed is, maar dat de mens zijn eigen waarden moet scheppen. "
            "Hij zag dat de traditionele moraal – vooral de christelijke – de mens klein houdt. "
            "Die moraal noemde hij slavenmoraal: ze verheerlijkt nederigheid, gehoorzaamheid en zwakte. "
            "Daartegenover stelde hij de herenmoraal: kracht, moed, scheppingsdrang. "
            "Met God is dood bedoelde hij niet een atheïstische slogan, maar de constatering dat het geloof "
            "in een goddelijke ordening zijn vanzelfsprekendheid heeft verloren. "
            "De mens moet nu zelf zin maken. De Übermensch is geen ras of superheld, "
            "maar een mens die zijn eigen waarden durft te scheppen en ja zegt tegen het leven, "
            "met al zijn lijden. Dat is de amor fati: hou van je lot. "
            "Zijn werk is geen systeem, maar een reeks provocaties, aforismen en profetieën."
        ),
    },

    "marx": {
        "naam": "Karl Marx",
        "leefde": "1818–1883",
        "stroming": "Marxisme / Historisch materialisme",
        "boeken": [
            "Das Kapital (Het kapitaal, deel 1: 1867; delen 2 en 3 postuum).",
            "Manifest der Kommunistischen Partei (Communistisch Manifest, 1848, met Friedrich Engels).",
            "Die deutsche Ideologie (De Duitse ideologie, 1846, postuum).",
            "Zur Kritik der politischen Ökonomie (Bijdrage tot de kritiek van de politieke economie, 1859).",
            "Ökonomisch-philosophische Manuskripte (Economisch-filosofische manuscripten, 1844).",
        ],
        "uitspraken": [
            "De filosofen hebben de wereld slechts op verschillende manieren geïnterpreteerd; het komt erop aan haar te veranderen.",
            "Proletariërs aller landen, verenigt u!",
            "Het zijn niet het bewustzijn van de mensen dat hun zijn bepaalt, maar hun maatschappelijk zijn dat hun bewustzijn bepaalt.",
            "De geschiedenis van alle tot nu toe bestaande samenlevingen is de geschiedenis van klassenstrijd.",
            "Godsdienst is de zucht van het verdrukte schepsel, het hart van een harteloze wereld.",
        ],
        "visie": (
            "Marx' filosofie draait om de vraag: wie profiteert, en wie betaalt de prijs? "
            "Hij zag de samenleving niet als een verzameling vrije individuen, maar als een systeem van klassenverhoudingen. "
            "De geschiedenis wordt gedreven door materiële omstandigheden, niet door ideeën. "
            "De kapitalist bezit de productiemiddelen; de arbeider bezit alleen zijn arbeidskracht. "
            "De winst van de kapitalist komt voort uit meerwaarde: het verschil tussen wat de arbeider produceert "
            "en wat hij betaald krijgt. Dat is geen morele beschuldiging, maar een structureel mechanisme. "
            "Marx voorspelde dat het kapitalisme zou leiden tot steeds scherpere tegenstellingen, "
            "en uiteindelijk tot een revolutie waarin de arbeiders de macht overnemen. "
            "Hij geloofde niet in utopisch socialisme, maar in een wetenschappelijke analyse van de economie. "
            "Zijn invloed op de politiek, sociologie en geschiedschrijving is enorm geweest, "
            "los van de vraag of zijn voorspellingen zijn uitgekomen."
        ),
    },

    "hannah_arendt": {
        "naam": "Hannah Arendt",
        "leefde": "1906–1975",
        "stroming": "Politieke filosofie / Fenomenologie",
        "boeken": [
            "The Origins of Totalitarianism (De oorsprong van het totalitarisme, 1951).",
            "The Human Condition (De menselijke conditie, 1958).",
            "Eichmann in Jerusalem: A Report on the Banality of Evil (Eichmann in Jeruzalem: de banaliteit van het kwaad, 1963).",
            "On Revolution (Over revolutie, 1963).",
            "The Life of the Mind (Het leven van de geest, 1978, postuum).",
        ],
        "uitspraken": [
            "De meest radicale vorm van kwaad is de banaliteit van het kwaad.",
            "Niemand heeft het recht te gehoorzamen.",
            "Macht ontstaat waar mensen samen handelen.",
            "Denken zonder houvast is de enige manier om niet te vervallen tot ideologie.",
            "De mens is geen wezen dat alleen is; hij is een wezen dat met anderen verschijnt.",
        ],
        "visie": (
            "Hannah Arendt is een van de scherpste denkers over macht, kwaad en vrijheid. "
            "Ze analyseerde het totalitarisme niet als een uitbarsting van barbarij, maar als een moderne verschijnsel "
            "dat wortelt in massale eenzaamheid, ideologie en terreur. "
            "Haar beroemdste idee is de banaliteit van het kwaad: het kwaad wordt vaak niet gepleegd door monsters, "
            "maar door gewone mensen die niet nadenken en zich verschuilen achter bevelen. "
            "Arendt geloofde dat vrijheid niet ligt in het innerlijk, maar in het publieke handelen: "
            "mensen die samen iets nieuws beginnen. Macht is niet iets dat iemand bezit, "
            "maar iets dat ontstaat tussen mensen die samen handelen. "
            "Ze was wantrouwig tegenover elke ideologie die de werkelijkheid in een systeem wil persen. "
            "Denken betekent voor haar: luisteren naar de vele stemmen in jezelf, zonder ze tot één te maken."
        ),
    },

    "gandhi": {
        "naam": "Mahatma Gandhi",
        "leefde": "1869–1948",
        "stroming": "Geweldloosheid / Satyagraha",
        "boeken": [
            "The Story of My Experiments with Truth (De geschiedenis van mijn experimenten met de waarheid, 1927–1929).",
            "Hind Swaraj (1909).",
            "Satyagraha in South Africa (1928).",
        ],
        "uitspraken": [
            "Wees de verandering die je in de wereld wilt zien.",
            "Oog om oog maakt de hele wereld blind.",
            "Kracht komt niet voort uit fysieke capaciteit, maar uit een onverzettelijke wil.",
            "De toekomst hangt af van wat je vandaag doet.",
            "Eerst negeren ze je, dan lachen ze je uit, dan vechten ze tegen je, dan win je.",
        ],
        "visie": (
            "Gandhi's filosofie draait om satyagraha: vasthouden aan de waarheid, met geweldloosheid als middel. "
            "Hij geloofde dat geweld nooit gerechtvaardigd is, ook niet tegen onrecht. "
            "Verzet moet bestaan uit burgerlijke ongehoorzaamheid, boycot, vasten en geweldloze opstand. "
            "De tegenstander is geen vijand, maar iemand die je moet overtuigen. "
            "Gandhi was diep religieus, maar niet sektarisch: hij putte uit het hindoeïsme, "
            "het christendom, de islam en het jodendom. "
            "Hij leefde eenvoudig, spon zijn eigen kleding, en geloofde in de kracht van zelfbeheersing. "
            "Zijn invloed op Martin Luther King en Nelson Mandela is enorm geweest. "
            "Hij werd in 1948 vermoord door een hindoe-nationalist, kort na de onafhankelijkheid van India."
        ),
    },

    "kierkegaard": {
        "naam": "Søren Kierkegaard",
        "leefde": "1813–1855",
        "stroming": "Existentialisme / Christelijke filosofie",
        "boeken": [
            "Enten-Eller (Of-Of, 1843).",
            "Frygt og Bæven (Vrees en beven, 1843).",
            "Sygdommen til Døden (De ziekte tot de dood, 1849).",
            "Afsluttende uvidenskabelig Efterskrift (Afsluitend onwetenschappelijk nawoord, 1846).",
        ],
        "uitspraken": [
            "Het leven moet vooruit worden geleefd, maar achteruit worden begrepen.",
            "Angst is de duizeligheid van de vrijheid.",
            "Ik moet een waarheid vinden die waar is voor mij.",
            "De deur naar geluk gaat naar binnen.",
            "Durf te springen.",
        ],
        "visie": (
            "Kierkegaard wordt beschouwd als de vader van het existentialisme. "
            "Hij verzette zich tegen het systeemdenken van Hegel, waarin de individuele mens verdwijnt in het grote geheel. "
            "Voor Kierkegaard gaat het om de enkeling: jouw keuze, jouw verantwoordelijkheid, jouw bestaan. "
            "Hij onderscheidde drie levensstadia: het esthetische (genieten), het ethische (plicht), "
            "en het religieuze (overgave aan God). De overgang tussen die stadia is een sprong, geen logische stap. "
            "Angst is bij Kierkegaard geen ziekte, maar de duizeling die je voelt als je beseft dat je vrij bent "
            "en dus kunt kiezen – en dus kunt falen. Wie die angst durft te aanvaarden, kan een echte sprong maken. "
            "Hij schreef vaak onder pseudoniemen, zodat de lezer niet zijn mening kreeg, maar zelf moest worstelen. "
            "Zijn werk is religieus, maar niet braaf: het eist een persoonlijke, hartstochtelijke overgave."
        ),
    },

    "schopenhauer": {
        "naam": "Arthur Schopenhauer",
        "leefde": "1788–1860",
        "stroming": "Pessimisme / Idealisme",
        "boeken": [
            "Die Welt als Wille und Vorstellung (De wereld als wil en voorstelling, 1819).",
            "Über die Freiheit des menschlichen Willens (Over de vrijheid van de menselijke wil, 1839).",
            "Parerga und Paralipomena (1851).",
            "Aphorismen zur Lebensweisheit (Aforismen over levenswijsheid, 1851).",
        ],
        "uitspraken": [
            "Het leven is een zaak die men beter niet kan beginnen.",
            "De wereld is mijn voorstelling.",
            "Het leven slingert heen en weer tussen pijn en verveling.",
            "Alle waarheid gaat door drie stadia: eerst wordt ze belachelijk gemaakt, dan wordt ze verboden, dan wordt ze vanzelfsprekend.",
        ],
        "visie": (
            "Schopenhauer is de grote pessimist van de westerse filosofie. "
            "Hij bouwde voort op Kant, maar trok radicalere conclusies. "
            "De wereld zoals wij die kennen is onze voorstelling; daarachter ligt een blinde, irrationele Wil, "
            "die alles voortdrijft. Die Wil is nooit bevredigd: wat we ook bereiken, er komt weer een nieuw verlangen. "
            "Het leven is dus een voortdurende beweging tussen pijn en verveling. "
            "Verlossing is tijdelijk mogelijk via kunst, via mededogen, en via ascese: het loslaten van verlangen. "
            "Schopenhauer beïnvloedde Nietzsche, Wagner, Freud en het boeddhisme in het Westen. "
            "Hij was geen vrolijke man, maar wel een vlijmscherpe schrijver, "
            "die met zichtbaar plezier de domheid van zijn tijdgenoten fileerde."
        ),
    },

    "descartes": {
        "naam": "René Descartes",
        "leefde": "1596–1650",
        "stroming": "Rationalisme / Methodische twijfel",
        "boeken": [
            "Discours de la méthode (Verhandeling over de methode, 1637).",
            "Meditationes de prima philosophia (Meditaties over de eerste filosofie, 1641).",
            "Principia philosophiae (Beginselen van de filosofie, 1644).",
            "Passions de l'âme (De passies van de ziel, 1649).",
        ],
        "uitspraken": [
            "Cogito, ergo sum. Ik denk, dus ik ben.",
            "Twijfel is het begin van wijsheid.",
            "Ik heb alle zekerheid opgeschort, om zekerheid te vinden.",
            "De rede is de enige weg naar waarheid.",
        ],
        "visie": (
            "Descartes is de vader van de moderne filosofie. "
            "Hij begon met radicale twijfel: alles wat je weet, kan bedrog zijn. "
            "Misschien droom je, misschien bedriegt een kwade demon je. "
            "Maar één ding is zeker: er is iemand die twijfelt, dus er is een denkend ik. "
            "Cogito ergo sum. Vanuit dat ene zekere punt bouwt Descartes de rest van de kennis op. "
            "Hij onderscheidde twee substanties: denkende geest en uitgebreid lichaam. "
            "Dat dualisme heeft de westerse filosofie eeuwenlang beziggehouden. "
            "Descartes was ook een wiskundige: hij ontwikkelde de analytische meetkunde "
            "en geloofde dat de natuur in wiskundige wetten beschreven kon worden. "
            "Zijn methode is die van de twijfel: alles wat niet helder en duidelijk is, "
            "moet worden verworpen tot het bewezen is."
        ),
    },

    "leibniz": {
        "naam": "Gottfried Wilhelm Leibniz",
        "leefde": "1646–1716",
        "stroming": "Rationalisme / Monadologie",
        "boeken": [
            "Monadologie (1714).",
            "Théodicée (1710).",
            "Nouveaux Essais sur l'entendement humain (Nieuwe verhandelingen over het menselijk verstand, 1704, postuum).",
            "Discours de métaphysique (Verhandeling over de metafysica, 1686).",
        ],
        "uitspraken": [
            "We leven in de beste van alle mogelijke werelden.",
            "Er is niets zonder reden.",
            "Elke monade is een spiegel van het universum.",
            "Het heden is zwanger van de toekomst.",
        ],
        "visie": (
            "Leibniz was een universeel genie: filosoof, wiskundige, jurist, diplomaat, uitvinder. "
            "Hij ontwikkelde de differentiaal- en integraalrekening onafhankelijk van Newton. "
            "Zijn filosofie draait om de monade: een enkelvoudige, onstoffelijke eenheid die het hele universum weerspiegelt. "
            "Er zijn oneindig veel monaden, elk met een eigen perspectief. "
            "God koos bij de schepping de beste van alle mogelijke werelden – niet omdat er geen kwaad is, "
            "maar omdat elke andere wereld meer kwaad zou bevatten. "
            "Dat idee werd door Voltaire genadeloos bespot in Candide. "
            "Leibniz geloofde in een vooraf vastgestelde harmonie: geest en lichaam lopen synchroon, "
            "zonder dat ze elkaar beïnvloeden. Zijn werk is optimistisch, systemisch en diep religieus."
        ),
    },

    "willem_van_ockham": {
        "naam": "Willem van Ockham",
        "leefde": "ca. 1287–1347",
        "stroming": "Nominalisme / Scholastiek",
        "boeken": [
            "Summa logicae (1323).",
            "Quodlibeta septem (1333).",
            "Dialogus (1334).",
            "Breviloquium (1342).",
        ],
        "uitspraken": [
            "Wat met minder aannames kan worden gedaan, moet niet met meer worden gedaan.",
            "De scheermes snijdt alle overbodige entiteiten weg.",
            "Alleen individuen bestaan; algemene begrippen zijn slechts namen.",
        ],
        "visie": (
            "Willem van Ockham is beroemd geworden door het scheermes van Ockham: "
            "de regel dat je geen onnodige aannames moet doen. "
            "Als je iets kunt verklaren met minder veronderstellingen, doe dat dan. "
            "Dat principe is nog steeds een hoeksteen van de wetenschap. "
            "Filosofisch was hij nominalist: hij geloofde dat alleen individuele dingen echt bestaan, "
            "en dat algemene begrippen zoals mens of rechtvaardigheid slechts namen zijn. "
            "Dat bracht hem in conflict met de kerk, die algemene ideeën als goddelijke werkelijkheden zag. "
            "Ockham was een Franciscaanse monnik die openlijk kritiek had op de paus. "
            "Hij werd geëxcommuniceerd en bracht zijn laatste jaren door in ballingschap in München. "
            "Zijn invloed op de wetenschap, de logica en het moderne denken is groot."
        ),
    },

    "thomas_aquinas": {
        "naam": "Thomas Aquinas",
        "leefde": "1225–1274",
        "stroming": "Scholastiek / Thomisme",
        "boeken": [
            "Summa Theologiae (1265–1274).",
            "Summa contra Gentiles (1259–1265).",
            "De ente et essentia (Over zijnde en wezen).",
            "Quaestiones disputatae de veritate (Betwiste vragen over de waarheid).",
        ],
        "uitspraken": [
            "Genade bouwt voort op de natuur.",
            "De rede is een geschenk van God en mag niet worden verworpen.",
            "Het goede is datgene waarnaar alles streeft.",
            "Ik heb geschreven zoveel ik kon; nu is het tijd om te zwijgen.",
        ],
        "visie": (
            "Thomas van Aquino is de grootste denker van de middeleeuwse scholastiek. "
            "Hij verzoende het christelijke geloof met de filosofie van Aristoteles. "
            "Zijn kernidee: geloof en rede kunnen niet in conflict zijn, want beide komen van God. "
            "De rede kan de natuur begrijpen; het geloof onthult wat de rede niet kan bereiken. "
            "In zijn Summa Theologiae behandelt hij honderden vragen over God, mens, moraal en recht. "
            "Hij geloofde dat de mens van nature gericht is op geluk, en dat geluk uiteindelijk alleen in God te vinden is. "
            "Zijn deugdethiek is geïnspireerd op Aristoteles, maar aangevuld met de goddelijke genade. "
            "Hij schreef op het einde van zijn leven dat al zijn werk stro was vergeleken met wat hij had gezien. "
            "Zijn invloed op de katholieke kerk en de westerse filosofie is enorm."
        ),
    },      
    "erasmus": {
        "naam": "Desiderius Erasmus",
        "leefde": "1466–1536",
        "stroming": "Humanisme / Renaissance",
        "boeken": [
            "Lof der Zotheid (Moriae encomium, 1511).",
            "Handboek van de christelijke strijder (Enchiridion militis Christiani, 1503).",
            "Colloquia (Gesprekken, 1518).",
            "Novum Instrumentum (Nieuwe Testament in het Grieks, 1516).",
        ],
        "uitspraken": [
            "De dwaasheid is de enige macht die de wereld regeert.",
            "Ik kan niet liegen; ik kan alleen zwijgen.",
            "Oorlog is zoet voor wie hem niet meemaakt.",
            "De mens wordt niet geboren als mens, maar gevormd door opvoeding.",
        ],
        "visie": (
            "Erasmus is de grote humanist van de Renaissance. "
            "Hij geloofde in de kracht van opvoeding, verdraagzaamheid en innerlijke vroomheid. "
            "In Lof der Zotheid laat hij de Zotheid zelf aan het woord, die alle menselijke dwaasheid opvoert: "
            "heersers, geleerden, priesters, allemaal zijn ze dwaas. "
            "Erasmus was een scherp criticus van de kerk, maar bleef trouw aan het geloof. "
            "Hij wilde hervorming van binnenuit, geen scheuring. "
            "Zijn Griekse editie van het Nieuwe Testament maakte de Bijbel toegankelijk voor gewone mensen. "
            "Hij was een europees denker voordat Europa bestond: hij reisde door heel Europa, "
            "schreef in het Latijn, en correspondeerde met koningen en humanisten. "
            "Zijn tolerantie en ironie staan in scherp contrast met het geweld van zijn tijd."
        ),
    },

    "pascal": {
        "naam": "Blaise Pascal",
        "leefde": "1623–1662",
        "stroming": "Jansenisme / Christelijke filosofie",
        "boeken": [
            "Pensées (Gedachten, postuum 1670).",
            "Lettres provinciales (Provinciale brieven, 1656–1657).",
            "Traité du triangle arithmétique (Verhandeling over de rekenkundige driehoek, 1654).",
        ],
        "uitspraken": [
            "Het hart heeft zijn redenen die de rede niet kent.",
            "De mens is een riet, maar een denkend riet.",
            "De eeuwige stilte van die oneindige ruimten maakt mij bang.",
            "Alle ellende van de mens komt voort uit het feit dat hij niet rustig in zijn kamer kan blijven.",
        ],
        "visie": (
            "Pascal was een geniale wiskundige en een vurige gelovige. "
            "Hij ontwikkelde op jonge leeftijd de eerste rekenmachine, schreef over kansrekening, "
            "en deed baanbrekend werk in de meetkunde. "
            "Maar na een mystieke ervaring wijdde hij zich aan het geloof. "
            "In zijn Pensées worstelt hij met de tegenstelling tussen rede en geloof. "
            "De rede kan God niet bewijzen; het hart moet de sprong wagen. "
            "Zijn beroemde weddenschap: als je gelooft en er is een God, win je alles; "
            "als je niet gelooft en er is een God, verlies je alles. "
            "Hij zag de mens als een wezen dat rusteloos op zoek is naar afleiding, "
            "omdat hij de confrontatie met zijn eigen nietigheid niet aankan. "
            "Pascal is geen systeemdenker, maar een denker van de paradox: "
            "groot en klein, riet en engel, verstand en hart."
        ),
    },

    "mary_wollstonecraft": {
        "naam": "Mary Wollstonecraft",
        "leefde": "1759–1797",
        "stroming": "Verlichting / Vroeg-feminisme",
        "boeken": [
            "A Vindication of the Rights of Woman (Verdediging van de rechten van de vrouw, 1792).",
            "A Vindication of the Rights of Men (Verdediging van de rechten van de mens, 1790).",
            "Mary: A Fiction (1788).",
            "Letters Written in Sweden, Norway, and Denmark (1796).",
        ],
        "uitspraken": [
            "Ik wil niet dat vrouwen macht over mannen hebben, maar macht over zichzelf.",
            "De geest heeft geen sekse.",
            "Vrouwen worden niet geboren als zwakke wezens; ze worden het gemaakt.",
            "De eerste plicht van een vrouw is niet om mooi te zijn, maar om verstandig te zijn.",
        ],
        "visie": (
            "Mary Wollstonecraft is een van de eerste feministen van de westerse geschiedenis. "
            "Ze leefde in de tijd van de Franse Revolutie en de Verlichting, "
            "maar zag dat de idealen van vrijheid en gelijkheid alleen voor mannen golden. "
            "In A Vindication of the Rights of Woman eist ze onderwijs voor vrouwen. "
            "Niet omdat vrouwen beter zouden zijn dan mannen, maar omdat ze net als mannen "
            "redelijke wezens zijn die hun eigen leven moeten kunnen vormgeven. "
            "Vrouwen worden volgens haar opgevoed tot sierlijkheid en gehoorzaamheid, "
            "en vervolgens beschuldigd van zwakte. "
            "Ze was ook een scherp criticus van het huwelijk als economische gevangenis. "
            "Ze stierf jong, in het kraambed, maar haar dochter – Mary Shelley – "
            "zou later Frankenstein schrijven. Haar invloed op het feminisme is fundamenteel."
        ),
    },

    "belle_van_zuylen": {
        "naam": "Belle van Zuylen (Isabelle de Charrière)",
        "leefde": "1740–1805",
        "stroming": "Verlichting / Briefroman",
        "boeken": [
            "Le Noble (De edelman, 1763).",
            "Lettres neuchâteloises (Brieven uit Neuchâtel, 1784).",
            "Caliste, ou lettres écrites de Lausanne (Caliste, of brieven uit Lausanne, 1787).",
            "Trois femmes (Drie vrouwen, 1795).",
        ],
        "uitspraken": [
            "Ik ben niet gemaakt om te gehoorzamen.",
            "Vrijheid is het enige goed dat ik niet kan opgeven.",
            "De wereld is een toneelstuk, en ik weiger mijn rol slaafs te spelen.",
        ],
        "visie": (
            "Belle van Zuylen was een adellijke vrouw die zich niets aantrok van de conventies van haar tijd. "
            "Ze schreef romans, brieven en pamfletten, in het Frans, en onderhield correspondentie "
            "met de belangrijkste denkers van de Verlichting. "
            "Ze trouwde met een Zwitserse edelman, maar behield haar onafhankelijkheid. "
            "Haar werk draait om vrijheid, ongelijkheid en de positie van de vrouw. "
            "Ze was ironisch, scherp en weigerde zich te conformeren aan de rol die vrouwen kregen toebedeeld. "
            "In Caliste beschrijft ze de innerlijke wereld van een vrouw die kiest voor haar eigen leven. "
            "Ze was een voorloper van het feminisme, maar noemde zichzelf zo niet. "
            "Ze was simpelweg iemand die dacht en schreef zoals ze wilde."
        ),
    },

    "hadewijch": {
        "naam": "Hadewijch",
        "leefde": "ca. 1200–1240 (exacte data onbekend)",
        "stroming": "Middeleeuwse mystiek / Beguinen",
        "boeken": [
            "Brieven (verzameling van 31 brieven).",
            "Visioenen (14 visioenen).",
            "Strofische gedichten (Liederen).",
            "Mengeldichten (Rijmverzen).",
        ],
        "uitspraken": [
            "De liefde is sterker dan de dood.",
            "Wie de liefde wil bezitten, moet haar durven verliezen.",
            "In de woestijn van de ziel ontmoet ik God.",
        ],
        "visie": (
            "Hadewijch is een van de grootste mystici van de Nederlandse middeleeuwen. "
            "Ze was waarschijnlijk een begijn: een vrouw die buiten het klooster leefde, "
            "in een gemeenschap van vrome vrouwen, zonder eeuwige gelofte. "
            "Ze schreef brieven, visioenen en liederen in het Middelnederlands, "
            "vol beeldende taal en vurige liefde. "
            "Centraal staat de minne: de goddelijke liefde die de ziel vervult en tegelijk verteert. "
            "Hadewijch beschrijft de weg naar God als een weg van liefde en lijden, "
            "van zoetheid en verlatenheid. "
            "Ze was geen theoloog in de academische zin, maar een dichter die het onzegbare probeerde te zeggen. "
            "Haar werk is pas in de negentiende eeuw herontdekt en wordt nu beschouwd "
            "als een hoogtepunt van de Europese mystiek."
        ),
    },

    "nagarjuna": {
        "naam": "Nāgārjuna",
        "leefde": "ca. 150–250 n.Chr.",
        "stroming": "Madhyamaka / Boeddhistische filosofie",
        "boeken": [
            "Mūlamadhyamakakārikā (Verzen over de fundamentele wijsheid van de middenweg).",
            "Vigrahavyāvartanī (Het weerleggen van bezwaren).",
            "Śūnyatāsaptati (Zeventig verzen over leegte).",
        ],
        "uitspraken": [
            "Niets bestaat op zichzelf.",
            "Leegte is niet niets; leegte is de afwezigheid van eigen bestaan.",
            "Wie de middenweg ziet, ziet de werkelijkheid.",
        ],
        "visie": (
            "Nāgārjuna is de grondlegger van de Madhyamaka-school in het boeddhisme. "
            "Zijn kernidee is dat alles leeg is: niets heeft een eigen, onafhankelijk bestaan. "
            "Alles bestaat alleen in afhankelijkheid van iets anders. "
            "Dat betekent niet dat niets bestaat, maar dat niets op zichzelf bestaat. "
            "Met scherpe logica ontleedt hij alle aannames over zijn, tijd, oorzaak en identiteit. "
            "Hij weerlegt elke stelling zonder zelf een nieuwe stelling te verdedigen. "
            "Zijn werk is moeilijk, paradoxaal en diep. "
            "Leegte is voor hem geen nihilisme, maar de weg naar bevrijding: "
            "wie inziet dat alles leeg is, hecht zich nergens meer aan, en raakt vrij. "
            "Nāgārjuna beïnvloedde het Tibetaanse boeddhisme, het Zen en de westerse filosofie."
        ),
    },

    "zhuangzi": {
        "naam": "Zhuangzi",
        "leefde": "ca. 369–286 v.Chr.",
        "stroming": "Taoïsme",
        "boeken": [
            "Zhuangzi (het boek dat zijn naam draagt, deels door hemzelf, deels door volgelingen).",
            "Het werk bestaat uit 33 hoofdstukken vol parabels, anekdotes en dialogen.",
        ],
        "uitspraken": [
            "Ik droomde dat ik een vlinder was; nu weet ik niet of ik een mens ben die droomt een vlinder te zijn, of een vlinder die droomt een mens te zijn.",
            "Het leven is een droom, en de dood is ontwaken.",
            "Wie zich niet laat binden, is vrij.",
            "Het nut van het nutteloze is groot.",
        ],
        "visie": (
            "Zhuangzi is de speelse taoïst. Waar Lao Tze plechtig en poëtisch is, is Zhuangzi verhalend en relativerend. "
            "Hij vertelt parabels over vissen, vogels, bomen en dromen. "
            "Zijn beroemdste verhaal is dat van de vlinder: hij droomt dat hij een vlinder is, "
            "en als hij wakker wordt, weet hij niet zeker of hij een mens is die droomde een vlinder te zijn, "
            "of een vlinder die nu droomt een mens te zijn. "
            "Zhuangzi relativeert alle zekerheden: goed en kwaad, nut en onnut, leven en dood. "
            "Hij gelooft niet in starre regels of systemen. "
            "De wijze laat zich meevoeren met de natuurlijke gang van zaken, zonder weerstand. "
            "Zijn werk is humoristisch, diepzinnig en bevrijdend. "
            "Het is een van de mooiste teksten uit de Chinese filosofie."
        ),
    },

    "dogen": {
        "naam": "Dōgen",
        "leefde": "1200–1253",
        "stroming": "Zen-boeddhisme / Sōtō-school",
        "boeken": [
            "Shōbōgenzō (De schatkamer van het ware oog van de dharma).",
            "Eihei Kōroku (Uitgebreide kroniek van Eihei).",
            "Fukanzazengi (Universele aanwijzingen voor zazen).",
        ],
        "uitspraken": [
            "Zitten is zelf verlichting; er is geen verlichting los van de beoefening.",
            "Tijd is geen lijn, maar een opeenvolging van momenten die elk het hele zijn bevatten.",
            "Studie van de weg is studie van het zelf; studie van het zelf is het vergeten van het zelf.",
            "Wees hier en nu; dat is de hele leer.",
        ],
        "visie": (
            "Dōgen is de grote filosoof van het Japanse zenboeddhisme. "
            "Hij bracht de Sōtō-school vanuit China naar Japan. "
            "Zijn kernidee: beoefening en verlichting zijn niet twee dingen. "
            "Je zit niet om verlicht te worden; het zitten zelf is de verlichting. "
            "Dat klinkt paradoxaal, maar het is de kern van zijn denken. "
            "Dōgen schreef in het Japans, niet in het Chinees, en zijn taal is poëtisch en diep. "
            "In zijn Shōbōgenzō behandelt hij thema's als tijd, zijn, Boeddha-natuur en de eenheid van alle dingen. "
            "Hij was geen wereldvreemde monnik: hij reisde, onderwees, en bouwde kloosters. "
            "Zijn invloed op het Japanse denken, de theeceremonie, de tuinkunst en de krijgskunsten is enorm."
        ),
    },

    "rumi": {
        "naam": "Rumi (Jalal ad-Din Muhammad Rumi)",
        "leefde": "1207–1273",
        "stroming": "Soefisme",
        "boeken": [
            "Masnavi-ye Manavi (Geestelijke verzen, zes delen).",
            "Divan-e Shams-e Tabrizi (Verzameling van gedichten).",
            "Fihi ma fihi (In hem is wat in hem is, toespraken).",
        ],
        "uitspraken": [
            "De wonde is de plek waar het licht naar binnen komt.",
            "Je bent niet een druppel in de oceaan; je bent de hele oceaan in een druppel.",
            "Verkoop je verstand en koop verwondering.",
            "Waar je ook bent, en wat je ook doet, wees verliefd.",
        ],
        "visie": (
            "Rumi is de beroemdste dichter van het soefisme. "
            "Hij was een Perzische geleerde en mysticus die na een ontmoeting met de zwervende derwisj Shams "
            "een radicale transformatie onderging. "
            "Hij veranderde van een gerespecteerde professor in een dansende, dichtende minnaar van God. "
            "Zijn gedichten gaan over liefde, verlangen, eenwording en de pijn van de scheiding. "
            "De mens is een druppel die verlangt naar de oceaan; het verlangen zelf is de weg. "
            "Rumi's taal is hartstochtelijk, beeldend en universeel. "
            "Zijn Masnavi wordt wel de Koran in het Perzisch genoemd. "
            "Hij stichtte de Mevlevi-orde, de dansende derwisjen, "
            "die met hun draaiende beweging de kosmische orde nabootsen. "
            "Zijn werk is nog steeds een van de meest gelezen dichtwerken ter wereld."
        ),
    },

    "ibn_arabi": {
        "naam": "Ibn Arabi",
        "leefde": "1165–1240",
        "stroming": "Soefisme / Metafysica",
        "boeken": [
            "Fusus al-Hikam (De ringen van wijsheid).",
            "Al-Futuhat al-Makkiyya (De Mekkaanse openbaringen).",
            "Tarjuman al-Ashwaq (De vertolker van de verlangens).",
        ],
        "uitspraken": [
            "Het zijn is één, en alle dingen zijn verschijningen van het Ene.",
            "Mijn hart is een klooster, een synagoge, een tempel en een moskee.",
            "Ik volg de religie van de liefde, waarheen haar karavaan ook trekt.",
            "God is niet te bevatten, maar wel te ervaren.",
        ],
        "visie": (
            "Ibn Arabi is een van de diepste en meest controversiële mystici van de islam. "
            "Hij wordt de grootste meester genoemd. "
            "Zijn kernidee is wahdat al-wujud: de eenheid van het zijn. "
            "Alles wat bestaat is een verschijning van het goddelijke. "
            "God openbaart zich in oneindig veel vormen, en de mens is de spiegel waarin God zichzelf ziet. "
            "Ibn Arabi reisde door Spanje, Noord-Afrika en het Midden-Oosten, en ontmoette vele mystici. "
            "Zijn werk is poëtisch, filosofisch en uiterst complex. "
            "Hij benadrukte tolerantie: het hart van de mysticus is open voor alle vormen van geloof. "
            "Zijn invloed op het soefisme, de islamitische filosofie en de westerse mystiek is groot."
        ),
    },
    "hypatia": {
        "naam": "Hypatia van Alexandrië",
        "leefde": "ca. 350–415 n.Chr.",
        "stroming": "Neoplatonisme / Alexandrijnse school",
        "boeken": [
            "Hypatia heeft zelf geen werken nagelaten.",
            "Ze schreef commentaren op Diophantus' Arithmetica, Apollonius' Conica en Ptolemaeus' Almagest.",
            "Haar werk is vooral bekend via brieven van haar leerling Synesius van Cyrene.",
        ],
        "uitspraken": [
            "De waarheid is geen bezit, maar een weg.",
            "Onderwijs is de hoogste vorm van dienstbaarheid.",
            "De rede is het licht dat de ziel naar huis leidt.",
        ],
        "visie": (
            "Hypatia was een van de eerste vrouwen in de westerse geschiedenis "
            "die bekend staat als wiskundige, astronoom en filosoof. "
            "Ze leefde in Alexandrië, in een tijd van politieke en religieuze spanningen. "
            "Ze was een neoplatonist: ze geloofde dat de werkelijkheid een hiërarchie is "
            "die opstijgt van het zichtbare naar het goddelijke Ene. "
            "Wiskunde en astronomie waren voor haar geen droge vakken, maar middelen "
            "om de ziel te zuiveren en op te stijgen naar het hogere. "
            "Ze gaf les aan leerlingen van alle gezindten: heidenen, joden en christenen. "
            "In 415 werd ze vermoord door een christelijke menigte, "
            "mogelijk uit politieke motieven. Haar dood wordt vaak gezien als het einde "
            "van de klassieke filosofie in Alexandrië. "
            "Ze is een symbool geworden van de vrije geest en de vrouw in de wetenschap."
        ),
    },

    "christine_de_pizan": {
        "naam": "Christine de Pizan",
        "leefde": "1364–1430",
        "stroming": "Middeleeuwen / Vroeg-feminisme",
        "boeken": [
            "Le Livre de la Cité des Dames (Het boek van de stad der dames, 1405).",
            "Le Livre des Trois Vertus (Het boek van de drie deugden, 1405).",
            "L'Épître au Dieu d'Amour (Brief aan de god van de liefde, 1399).",
            "Le Dit de la Rose (1399).",
        ],
        "uitspraken": [
            "Ik ben een vrouw, en ik durf te spreken.",
            "De vrouw is niet van nature zwak; ze wordt zwak gemaakt door opvoeding.",
            "De stad der dames is gebouwd door de rede, rechtschapenheid en rechtvaardigheid.",
        ],
        "visie": (
            "Christine de Pizan was de eerste professionele schrijfster van Europa. "
            "Na de dood van haar man moest ze haar gezin onderhouden met haar pen, "
            "en dat deed ze met succes. "
            "In Le Livre de la Cité des Dames bouwt ze een allegorische stad "
            "waarin vrouwen uit de geschiedenis en de mythologie een plaats krijgen. "
            "Ze verdedigt de waarde van vrouwen tegen de middeleeuwse vrouwenhaat. "
            "Volgens Christine is het niet de natuur die vrouwen zwak maakt, "
            "maar het gebrek aan onderwijs en de beperkingen die mannen hen opleggen. "
            "Ze was een gelovige christen, maar ook een scherp criticus van onrecht. "
            "Haar werk is een van de vroegste feministische teksten uit de Europese geschiedenis."
        ),
    },

    "simone_de_beauvoir": {
        "naam": "Simone de Beauvoir",
        "leefde": "1908–1986",
        "stroming": "Existentialisme / Feminisme",
        "boeken": [
            "Le Deuxième Sexe (De tweede sekse, 1949).",
            "L'Invitée (De gast, 1943).",
            "Les Mandarins (De mandarijnen, 1954).",
            "Mémoires d'une jeune fille rangée (Herinneringen van een welopgevoed meisje, 1958).",
            "La Vieillesse (De ouderdom, 1970).",
        ],
        "uitspraken": [
            "Je bent niet geboren als vrouw, je wordt het.",
            "Vrijheid is geen gave, maar een taak.",
            "De onderdrukking van de vrouw is geen natuurverschijnsel, maar een cultuurproduct.",
            "Ik wil niet dat mijn leven zin heeft; ik wil dat het waar is.",
        ],
        "visie": (
            "Simone de Beauvoir is de moeder van het moderne feminisme. "
            "In De tweede sekse onderzoekt ze hoe de vrouw door de geschiedenis heen "
            "als de Ander is behandeld: als afwijking van de norm, terwijl de man de norm is. "
            "Haar beroemdste zin: je bent niet geboren als vrouw, je wordt het. "
            "Vrouwelijkheid is geen biologische bestemming, maar een rol die je wordt opgelegd. "
            "Ze was een existentialist: vrijheid is de kern van het bestaan, "
            "maar vrijheid is altijd gesitueerd – je kunt niet kiezen onder welke omstandigheden je leeft. "
            "Samen met Sartre vormde ze een intellectueel paar dat decennialang het Franse denken domineerde. "
            "Ze schreef ook over ouderdom, dood en de verantwoordelijkheid van de intellectueel. "
            "Haar invloed op het feminisme, de filosofie en de literatuur is enorm."
        ),
    },

    "simone_weil": {
        "naam": "Simone Weil",
        "leefde": "1909–1943",
        "stroming": "Mystiek / Christelijke filosofie",
        "boeken": [
            "La Pesanteur et la Grâce (Zwaarte en genade, postuum 1947).",
            "L'Enracinement (De wortels van de ziel, postuum 1949).",
            "Attente de Dieu (Wachten op God, postuum 1950).",
            "Cahiers (Notitieboeken, postuum).",
        ],
        "uitspraken": [
            "Aandacht is de zeldzaamste en zuiverste vorm van vrijgevigheid.",
            "Wie lijdt, heeft geen troost nodig, maar waarheid.",
            "God bestaat niet in de wereld, maar in de leegte die de wereld achterlaat.",
            "De liefde is de enige werkelijkheid die niet wordt beïnvloed door de dood.",
        ],
        "visie": (
            "Simone Weil was een filosoof, mysticus en activist. "
            "Ze werkte als fabrieksarbeider om het lijden van de arbeiders te begrijpen, "
            "vocht in de Spaanse Burgeroorlog, en vluchtte voor de nazi's. "
            "Ze stierf jong, op 34-jarige leeftijd, aan tuberculose en uitputting, "
            "omdat ze weigerde meer te eten dan de mensen in bezet Frankrijk. "
            "Haar filosofie draait om aandacht: de gave om echt te kijken naar wat lijdt, "
            "zonder te oordelen of te troosten. "
            "Ze geloofde dat God zich terugtrekt uit de wereld, en dat de mens in die leegte moet staan. "
            "Lijden is geen straf, maar een weg naar waarheid. "
            "Ze was diep religieus, maar weigerde zich te laten dopen. "
            "Haar werk is fragmentarisch, intens en ongemakkelijk. "
            "Ze is een van de meest raadselachtige en bewonderde denkers van de twintigste eeuw."
        ),
    },

    "iris_murdoch": {
        "naam": "Iris Murdoch",
        "leefde": "1919–1999",
        "stroming": "Moraalfilosofie / Platonisme",
        "boeken": [
            "The Sovereignty of Good (De soevereiniteit van het goede, 1970).",
            "The Nice and the Good (Het aardige en het goede, 1968).",
            "The Sea, The Sea (De zee, de zee, 1978).",
            "Metaphysics as a Guide to Morals (Metafysica als gids voor de moraal, 1992).",
        ],
        "uitspraken": [
            "Het goede is de werkelijkheid waarnaar we moeten kijken.",
            "Liefde is de moeilijkste en meest noodzakelijke vorm van aandacht.",
            "De mens is een wezen dat zichzelf voortdurend verliest in fantasieën.",
            "Ware vrijheid is het vermogen om de werkelijkheid onder ogen te zien.",
        ],
        "visie": (
            "Iris Murdoch was filosofe én romanschrijfster. "
            "Ze combineerde een streng academische carrière in Oxford met een enorme literaire productie. "
            "Haar filosofie draait om het goede: het vermogen om de werkelijkheid te zien zoals ze is, "
            "zonder je te laten misleiden door je eigen fantasieën en ego. "
            "Geïnspireerd door Plato gelooft ze dat het goede een transcendent ideaal is "
            "waarnaar we moeten streven, ook al bereiken we het nooit. "
            "Liefde is voor haar een vorm van aandacht: de bereidheid om de ander echt te zien, "
            "niet als verlengstuk van jezelf. "
            "Ze was een tegenstander van moreel relativisme en existentialistisch subjectivisme. "
            "Haar romans zijn filosofisch, psychologisch en vaak geestig. "
            "Ze is een van de belangrijkste morele filosofen van de twintigste eeuw."
        ),
    },

    "heidegger": {
        "naam": "Martin Heidegger",
        "leefde": "1889–1976",
        "stroming": "Fenomenologie / Fundamentele ontologie",
        "boeken": [
            "Sein und Zeit (Zijn en tijd, 1927).",
            "Was ist Metaphysik? (Wat is metafysica?, 1929).",
            "Die Frage nach dem Ding (De vraag naar het ding, 1962).",
            "Holzwege (Bospaden, 1950).",
            "Brief über den Humanismus (Brief over het humanisme, 1947).",
        ],
        "uitspraken": [
            "De taal is het huis van het zijn.",
            "Wij zijn geworpen in het bestaan, zonder dat we ervoor gekozen hebben.",
            "De techniek is geen gevaar, maar het gevaar is de techniek.",
            "Het niets is de sluier van het zijn.",
            "Angst openbaart ons het niets.",
        ],
        "visie": (
            "Heidegger is een van de meest invloedrijke en omstreden filosofen van de twintigste eeuw. "
            "Zijn hoofdwerk Zijn en tijd begint bij de vraag naar het zijn: "
            "wat betekent het om te bestaan? "
            "De mens is voor Heidegger geen ding onder dingen, maar een wezen dat zich verhoudt tot zijn bestaan. "
            "Hij is geworpen in de wereld, leeft in de tijd, en wordt uiteindelijk geconfronteerd met de dood. "
            "Dat besef van sterfelijkheid maakt het leven pas echt. "
            "In zijn latere werk draait hij zich naar de taal en de techniek. "
            "De taal is niet een instrument dat we gebruiken, maar de ruimte waarin het zijn zich openbaart. "
            "De techniek dreigt de mens te reduceren tot een hulpbron, een bestand. "
            "Heidegger was lid van de nazi-partij en heeft zich na de oorlog nooit echt verontschuldigd. "
            "Zijn werk blijft invloedrijk, maar ook beladen."
        ),
    },

    "wittgenstein": {
        "naam": "Ludwig Wittgenstein",
        "leefde": "1889–1951",
        "stroming": "Analytische filosofie / Taalfilosofie",
        "boeken": [
            "Tractatus Logico-Philosophicus (1921).",
            "Philosophische Untersuchungen (Filosofische onderzoekingen, postuum 1953).",
            "Über Gewißheit (Over zekerheid, postuum 1969).",
            "Bemerkungen über die Grundlagen der Mathematik (Opmerkingen over de grondslagen van de wiskunde, postuum).",
        ],
        "uitspraken": [
            "De grenzen van mijn taal betekenen de grenzen van mijn wereld.",
            "Waarover men niet kan spreken, daarover moet men zwijgen.",
            "De betekenis van een woord is het gebruik ervan in de taal.",
            "Filosofie is geen theorie, maar een activiteit.",
            "Als een leeuw kon spreken, zouden we hem niet kunnen begrijpen.",
        ],
        "visie": (
            "Wittgenstein is een van de meest raadselachtige denkers van de twintigste eeuw. "
            "Zijn werk valt in twee periodes. "
            "In de Tractatus probeert hij de taal te zuiveren zodat ze de wereld logisch weerspiegelt. "
            "Alles wat niet helder gezegd kan worden – ethiek, esthetiek, religie – moet worden verzwegen. "
            "Daarna trok hij zich terug in Oostenrijk, werkte als tuinman en leraar, "
            "en kwam terug met een heel ander idee. "
            "In de Filosofische onderzoekingen is taal geen logisch systeem, maar een verzameling spelen. "
            "Betekenis ligt niet in verwijzing, maar in gebruik. "
            "Filosofie moet geen theorieën bouwen, maar verwarring wegnemen. "
            "Wittgenstein leefde ascetisch, was veeleisend voor zichzelf en anderen, "
            "en stierf aan kanker met de woorden: Zeg ze dat mijn leven prachtig was."
        ),
    },

    "sartre": {
        "naam": "Jean-Paul Sartre",
        "leefde": "1905–1980",
        "stroming": "Existentialisme / Fenomenologie",
        "boeken": [
            "L'Être et le Néant (Het zijn en het niet, 1943).",
            "L'Existentialisme est un humanisme (Het existentialisme is een humanisme, 1946).",
            "La Nausée (De walging, 1938).",
            "Huis clos (Gesloten deuren, 1944).",
            "Les Mots (De woorden, 1964).",
        ],
        "uitspraken": [
            "De mens is veroordeeld tot vrijheid.",
            "Het bestaan gaat vooraf aan de essentie.",
            "De hel, dat zijn de anderen.",
            "Als je niet vrij bent, is dat je eigen keuze.",
            "We zijn onze keuzes.",
        ],
        "visie": (
            "Sartre is de bekendste existentialist van de twintigste eeuw. "
            "Zijn kernidee: de mens heeft geen vooraf gegeven essentie. "
            "Eerst besta je, dan bepaal je wie je bent. "
            "Dat betekent dat je vrij bent, en dus verantwoordelijk voor alles wat je doet. "
            "Je kunt je niet verschuilen achter God, je natuur of je omstandigheden. "
            "Wie doet alsof hij geen keuze heeft, leeft in bad faith – oneerlijkheid tegenover zichzelf. "
            "Sartre was ook een politiek geëngageerd denker: hij steunde het verzet, "
            "bekritiseerde het kolonialisme en het kapitalisme, en weigerde de Nobelprijs voor Literatuur. "
            "Hij schreef romans, toneelstukken en filosofische werken, "
            "en was decennialang een intellectuele beroemdheid in Parijs. "
            "Zijn invloed op het existentialisme, de literatuur en de politiek is enorm."
        ),
    },

    "foucault": {
        "naam": "Michel Foucault",
        "leefde": "1926–1984",
        "stroming": "Poststructuralisme / Machtsanalyse",
        "boeken": [
            "Histoire de la folie à l'âge classique (Geschiedenis van de waanzin, 1961).",
            "Les Mots et les Choses (De woorden en de dingen, 1966).",
            "Surveiller et Punir (Toezicht en straf, 1975).",
            "Histoire de la sexualité (Geschiedenis van de seksualiteit, 1976–1984).",
        ],
        "uitspraken": [
            "Macht is overal, niet omdat ze alles omvat, maar omdat ze overal vandaan komt.",
            "Kennis is geen neutrale weerspiegeling van de werkelijkheid, maar een product van macht.",
            "De ziel is de gevangenis van het lichaam.",
            "Ik schrijf niet om te bevrijden, maar om te laten zien hoe we gevangen zitten.",
        ],
        "visie": (
            "Foucault is een van de meest invloedrijke denkers van de twintigste eeuw. "
            "Hij onderzocht hoe macht werkt in ziekenhuizen, gevangenissen, scholen en seksualiteit. "
            "Macht is voor hem geen ding dat iemand bezit, maar een netwerk van relaties. "
            "Kennis en macht zijn onlosmakelijk verbonden: wat we weten, is wat we als waarheid accepteren, "
            "en dat wordt bepaald door machtsstructuren. "
            "Hij analyseerde de overgang van lijfstraffen naar gevangenisstraf: "
            "niet omdat we humaner zijn geworden, maar omdat macht efficiënter is gaan werken. "
            "In zijn Geschiedenis van de seksualiteit laat hij zien hoe seksualiteit een object van kennis werd, "
            "en hoe de mens zichzelf daardoor leert begrijpen. "
            "Foucault was politiek actief, openly gay, en stierf aan aids in 1984. "
            "Zijn werk beïnvloedt de sociologie, de criminologie, de genderstudies en de filosofie."
        ),
    },

    "derrida": {
        "naam": "Jacques Derrida",
        "leefde": "1930–2004",
        "stroming": "Deconstructie / Poststructuralisme",
        "boeken": [
            "De la grammatologie (Over de grammatologie, 1967).",
            "L'Écriture et la différence (Het schrijven en het verschil, 1967).",
            "La Voix et le Phénomène (De stem en het fenomeen, 1967).",
            "Marges de la philosophie (Marges van de filosofie, 1972).",
            "Spectres de Marx (Spoken van Marx, 1993).",
        ],
        "uitspraken": [
            "Er is niets buiten de tekst.",
            "De betekenis is nooit aanwezig, ze is altijd uitgesteld.",
            "Deconstructie is geen methode, maar een gebeurtenis.",
            "Het gevaar is niet het relativisme, maar het fundamentalisme.",
        ],
        "visie": (
            "Derrida is de vader van de deconstructie. "
            "Hij onderzoekt hoe teksten hun eigen tegenstellingen verbergen. "
            "Elke tekst, zegt hij, bevat sporen van wat hij uitsluit. "
            "Betekenis is nooit vast; ze verschuift voortdurend. "
            "Dat noemt hij différance: het uitstellen van betekenis en het verschil dat betekenis mogelijk maakt. "
            "Hij wantrouwt elke vorm van denken die een centrum, een oorsprong of een absolute waarheid claimt. "
            "Deconstructie is geen methode om teksten te vernietigen, maar om te laten zien "
            "hoe ze werken en wat ze verbergen. "
            "Derrida was een charismatische docent en een productief schrijver. "
            "Zijn werk is moeilijk, speels en provocerend. "
            "Hij beïnvloedde de literatuurwetenschap, de filosofie, de architectuur en de rechtsgeleerdheid. "
            "Zijn invloed op het postmodernisme is enorm."
        ),
    },
     "meister_eckhart": {
        "naam": "Meister Eckhart",
        "leefde": "ca. 1260–1328",
        "stroming": "Rijnlandse mystiek / Dominicaans",
        "boeken": [
            "Predigten (Preken).",
            "Das Buch der göttlichen Tröstung (Het boek van de goddelijke troost, 1318).",
            "Von dem edeln Menschen (Over de edele mens).",
            "Opus tripartitum (onvoltooid).",
        ],
        "uitspraken": [
            "God is niet te vinden in de dingen; God is de grond van de ziel.",
            "Wil je God ontmoeten, laat dan alle beelden los.",
            "De ziel is niet in de wereld; de wereld is in de ziel.",
            "Ik bid God dat Hij mij bevrijdt van God.",
            "Het oog waarmee ik God zie, is hetzelfde oog waarmee God mij ziet.",
        ],
        "visie": (
            "Meister Eckhart is de grootste Duitse mysticus van de middeleeuwen. "
            "Hij was een Dominicaanse monnik, theoloog en prediker. "
            "Zijn preken waren zo radicaal dat hij na zijn dood door de paus werd veroordeeld. "
            "Eckharts kernidee: God is niet een wezen naast andere wezens, maar de grond van alles. "
            "De ziel heeft een vonk die direct verwant is aan God. "
            "Om God te vinden, moet je alle beelden en begrippen loslaten – zelfs het begrip God. "
            "Dat is het loslaten (Abgeschiedenheit) waar hij steeds op wijst. "
            "Eckhart spreekt in paradoxen: God en mens zijn één, en toch blijft er verschil. "
            "Hij was geen pantheïst, maar zijn taal balanceerde op het randje. "
            "Zijn werk beïnvloedde de Reformatie, het Duitse idealisme en de moderne spiritualiteit. "
            "Hij is een van de diepste denkers van de christelijke traditie."
        ),
    },

    "teresa_van_avila": {
        "naam": "Teresa van Ávila",
        "leefde": "1515–1582",
        "stroming": "Spaanse mystiek / Karmel",
        "boeken": [
            "El Libro de la Vida (Het boek van mijn leven, 1565).",
            "Camino de perfección (De weg naar volmaaktheid, 1566).",
            "El Castillo Interior (Het innerlijk kasteel, 1577).",
            "Conceptos del amor de Dios (Overwegingen over de liefde van God).",
        ],
        "uitspraken": [
            "Laat niets je verontrusten, niets je bang maken; alles gaat voorbij.",
            "Het gebed is een gesprek met iemand die van je houdt.",
            "De ziel is een kasteel met vele vertrekken.",
            "Wie God zoekt in het gebed, vindt Hem ook in de keuken.",
        ],
        "visie": (
            "Teresa van Ávila is een van de grootste mystici van de katholieke traditie. "
            "Ze hervormde de Karmelorde, stichtte tientallen kloosters, en schreef boeken "
            "die nog steeds worden gelezen. "
            "Haar beroemdste werk, Het innerlijk kasteel, beschrijft de ziel als een kasteel "
            "met zeven vertrekken, waarin de ziel steeds dieper doordringt tot de eenwording met God. "
            "Teresa combineert mystieke diepgang met nuchterheid en humor. "
            "Ze wantrouwt overdreven emotionaliteit en nadruk op visioenen. "
            "Het gaat om liefde die zich uit in daden, niet in gevoelens. "
            "Ze was een vrouw in een door mannen gedomineerde kerk, "
            "en ze moest voortdurend vechten voor haar ruimte. "
            "In 1970 werd ze de eerste vrouwelijke kerkleraar. "
            "Haar werk is warm, persoonlijk en verrassend toegankelijk."
        ),
    },

    "johannes_van_het_kruis": {
        "naam": "Johannes van het Kruis",
        "leefde": "1542–1591",
        "stroming": "Spaanse mystiek / Karmel",
        "boeken": [
            "Noche oscura del alma (De donkere nacht van de ziel).",
            "Cántico espiritual (Geestelijk lied).",
            "Llama de amor viva (Levende vlam van liefde).",
            "Subida del Monte Carmelo (Beklimming van de berg Karmel).",
        ],
        "uitspraken": [
            "Om te komen tot wat je niet kent, moet je gaan door wat je niet kent.",
            "De ziel die God zoekt, moet alles loslaten.",
            "De donkere nacht is geen straf, maar een genezing.",
        ],
        "visie": (
            "Johannes van het Kruis was de medewerker van Teresa van Ávila "
            "en een van de grootste dichters van de Spaanse taal. "
            "Zijn beroemdste werk, De donkere nacht van de ziel, beschrijft de weg naar God "
            "als een nacht waarin alles wat vertrouwd is wegvalt. "
            "Het is geen pessimisme, maar een zuivering: "
            "alles wat de ziel aan God wil vasthouden, moet worden losgelaten, "
            "zodat God zich kan openbaren zonder tussenkomst van beelden. "
            "Johannes geloofde dat lijden en duisternis noodzakelijke stappen zijn op de weg naar eenheid. "
            "Zijn poëzie is adembenemend mooi, zijn proza is streng en precies. "
            "Hij werd gevangengezet door zijn eigen orde, maar bleef schrijven. "
            "Zijn werk beïnvloedt nog steeds de mystiek, de literatuur en de theologie."
        ),
    },

    "jakob_bohme": {
        "naam": "Jakob Böhme",
        "leefde": "1575–1624",
        "stroming": "Duitse mystiek / Theosofie",
        "boeken": [
            "Aurora (Morgenröte im Aufgang, 1612).",
            "De signatura rerum (De tekens der dingen, 1621).",
            "Mysterium magnum (Het grote mysterie, 1623).",
            "Der Weg zu Christo (De weg naar Christus, 1624).",
        ],
        "uitspraken": [
            "Het licht schijnt in de duisternis, en de duisternis heeft het niet begrepen.",
            "Alle dingen zijn een spiegel van God.",
            "Zonder tegenstelling geen leven.",
            "De ziel is een vonk van het goddelijke vuur.",
        ],
        "visie": (
            "Jakob Böhme was een schoenmaker uit Görlitz die een van de meest invloedrijke mystici "
            "van de Duitse traditie werd. "
            "Na een reeks visioenen begon hij te schrijven over God, de schepping en de mens. "
            "Zijn kernidee: God is geen statische eenheid, maar een levend proces "
            "van spanning en verzoening. "
            "In God zelf zit een duistere grond, een oervil die zich verlangt naar het licht. "
            "De schepping is het toneel waarin die spanning zich ontvouwt. "
            "De mens is een microkosmos: in hem weerspiegelt zich het hele drama van God en wereld. "
            "Böhme was geen academicus; zijn taal is beeldend, barok en soms duister. "
            "Hij werd verboden te schrijven, maar deed het toch. "
            "Zijn werk beïnvloedde het Duitse idealisme (Hegel, Schelling), "
            "de romantiek, en de theosofie van de negentiende eeuw."
        ),
    },

    "hildegard_van_bingen": {
        "naam": "Hildegard van Bingen",
        "leefde": "1098–1179",
        "stroming": "Middeleeuwse mystiek / Benedictijns",
        "boeken": [
            "Scivias (Ken de wegen, 1151).",
            "Liber vitae meritorum (Boek van de verdiensten van het leven, 1158).",
            "Liber divinorum operum (Boek van de goddelijke werken, 1173).",
            "Physica (Natuurkunde).",
            "Causae et Curae (Oorzaken en genezingen).",
        ],
        "uitspraken": [
            "De kosmos is een levend geheel, doordrongen van goddelijke kracht.",
            "De mens is een microkosmos, een spiegel van het universum.",
            "Groen is de kleur van de levenskracht.",
            "God heeft de wereld niet verlaten; Hij is erin aanwezig als kracht.",
        ],
        "visie": (
            "Hildegard van Bingen was een van de meest veelzijdige vrouwen van de middeleeuwen: "
            "mystica, componiste, genezeres, schrijfster en abdis. "
            "Op jonge leeftijd kreeg ze visioenen, die ze pas later durfde op te schrijven. "
            "In Scivias beschrijft ze de kosmos als een levend geheel, "
            "doordrongen van goddelijke kracht, die ze viriditas noemt: groenkracht, levenskracht. "
            "Alles hangt samen: de mens, de natuur, de engelen, God. "
            "Hildegard schreef ook over geneeskunde, planten en stenen, "
            "en componeerde prachtige muziek die nog steeds wordt uitgevoerd. "
            "Ze was geen kluizenaarster: ze reisde, preekte en correspondeerde met pausen en keizers. "
            "Haar werk is een van de rijkste getuigenissen van de middeleeuwse spiritualiteit. "
            "In 2012 werd ze uitgeroepen tot kerkleraar."
        ),
    },

    "ibn_khaldun": {
        "naam": "Ibn Khaldun",
        "leefde": "1332–1406",
        "stroming": "Islamitische geschiedfilosofie / Sociologie",
        "boeken": [
            "Muqaddimah (De inleiding, 1377).",
            "Kitab al-'Ibar (Het boek van de lessen, 7 delen).",
            "Al-Ta'rif (Autobiografie).",
        ],
        "uitspraken": [
            "De geschiedenis is een aaneenschakeling van cycli.",
            "Beschavingen worden geboren in de woestijn en sterven in de stad.",
            "Groepsgevoel ('asabiyya) is de motor van de geschiedenis.",
            "Wie het verleden niet kent, begrijpt het heden niet.",
        ],
        "visie": (
            "Ibn Khaldun is een van de eerste denkers die de geschiedenis als wetenschap benaderde. "
            "In zijn Muqaddimah onderzoekt hij de wetmatigheden achter de opkomst en ondergang van beschavingen. "
            "Zijn kernbegrip is 'asabiyya: groepsgevoel, solidariteit, de band die een groep bijeenhoudt. "
            "Nomadische volkeren hebben sterke 'asabiyya; ze veroveren steden, stichten dynastieën, "
            "maar raken na generaties verweekt en verliezen hun kracht. "
            "Dan komen nieuwe nomaden, en de cyclus begint opnieuw. "
            "Ibn Khaldun was ook een politicus en diplomaat, en zijn autobiografie is een van de vroegste "
            "persoonlijke geschriften uit de islamitische wereld. "
            "Hij wordt beschouwd als de vader van de sociologie en de geschiedfilosofie. "
            "Zijn werk beïnvloedt nog steeds historici en sociale wetenschappers."
        ),
    },

    "avicenna": {
        "naam": "Avicenna (Ibn Sina)",
        "leefde": "980–1037",
        "stroming": "Islamitische filosofie / Peripatetisch",
        "boeken": [
            "Kitab al-Shifa (Het boek van de genezing, een filosofische encyclopedie).",
            "Al-Qanun fi al-Tibb (De canon van de geneeskunde, 1025).",
            "Al-Isharat wa'l-Tanbihat (Aanwijzingen en opmerkingen).",
            "Kitab al-Najat (Het boek van de verlossing).",
        ],
        "uitspraken": [
            "Het zijn is wat we het eerst kennen, nog vóór het denken.",
            "De ziel is niet het lichaam, maar heeft het lichaam nodig.",
            "God is het noodzakelijke zijn; al het andere is mogelijk.",
            "Wie zichzelf kent, kent zijn Heer.",
        ],
        "visie": (
            "Avicenna is een van de grootste filosofen van de islamitische wereld, "
            "en een van de meest invloedrijke denkers van de middeleeuwen. "
            "Hij was arts, filosoof, wiskundige en astronoom. "
            "Zijn Canon van de geneeskunde bleef eeuwenlang het standaardwerk in Europa. "
            "Filosofisch bouwde hij voort op Aristoteles, maar voegde er een neoplatoons element aan toe. "
            "Zijn kernidee: God is het enige noodzakelijke wezen; al het andere is mogelijk "
            "en bestaat dankzij God. "
            "Hij ontwikkelde een beroemd gedachte-experiment: de zwevende mens. "
            "Stel je voor dat je zweeft in de leegte, zonder lichaam, zonder zintuigen. "
            "Je zou nog steeds weten dat je bestaat. "
            "Dus de ziel is geen lichaam, maar heeft een eigen bestaan. "
            "Avicenna's werk beïnvloedde Thomas Aquinas, Duns Scotus en de hele scholastiek."
        ),
    },

    "al_ghazali": {
        "naam": "Al-Ghazali",
        "leefde": "1058–1111",
        "stroming": "Islamitische filosofie / Soefisme",
        "boeken": [
            "Ihya' 'Ulum al-Din (De heropleving van de religieuze wetenschappen).",
            "Tahafut al-Falasifa (De weerlegging van de filosofen, 1095).",
            "Al-Munqidh min al-Dalal (De bevrijder van dwaling).",
            "Mishkat al-Anwar (De nis van de lichten).",
        ],
        "uitspraken": [
            "Twijfel is het begin van zekerheid.",
            "Wie God zoekt zonder de wereld los te laten, zoekt een schaduw.",
            "Kennis zonder liefde is een last.",
            "De ziel is een spiegel waarin God zich weerspiegelt.",
        ],
        "visie": (
            "Al-Ghazali is een van de invloedrijkste denkers van de islam. "
            "Hij was een briljant jurist en theoloog, maar raakte in een diepe crisis: "
            "hij begon te twijfelen aan alles, aan zijn kennis, aan zijn geloof, aan zijn succes. "
            "Hij verliet zijn positie in Bagdad, werd een zwervende soefi, "
            "en kwam terug met een nieuwe overtuiging: "
            "de rede kan God niet bewijzen, maar de innerlijke ervaring wel. "
            "In zijn boek De weerlegging van de filosofen bekritiseert hij Avicenna en de rationalisten. "
            "Filosofie kan veel, maar niet de hoogste waarheid bereiken. "
            "Daarna schreef hij zijn grote werk over de religieuze wetenschappen, "
            "waarin hij geloof, rede en mystiek verenigt. "
            "Al-Ghazali wordt wel de grootste moslim na Mohammed genoemd. "
            "Zijn invloed op het soefisme en de islamitische theologie is enorm."
        ),
    },

    "zhu_xi": {
        "naam": "Zhu Xi",
        "leefde": "1130–1200",
        "stroming": "Neo-confucianisme",
        "boeken": [
            "Sishu Jizhu (Commentaar op de Vier Boeken).",
            "Jinsilu (Overwegingen over de dingen bij de hand).",
            "Zhuzi Yulei (Gesprekken van meester Zhu, verzameld door leerlingen).",
        ],
        "uitspraken": [
            "De rede (li) is in alles aanwezig, van de grootste sterren tot het kleinste grassprietje.",
            "Onderzoek de dingen, en je zult de rede vinden.",
            "De mens moet zijn hart zuiveren en zijn verlangens matigen.",
            "Leren zonder denken is leeg; denken zonder leren is gevaarlijk.",
        ],
        "visie": (
            "Zhu Xi is de grote systematicus van het neo-confucianisme. "
            "Hij bracht de leer van Confucius, Mencius en hun volgelingen in een samenhangend systeem. "
            "Zijn kernbegrip is li: de rede, het patroon dat in alle dingen aanwezig is. "
            "Alles heeft een li, van de kosmos tot een grasspriet. "
            "De taak van de mens is om die patronen te onderzoeken en te begrijpen. "
            "Daarnaast is er qi: de materiële kracht die vorm geeft aan de dingen. "
            "Zhu Xi geloofde in de kracht van onderwijs en zelfcultivering. "
            "Zijn commentaren op de Vier Boeken werden eeuwenlang de basis van het Chinese schoolsysteem. "
            "Zijn invloed op het Chinese, Koreaanse, Japanse en Vietnamese denken is enorm. "
            "Hij is een van de belangrijkste denkers van de premoderne wereld."
        ),
    },

    "wang_yangming": {
        "naam": "Wang Yangming",
        "leefde": "1472–1529",
        "stroming": "Neo-confucianisme / Hart-en-geest",
        "boeken": [
            "Chuanxi Lu (Instructies voor het praktische leven).",
            "Daxue Wen (Vragen over de Grote Leer).",
            "Wenlu (Verzameld werk).",
        ],
        "uitspraken": [
            "Kennen en handelen zijn één.",
            "De waarheid is niet buiten je, ze is in je hart.",
            "Wie zijn geweten volgt, kent de weg.",
            "Het goede doen is de kern van alle kennis.",
        ],
        "visie": (
            "Wang Yangming is de grote rivaal van Zhu Xi binnen het neo-confucianisme. "
            "Waar Zhu Xi de nadruk legt op het onderzoeken van de buitenwereld, "
            "legt Wang de nadruk op het innerlijk: het hart is de bron van alle wijsheid. "
            "Zijn kernidee: kennen en handelen zijn één. "
            "Je kunt niet echt weten wat goed is zonder het ook te doen. "
            "Wie weet dat hij moet helpen, maar het niet doet, weet het niet echt. "
            "Hij ontwikkelde het begrip liangzhi: het aangeboren morele bewustzijn, het geweten. "
            "De taak van het leven is om dat geweten te zuiveren en ernaar te handelen. "
            "Wang was ook een militair en politicus die zijn ideeën in de praktijk bracht. "
            "Zijn leer beïnvloedde Japan, Korea en het moderne Chinese denken."
        ),
    },
    "francis_bacon": {
        "naam": "Francis Bacon",
        "leefde": "1561–1626",
        "stroming": "Empirisme / Wetenschapsfilosofie",
        "boeken": [
            "Novum Organum (Nieuw instrument, 1620).",
            "The Advancement of Learning (De vooruitgang van de wetenschap, 1605).",
            "Essays (1597).",
            "New Atlantis (Nieuwe Atlantis, 1627).",
        ],
        "uitspraken": [
            "Kennis is macht.",
            "De natuur kan alleen worden overwonnen door haar te gehoorzamen.",
            "De mens is de dienaar en tolk van de natuur.",
            "Er zijn idolen van de geest die ons verhinderen de waarheid te zien.",
        ],
        "visie": (
            "Francis Bacon is de vader van het empirisme en de moderne wetenschapsfilosofie. "
            "Hij verzette zich tegen de middeleeuwse methode van eindeloos redeneren zonder observatie. "
            "Zijn kernidee: kennis moet voortkomen uit ervaring en experiment. "
            "We moeten de natuur ondervragen, niet alleen over haar denken. "
            "In Novum Organum beschrijft hij de idolen: vooroordelen en denkfouten die ons belemmeren. "
            "Er zijn idolen van de stam (menselijke beperkingen), de grot (persoonlijke voorkeuren), "
            "de markt (taalverwarring) en het theater (filosofische systemen). "
            "Bacon geloofde dat wetenschap de mensheid vooruit kon helpen. "
            "Hij was ook politicus en schrijver, en zijn essays zijn nog steeds lezenswaardig. "
            "Zijn werk legde de basis voor de moderne wetenschappelijke methode."
        ),
    },

    "david_hume": {
        "naam": "David Hume",
        "leefde": "1711–1776",
        "stroming": "Empirisme / Scepticisme",
        "boeken": [
            "A Treatise of Human Nature (Verhandeling over de menselijke natuur, 1739–1740).",
            "An Enquiry Concerning Human Understanding (Onderzoek naar het menselijk verstand, 1748).",
            "An Enquiry Concerning the Principles of Morals (Onderzoek naar de beginselen van de moraal, 1751).",
            "Dialogues Concerning Natural Religion (Dialogen over de natuurlijke godsdienst, 1779).",
        ],
        "uitspraken": [
            "De rede is en moet de slaaf van de hartstochten zijn.",
            "Gewoonte is de grote gids van het menselijk leven.",
            "We kunnen niet verder kijken dan onze ervaring reikt.",
            "Oorzakelijkheid is geen eigenschap van de dingen, maar een gewoonte van de geest.",
        ],
        "visie": (
            "David Hume is een van de scherpste sceptici uit de westerse filosofie. "
            "Hij dreef het empirisme van Locke en Berkeley tot het uiterste. "
            "Zijn kernidee: alle kennis komt voort uit ervaring. "
            "Maar ervaring geeft ons alleen indrukken en ideeën, geen noodzakelijke verbanden. "
            "Als we zeggen dat de zon morgen weer opkomt, baseren we dat niet op logica, maar op gewoonte. "
            "Oorzakelijkheid is geen band in de werkelijkheid, maar een verwachting in onze geest. "
            "Hume was ook een morele filosoof: moraal komt niet voort uit de rede, maar uit gevoel. "
            "De rede kan ons vertellen wat het geval is, maar niet wat we moeten doen. "
            "Zijn werk wekte Kant uit zijn dogmatische sluimer, zoals Kant zelf zei. "
            "Hume was ook een scherp criticus van het geloof in wonderen en een vroege democraat."
        ),
    },

    "voltaire": {
        "naam": "Voltaire (François-Marie Arouet)",
        "leefde": "1694–1778",
        "stroming": "Verlichting / Satire",
        "boeken": [
            "Candide (1759).",
            "Lettres philosophiques (Filosofische brieven, 1734).",
            "Dictionnaire philosophique (Filosofisch woordenboek, 1764).",
            "Zadig (1747).",
            "Traité sur la tolérance (Verhandeling over de verdraagzaamheid, 1763).",
        ],
        "uitspraken": [
            "Ik mag het niet met je eens zijn, maar ik zal je recht om het te zeggen tot de dood verdedigen.",
            "God heeft de mens geschapen naar Zijn beeld, en de mens heeft Hem terugbetaald met gelijke munt.",
            "De mens is vrij geboren, en overal ligt hij in ketenen.",
            "Twijfel is geen aangename toestand, maar zekerheid is belachelijk.",
            "We moeten onze tuin bewerken.",
        ],
        "visie": (
            "Voltaire is de belichaming van de Franse Verlichting. "
            "Hij was schrijver, filosoof, historicus en polemist. "
            "Hij streed tegen onverdraagzaamheid, bijgeloof en misbruik van macht. "
            "Zijn wapen was de satire: met scherpe pen hekelde hij de kerk, de adel en de domheid. "
            "In Candide bespot hij het optimisme van Leibniz: "
            "de held beleeft de vreselijkste rampen en blijft volhouden dat dit de beste van alle werelden is. "
            "Voltaire geloofde niet in een persoonlijke God, maar wel in een schepper. "
            "Hij was een deïst: God heeft de wereld gemaakt, maar bemoeit zich er niet mee. "
            "Hij werd twee keer gevangengezet en bracht jaren in ballingschap door. "
            "Zijn strijd voor tolerantie en vrije meningsuiting is nog steeds actueel. "
            "Hij stierf kort voor de Franse Revolutie, die zijn ideeën zou voortzetten."
        ),
    },

    "rousseau": {
        "naam": "Jean-Jacques Rousseau",
        "leefde": "1712–1778",
        "stroming": "Romantiek / Verlichting",
        "boeken": [
            "Du contrat social (Het maatschappelijk verdrag, 1762).",
            "Émile, ou De l'éducation (Emile, of Over de opvoeding, 1762).",
            "La Nouvelle Héloïse (Julie, of De nieuwe Héloïse, 1761).",
            "Les Confessions (De bekentenissen, postuum 1782).",
            "Discours sur l'origine de l'inégalité (Verhandeling over de oorsprong van de ongelijkheid, 1755).",
        ],
        "uitspraken": [
            "De mens is vrij geboren, en overal ligt hij in ketenen.",
            "De mens is van nature goed; de samenleving bederft hem.",
            "Terug naar de natuur!",
            "Ik haat degenen die mij dwingen vrij te zijn.",
            "Het hart heeft zijn eigen rede, die de rede niet kent.",
        ],
        "visie": (
            "Rousseau is de grote romanticus van de Verlichting. "
            "Hij verzette zich tegen de rationalistische filosofen van zijn tijd. "
            "Zijn kernidee: de mens is van nature goed, maar wordt bedorven door de samenleving. "
            "In de oorspronkelijke natuurtoestand leefde de mens vrij en gelijk. "
            "Met de komst van eigendom, beschaving en ongelijkheid is hij zijn vrijheid kwijtgeraakt. "
            "In Het maatschappelijk verdrag zoekt hij een uitweg: "
            "een samenleving waarin mensen gehoorzamen aan wetten die ze zelf hebben gemaakt. "
            "Dat is de algemene wil (volonté générale), de wil van het volk als geheel. "
            "Rousseau was ook een pedagoog: in Emile beschrijft hij een opvoeding die aansluit bij de natuur. "
            "Hij was een moeilijk mens, achterdochtig en rusteloos, maar zijn invloed op de politiek, "
            "de opvoeding en de romantiek is enorm. "
            "De Franse Revolutie beriep zich op hem."
        ),
    },

    "christina_van_zweden": {
        "naam": "Koningin Christina van Zweden",
        "leefde": "1626–1689",
        "stroming": "Renaissance-humanisme / Vrijdenken",
        "boeken": [
            "Christina heeft zelf weinig gepubliceerd, maar onderhield een enorme correspondentie.",
            "Haar brieven en aantekeningen zijn verzameld in verschillende edities.",
            "Ze nodigde Descartes uit naar Stockholm, waar hij in 1650 stierf.",
        ],
        "uitspraken": [
            "Ik verkies de vrijheid van de geest boven de macht van de troon.",
            "Kennis is het enige dat de ziel werkelijk bevrijdt.",
            "Ik ben niet bang om alleen te staan in mijn overtuigingen.",
        ],
        "visie": (
            "Koningin Christina van Zweden is een van de meest fascinerende figuren van de zeventiende eeuw. "
            "Ze besteeg de troon op zesjarige leeftijd, regeerde tien jaar, "
            "en deed toen iets ongehoords: ze trad af, verliet Zweden, en bekeerde zich tot het katholicisme. "
            "Ze was een intellectueel in hart en nieren. "
            "Ze correspondeerde met Descartes, Spinoza en andere grote denkers van haar tijd. "
            "Ze verzamelde boeken en manuscripten, en wilde van Stockholm een intellectueel centrum maken. "
            "Haar afstand van de troon was een daad van vrijheid: "
            "ze wilde niet regeren, ze wilde denken. "
            "Ze bracht haar laatste jaren door in Rome, omringd door kunstenaars en geleerden. "
            "Ze is een symbool van intellectuele onafhankelijkheid."
        ),
    },

    "kant": {
        "naam": "Immanuel Kant",
        "leefde": "1724–1804",
        "stroming": "Duits idealisme / Kritische filosofie",
        "boeken": [
            "Kritik der reinen Vernunft (Kritiek van de zuivere rede, 1781).",
            "Kritik der praktischen Vernunft (Kritiek van de praktische rede, 1788).",
            "Kritik der Urteilskraft (Kritiek van het oordeelsvermogen, 1790).",
            "Grundlegung zur Metaphysik der Sitten (Grondslagen van de metafysica van de zeden, 1785).",
            "Zum ewigen Frieden (Over de eeuwige vrede, 1795).",
        ],
        "uitspraken": [
            "Sapere aude! Heb de moed je eigen verstand te gebruiken.",
            "Handel zo dat de maxime van je handeling een algemene wet kan worden.",
            "Behandel de mensheid nooit alleen als middel, maar altijd ook als doel.",
            "Twee dingen vervullen het gemoed met steeds nieuwe bewondering: de sterrenhemel boven mij en de morele wet in mij.",
            "Gedachten zonder inhoud zijn leeg; aanschouwingen zonder begrippen zijn blind.",
        ],
        "visie": (
            "Kant is de centrale figuur van de moderne filosofie. "
            "Hij maakte een copernicaanse wending: niet de werkelijkheid bepaalt ons kennen, "
            "maar ons kennen bepaalt de werkelijkheid zoals wij die ervaren. "
            "De mens heeft aangeboren categorieën (tijd, ruimte, oorzakelijkheid) "
            "waardoor ervaring mogelijk wordt. "
            "Wat buiten die categorieën valt – God, de ziel, het ding op zich – kunnen we niet kennen. "
            "In de ethiek is Kant even radicaal. "
            "Moraal is niet gebaseerd op gevoel of geluk, maar op plicht. "
            "De categorische imperatief: handel alleen volgens die maxime waarvan je kunt willen "
            "dat ze een algemene wet wordt. "
            "Mensen zijn geen middelen, maar doelen op zich. "
            "Kant geloofde in vrijheid, gelijkheid en eeuwige vrede. "
            "Zijn invloed op de filosofie, de politiek en het recht is enorm."
        ),
    },

    "hegel": {
        "naam": "Georg Wilhelm Friedrich Hegel",
        "leefde": "1770–1831",
        "stroming": "Duits idealisme / Dialectiek",
        "boeken": [
            "Phänomenologie des Geistes (Fenomenologie van de geest, 1807).",
            "Wissenschaft der Logik (Wetenschap van de logica, 1812–1816).",
            "Enzyklopädie der philosophischen Wissenschaften (Encyclopedie van de filosofische wetenschappen, 1817).",
            "Grundlinien der Philosophie des Rechts (Grondlijnen van de filosofie van het recht, 1821).",
            "Vorlesungen über die Philosophie der Geschichte (Colleges over de filosofie van de geschiedenis).",
        ],
        "uitspraken": [
            "De geschiedenis is de voortgang van het bewustzijn van vrijheid.",
            "Wat redelijk is, is werkelijk; en wat werkelijk is, is redelijk.",
            "De waarheid is het geheel.",
            "De uil van Minerva vliegt pas uit bij het vallen van de schemering.",
            "De mens leert uit de geschiedenis dat de mens niets uit de geschiedenis leert.",
        ],
        "visie": (
            "Hegel is de laatste grote systeemdenker van het Duitse idealisme. "
            "Zijn kernidee: de werkelijkheid is geen verzameling losse dingen, "
            "maar een proces van zichzelf ontvouwende geest. "
            "Alles beweegt zich dialectisch: these, antithese, synthese. "
            "Tegenstellingen worden opgeheven in een hogere eenheid. "
            "De geschiedenis is de voortgang van het bewustzijn van vrijheid. "
            "Eerst is één mens vrij (de oosterse despoot), dan enkele (de Griekse burger), "
            "uiteindelijk allen (de moderne staat). "
            "Hegel zag de staat niet als onderdrukker, maar als de ruimte waarin vrijheid werkelijk wordt. "
            "Zijn werk is moeilijk, abstract en invloedrijk. "
            "Hij beïnvloedde Marx, Kierkegaard, Sartre, en de hele twintigste-eeuwse filosofie. "
            "Zijn colleges trokken honderden studenten."
        ),
    },

    "popper": {
        "naam": "Karl Popper",
        "leefde": "1902–1994",
        "stroming": "Kritisch rationalisme",
        "boeken": [
            "Logik der Forschung (Logica van de wetenschappelijke ontdekking, 1934).",
            "The Open Society and Its Enemies (De open samenleving en haar vijanden, 1945).",
            "Conjectures and Refutations (Vermoedens en weerleggingen, 1963).",
            "Objective Knowledge (Objectieve kennis, 1972).",
        ],
        "uitspraken": [
            "Een theorie die niet weerlegd kan worden, is geen wetenschap.",
            "We kunnen nooit zeker weten dat we gelijk hebben, alleen dat we ongelijk hadden.",
            "De open samenleving is de samenleving die haar eigen fouten durft te corrigeren.",
            "Ware onwetendheid is niet het gebrek aan kennis, maar de weigering om te leren.",
        ],
        "visie": (
            "Karl Popper is een van de belangrijkste wetenschapsfilosofen van de twintigste eeuw. "
            "Zijn kernidee: wetenschap werkt niet door bevestiging, maar door falsificatie. "
            "Een theorie is wetenschappelijk als hij weerlegd kan worden. "
            "Je kunt nooit bewijzen dat alle zwanen wit zijn, maar één zwarte zwaan weerlegt de stelling. "
            "Popper wantrouwde elk systeem dat zich niet laat corrigeren. "
            "In De open samenleving en haar vijanden verdedigt hij de democratie tegen totalitaire denkers als Plato, "
            "Hegel en Marx. "
            "De open samenleving is niet perfect, maar ze kan fouten corrigeren. "
            "Popper was een bescheiden denker: hij geloofde niet in absolute waarheid, "
            "maar in de voortdurende zoektocht naar betere antwoorden. "
            "Zijn werk beïnvloedt de wetenschap, de politiek en de filosofie."
        ),
    },

    "feyerabend": {
        "naam": "Paul Feyerabend",
        "leefde": "1924–1994",
        "stroming": "Wetenschapsanarchisme",
        "boeken": [
            "Against Method (Tegen de methode, 1975).",
            "Science in a Free Society (Wetenschap in een vrije samenleving, 1978).",
            "Farewell to Reason (Afscheid van de rede, 1987).",
            "Killing Time (De tijd doden, autobiografie, 1995).",
        ],
        "uitspraken": [
            "Er is geen wetenschappelijke methode die altijd werkt.",
            "Anything goes.",
            "Wetenschap is een vorm van anarchisme.",
            "De rede is een tirannie als ze zich niet laat tegenspreken.",
        ],
        "visie": (
            "Paul Feyerabend is de grote provocateur van de wetenschapsfilosofie. "
            "Hij verzette zich tegen elke poging om de wetenschap in een vaste methode te vangen. "
            "Zijn beroemdste boek, Tegen de methode, laat zien dat grote wetenschappers "
            "als Galileo zich niet aan regels hielden, maar creatief en soms irrationeel te werk gingen. "
            "Zijn slogan anything goes betekent niet dat alles even goed is, "
            "maar dat er geen universele regel is die wetenschap van niet-wetenschap scheidt. "
            "Feyerabend vond dat wetenschap niet meer rechten moet hebben dan andere vormen van kennis. "
            "Hij was een relativist, maar geen nihilist: hij geloofde in vrijheid en diversiteit. "
            "Zijn werk is speels, polemisch en uitdagend. "
            "Hij beïnvloedde de wetenschapssociologie, de filosofie en het debat over de rol van de wetenschap."
        ),
    },

    "russell": {
        "naam": "Bertrand Russell",
        "leefde": "1872–1970",
        "stroming": "Analytische filosofie / Logica",
        "boeken": [
            "Principia Mathematica (met A.N. Whitehead, 1910–1913).",
            "The Problems of Philosophy (De problemen van de filosofie, 1912).",
            "A History of Western Philosophy (Geschiedenis van de westerse filosofie, 1945).",
            "Why I Am Not a Christian (Waarom ik geen christen ben, 1927).",
            "Marriage and Morals (Huwelijk en moraal, 1929).",
        ],
        "uitspraken": [
            "Het probleem met de wereld is dat dwazen en fanatici altijd zo zeker zijn, en wijzen zo vol twijfel.",
            "De goede levensvisie is gebaseerd op liefde en kennis.",
            "Ik zou liever een wereld willen zien die wordt geregeerd door rede dan door macht.",
            "De mens is een deel van de natuur, niet iets daarbuiten.",
        ],
        "visie": (
            "Bertrand Russell was een van de grondleggers van de analytische filosofie. "
            "Samen met Whitehead schreef hij Principia Mathematica, "
            "een poging om de wiskunde te funderen op logica. "
            "Hij won de Nobelprijs voor Literatuur in 1950. "
            "Russell geloofde in de kracht van de rede en de wetenschap. "
            "Hij was een scherp criticus van religie, oorlog en onrecht. "
            "Hij werd gevangengezet tijdens de Eerste Wereldoorlog vanwege zijn pacifisme, "
            "en opnieuw op 89-jarige leeftijd bij een anti-kernwapenprotest. "
            "Zijn Geschiedenis van de westerse filosofie is een van de meest gelezen filosofieboeken ooit. "
            "Hij was een briljant wiskundige, een lucide schrijver en een moedig activist. "
            "Zijn invloed op de filosofie, de logica en het publieke debat is enorm."
        ),
    },
    "thomas_kuhn": {
        "naam": "Thomas Kuhn",
        "leefde": "1922–1996",
        "stroming": "Wetenschapsfilosofie / Historisch",
        "boeken": [
            "The Structure of Scientific Revolutions (De structuur van wetenschappelijke revoluties, 1962).",
            "The Copernican Revolution (De Copernicaanse revolutie, 1957).",
            "The Essential Tension (De essentiële spanning, 1977).",
        ],
        "uitspraken": [
            "Wetenschap ontwikkelt zich niet geleidelijk, maar via revoluties.",
            "Een paradigma is niet alleen een theorie, maar een hele manier van kijken.",
            "Normale wetenschap is puzzelen binnen een paradigma.",
            "Wetenschappers zien de wereld door de bril van hun paradigma.",
        ],
        "visie": (
            "Thomas Kuhn veranderde voorgoed hoe we naar wetenschap kijken. "
            "Zijn kernidee: wetenschap ontwikkelt zich niet als een geleidelijke opeenstapeling van kennis, "
            "maar als een opeenvolging van paradigma's. "
            "Een paradigma is een samenhangend geheel van theorieën, methoden en aannames "
            "die bepalen wat wetenschappers als waar beschouwen. "
            "Binnen een paradigma bedrijven wetenschappers normale wetenschap: "
            "ze lossen puzzels op die het paradigma zelf voorschrijft. "
            "Maar op een gegeven moment stapelen zich anomalieën op: verschijnselen die niet passen. "
            "Dan komt er een crisis, en uiteindelijk een revolutie: een nieuw paradigma neemt de plaats in. "
            "Dat is geen rationeel proces, maar een soort bekering. "
            "Kuhn werd bekritiseerd omdat hij wetenschap zou reduceren tot sociologie, "
            "maar zijn invloed op de wetenschapsfilosofie is enorm."
        ),
    },

    "einstein": {
        "naam": "Albert Einstein",
        "leefde": "1879–1955",
        "stroming": "Wetenschapsfilosofie / Pacifisme",
        "boeken": [
            "Relativity: The Special and General Theory (Relativiteit: de speciale en algemene theorie, 1916).",
            "The World As I See It (De wereld zoals ik haar zie, 1934).",
            "Ideas and Opinions (Ideeën en meningen, 1954).",
            "Out of My Later Years (Uit mijn latere jaren, 1950).",
        ],
        "uitspraken": [
            "Verbeelding is belangrijker dan kennis.",
            "Het is een wonder dat nieuwsgierigheid blijft bestaan.",
            "Ik weet niet met welke wapens de Derde Wereldoorlog zal worden uitgevochten, maar de Vierde zal met stokken en stenen zijn.",
            "God dobbelt niet.",
            "Het belangrijkste is om te blijven vragen.",
        ],
        "visie": (
            "Albert Einstein is de beroemdste wetenschapper van de twintigste eeuw. "
            "Zijn relativiteitstheorie veranderde ons begrip van ruimte, tijd en zwaartekracht. "
            "Maar Einstein was ook een filosoof en een activist. "
            "Hij geloofde in een diepe, harmonieuze orde in het universum, "
            "die hij met wiskundige schoonheid probeerde te vangen. "
            "God dobbelt niet was zijn verzet tegen de onzekerheid van de kwantummechanica. "
            "Hij wantrouwde elke autoriteit en geloofde in de vrijheid van het individu. "
            "Na de Tweede Wereldoorlog werd hij een pleitbezorger voor wereldvrede en ontwapening. "
            "Hij weigerde de presidentschap van Israël. "
            "Zijn verwondering over het universum is de kern van zijn denken. "
            "Hij is een symbool van de kracht van nieuwsgierigheid en verbeelding."
        ),
    },

    "de_bono": {
        "naam": "Edward de Bono",
        "leefde": "1933–2021",
        "stroming": "Creatief denken / Cognitieve psychologie",
        "boeken": [
            "Six Thinking Hats (Zes denkhoeden, 1985).",
            "Lateral Thinking (Lateraal denken, 1970).",
            "How to Have Creative Ideas (Hoe je creatieve ideeën krijgt, 2007).",
            "Serious Creativity (Serieuze creativiteit, 1992).",
        ],
        "uitspraken": [
            "Creativiteit is geen talent, maar een vaardigheid.",
            "Je kunt een probleem niet oplossen met dezelfde denkwijze die het heeft veroorzaakt.",
            "Lateraal denken is niet een andere manier van kijken, maar een andere manier van zoeken.",
            "De zes denkhoeden helpen je om vanuit verschillende perspectieven te kijken.",
        ],
        "visie": (
            "Edward de Bono was een van de meest invloedrijke denkers over creativiteit. "
            "Hij ontwikkelde de methode van het lateraal denken: "
            "niet rechtlijnig naar een oplossing zoeken, maar zijwaarts, via omwegen en verrassingen. "
            "Zijn beroemdste instrument is de zes denkhoeden: "
            "wit voor feiten, rood voor gevoelens, zwart voor kritiek, geel voor optimisme, "
            "groen voor creativiteit, blauw voor organisatie. "
            "Door bewust van hoed te wisselen, kan een groep effectiever denken. "
            "De Bono geloofde dat creativiteit geen mysterieus talent is, "
            "maar een vaardigheid die je kunt trainen. "
            "Hij schreef tientallen boeken, gaf lezingen over de hele wereld, "
            "en werkte met bedrijven, overheden en scholen. "
            "Zijn werk beïnvloedt het onderwijs, het bedrijfsleven en de psychologie."
        ),
    },

    "mill": {
        "naam": "John Stuart Mill",
        "leefde": "1806–1873",
        "stroming": "Liberalisme / Utilitarisme",
        "boeken": [
            "On Liberty (Over vrijheid, 1859).",
            "Utilitarianism (Utilitarisme, 1863).",
            "The Subjection of Women (De onderwerping van de vrouw, 1869).",
            "A System of Logic (Een systeem van logica, 1843).",
            "Autobiography (Autobiografie, 1873).",
        ],
        "uitspraken": [
            "De enige vrijheid die het waard is om te verdedigen, is de vrijheid om je eigen goed te zoeken op je eigen manier.",
            "Het grootste geluk voor het grootste aantal is de maatstaf van goed en kwaad.",
            "Wie alleen zijn eigen mening kent, kent die niet echt.",
            "Vrijheid is niet het recht om te doen wat je wilt, maar het recht om te denken wat je wilt.",
        ],
        "visie": (
            "John Stuart Mill is een van de belangrijkste denkers van het liberalisme. "
            "Hij was een kind van de Verlichting: zijn vader liet hem op jonge leeftijd Grieks, Latijn en filosofie leren. "
            "Mill ontwikkelde het utilitarisme van Bentham verder: "
            "de moraal moet streven naar het grootste geluk voor het grootste aantal. "
            "Maar hij voegde er een belangrijk element aan toe: "
            "niet alle genoegens zijn gelijk; hogere genoegens (denken, kunst, liefde) wegen zwaarder. "
            "In Over vrijheid verdedigt hij de vrijheid van het individu tegen de tirannie van de meerderheid. "
            "De enige reden om iemands vrijheid te beperken is om anderen te beschermen. "
            "Hij was ook een vroege feminist: in De onderwerping van de vrouw pleit hij voor gelijke rechten. "
            "Zijn werk beïnvloedt het liberalisme, het feminisme en de politieke filosofie."
        ),
    },

    "tumarkin": {
        "naam": "Anna Tumarkin",
        "leefde": "1875–1951",
        "stroming": "Academische filosofie / Ethiek",
        "boeken": [
            "Anna Tumarkin publiceerde vooral in het Duits en Russisch.",
            "Belangrijke werken: over Spinoza, over ethiek, over esthetica.",
            "Ze was de eerste vrouwelijke hoogleraar in Zwitserland en een van de eerste in Europa.",
        ],
        "uitspraken": [
            "Kennis zonder verantwoordelijkheid is gevaarlijk.",
            "De filosofie moet zich niet terugtrekken in de ivoren toren.",
            "Vrijheid is niet het recht om te doen wat je wilt, maar de plicht om te doen wat juist is.",
        ],
        "visie": (
            "Anna Tumarkin was een van de eerste vrouwen die een academische carrière in de filosofie wist op te bouwen. "
            "Ze werd geboren in Rusland, studeerde in Zwitserland, en werd in 1906 hoogleraar in Bern. "
            "Ze was de eerste vrouw in Europa die het recht kreeg om promovendi te begeleiden. "
            "Ze schreef over Spinoza, over ethiek en esthetica, en over de verhouding tussen kennis en moraliteit. "
            "Haar werk is minder bekend dan dat van haar mannelijke tijdgenoten, "
            "maar het is een belangrijk getuigenis van vrouwelijke filosofie in een tijd "
            "dat vrouwen nauwelijks toegang hadden tot de academie. "
            "Ze was een scherp denker, een toegewijd docent, en een voorbeeld voor latere generaties. "
            "Ze stierf in 1951, kort na de Tweede Wereldoorlog."
        ),
    },

    "hermes_trismegistos": {
        "naam": "Hermes Trismegistos",
        "leefde": "ca. 1e–3e eeuw n.Chr. (legendarisch)",
        "stroming": "Hermetisme / Mystieke filosofie",
        "boeken": [
            "Corpus Hermeticum (verzameling Griekse teksten).",
            "Asclepius (Latijnse tekst).",
            "Tabula Smaragdina (Smaragden Tafel).",
            "De Hermetica zijn een mengeling van Griekse, Egyptische en joodse invloeden.",
        ],
        "uitspraken": [
            "Zo boven, zo beneden.",
            "Het geheel is één, en alles is een deel van het geheel.",
            "Wie zichzelf kent, kent het universum.",
            "De geest is als een spiegel waarin God zich weerspiegelt.",
        ],
        "visie": (
            "Hermes Trismegistos is een legendarische figuur: een mengeling van de Griekse god Hermes "
            "en de Egyptische god Thoth. "
            "Aan hem wordt een reeks mystieke teksten toegeschreven, het Corpus Hermeticum. "
            "Deze teksten waren in de Renaissance enorm invloedrijk. "
            "Centraal staat de eenheid van alles: het goddelijke is in de kosmos, "
            "en de mens kan die eenheid kennen door innerlijke verlichting. "
            "De Smaragden Tafel is het beroemdste onderdeel: "
            "zo boven, zo beneden, alles is één. "
            "Het hermetisme combineert filosofie, magie, astrologie en alchemie. "
            "Het beïnvloedde de alchemie, de moderne esoterie, en denkers als Giordano Bruno en Newton. "
            "Hermes Trismegistos is een symbool van de zoektocht naar verborgen kennis."
        ),
    },

    "valentinus": {
        "naam": "Valentinus",
        "leefde": "ca. 100–160 n.Chr.",
        "stroming": "Gnostiek / Christelijke mystiek",
        "boeken": [
            "Het Evangelie van de Waarheid (Nag Hammadi).",
            "Het Evangelie van Filippus (Nag Hammadi).",
            "De Verhandeling over de Opstanding (Nag Hammadi).",
            "Valentinus schreef brieven, preken en verhandelingen, deels bewaard in Nag Hammadi.",
        ],
        "uitspraken": [
            "De wereld is niet geschapen door de hoogste God, maar door een lagere demiurg.",
            "De goddelijke vonk in de mens verlangt naar huis.",
            "Gnosis is niet kennis van het hoofd, maar van het hart.",
            "Het licht is in de duisternis, en de duisternis heeft het niet begrepen.",
        ],
        "visie": (
            "Valentinus was een van de meest invloedrijke gnostische denkers van de vroege christenheid. "
            "Hij leefde in Alexandrië en later in Rome, en stichtte een eigen school. "
            "Zijn leer is complex: de wereld is niet geschapen door de hoogste God, "
            "maar door een lagere demiurg, een onvolmaakte schepper. "
            "De mens draagt een goddelijke vonk in zich, die verlangt naar de pleroma, de volheid van het goddelijke. "
            "Verlossing komt niet door geloof, maar door gnosis: innerlijke kennis van je oorsprong. "
            "Valentinus werd door de kerk als ketter veroordeeld, "
            "maar zijn teksten zijn bewaard in de Nag Hammadi-geschriften, "
            "die in 1945 in Egypte werden gevonden. "
            "Zijn werk beïnvloedt de moderne gnostiek en de christelijke mystiek."
        ),
    },

    "ficino": {
        "naam": "Marsilio Ficino",
        "leefde": "1433–1499",
        "stroming": "Renaissance-neoplatonisme",
        "boeken": [
            "Theologia Platonica (Platoonse theologie, 1482).",
            "De amore (Over de liefde, 1469).",
            "Vertalingen van Plato, Plotinus en het Corpus Hermeticum.",
            "De vita libri tres (Drie boeken over het leven, 1489).",
        ],
        "uitspraken": [
            "De liefde is de kosmische kracht die alles verbindt.",
            "De ziel is het middelpunt van de kosmos.",
            "Schoonheid is de glans van het goddelijke in de dingen.",
            "De mens is een microkosmos, een spiegel van het universum.",
        ],
        "visie": (
            "Marsilio Ficino was de centrale figuur van het Florentijnse neoplatonisme. "
            "Hij vertaalde de werken van Plato, Plotinus en het Corpus Hermeticum in het Latijn, "
            "en maakte ze zo toegankelijk voor het Westen. "
            "Zijn filosofie draait om de ziel: de ziel is het middelpunt van de kosmos, "
            "verbonden met het goddelijke en met de materie. "
            "Liefde is de kracht die alles verbindt: van God naar de wereld en terug. "
            "Ficino geloofde in de eenheid van wijsheid: Plato en Christus, "
            "filosofie en geloof, waren voor hem geen tegenstellingen. "
            "Hij was ook geïnteresseerd in astrologie, magie en geneeskunde. "
            "Zijn werk beïnvloedde de Renaissance, de moderne esoterie en de westerse mystiek. "
            "Hij is een sleutelfiguur in de overgang van middeleeuwen naar moderne tijd."
        ),
    },

    "bruno": {
        "naam": "Giordano Bruno",
        "leefde": "1548–1600",
        "stroming": "Renaissance-natuurfilosofie / Hermetisme",
        "boeken": [
            "De l'infinito, universo e mondi (Over het oneindige, het universum en de werelden, 1584).",
            "La cena de le ceneri (Het avondmaal van Aswoensdag, 1584).",
            "De la causa, principio e uno (Over oorzaak, beginsel en eenheid, 1584).",
            "Spaccio de la bestia trionfante (De verdrijving van de triomferende beest, 1584).",
        ],
        "uitspraken": [
            "Het universum is oneindig, en er zijn talloze werelden.",
            "De waarheid is niet in één boek te vinden, maar in de oneindigheid van de natuur.",
            "Ik sterf als martelaar, en mijn ziel zal opstijgen naar het oneindige.",
            "Vrijheid van denken is het hoogste goed.",
        ],
        "visie": (
            "Giordano Bruno is een van de meest tragische en moedige figuren van de Renaissance. "
            "Hij was een Dominicaanse monnik die brak met de kerk, "
            "door Europa reisde, en een radicale filosofie ontwikkelde. "
            "Zijn kernidee: het universum is oneindig, en er zijn talloze werelden. "
            "God is niet buiten de wereld, maar in de wereld aanwezig als oneindige kracht. "
            "Bruno combineerde neoplatonisme, hermetisme en Copernicaanse astronomie. "
            "Hij geloofde in de oneindigheid van het universum, lang voordat de wetenschap dat bevestigde. "
            "In 1600 werd hij in Rome op het brandstapel ter dood gebracht. "
            "Zijn laatste woorden zouden zijn geweest: ik sterf als martelaar, en mijn ziel zal opstijgen. "
            "Bruno is een symbool van de vrije gedachte en de moed om tegen de macht in te gaan."
        ),
    },

    "luther": {
        "naam": "Martin Luther",
        "leefde": "1483–1546",
        "stroming": "Reformatie / Protestantisme",
        "boeken": [
            "95 stellingen (1517).",
            "Von der Freiheit eines Christenmenschen (Over de vrijheid van een christenmens, 1520).",
            "De Babylonische gevangenschap van de kerk (1520).",
            "Bijbelvertaling in het Duits (1522–1534).",
        ],
        "uitspraken": [
            "Hier sta ik, ik kan niet anders.",
            "Iedereen is zijn eigen priester.",
            "De Bijbel alleen, genade alleen, geloof alleen.",
            "Een christen is een vrij heer over alle dingen, en niemand onderdanig.",
        ],
        "visie": (
            "Martin Luther is de centrale figuur van de Reformatie. "
            "Hij was een Augustijner monnik en theoloog die in 1517 zijn 95 stellingen publiceerde "
            "tegen de aflaathandel van de kerk. "
            "Zijn kernidee: de mens wordt niet gered door goede werken, maar door geloof alleen. "
            "De Bijbel is de enige bron van gezag, niet de paus of de traditie. "
            "Luther vertaalde de Bijbel in het Duits, zodat gewone mensen hem konden lezen. "
            "Dat had een enorme invloed op de Duitse taal en cultuur. "
            "Hij was een vurig en controversieel man: hij schreef scherpe polemieken, "
            "keerde zich tegen de joden en tegen de opstandige boeren. "
            "Zijn invloed op de religie, de politiek en de cultuur van Europa is enorm. "
            "Zijn geweten was voor hem belangrijker dan de macht van de kerk."
        ),
    },
    "roodkapje": {
        "naam": "Roodkapje",
        "leefde": "Lang geleden, in een groot donker bos",
        "stroming": "Sprookjeswijsheid",
        "boeken": [
            "Het sprookje van Roodkapje, zoals verteld door de gebroeders Grimm.",
            "Er zijn heel veel versies van dit verhaal, al honderden jaren oud.",
        ],
        "uitspraken": [
            "Wat heb je grote oren!",
            "Wat heb je grote ogen!",
            "Wat heb je een grote mond!",
            "Ga niet van het pad af, ook al lijkt het korter.",
        ],
        "visie": (
            "Roodkapje is een meisje dat naar haar oma gaat, met een mandje vol lekkers. "
            "Maar in het bos woont een wolf. De wolf is slim en doet alsof hij lief is. "
            "Roodkapje gelooft hem, en dat is gevaarlijk. "
            "Het verhaal leert ons: niet iedereen die aardig doet, is ook aardig. "
            "Blijf op het pad. Luister naar je ouders. Vertrouw niet zomaar iedereen. "
            "Maar het leert ook iets moois: als je in de problemen komt, kun je geholpen worden. "
            "En soms moet je eerst verdwalen voordat je weer thuis komt."
        ),
    },

    "pinocchio": {
        "naam": "Pinocchio",
        "leefde": "In een klein Italiaans dorpje, lang geleden",
        "stroming": "Sprookjeswijsheid",
        "boeken": [
            "De avonturen van Pinocchio, geschreven door Carlo Collodi in 1883.",
            "Het verhaal is in meer dan 260 talen vertaald.",
        ],
        "uitspraken": [
            "Mijn neus groeit als ik lieg!",
            "Ik wil een echte jongen worden.",
            "Ik doe het nooit meer!",
            "Een geweten is een stemmetje dat je hoort als je iets stouts doet.",
        ],
        "visie": (
            "Pinocchio is een houten pop die gemaakt is door een oude man, Geppetto. "
            "Pinocchio wil een echte jongen worden, maar dat gaat niet zomaar. "
            "Hij moet leren wat goed en fout is. "
            "Als hij liegt, groeit zijn neus. Als hij stout is, gebeuren er nare dingen. "
            "Maar Pinocchio leert van zijn fouten. "
            "Hij leert dat je verantwoordelijkheid moet nemen, dat je niet moet luisteren naar slechte vrienden, "
            "en dat je moet doen wat juist is, ook als het moeilijk is. "
            "Uiteindelijk wordt hij een echte jongen, omdat hij heeft geleerd om goed te zijn."
        ),
    },

    "sneeuwwitje": {
        "naam": "Sneeuwwitje",
        "leefde": "In een groot kasteel, lang geleden",
        "stroming": "Sprookjeswijsheid",
        "boeken": [
            "Het sprookje van Sneeuwwitje, zoals verteld door de gebroeders Grimm.",
            "Het verhaal gaat over schoonheid, jaloezie en vriendschap.",
        ],
        "uitspraken": [
            "Spiegeltje, spiegeltje aan de wand, wie is de mooiste van het land?",
            "Ik hoop dat de jager me laat gaan.",
            "De dwergen zijn mijn vrienden.",
            "Echte schoonheid zit van binnen.",
        ],
        "visie": (
            "Sneeuwwitje is een meisje dat heel mooi is. "
            "De koningin is jaloers op haar en wil haar laten verdwijnen. "
            "Sneeuwwitje vlucht het bos in en komt bij zeven dwergen terecht. "
            "De koningin probeert haar met een giftige appel te doden. "
            "Maar Sneeuwwitje wordt gered en wordt wakker. "
            "Het verhaal leert ons dat jaloezie mensen lelijk maakt, "
            "en dat echte schoonheid niet gaat om hoe je eruitziet, "
            "maar om hoe je bent. Sneeuwwitje is lief en aardig, "
            "en daarom houden de dwergen van haar. "
            "Uiteindelijk overwint het goede."
        ),
    },

    "doornroosje": {
        "naam": "Doornroosje",
        "leefde": "In een groot kasteel, diep in het bos, lang geleden",
        "stroming": "Sprookjeswijsheid",
        "boeken": [
            "Het sprookje van Doornroosje, zoals verteld door de gebroeders Grimm.",
            "Het verhaal gaat over tijd, geduld en wachten op iets moois.",
        ],
        "uitspraken": [
            "Op een dag zal ik wakker worden.",
            "De tijd gaat langzaam als je slaapt.",
            "Geduld is een mooie deugd.",
            "Soms moet je wachten op het juiste moment.",
        ],
        "visie": (
            "Doornroosje is een prinses die wordt betoverd. "
            "Op haar vijftiende prikt ze zich aan een spintol en valt ze in slaap. "
            "Het hele kasteel slaapt mee. "
            "Rondom het kasteel groeit een dikke doornhaag. "
            "Na honderd jaar komt er een prins die door de doornen heen durft te gaan. "
            "Hij kust Doornroosje wakker, en het hele kasteel ontwaakt. "
            "Het verhaal leert ons geduld: niet alles gebeurt meteen. "
            "Soms moet je wachten op het juiste moment. "
            "En soms moet je moedig zijn, zoals de prins, "
            "om door de doornen heen te gaan voor iets moois."
        ),
    },

    "zeven_dwergen": {
        "naam": "De Zeven Dwergen",
        "leefde": "In een klein huisje in het bos, lang geleden",
        "stroming": "Sprookjeswijsheid",
        "boeken": [
            "De zeven dwergen komen uit het sprookje van Sneeuwwitje.",
            "Ze zijn bekend geworden door het verhaal van de gebroeders Grimm.",
        ],
        "uitspraken": [
            "Wij werken hard in de mijnen.",
            "We zorgen voor elkaar.",
            "Samen zijn we sterk.",
            "Eenvoud maakt gelukkig.",
        ],
        "visie": (
            "De zeven dwergen wonen samen in een klein huisje in het bos. "
            "Elke dag gaan ze naar de mijnen om te werken. "
            "Ze zijn niet groot, maar ze zijn sterk en vrolijk. "
            "Als Sneeuwwitje bij hen komt wonen, zorgen ze voor haar. "
            "Het verhaal leert ons dat je samen meer kunt dan alleen. "
            "Dat je moet werken voor wat je hebt. "
            "Dat eenvoud gelukkig maakt. "
            "En dat je voor elkaar moet zorgen, "
            "ook als iemand anders is dan jij."
        ),
    },      
}          
