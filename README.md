## Automated posting

This repository handles some automated tasks, such as publishing content gathered from apis to my X account.

Consider viewing the account here:
[@xautocount](https://x.com/xautocount).

Automation is handled via the **crond** commmand, using given instructions in the in the "config/cronjobs" file.

Apis used to gather data so far are
+ Github: for contribution data
+ Leetcode: for tracking completed problems
+ Marketstack: stock end of day statistics
+ Spotify: song recommendations, current favorites, new album releases for artists I follow
+ Weatherstack: weather data

A LLM may be added to the project to give some flare to the output text.
