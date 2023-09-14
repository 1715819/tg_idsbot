## Environment Variables

#### Mandatory Vars

- `API_ID` - Get this from [my.telegram.org](https://my.telegram.org/auth) or [@UseTGZKBot](https://t.me/usetgzkbot)
- `API_HASH` - Get this from [my.telegram.org](https://my.telegram.org/auth) or [@UseTGzKbot](https://t.me/usetgzkbot)
- `BOT_TOKEN` - Get this from [@BotFather](https://t.me/BotFather)

#### Optional Vars

> (fill both or neither)

- `OWNER_ID` - Get it from [@UseTGidBot](https://t.me/UseTGidBot) by sending /id to it.
- `OWNER_NAME` - Your Name (to be shown as owner in bot)

---

### Deploy in your VPS

```
git clone https://github.com/ZauteKm/tg_idsbot
cd tg_idsbot
pip3 install -r requirements.txt
# <Create Variables appropriately>
python3 bot.py
```

```
docker build -t c5 .

docker run -p 5001:5000 -e API_ID= -e API_HASH= -e BOT_TOKEN= -e OWNER_ID= -e OWNER_NAME= c5


```

###
与https://github.com/1715819/id-on-render配合使用，从https://github.com/1715819/id-on-render构建
