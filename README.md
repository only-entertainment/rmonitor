# Race Monitor Client

### What is this?

TODO

### Pre-Requisites, assumes OSX

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
	$ git clone https://github.com/krisneuharth/race_monitor race_monitor

2) Switch to project directory:

	$ cd race_monitor

3) Create virtualenv:

	$ mkvirtualenv --python=/usr/local/bin/python3 race_monitor

4) Activate environment:

	$ workon race_monitor

5) Install Python dependencies:

	(race_monitor) $ pip install -r requirements.txt
	(race_monitor) $ python setup.py develop

6) Run unit tests:

    (race_monitor) $ nosetests
    
    
### Running the app

## Contributors

## License

