# coding: utf-8

foo = """
 Schon bald stehen dem deutschen Arbeitsmarkt deutlich weniger Menschen zur Verfügung. Deshalb fordert die Bundesagentur für Arbeit, mehr Fachkräfte aus dem Ausland anzuwerben. Auch zur Rettung der Sozialsysteme.

Raimund Becker aus dem Vorstand der Bundesagentur für Arbeit hält die künftige Entwicklung auf dem deutschen Arbeitsmarkt für dramatisch. Nur wenn qualifizierte Arbeitnehmer aus dem Ausland angeworben werden, kann seiner Ansicht nach der Arbeitskräftebedarf in Zukunft gedeckt werden.

Vor allem im medizinischen Bereich ist der Fachkräftemangel schon da. Bei Ärzten, Apothekern und Krankenpflegern können freie Positionen oft erst nach Monaten oder gar nicht mehr besetzt werden. Denn viele deutsche Mediziner arbeiten lieber in der Schweiz oder in Großbritannien, dort sind sowohl die Arbeitsbedingungen als auch die Bezahlung im Durchschnitt besser als in Deutschland. Bei den Pflegekräften sorgen ungünstige Arbeitszeiten und niedrige Bezahlung dafür, dass sich nicht genügend Bewerber finden - während der Bedarf stetig steigt.
"""

f = open('out','w')
f.write(foo)
f.close()
