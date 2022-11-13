# Reddit Flair Bot

![Python](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white) ![Open-Source](https://img.shields.io/badge/Open%20Source%20Initiative-3DA639.svg?style=for-the-badge&logo=Open-Source-Initiative&logoColor=white)

This is a Reddit bot that helps users set their own flair easily with the help of the `!flair` command.

Here's how the Reddit Flair Bot functions:

 - The `redditflairbot.py` file is executed
 - The bot starts running in an infinite loop
 - It waits and listen to a designated sub for the `!flair` command in the comments
 - When it receives the command from any user, it sets the flair of that user with the text that comes after the command

This bot is created using Python, and utilizes PRAW to set the user flair.

## How to run this bot

I am running this Bot using GitHub Actions. The `redditflairbot.yml` file, located in the `.github/workflows/` directory of the repo, contains the instruction to run the bot on GitHub. The `*/10 * * * *` specifies a cron job which runs the bot every 10th minutes. However, `workflow_dispatch:` ensures that the bot can also be run manually.

## List of requirements

The `requirements.txt` file contains all the modules required to compile and run this bot.

## Proposed improvements

Here are some of the points of improvements that can be implemented:

 - The bot needs a reset command that can be used to set the user flair to blank.

## Contribution

This is an open-source project. We invite your participation through issues and pull requests! Please ensure that you follow the [contributing guidelines](CONTRIBUTING.md). Also, do go through out [code of conduct](CODE_OF_CONDUCT.md) guidelines for contributors.

## List of Contributors

![GitHub Contributors Image](https://contrib.rocks/image?repo=rajtilakjee/redditflairbot)

## Additional Notes

This bot can be run 24/7 on PythonAnywhere service.
