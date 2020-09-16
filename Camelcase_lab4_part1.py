def camelcase(a_string):
     
    for c in a_string: # checking lowercase characters
        if c != 'lower'.lower(): 
            return c.capitalize()#convert to uppercase
           

def main():
    a_string = 'today is tuesday'
    output = camelcase(a_string)
    
    print(output)

if __name__ == '__main__':
     main()        


            
