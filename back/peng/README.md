# PENG

## Requirements and installation

 - virtualenv named `peng` (used pyenv)
 - python 3.10.0
 - pyenv local peng
 - pip, pip-tools
 - pip-compile
 - pip-sync

## Explanation

I choose to use [plotly](https://plotly.com/) to show graph as the interface is nice and straightforward.
Can show complex graph with a minimum amount of code.
It's also customizable and a known/stared library with huge community and documentation.
In addition, it's possible to interact with the graph (zoom, download, autoscale, ...).

## Results

### General vouchers statistics
<img src="screenshots/general/dollar_off.png" alt="">
<img src="screenshots/general/percent_off.png">

### Macys vouchers statistics
<img src="screenshots/macys/dollar_off.png" alt="">
<img src="screenshots/macys/percent_off.png">

### Nike vouchers statistics
<img src="screenshots/nike/dollar_off.png" alt="">
<img src="screenshots/nike/percent_off.png">

### NordStorm vouchers statistics
<img src="screenshots/nordstrom/dollar_off.png" alt="">
<img src="screenshots/nordstrom/percent_off.png">

## Unit testing

Some basic testing have been implemented using `unittest`
```python
python -m unittest test_voucher_computer.py
```