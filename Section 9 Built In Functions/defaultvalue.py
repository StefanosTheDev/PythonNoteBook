accounts = {
    'checking': 1958.00,
    'savings': 3685.50
}

## any argument that does not have a default value has to follow the default. Default values go at the end. 
def add_balance(amount: float, name: str = 'checking') -> float:
    '''
    function to update the balance of an account and return the new blaance
    '''
    accounts[name] += amount
    return accounts[name]

add_balance(500.00)
print(accounts['checking'])




## Avoid Mutable Default Arguments.
def create_account(name: str, holder: str, account_holders = None):
    # Creates the default account holder. this was not valued. 
    if not account_holders:
        account_holders = []

    account_holders.append(holder)

    return {
        'name': name,
        'main_account_holder': holder, 
        'account_holders': account_holders
    }

a1 = create_account('checking', 'Rolf')
print(a1)