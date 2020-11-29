from samplebanking import Bank, Person, Client, Account, Regular, Savings

bank = Bank()
client1 = Client('Jane Doe', 27)
client2 = Client('John Doe', 25)

acc1 = Regular(1111, 2639236, 1000, 500)
acc2 = Savings(2222, 6369693, 100)

client1.assign_account(acc1)
client2.assign_account(acc2)

client1.account.takeout(200)
client1.account.takeout(1000)
client1.account.takeout(350)

client1.account.deposit(100)

client2.account.deposit(10)

client2.account.takeout(50)
client2.account.takeout(500)
