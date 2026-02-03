import operazioni

def _parse_number(s: str):
    s = s.strip()
    if s == "":
        return None
    try:
        # prefer int when possible
        if "." in s or "e" in s.lower():
            return float(s)
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return None


def main():
    try:
        a_raw = input("Inserisci il primo numero: ")
        a = _parse_number(a_raw)
        if a is None:
            print("Primo valore non numerico: verrà considerato 0")
            a = 0

        b_raw = input("Inserisci il secondo numero: ")
        b = _parse_number(b_raw)
        if b is None:
            print("Secondo valore non numerico: verrà considerato 0")
            b = 0

        op = input("Operazione (s = somma, t = sottrazione): ").strip().lower()
        if op in ("s", "somma", "+"):
            res = operazioni.somma(a, b)
            print(f"{a} + {b} = {res}")
        elif op in ("t", "sottrazione", "-"):
            res = operazioni.sottrazione(a, b)
            print(f"{a} - {b} = {res}")
        else:
            print("Operazione non riconosciuta. Usa 's' per somma o 't' per sottrazione.")
    except (KeyboardInterrupt, EOFError):
        print("\nInterrotto dall'utente")

if __name__ == "__main__":
    main()