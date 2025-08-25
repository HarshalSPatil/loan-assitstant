
# Loan sites definitions
sites = [
    {
        "name": "Bank of Maharashtra Home Loan",
        "url": "https://bankofmaharashtra.in/personal-banking/loans/home-loan",
       
    },
    {
        "name": "Retail Loans Static",
        "url": "https://bankofmaharashtra.in/retail-loans",
       
    },
    {
        "name": "Loan offers",
        "url": "https://bankofmaharashtra.in/offers",
        "needs_js": True,      # always fetch via Playwright
        "parse_type": "json_blob"  # parser will extract JSON-injection scripts
    },
    {
        "name": "Bank of Maharashtra  Loan",
        "url": "https://bankofmaharashtra.in/personal-banking/loans/personal-loan",
       
    },
    # {
    #     "name": "Bank of Maharashtra Education Loan",
    #     "url": "https://bankofmaharashtra.in/personal-banking/loans/education-loan",
       
    # },
    {
        "name": "Bank of Maharashtra Loan",
        "url": "https://bankofmaharashtra.in/online-loans",
       
    },
]