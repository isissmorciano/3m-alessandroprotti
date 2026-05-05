def scrivi_file(frasi, nome_file):
    with open( nome_file , "w" ,encoding ="utf-8" ) as file:
        for f in frasi :
            file.write((f) + "\n")
        
        
    
    

def leggi_file(nome_file):
    righe = []
    with open( nome_file , "r" ,encoding ="utf-8" ) as file:
     for line in file :
         righe.append(line.strip())
    return righe
         
             

def main():
    frasi = ["Ciao mondo", "Python è divertente", "File handling"]
    
    nome_file =  "esercizio56.txt"
     
    
    
    scrivi_file(frasi, nome_file)
    
    contenuto=leggi_file(nome_file)
    print ('-' * 120)
    print() 
    print ('CONTENUTO FILE:'.center(120))
    print()
    
    for _ in contenuto:
        print ((_).center(120))
        print()
    print ('-' * 120)
    
   
main()