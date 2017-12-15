class Constants:
    def __init__(self):
        pass

    BALANCE_SHEET_HEADERS = ["Last Updated", "Institution", "Account", "Investment", "Owner", "Asset Class", "Value"]
    BALANCE_SHEET_SPACERS = ["---", "---", "---", "---", "---", "---", "---"]
    DAYS_PER_YEAR = 365
    GENERAL_LEDGER_HEADERS = ["Timestamp", "Institution", "Description", "Owner", "Symbol", "Account Type", "Value", "Asset Class"]
    LEDGERS_DIRECTORY = "../general_ledger/csv/"
    LIABILITIES_HEADERS = ["Last Updated", "Institution", "Account", "Owner", "Value"]
    LOCAL_LEDGER_PATH = "local_ledger.csv"
    SECONDS_PER_DAY = 86400
    DATA_URL = "http://localhost:4567"
