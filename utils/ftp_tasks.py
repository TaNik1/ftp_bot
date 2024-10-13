from ftplib import FTP
from typing import List
import datetime as dt
from pytz import timezone
from Bot.keyboard import parsers
from Bot.message import send_notification


def get_parsers() -> List[str]:
    ftp = FTP(host="82.202.173.230", user="mainparser", passwd="oD5zA2bJ7x")
    ftp.cwd("www/parser-poiskzip.ru")

    directories = [name for name, facts in ftp.mlsd() if facts['type'] == 'dir' and "parser" in name]

    ftp.quit()

    return directories


def get_json(path) -> str:
    ftp = FTP(host="82.202.173.230", user="mainparser", passwd="oD5zA2bJ7x")
    ftp.cwd(f"www/parser-poiskzip.ru/{path}")

    file_name, fact = [(name, facts) for name, facts in ftp.mlsd() if ".json" in name][0]

    ftp.quit()

    return file_name


async def check_updates() -> None:
    ftp = FTP(host="host", user="username", passwd="password")
    ftp.cwd(f"www/parser-poiskzip.ru")
    for name_parser in parsers:
        ftp.cwd(name_parser)
        try:
            file_name, fact = [(name, facts) for name, facts in ftp.mlsd() if ".json" in name][0]
        except IndexError:
            ftp.cwd("..")
            continue
        file_modify = dt.datetime(year=2024, month=int(fact['modify'][4:][:2]), day=int(fact['modify'][4:][2:4]),
                                  hour=int(fact['modify'][4:][4:6]), minute=int(fact['modify'][4:][6:8]))
        moscow_tz = timezone("Europe/Moscow")
        file_modify = moscow_tz.localize(file_modify)
        if dt.datetime.now(tz=moscow_tz) - file_modify >= dt.timedelta(days=1):
            await send_notification(name_parser)
        ftp.cwd("..")
    ftp.quit()
