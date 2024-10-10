include .env

postauthxauto:
	python3 /code/auth/auth1_0.py --envpath="./tweets/.env" --crudtype="POST" \
	--baseurl="https://api.twitter.com/2/tweets" --token=${xautocount_TOKEN} --accesstoken=${xautocount_ACCESS_TOKEN} \
	--tokensecret=${xautocount_TOKEN_SECRET} --accesstokensecret=${xautocount_ACCESS_TOKEN_SECRET} \
	--variablename="AUTHORIZATION_HEADER"

deleteauthxauto:
	python3 /code/auth/auth1_0.py --envpath="./tweets/.env" --crudtype="DELETE" \
	--baseurl="https://api.twitter.com/2/tweets" --token=${xautocount_TOKEN} --accesstoken=${xautocount_ACCESS_TOKEN} \
	--tokensecret=${xautocount_TOKEN_SECRET} --accesstokensecret=${xautocount_ACCESS_TOKEN_SECRET} \
	--variablename="AUTHORIZATION_HEADER"

postxauto: postauthxauto
	python3 /code/tweets/post.py

deletexauto: deleteauthxauto
	python3 /code/tweets/delete.py --tweetid=""

weatherpost: weatherstackdata postxauto

githubpost: githubdata postxauto

marketstackpost: marketstackdata postxauto

spotifypost: spotifydata postxauto

githubdata:
	python3 /code/api/github/get.py

leetcodedata:
	python3 /code/api/leetcode/get.py

marketstackdata:
	python3 /code/api/marketstack/get.py

pinterestdata:
	python3 /code/api/pinterest/get.py

spotifyrefresh:
	python3 /code/api/spotify/refresh_token.py

spotifydata:
	python3 /code/api/spotify/get.py

weatherstackdata:
	python3 /code/api/weatherstack/get.py

migrateup:
	python3 /code/migrations/up.py

migratedown:
	python3 /code/migrations/up.py