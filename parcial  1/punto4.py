import time 
import contarPalabrasV1 as Cpv1 
import contarPalabrasV2 as Cpv2

parrafo = '''La justicia sobre la fuerza es la impotencia, la fuerza sin justicia es tiranía.
            Vale más saber alguna cosa de todo que saberlo todo de una sola cosa.
            Dos excesos: excluir la razón, no admitir más que la razón.
            Nuestra naturaleza está en movimiento. El reposo absoluto es la muerte.
            El hombre tiene ilusiones como el pájaro alas. Eso es lo que lo sostiene.
            El hombre está dispuesto siempre a negar todo aquello que no comprende.
            Aquel que duda y no investiga, se torna no sólo infeliz, sino también injusto.
            A fuerza de hablar de amor, uno llega a enamorarse.
            ¿De qué le sirve al hombre ganar el mundo si pierde su alma?'''

inicio = time.time()
Cpv1= parrafo
deltaCpv1 = time.time()-inicio 

inicio= time.time()
Cpv2 = parrafo 
deltaCpv2 = time.time()-inicio 

print(deltaCpv1,deltaCpv2)