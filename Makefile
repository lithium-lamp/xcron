include .env

# ==================================================================================== #
# HELPERS
# ==================================================================================== #

## help: print this help message
.PHONY: help
help:
	@echo 'Usage:'
	@sed -n 's/^##//p' ${MAKEFILE_LIST} | column -t -s ':' | sed -e 's/^/ /'

.PHONY: confirm
confirm:
	@echo -n 'Are you sure? [y/N] ' && read ans && [ $${ans:-N} = y ]

# ==================================================================================== #
# TWITTER
# ==================================================================================== #

## postauthxauto: authenticate before posting
.PHONY: postauthxauto
postauthxauto:
	python3 /code/auth/auth1_0.py --envpath="./tweets/.env" --crudtype="POST" \
	--baseurl="https://api.twitter.com/2/tweets" --token=${xautocount_TOKEN} --accesstoken=${xautocount_ACCESS_TOKEN} \
	--tokensecret=${xautocount_TOKEN_SECRET} --accesstokensecret=${xautocount_ACCESS_TOKEN_SECRET} \
	--variablename="AUTHORIZATION_HEADER"

## deleteauthxauto: authenticate before posting
.PHONY: deleteauthxauto
deleteauthxauto:
	python3 /code/auth/auth1_0.py --envpath="./tweets/.env" --crudtype="DELETE" \
	--baseurl="https://api.twitter.com/2/tweets" --token=${xautocount_TOKEN} --accesstoken=${xautocount_ACCESS_TOKEN} \
	--tokensecret=${xautocount_TOKEN_SECRET} --accesstokensecret=${xautocount_ACCESS_TOKEN_SECRET} \
	--variablename="AUTHORIZATION_HEADER"

## postxauto: create X post
.PHONY: postxauto
postxauto: postauthxauto
	python3 /code/tweets/post.py

## deletexauto: delete X post
.PHONY: deletexauto
deletexauto: deleteauthxauto
	python3 /code/tweets/delete.py --tweetid=""

## weatherpost: get weather data and post
.PHONY: weatherpost
weatherpost: weatherstackdata postxauto

## leetcodepost: get leetcode data and post
.PHONY: leetcodepost
leetcodepost: leetcodedata postxauto

## githubpost: get github data and post
.PHONY: githubpost
githubpost: githubdata postxauto

## marketstackpost: get stock data and post
.PHONY: marketstackpost
marketstackpost: marketstackdata postxauto

## spotifypost: get spotify data and post
.PHONY: spotifypost
spotifypost: spotifydata postxauto

# ==================================================================================== #
# GET DATA
# ==================================================================================== #

## githubdata: get github data and
.PHONY: githubdata
githubdata:
	python3 /code/api/github/get.py

## leetcodedata: get github data and
.PHONY: leetcodedata
leetcodedata:
	python3 /code/api/leetcode/get.py

## marketstackdata: get github data and
.PHONY: marketstackdata
marketstackdata:
	python3 /code/api/marketstack/get.py

## pinterestdata: get github data and
.PHONY: pinterestdata
pinterestdata:
	python3 /code/api/pinterest/get.py

## spotifydata: get github data and
.PHONY: spotifydata
spotifydata:
	python3 /code/api/spotify/get.py

## weatherstackdata: get github data and
.PHONY: weatherstackdata
weatherstackdata:
	python3 /code/api/weatherstack/get.py

# ==================================================================================== #
# MIGRATION
# ==================================================================================== #

## migrateup: migrate up
.PHONY: migrateup
migrateup:
	python3 /code/migrations/up.py

## migratedown: migrate down
.PHONY: migratedown
migratedown: confirm
	python3 /code/migrations/down.py

# ==================================================================================== #
# REFRESH
# ==================================================================================== #

## spotifyrefresh: refresh spotify token
.PHONY: spotifyrefresh
spotifyrefresh:
	python3 /code/api/spotify/refresh_token.py