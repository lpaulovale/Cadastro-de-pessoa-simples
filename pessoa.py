class pesoa:

   cpf = 0
   nome = ""

   def printp(self):
     print(self.cpf, self.nome)

   def __init__(self, cpf, nome):
     self.cpf = cpf
     self.nome = nome


a = pessoa(123, "paulo")
a.printp()
