#### Soal 2 Crypto Compfest

File yang diberikan : 
<ol>
<li>encrypted.txt (Ciphertext) </li>
<li>prob.py (Encription Code)</li>
</ol>

dari prob.py kita mendapatkan informasi bahwa : 

```python

a = 10**400
b = 10**500
n = random.randint(a, b)

```
n adalah random integer antara 1^400 - 10^500  

```python
while(not(f(n))):
    n = random.randint(a, b)
```
n akan di random sampai nilai fungsi f True

```python
def f(n):
    c = 0
    for i in range(2, n):
        if (n^0 == n):
            if (n*n // n == n):
                if (2*n != n-1):
                    if (n**0 + 1 != 1):
                        m = n
                        while (m > 0):
                            m -= i
                        if (m == 0):
                            c += 1
    if (c == 1):
        return True
    else:
        return False
```
fungsi f True jika n hanya dapat dikurangi habis oleh 1 buah angka antara 2 - n atau dengan kata lain n = bilangan prima^2

```python
encrypted.append(c ^ n)
```
Enkripsi dilakuakn dengan melakuakn operasi xor antara c dan n

```python
for c in FLAG:
    while(not(f(n))):
        n = random.randint(a, b)
    encrypted.append(c ^ n)
    n += 1
```
Setiap karakter dienkripsi dengan key yang unik


> Flag : COMPFEST12{ez_pz_lemonade_squeez_a42447}
