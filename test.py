from twistedgadu import *

# pokazuje na czym polegaja zdarzenia (eventy), opisuje je z krotsza
# pamietajmy ze na dzien dzisiejszy wszystkie te eventy musza byc zdefiniowane w kodzie

class GaduTest(object):
    def __init__(self):
        # tworzymy instancje klasy. Cos trzeba tlumaczyc? ;)
        # UWAGA! Ponizsza zmienna jest wymagana!
        #self.contacts_list = ContactsList([Contact({'uin':3993939,'shown_name':'Tralala'}), Contact({'uin':4668758,'shown_name':'Anna'}), Contact({'uin':5120225,'shown_name':'kkszysiu'})])
        self.contacts_list = ContactsList()

    def on_auth_got_seed(self, conn, seed):
        # te zdarzenie jest wykonywane jesli uda nam sie pobrac seed potrzebny do zalogowania
        print 'mamy seed: ', seed
        #login zawsze MUSI byc wykonywany w on_auth_got_seed
        #login przyjmuje seed, uin, password, status i opis
        conn.login(seed, 4634020, 'xxxxxx', GGStatuses.Avail, '')

    def on_login_ok(self, conn):
        #ten event informuje nas ze zostalismy poprawnie zalgoowani. Nie jest to jeszcze koniec
        # bowiem aby moc wysylac komendy i miec info o uzytkownikach musimy jeszcze odpytac serwer o info o kontaktach z listy
        print 'zalogowano!'
        conn.import_contacts_list()

    def on_login_failed(self, conn):
        # ten event wystepuje jesli logowanie sie nie powiedzie. zazwyczaj oznacza to bledny seed lub nieprawidlowa nazwe uzytkonika i/lub haslo
        print 'logowanie nie powiodlo sie!'

    def on_need_email(self, conn):
        # event informuje o potrzebuie podania adresu email. Nie jest on juz chyba uzywany niemniej GG jeszcze go obsluguje...
        print 'musisz uzupelnic email!'

    def on_disconnecting(self, conn):
        # trzeba cos tlumaczyc? Event wystepuje gdy GG ozlaczy nas z serwerem. Najczesciej oznacza to ze podlaczyl sie nny klient uzywajacy naszego numeru GG
        print 'rozlaczanie!'

    def on_notify_reply(self, conn, contacts):
        # hurej! Jesli klient powiadomil nas o tym evencie oznacza to ze pobralismy ingo o kontaktach z naszej listy i jestesmuy gotowi do wysylania pakietow do serwera GG
        print 'info o kontaktach pobrane'
#        conn.add_contact(Contact({'uin':13643147, 'shown_name':'MojDrugiNumer'}))
#        try:
#            #zobaczymy to:
#            print 'Po dodaniu: ', conn.__contacts_list[13643147].uin
#        except:
#            print 'Nie udalo sie pobrac numeru GG tego kontaktu'
#        #I uwuwamy kontakt
#        conn.remove_contact(13643147)

    def on_msg_recv(self, conn, sender, seq, time, msg_class, message):
        print "Odebrano wiadomosc:\nSender: %s\nSeq: %s\n Time: %s\n Class: %s\n Msg: %s\n" % (sender, seq, time, msg_class, message)
        conn.send_msg(sender, message)

    def on_msg_ack(self, conn, status, recipient, seq):
        print "Odebrano powierdzenie wyslania wiadomosci:\n   Status: %s\n   Recipient: %s\n   Seq: %s\n" % (status, recipient, seq)

    def on_status(self, conn, contact):
        print "Kontakt %s zmienil status na %s, opis: %s" % (contact.uin, contact.status, contact.description)

    def on_status60(self, conn, contact):
        print "Kontakt %s zmienil status na %s, opis: %s" % (contact.uin, contact.status, contact.description)

    def on_userlist_reply(self, conn, contacts):
        print 'lista kontaktow zaimportowana'
        print contacts[5120225].description

    def on_userlist_exported_or_deleted(self, conn, reqtype, request):
        print 'lista kontaktow, reqtype - %s, request - %s' % (reqtype, request)

def main():
    t = GaduTest()
    factory = GGClientFactory(t)
    reactor.connectTCP('91.197.13.83', 8074, factory)
    #factory.sendMessage()
    #factory.Login(4634020, 'xxxxxx', GGStatuses.Avail, 'test')
    reactor.run()

if __name__ == '__main__':
    main()
