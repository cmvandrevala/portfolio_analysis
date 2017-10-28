class Constants:
    BALANCE_SHEET_HEADERS = ["Last Updated", "Institution", "Name", "Symbol", "Owner", "Asset Class", "Value"]
    BALANCE_SHEET_SPACERS = ["---", "---", "---", "---", "---", "---", "---"]
    DAYS_PER_YEAR = 365
    GENERAL_LEDGER_HEADERS = ["Timestamp", "Institution", "Description", "Owner", "Symbol", "Account Type", "Value", "Asset Class"]
    LEDGERS_DIRECTORY = "../general_ledger/csv/"
    LOCAL_LEDGER_PATH = "local_ledger.csv"
    SECONDS_PER_DAY = 86400
    YES_REPONSES = ["y", "ye", "yes"]
    DATA_URL = "http://localhost:5000"
