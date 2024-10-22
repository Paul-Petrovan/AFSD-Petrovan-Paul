sir="Andrei Raţiu a impresionat în această ediție de LaLiga şi este deja căutat de granzii Spaniei."
mid=len(sir)//2
pt1=sir[:mid]
pt2=sir[mid:]
pt1.strip()
pt2=pt2[::-1]
pt=pt2.replace(',',' ')
pt2=pt2.replace('.',' ')
print(pt1.upper()+pt2.capitalize())