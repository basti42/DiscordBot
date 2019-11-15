import sqlite3
import os

class CommandLogger:


    def __init__(self, dbname="commands_log.sqlite", tablename="commands"):
        self.path = dbname
        self.tablename = tablename
        self.connection = sqlite3.connect(self.path, timeout=5.0)
        self.c = self.connection.cursor()
        # if the table does not exist create it
        if not self.__check_table_exists__():
            print("\r[*] initializing tables ... ", end="")
            self.__initialize_tables__()
            print("[!] initializing tables ... DONE")
        else:
            print("[!] connected to database: '{}'".format(self.path))


    def closeLogger(self) -> None:
        """closes the underlying database"""
        self.connection.close()


    def logContext(self, ctx) -> bool:
        """
        add a new log to the database
        :param ctx : discord.Context
        """
        author = ctx.message.author.name    #str
        text = ctx.message.clean_content    #str
        channel = ctx.message.channel.name  #str
        guild = ctx.message.guild.name      #str
        validCommand = ctx.valid            #str
        cmddate = ctx.message.created_at    #datetime.datetime
        try:
            self.c.execute("""INSERT INTO {} (author, text, channel, guild, validCommand, cmddate)
            VALUES ('{}','{}','{}','{}','{}','{}')""".format(
                self.tablename, author, text, channel,
                guild, validCommand, cmddate.strftime("%m/%d/%Y, %H:%M:%S")
            ))
            self.connection.commit()
            return True
        except BaseException as bex:
            print("[E] could not insert into table! Error: {}".format(bex))
            return False


    def __check_table_exists__(self) -> bool:
        q = self.c.execute("""
        SELECT name FROM sqlite_master WHERE type='table'
        AND name='{}';""".format(self.tablename))
        return True if q.fetchone() is not None else False


    def __initialize_tables__(self) -> None:
        print("initialize tables")
        print(self.path)
        self.c.execute("""
            CREATE TABLE {} (
                commandID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                author TEXT,
                text TEXT,
                channel TEXT,
                guild TEXT,
                validCommand BOOLEAN,
                cmddate TEXT
            );""".format(self.tablename))
        self.connection.commit()


if __name__ == "__main__":
    logger = CommandLogger()
    logger.closeLogger()
