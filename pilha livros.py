pilhadelivros = []

def print_stack():
	print("Livros atualmente na pilha: ")
	i = 1
	for livro in reversed(pilhadelivros):
		print("{}. {}".format(i, livro))
		i += 1


while True:
	livro = input('Digite o nome do livro para adicionar à pilha, pressione a tecla ENTER para listar a pilha atual ou escreva RETIRA para retirar o primeiro livro da pilha atual: ')
	if livro == '':
		print_stack()
	elif livro == 'RETIRA':
		if len(pilhadelivros) > 0:
			pilhadelivros.pop()
		if len(pilhadelivros) > 0:
			print_stack()
	else:
		pilhadelivros.append(livro)
		print_stack()