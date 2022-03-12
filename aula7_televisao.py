# lembre que método no Python NUNCA retorna um valor
# sendo assim, temos métodos aqui abaixo

class Televisao:
    def __init__(self):
        self.ligada = True
        self.canal = 3

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1


televisao = Televisao()
print('A televisão está ligada? {}'.format(televisao.ligada))

televisao.power()
print('A televisão agora está ligada? {}'.format(televisao.ligada))

televisao.power()
print('A televisão agora está ligada? {}'.format(televisao.ligada))

print('A televisão está no canal: {}'.format(televisao.canal))

televisao.aumenta_canal()
print('Agora a televisão está no canal: {}'.format(televisao.canal))

televisao.aumenta_canal()
print('Agora a televisão está no canal: {}'.format(televisao.canal))

televisao.diminui_canal()
print('Agora a televisão está no canal: {}'.format(televisao.canal))
