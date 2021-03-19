from pymongo import MongoClient


class Data:
    
    @classmethod
    def connexion(cls):
        cls.client = MongoClient("mongodb+srv://Guillaume:Guillaume@cluster0.bk25f.mongodb.net/Scraper?retryWrites=true&w=majority")
        cls.col = cls.client.Scraper.laTunes

    @classmethod
    def deconnexion(cls):
        cls.client.close()

    @classmethod
    def insert(cls, data):
        cls.connexion()
        cls.col.insert_many([data])
        cls.deconnexion()