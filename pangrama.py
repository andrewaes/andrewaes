lista = ["a", "b" ,"c" ,"d" ,"e" ,"f" ,"g" ,"h" ,"i" ,"j" ,"l" ,"m" ,"n" ,"o", "p", "q", "r", "s", "t", "u", "v" ,"x", "z"]

pangrama = "gazeta publica hoje: breve anuncio de faxina na quermesse"

qtd_letras = 0

for i in lista[0:]:
    if i in pangrama:
        qtd_letras += 1

if qtd_letras == 23:
    print("sim")
else:
    print("nao")
        
