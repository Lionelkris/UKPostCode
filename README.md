###### **Validating the UKPostCode**

instruction to run :

`git clone https://github.com/Lionelkris/UKPostCode.git`

go inside the project folder

`cd UKPostCode`

open the python3 terminal

`python3`

import the UKPostCode library

`from UKPostCode.validate import UKPostCode`

create an instance of UKPostCode

`f = UKPostCode()`

validate the UKPostCode "SW1W 0NY"

`f.validate('SW1W 0NY')`

Please note: The post codes with capital letters and with / without space between Outward and Inward codes are only considered as correct format.
To check the terminated post codes, postcodes.io api is being used.

To run the unit tests, you can exit the python3 console and type the below command:

`python3 -m unittest discover`
