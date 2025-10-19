
paginas = [4,6,7,8,1,6,10,15,16,4,2,1,4,6,12,15,16,11 ]

quadros = 8

memoria = [None] * quadros
ordem = []

contador_page_faults = 0

for pagina in paginas:
    print('____')
    print("acessando a página " + str(pagina))
    
    if pagina in ordem:
        ordem.remove(pagina)
        ordem.append(pagina)
        print ("HIT")
    
    else:
        contador_page_faults += 1

        if None in memoria:
            index = memoria.index(None)
            memoria[index] = pagina

        else:
            mru = ordem.pop()
            index = memoria.index(mru)
            memoria[index] = pagina
    
        ordem.append(pagina)
        print("MISS")
    
    print(f"Memória: {memoria}")
    print(f"Ordem do mais antigo para o mais recente: {ordem}")


print("RESULTADO FINAL:")
for i, pagina in enumerate(memoria):
    print(f"Quadro {i}: Página {pagina}")

print(f"Page faults: {contador_page_faults}")