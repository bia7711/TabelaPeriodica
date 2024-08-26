Tabela = {
'H':{'Nome':'Hidrogênio','Número Atómico':1,'Massa Atómica':1008},
'C': {'Nome':'Carbono','Número Atómico':6,'Massa Atómica':12.011},
'N': {'Nome':'Nitrogênio','Número Atómico':7,'Massa Atómica':14.007},
'O': {'Nome':'Oxigênio','Número Atómico':8,'Massa Atómica':15.999},
'P': {'Nome':'Fósforo','Número Atómico':15,'Massa Atómica':30.974},
'B': {'Nome':'Boro','Número Atómico':5,'Massa Atómica':10.811},
'F': {'Nome':'Flúor','Número Atómico':9,'Massa Atómica':18.998},
'I': {'Nome':'Iodo','Número Atómico':53,'Massa Atómica':126.904},
'AR': {'Nome':'Argônio','Número Atómico':18,'Massa Atómica':39.948},
'RA':{'Nome':'Radônio','Número Atómico':86,'Massa Atómica':222}
}

sigla =('H' 'C' 'N' 'O' 'P' 'B' 'F' 'I' 'AR' 'RA')
simbolo = input("Digite uma sigla da tabela periódica: ")
simbolo=simbolo.upper()
if simbolo in sigla:
    print(f"Nome: {Tabela[simbolo]['Nome']}")
    print(f"Número Atómico: {Tabela[simbolo]['Número Atómico']}")
    print(f"Massa Atómica: {Tabela[simbolo]['Massa Atómica']}")
else:
    print("Sigla inválida,digite novamente")




   