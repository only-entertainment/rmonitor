# RMonitor Client

### What is this?

A Python library for parsing the RMonitor timing protocol used in the live timing of automotive and karting events.

### Prior Work

This code draws inspiration from this work:

        https://github.com/zacharyfox/RMonitorLeaderboard
    
The protocol specifications are from:

        http://www.imsatiming.com/software/protocols/AMB%20RMonitor%20Timing%20Protocol.pdf
        http://www.imsatiming.com/software/protocols/IMSA%20Enhanced%20RMon%20Timing%20Protocol%20v1.03.pdf
    

### Pre-Requisites for development, assumes OSX

1) Install Brew:

	    $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

2) Install Python3:

	    $ brew install python3

3) Install Virtualenv:

	    $ pip3 install virtualenv

4) Install Virtualenv Wrapper:

	    $ pip3 install virtualenvwrapper

5) Create Virtualenvs dir:

        $ cd ~
	    $ mkdir ~/.virtualenvs

6) Open .bashrc with sudo:

	    $ sudo nano .bashrc

7) Add to .bashrc:

	    export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3
	    export WORKON_HOME=~/.virtualenvs
	    source /usr/local/bin/virtualenvwrapper.sh


### Installation

1) Clone the project:

        (optional but this is a good place)
        $ cd ~
        $ mkdir projects
        $ cd projects

        (required)
	    $ git clone https://github.com/krisneuharth/rmonitor rmonitor

2) Switch to project directory:

	    $ cd rmonitor

3) Create virtualenv:

	    $ mkvirtualenv --python=/usr/local/bin/python3 rmonitor

4) Activate environment:

	    $ workon rmonitor

5) Install Python dependencies:

	    (rmonitor) $ python setup.py develop

6) Run unit tests:

        (rmonitor) $ nosetests
    

### Configuring the app to run

1) Add server and port of the RMonitor live feed in `rmonitor/settings/settings.py`.

        ADDRESS = "50.56.75.58:50095"
    
    
### Running the app

1) From the root of the project:

        (rmonitor) $ python ./bin/run_server.py
        (rmonitor) $ python ./bin/run_client.py


## Contributions

All pull requests are welcome! Look at the issues list for ideas or bugs.


## Contributors

        Kris Neuharth (kris.neuharth@gmail.com)
        Ryan Kuhl (rkk09c@gmail.com)
