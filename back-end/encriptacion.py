def encriptar(psswd, BTSN):
	diccionario_de_caracteres = "0123456789abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
	BITSNumber = BTSN or 32
	integer = 0
	finalWord = ""

	while integer < 10:
		prohi = "#%&*{ }:<>?/+, $.-"
		
		cadena = psswd * 20

		sortWord = sorted(cadena, reverse = True)

		abc123 = "0123456789abcdefghijklmnñopqrstuvwxyz"
		ABC123M = "0123456789ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"


		def desordenar(sortWord, a, b):
			for i in range(len(sortWord)):
				j = i * a
				k = i * b
				try:
					sortWord.append(sortWord[j])
					sortWord.append(sortWord[i])
				except:
					try:
						sortWord.append(sortWord[k])
					except:
						sortWord.append(sortWord[i])
				sortWord.remove(sortWord[i])

		desordenar(sortWord, len(psswd), len(psswd)-3)

		desordenar(sortWord, len(psswd)+4, len(psswd))

		desordenar(sortWord, 11, 2)

		desordenar(sortWord, len(psswd)+7, len(psswd)+6)


		palabraEncriptada = ""
		for i in range(len(sortWord)):
			i = i%len(abc123)
			if i%3 == 0:
				val = abc123[i]
			elif i%2 == 0:
				val = ABC123M[i]
			else:
				val = sortWord[i]

			palabraEncriptada += val


		def shuffleW(palabra, contador, a):
			while contador < 20:
				for i in range(70):
					try:
						palabra += palabra[i * a]
					except:
						pass
					contador += 1
			return palabra

		palabraEncriptada = shuffleW(palabraEncriptada, 0, 3)
		palabraEncriptada = shuffleW(palabraEncriptada, 0, 7)
		palabraEncriptada = shuffleW(palabraEncriptada, 0, 5)
		palabraEncriptada = shuffleW(palabraEncriptada, 0, 11)
		palabraEncriptada = palabraEncriptada[:256]


		def changing(p):
			try:
				num = abc123.index(p[25].lower())
			except:
				num = 10

			x1=p.replace('M', str(num))
			num -= 2
			x2=x1.replace('U', str(num))
			num -= 2
			x3=x2.replace('R', str(num))
			num -= 2
			x4=x3.replace('C', str(num))
			num -= 2
			x5=x4.replace('I', str(num))
			num -= 2
			x6=x5.replace('E', str(num))
			num -= 2
			x7=x6.replace('L', str(num))
			num -= 2
			x8=x7.replace('A', str(num))
			num -= 2
			x9=x8.replace('G', str(num))
			num -= 2
			x0=x9.replace('O', str(num))
			return x0

		psswd = changing(palabraEncriptada)[:32]

		for i in prohi:
			psswd = psswd.replace(i, "")

		clave = "DBG4m3syt"

		newWorld = ""

		i = 0
		j = 0
		while i < len(psswd):
			letraN1 = diccionario_de_caracteres.index(psswd[i])
			while j < len(clave):
				letraN2 = diccionario_de_caracteres.index(clave[j])
				value = (letraN1 + letraN2) % len(diccionario_de_caracteres)
				i += 1
				j += 1
				
				newWorld += diccionario_de_caracteres[value]
				
			j = 0

		finalWord += changing(newWorld[:-len(clave)])[:32]

		integer += 1
		
	return finalWord[115:115+BITSNumber]