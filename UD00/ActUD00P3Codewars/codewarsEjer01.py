def substring_test(s1, s2):


   # Convertimos las dos cadenas a minúsculas.
   # Así, "HOLA" y "hola" se consideran iguales.
   s1 = s1.lower()
   s2 = s2.lower()


   # Recorremos la primera cadena carácter por carácter.
   # Restamos 1 porque necesitamos coger 2 caracteres juntos.
   for i in range(len(s1) - 1):


       # Cogemos 2 caracteres consecutivos de la primera cadena.
       # Por ejemplo, si s1 = "casa":
       # Primera vuelta: "ca"
       # Segunda vuelta: "as"
       # Tercera vuelta: "sa"
       subcadena = s1[i:i+2]


       # Comprobamos si esos 2 caracteres aparecen
       # en algún lugar de la segunda cadena.
       if subcadena in s2:


           # Si encontramos la subcadena, devolvemos True.
           # True significa que SÍ existe una coincidencia.
           return True


   # Si terminamos el bucle sin encontrar ninguna coincidencia,
   # devolvemos False.
   # False significa que NO existe ninguna coincidencia.
   return False




# Pruebas del ejercicio.
# En cada prueba mostramos el resultado por pantalla.


print("Prueba 1:", substring_test("Something", "Home"))
print("Prueba 2:", substring_test("Something", "Fun"))
print("Prueba 3:", substring_test("Something", ""))
print("Prueba 4:", substring_test("", "Something"))
print("Prueba 5:", substring_test("BANANA", "banana"))
print("Prueba 6:", substring_test("test", "lllt"))
print("Prueba 7:", substring_test("", ""))
print("Prueba 8:", substring_test("1234567", "541265"))


print("Prueba 9:", substring_test(
   "supercalifragilisticexpialidocious",
   "SoundOfItIsAtrocious"
))


print("Prueba 10:", substring_test(
   "LoremipsumdolorsitametconsecteturadipiscingelitAeneannonal"
   "iquetligulautplaceratorciSuspendissepotentiMorbivolutpatau"
   "ctoripsumegetaliquamPhasellusidmagnaelitNullamerostelluste"
   "mporquismolestieaornarevitaediamNullaaliquamrisusnonviverr"
   "asagittisInlaoreetultricespretiumVestibulumegetnullatincid"
   "untsempersemacrutrumfelisPraesentpurusarcutempusnecvariusi"
   "dultricesaduiPellentesqueultriciesjustolobortisrhoncusdign"
   "issimNuncviverraconsequatblanditUtbibendumatlacusactristiq"
   "ueAliquamimperdietnuncsempertortorefficiturviverra",
   "thisisalongstringtest"
))
