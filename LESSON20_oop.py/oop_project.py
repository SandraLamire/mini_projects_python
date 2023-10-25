# if : import bank_accounts, must use bank_accounts.balance
# with : from bank_accounts import *, we can just use balance
from bank_accounts import *

sandra = BankAccount(1000, "Sandra")
dave = BankAccount(2000, "Dave")

# Account 'Sandra' created.
# Balance = $1000.00       

# Account 'Dave' created.
# Balance = $2000.00    

sandra.getBalance()
# Account 'Sandra' balance = $1000.00
dave.getBalance()
# Account 'Dave' balance = $2000.00

sandra.deposit(500)
# Deposit complete.
# Account 'Sandra' balance = $1500.00

dave.withdraw(10000)
# Withdraw interrupted:
# Sorry, account 'Dave' only has a balance of $2000.00  

dave.withdraw(10)
# Withdraw complete.
# Account 'Dave' balance = $1990.00

dave.transfer(10000, sandra)
# **********
# Beginning Transfer.. 🚀
# Tranfer interrupted. ❌
# **********

dave.transfer(1000, sandra)
# **********
# Beginning Transfer.. 🚀
# Withdraw complete.
# Account 'Dave' balance = $990.00
# Deposit complete.
# Account 'Sandra' balance = $2500.00
# Tranfer complete! ✅
# **********

jim = InterestRewardAcct(1000, "Jim")
# Account 'Jim' created.
# Balance = $1000.00

jim.getBalance()
# Account 'Jim' balance = $1000.00

jim.deposit(100)
# Deposit complete.
# Account 'Jim' balance = $1105.00

jim.transfer(100, dave)
# **********
# Beginning Transfer.. 🚀
# Withdraw complete.
# Account 'Jim' balance = $1005.00
# Deposit complete.
# Account 'Dave' balance = $1090.00
# Tranfer complete! ✅
# **********

blaze = SavingAcct(1000, "Blaze")
# Account 'Blaze' created.
# Balance = $1000.00
blaze.getBalance()
# Account 'Blaze' balance = $1000.00
blaze.deposit(100)
# Deposit complete.
# Account 'Blaze' balance = $1105.00
blaze.transfer(10000, sandra)
# **********
# Beginning Transfer.. 🚀
# Tranfer interrupted. ❌
# Sorry, account 'Blaze' only has a balance of $1105.00     
# **********
blaze.transfer(1000, sandra)
# **********
# Beginning Transfer.. 🚀
# Withdraw complete.
# Account 'Blaze' balance = $100.00
# Deposit complete.
# Account 'Sandra' balance = $3500.00
# Tranfer complete! ✅
# **********




