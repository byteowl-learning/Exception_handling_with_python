# define a function to transfer money between two accounts.
def transfer_money(source_account_number, destination_amount_number, amount):

    print(f'Attempting to transfer ${amount} from account number {source_account_number} to account number {destination_amount_number}')

    if(	len(source_account_number) < 5):
        raise ValueError("Error: source_account_number is invalid")

    if ( len(destination_amount_number) < 5):
        raise ValueError("Error: destination_amount_number is invalid")

    if ( amount == 0 ):
        raise ValueError("Error: amount is 0")

    print('Money has been transferred.')


# use the transfer_money function.
try:
    # this call will succeed.
    transfer_money('178654', '265193', 1000)

    # this call will fail.
    transfer_money('178654', '265193', 0)
except ValueError as e:
    print (e)
finally:
    pass