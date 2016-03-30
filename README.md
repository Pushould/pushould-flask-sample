# Minimal [Flask](http://flask.pocoo.org/) App with [Pushould](https://yhoshino11.github.io)

#### 1. Create Account at pushoud.com
```sh
$ gem install pushould
$ pushould signup
```

#### 2. set environment variables
```sh
# .zshrc
# add these on the bottom of your .zshrc
export EMAIL='your_awesome@email.com'
export PASSWORD='your_awesome_password'
export URL='your_api_url'
export CLIENT_TOKEN='your_client_token'
export SERVER_TOKEN='your_server_token'
```
```sh
$ exec $SHELL -l
```

#### 3. Boom!
```sh
$ pip install flask
$ pip install pushould-python
$ python app.py
```
