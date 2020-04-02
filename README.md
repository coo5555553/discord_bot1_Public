# 惠ちゃん 
### 多功能型聊天機器人(?)
##### *不定時更新...*
[![Python 3.6.10](https://img.shields.io/badge/Python-3.6.10-blue?style=flat&logo=python)](https://www.python.org/downloads/release/python-3610/)
![Discord.py](https://img.shields.io/badge/discord.py-1.3.1-blue?style=flat&logo=discord)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

---
#### 取名純屬私心
---

## 建置步驟：
1. 打開 `jsons/settings.json`
```json
{
    "TOKEN": "BOT的Token",
    "GAME": "自訂遊戲狀態"
}
```
2.打開 `jsons/weather.json`
```json
{
    "URL": "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization={在此放入中央氣象局API KEY}&limit=1&locationName=",
    "CHANNEL": "定時天氣頻道ID"
}
```
3.打開 `jsons/alert.json`
```json
{
    "URL": "https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0015-001?Authorization={在此放入中央氣象局API KEY}&limit=1",
    "CHANNEL": "地震資訊頻道ID",
    "No": 109018
}
```
4.編輯 `cmds/COVID.py` 第21列
```py
ch = self.bot.get_channel(CH) # CH改為每日疫情頻道ID
```
4. 運作`body.py`

---
### 開發者
|林睿騰(Duck)|
|:------------:|
|[![Duck](https://avatars0.githubusercontent.com/u/60691401?s=4=128&u=95da0bc00d5d37fe4d6e83368a61823d00dc48bd&v=4)](https://github.com/coo5555553)|
---
### 目前功能s
 **Prefix可在 `body.py` 第11列更改**
* 模組管理指令
    * `|load <module name>` ： 載入目標模組 
    * `|unload <module name>` ：卸載指定模組
    * `|reload <module name>` ：重載指定模組 
* Owner指令
    * `|set_game <Activity>` ：更改自定義狀態
    * `|voice_move(|vm) <ch1> <ch2>` ： 把ch1語音頻道的使用者移動到ch2
    * `|avatar <User>` ： 獲得指定使用者的頭像
    * `|alert_ch <ch>` ： 指定地震訊息頻道
* 主要指令
    * `|kick <User>` ： 踢出指定使用者
    * `|online_cnt` ： 計算線上人數
    * `|ping` ： 檢測機器人延遲
    * `|help <Type(選填)>` ： 指令幫助，可以指定Type以獲得更詳細的幫助
* Alert指令
    * `|latest_EQ` ： 查詢最近大規模地震
* COVID指令
    * `|COVID19 <all(選填)>` ： 查詢台灣COVID-19疫情資訊，all可查詢全球資訊
* Extra指令
    * `|get_user <User>` ： 查詢該使用者及其線上狀態 (機器人必須與其有共同伺服器)
    * `|fetch_user <User>` ： 獲得該使用者的資訊 (機器人不必與其有共同伺服器)
    * `|get_channel <Ch ID>` ： 查找指定頻道
    * `|invite_create <T(選填)> <C(選填)>` ： 創建一個耐久為T秒(預設100秒)，C次(預設1次)的伺服器邀請
    * `|invite_list` ： 查看伺服器的邀請列表
* Gamble指令
    * `|roll <C(選填)>` ： 擲C枚骰子(預設1枚)
* Vote指令
    * `|vote <Title> <Choices>` ： 建立投票，選項用空格分開
* Weather指令
    * `|weather <縣市>` ： 查詢該縣市24(或36)小時內的氣候概況
    * `|weather_now <縣市>` ： 查詢該縣市目前的天氣概況
