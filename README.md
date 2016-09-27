# CHIP control of Plugable PS-BTAPS1 Bluetooth Home Automation Switch.

The [Plugable Home Automation Switch](http://plugable.com/products/ps-btaps1) had an easy to use [python library](https://github.com/bernieplug/plugable-btaps) so I combined it with a [$9 CHIP](https://getchip.com/pages/chip) dev board and a button to demonstrate simple on/off control of the outlet with the button.

The outlet is on whenever the button is pressed and will be turned off when the button is released.  The python script must be run on the device after the outlet is plugged in.

I haven't tried it, but [this switch](https://amzn.com/B0171Z0B28) looks like it might work as well.  Monoprice used to sell a rebranded version (product id 10530) but it appears to be gone from their site.

## Setup
Follow the instructions at the following repositories to install the required dependencies:

CHIP GPIO library: https://github.com/xtacocorex/CHIP_IO  
Plugable Library: https://github.com/bernieplug/plugable-btaps

For the impatient and those feeling lucky here are summarized instructions:

>\# Install plugable-btaps
>sudo apt-get update  
>sudo apt-get install python-bluez  
>sudo apt-get install python-pip  
>sudo pip install plugable-btaps  
>  
> \# Install CHIP_IO  
>cd ~  
>sudo apt-get install git build-essential python-dev python-pip flex bison -y  
>git clone https://github.com/atenart/dtc  
>cd dtc  
>make  
>sudo make install PREFIX=/usr  
>cd ..  
>git clone git://github.com/xtacocorex/CHIP_IO.git  
>cd CHIP_IO  
>sudo python setup.py install  
>cd ..  
>sudo rm -rf CHIP_IO 

Once the dependent libraries are installed place outletcontrol.py on your CHIP (we'll use /home/chip/outletcontrol.py).

## Wiring

Connect a button to the GND and XIO-P1 pins on your CHIP.

## Usage

Following the Setup instructions you should have CHIP_IO and Plugable BTAPS libraries installed and outletcontrol.py should be on your CHIP (/home/chip/outletcontrol.py).

To execute it just do

    sudo python outletcontrol.py 00:00:00:00:00:00
    
with 00:00:00:00:00:00 replaced with the address of your plug.  When you press the button the outlet should turn on and then turn off again when the button is released.

## Auto-start

Edit `/etc/rc.local` and add the following before the `exit 0` that should already exist in the file:

    python /home/chip/outletcontrol.py 00:00:00:00:00:00 &

Make sure to replace 00:00:00:00:00:00 with the address of your plug.  (Also make sure to include the & at the end of the line)
