## Automated posting

This repository handles some automated tasks, such as publishing content gathered from apis to my X account.

Consider viewing the account here:
[@xautocount](https://x.com/xautocount), or just follow me <a href="https://twitter.com/xautocount?ref_src=twsrc%5Etfw" class="twitter-follow-button" data-show-screen-name="false" data-dnt="true" data-show-count="false">Follow @xautocount</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>.

Automation is handled via the **crond** commmand, using given instructions in the in the "config/cronjobs" file.

Apis used to gather data so far are
+ Github: for contribution data
+ Marketstack: stock end of day statistics
+ Spotify: song recommendations, current favorites, new album releases for artists I follow
+ Weatherstack: weather data

A LLM may be added to the project to give some flare to the output text.