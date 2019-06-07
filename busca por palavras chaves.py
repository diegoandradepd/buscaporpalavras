import os
import re

dir = 'Y:/'
busca = ['pagamento', 'comprovante', 'recibo', 'contrato', 'cpf']
principalDir = os.listdir(dir)
arquivosLidos = 0
diretoriosVerificados = 0

def buscaRecursiva(sub):
	
	global arquivosLidos, diretoriosVerificados
	
	#print('recursiva ' + sub)
	
	if os.path.exists(sub) == True:
	
		subdir = os.listdir(sub)
		
		for s in subdir:
			if os.path.isfile(sub + s):					
				for b in busca:
					if re.search(b, s):							
						criatxt = open('resultado.txt', 'a', encoding='utf-8')
						criatxt.write(str(sub) + str(s) + ' \n')
						criatxt.close()																			
				arquivosLidos = arquivosLidos + 1	
				os.system('cls')
				print('Diretorios verificados: ', diretoriosVerificados)
				print('Arquivos processados: ', arquivosLidos)
				print('Processamento atual: ', sub + s)
			else:
				diretoriosVerificados = diretoriosVerificados + 1
				os.system('cls')
				print('Diretorios verificados: ', diretoriosVerificados)
				print('Arquivos processados: ', arquivosLidos)
				print('Processamento atual: ', sub + s, '/')
				buscaRecursiva(sub + s + '/')
		
for a in principalDir:

	if os.path.isfile(dir + a):	
	
		for b in busca:				
			if re.search(b, a):					
				
				criatxt = open('resultado.txt', 'a', encoding='utf-8')
				criatxt.write(str(dir) + str(a) + ' \n')
				criatxt.close()					
		arquivosLidos = arquivosLidos + 1
		os.system('cls')
		print('Processamento atual: ', dir + a)
		print('Diretorios verificados: ', diretoriosVerificados)
		print('Arquivos processados: ', arquivosLidos)
	else:
		diretoriosVerificados = diretoriosVerificados + 1
		os.system('cls')
		print('Processamento atual: ', dir + a, '/')
		print('Diretorios verificados: ', diretoriosVerificados)
		print('Arquivos processados: ', arquivosLidos)
		buscaRecursiva(dir + a + '/')		
	
print('Finish!')