# Minimal [Flask](http://flask.pocoo.org/) App with [Pushould](https://yhoshino11.github.io)

## 1. Create Account at [pushould.com](https://pushould.com)
```sh
$ gem install pushould
$ pushould signup
```

## 2. Set Environment Variables
```sh
# .zshrc
# add these on the bottom of your .zshrc
export O_EMAIL='your_awesome@email.com'
export O_PASSWORD='your_awesome_password'
export O_URL='your_api_url'
export O_CLIENT_TOKEN='your_client_token'
export O_SERVER_TOKEN='your_server_token'
```
```sh
$ exec $SHELL -l
```

Alternatively, you can use a tool like
[foreman](http://ddollar.github.io/foreman/) to automatically manage your
environment variables. In that case, you can put all environment variables in a
`.env` file.

## 3. Boom!
```sh
$ pip install -r requirements.txt
$ python app.py
```

Finally, open up your browser at [localhost:5000](http://localhost:5000) and try
sending a message.
