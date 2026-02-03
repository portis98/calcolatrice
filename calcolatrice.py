import operazioni

def main():
    print("1+2=", operazioni.somma(1,2))
    print("-1+2=", operazioni.somma(-1,2))
    print("1+'a'=", operazioni.somma(1,'a'))
    print("1+2=", operazioni.somma(1,2))

if __name__ == "__main__":
    main()