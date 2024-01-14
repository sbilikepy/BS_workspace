from mock.bank_account import BankAccount

from unittest import mock


@mock.patch("bank_api.bank_api.transfer")
def test_should_transfer_request(mocked_transfer):
    test_account = BankAccount("My", 100)
    test_account.pay("Other", 50)

    mocked_transfer.assert_called_once_with(
        test_account.account_number, other_account, 50
    )
