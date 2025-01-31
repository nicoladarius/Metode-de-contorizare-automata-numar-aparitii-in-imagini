# Metode de contorizare automată numar apariți în imagini - partea aplicativă
### Numărarea obiectelor dintr-o imagine, folosind Python-OpenCV 
Aplicația noastră ne permite să aflăm câte obiecte se pot găsi într-o imagine.

Din nefericire, aplicația dispune de o mârșa de eroare. În funcție de complexitatea obiectelor din imagine, această mârșa de eroare poate fi semnificativă sau minoră.

Cerințe Aplicație:
>- OpenCV  : Este un instrument excelent pentru procesarea imaginilor și efectuarea sarcinilor de viziune computerizată.
>- Pillow  : Este o bibliotecă de imagini Python (PIL), care adaugă suport pentru deschiderea, manipularea și salvarea imaginilor.
>- Tkinter : Este biblioteca standard GUI pentru Python.
#### Pași

1. Instalați librăriile

```bash
  pip install -r CerințeInstalareLibrării.txt
```

2. Porniți Aplicația

```bash
  python contorizareNumarAparitiiInImagini.py
```
3. Selectați imaginea

```bash
  ...\Metode de contorizare automata numar aparitii in imagini partea aplicativa\Imagini functionalitate proiect
```

Funcţionalitate:
> Pasul 1: Importăm imaginea folosind opencv </br>

> Pasul 2: Manipularea imaginii, ce cuprinde: </br>
 - Scalarea de gri a imaginii (Gray Scaling)
 - Încețoșarea imaginii (Bluring)
 - Aflarea marginilor imaginii
 - Calcularea contorului obiectelor imaginii
 - Afișarea rezultatului


