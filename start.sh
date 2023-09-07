echo "Cloning Repo...."
git clone https://github.com/1715819/tg_idsbot.git /tg_idsbot
cd /tg_idsbot
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 bot.py &
python3 app.py &
