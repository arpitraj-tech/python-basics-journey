ask=input("do u want to code a secret text or decode : ").strip()
if ask.lower() == "code":
    code_txt=input("type the msg u want to be coded  : ").lower()
    coding_structure = str.maketrans( { "a":"14h", "e":"67j","i":"12s","o":"10r","u":"1n1","b":"56u","c":"3m3", "d":"7o8","f":"101b","g":"615","h":"8oo","j":"oo2","k":"00o","l":"14oo7","m":"qw10","n":"881q","p":"1b","q":"occ","r":"69x","s":"5o0","t":"jj1","v":"1no","w":"1xs","x":"1se0","y":"004n","z":"3kk0","0":"!!!@#","1":"@%","2":")*","3":"_&","4":"%(","5":"^^","6":"*$","7":"$^","8":"&%@","9":"###" } )
    coded_output= code_txt.translate(coding_structure)
    print(coded_output)
    print("now share the secret with whomever u wish ; )")
elif ask.lower() == "decode":
    code_txtr=input("type the msg u want to be decoded  : ").lower()
    reverse_structure = { "14h":"a", "67j":"e","12s":"i","10r":"o","1n1":"u","56u":"b","3m3":"c","7o8":"d","101b":"f","615":"g","8oo":"h","oo2":"j","00o":"k","14oo7":"l","qw10":"m","881q":"n","1b":"p","occ":"q","69x":"r","5o0":"s","jj1":"t","1no":"v","1xs":"w","1se0":"x","004n":"y","3kk0":"z","!!!@#":"0","@%":"1",")*":"2","_&":"3","%(":"4","^^":"5","*$":"6","$^":"7","&%@":"8","###":"9" }
    decoded_output = code_txtr
    sorted_keys = sorted(reverse_structure.keys(), key=len, reverse=True)

    for coded_charecter, original_charecter in reverse_structure.items():
        decoded_output = decoded_output.replace(coded_charecter, original_charecter)
        
    print(decoded_output)
    print("this is the msg someone send u ; ) ")

    
