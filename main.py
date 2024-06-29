from pessoas import Pessoa

sexo = input("Qual o seu sexo? : ").lower()
peso = float(input("Qual o seu peso em KG? : "))

pessoa = Pessoa(sexo=sexo, peso=peso)


resultado1 = pessoa.calcularHomem()
resultado2 = pessoa.calcularMulher()

if resultado1:
        print(f"O gasto diário calórico é {resultado1:.2f} calorias.")


elif resultado2:
    print(f"O gasto diário calórico é {resultado2:.2f} calorias.")

  