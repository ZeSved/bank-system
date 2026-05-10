# Enkelt Banksystem

Ett filbaserat banksystem skrivet i Python och som är uppbyggt av klasser. Systemet gör så att
användare kan skapa konton samt att göra operationer som deposit och withdraw. Allt sparas i JSON
filer för långtidssparande.

## Funktioner

- **User authentication**: Ett system som automatiskt skapar en 4 siffrig kod till användaren så att
  bara användaren kan komma åt sin data
- **Kontohantering**: Man kan skapa, öppna och radera flera konton (t.ex. "Sparkonto", "Lönekonto").
- **Operationer**:
  - **Deposit**: Sätta in pengar med validering av indata.
  - **Withdraw**: Ta ut pengar med gränser för att se till att inte för mycket tas ut.
  - **Överföringar**: Skicka pengar mellan olika konton i systemet.
- **Transaktionshistorik**: Varje pengaförflyttning loggas som ett `Transaction`-objekt och sparas i
  kontots historik för att kunna hitta den igen.
- **Datapersistens**: All användardata, saldon och historik sparas i JSON-filer i en egen mapp,
  vilket gör att informationen finns kvar även när programmet stängs.

## Projektstruktur

Projektet följer en modulär arkitektur för att separera användargränssnitt, affärslogik och
datalagring:

- `main.py` **Frontend (CLI)** Hanterar menyer, användarinteraktion och koordinerar med backend.
- `backend.py` **Backend-motor** Hanterar JSON-filer (läsa/skriva), sessioner och att hämta data.
- `account.py` **Kontomodell** Innehåller logik för deposits, withdraws och hantering av saldo.
- `user.py` **Användarmodell** En dataklass för att lagra användarprofiler och dess konton.
- `transaction.py`**Transaktionsmodell** En dataklass som representerar en enskild transaktion.

## Kom igång

### Förutsättningar

- Senaste Python versionen.

### Installation

1.  Klona repository från Github.
2.  Systemet skapar automatiskt mappen `./user_data/` och filen `users.json` vid första uppstarten.

### Användning

Starta programmet via terminalen:

```bash
py app.py
```
