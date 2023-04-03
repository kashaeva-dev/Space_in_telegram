# Space in telegram

This repository contains four python scripts that allow you to download images and send them to a Telegram channel. The scripts are:

* fetch_nasa_apod.py
* fetch_nasa_epic.py
* fetch_spacex_images.py
* send_all_to_channel.py
* send_one_to_channel.py

## Setup
1. Clone the repository to your local machine.
2. Create virtual environment to the project:
```
python -m venv env
```
3. Activate the virtual environment:

*for Windows:*

```
.\env\Scripts\activate
```
*for Linux or macOS:*

```
source env/bin/activate
```
4. Install the requirements: ```pip install -r requirements.txt```

5. Set environment variables in a file named .env. Create it in the root directory of the project 
and add your telegram bot API token and chat ID as well as NASA API token as follows:

```
TELEGRAM_BOT_TOKEN=<your_telegram_bot_token>
TELEGRAM_CHAT_ID=<your_telegram_chat_id>
NASA_API_KEY=<your_nasa_api_key>
```
Please, visit the following [website](https://api.nasa.gov/) to get NASA API.

 [Here](https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram.html) you can see, how to get a Telegram bot API.
And [here](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/) you can read how to get chat ID.
## Usage

**fetch_nasa_apod.py**

This script allows you to download a specified number of images from the Astronomy Picture of the Day website. 
The default number of images is 5, and you can change it by specifying the count argument.

```
python fetch_nasa_apod.py [-c count]
```
**fetch_nasa_epic.py**

This script allows you to download the yesterday Earth images from the Earth Polychromatic Imaging Camera. 

```
python fetch_nasa_epic.py
```

**fetch_spacex_images.py**

This script allows you to download the images from a SpaceX launch. 
By default, it downloads the images from the latest launch, but you can change it by specifying the flight_id argument.

```
python fetch_spacex_images.py [-id flight_id]
```

**send_all_to_channel.py**

This script allows you to send images from a specified directory to a Telegram channel in a given interval of time.
The default directory is "images", and the default interval is 4 hours. You can change the interval by specifying the
hours argument. You can also change the directory by specifying the directory when running the script.

```
python send_all_to_channel.py [-h hours] [-d directory]
```

**send_one_to_channel.py**

This Python script allows you to send one specified photo or a random photo from the "images" directory to
a Telegram channel using a bot. The bot token and chat ID are retrieved from the environment file. The script can be
run from the command line using the argument "-f" or "--filename", optional argument to specify 
the filename of the photo to send. If not specified, a random photo will be chosen from the "images" directory.

```
python send_one_to_channel.py [-f filename]
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.