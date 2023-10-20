import cv2
import os
import sqlite3

# dir = os.getcwd()
# for folder in os.listdir(dir):
#     if not os.path.isfile(os.path.join(dir, folder)):
#         dir = os.path.join(dir, folder)
#         for file in os.listdir(dir):
#             print(file)
#             img = os.path.join(dir, file)
#             img = cv2.imread(img)

#             cv2.imshow('window', img)
#             cv2.waitKey(0)
#             cv2.destroyAllWindows()

def main():
    # Create database
    db = Database()
    db.initTables()

    # Load data into Dataframe
    obj = Data()
    obj.readData()
    # Clean data

    # Populate tables in database

    # Query player positional data in first frame of each play

class Database():
    def __init__(self):
        # Connect to DB
        print('Creating DB connection to RunningLogs DB')
        self.conn = sqlite3.connect('play.db')
        self.dest = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        
        # Create backup
        self.conn.backup(self.dest)
        print('Connection to DB established, backup saved in memory')

        # Commit changes to DB
        self.conn.commit()
        self.conn.backup(self.dest)

    def initTables(self):
        # Create tables for play and player data
        cursor = self.conn.cursor()

        sql = """DROP TABLE IF EXISTS playData;"""

        cursor.execute(sql)

        sql = """CREATE TABLE playData (
            gameId int PRIMARY KEY NULL,
            playId int NULL,
            playDescription text NULL,
            quarter int NULL,
            down int NULL,
            yardsToGo int NULL,
            team text NULL,
            playDirection text NULL,
            x double NULL,
            y double NULL, 
            s double NULL,
            a double NULL, 
            dis double NULL,
            o.double NULL,
            dir double NULL,
            event text NULL
            );"""
        
        cursor.execute(sql)
    
        sql = """DROP TABLE IF EXISTS playerPlayData;"""

        cursor.execute(sql)

        sql = """CREATE TABLE playerPlayData (
            gameId int REFERENCES playData (gameId) NULL,
            playId int NULL,
            nflId int NULL,
            frameId int NULL,
            time int NULL,
            jerseyNumber int NULL,
            team text NULL,
            playDirection text NULL,
            x double NULL,
            y double NULL, 
            s double NULL,
            a double NULL, 
            dis double NULL,
            o.double NULL,
            dir double NULL,
            event text NULL
            );"""

        cursor.execute(sql)

        self.conn.commit()
        self.conn.backup(self.dest)
        return;

class Data():
    def __init__(self):
        pass

    def readData(self):
        pass

    def cleanData(self):
        pass

    def load2DB(self):
        pass

if __name__ == '__main__':
    main()